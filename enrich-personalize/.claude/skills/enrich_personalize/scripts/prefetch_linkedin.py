#!/usr/bin/env python3
"""Bulk LinkedIn pre-fetch via Apify: profile bio for every lead (posts optional).

Batched: one actor run handles many profile URLs (far cheaper than per-lead calls).
Cost: ~$4 per 1,000 profiles (bio mode). Output: <cache-dir>/linkedin/row_<n>.json
  {"row": n, "profile": {...} | null, "posts": [...], "status": "ok|partial|none"}

Reads APIFY_API_TOKEN from the environment or a .env in the current directory.
Usage: python3 prefetch_linkedin.py <leads.csv> [--rows 1-100] [--batch 80]
       [--with-posts] [--cache-dir ./enrich_cache]
"""
import csv, json, os, sys, time, argparse, urllib.request
from pathlib import Path

PROFILE_ACTOR = "harvestapi~linkedin-profile-scraper"   # bio/about/headline/experience
POSTS_ACTOR = "harvestapi~linkedin-profile-posts"       # recent posts (off by default)
POSTS_PER_PROFILE = 5
LINKEDIN_COLS = ("linkedin_url", "linkedin", "person_linkedin_url", "contact_linkedin", "li_url")


def token():
    t = os.environ.get("APIFY_API_TOKEN")
    if t:
        return t
    env = Path(".env")
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("APIFY_API_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"')
    sys.exit("APIFY_API_TOKEN not found (env var or ./.env)")


def api(method, url, tok, body=None, timeout=300):
    req = urllib.request.Request(
        url + ("&" if "?" in url else "?") + "token=" + tok,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Content-Type": "application/json"}, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def run_actor(slug, inp, tok):
    run = api("POST", f"https://api.apify.com/v2/acts/{slug}/runs", tok, inp)["data"]
    rid = run["id"]
    while True:
        time.sleep(8)
        r = api("GET", f"https://api.apify.com/v2/actor-runs/{rid}", tok)["data"]
        if r["status"] in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            break
    usage = r.get("usageTotalUsd", 0)
    if r["status"] != "SUCCEEDED":
        print(f"  ! {slug} run {rid} -> {r['status']}", file=sys.stderr)
        return [], usage
    items = api("GET", f"https://api.apify.com/v2/datasets/{r['defaultDatasetId']}/items?clean=true", tok)
    return items, usage


def norm(url):
    u = (url or "").strip().lower().rstrip("/")
    return u.replace("http://", "").replace("https://", "").replace("www.", "")


def match_lead(nurl, pid, by_url):
    """Match an item to a lead row: exact normalized URL, then publicIdentifier fragment."""
    i = by_url.get(nurl)
    if i is not None:
        return i
    if pid:
        for nu, j in by_url.items():
            slug = nu.rsplit("/in/", 1)[-1]
            if slug == pid or slug.startswith(pid) or pid.startswith(slug):
                return j
    return None


def slim_post(it):
    return {"postedAt": it.get("postedAt"), "type": it.get("type"),
            "content": (it.get("content") or "")[:1200],
            "repost": bool(it.get("repost") or it.get("repostId"))}


def slim_profile(p):
    """Trim a raw profile item to enrichment-relevant fields (keeps cache ~8KB/lead)."""
    if not p:
        return None
    keep = {}
    for k in ("firstName", "lastName", "headline", "about", "location", "publicIdentifier",
              "linkedinUrl", "openToWork", "creator", "memorialized"):
        if p.get(k) not in (None, "", [], {}):
            keep[k] = p[k]
    for k in ("experience", "education", "volunteering", "certifications", "honorsAndAwards",
              "currentPosition", "skills"):
        v = p.get(k)
        if v:
            keep[k] = json.loads(json.dumps(v))
            if isinstance(keep[k], list):
                keep[k] = keep[k][:6]
    return keep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--rows", default=None)
    ap.add_argument("--batch", type=int, default=80)
    ap.add_argument("--with-posts", action="store_true",
                    help="also scrape recent posts (default off: rarely yields signals on low-activity B2B profiles)")
    ap.add_argument("--cache-dir", default="./enrich_cache")
    a = ap.parse_args()
    tok = token()
    rows = list(csv.DictReader(open(a.csvfile)))
    col = next((c for c in LINKEDIN_COLS if c in rows[0]), None)
    if not col:
        raise SystemExit(f"no linkedin column found (looked for {LINKEDIN_COLS})")
    lo, hi = (1, len(rows))
    if a.rows:
        lo, hi = (int(x) for x in a.rows.split("-"))
    leads = [(i, (r.get(col) or "").strip()) for i, r in enumerate(rows, 1)
             if lo <= i <= hi and (r.get(col) or "").strip()]
    cache = Path(a.cache_dir) / "linkedin"
    cache.mkdir(parents=True, exist_ok=True)
    t0, total_usd = time.time(), 0.0
    results = {i: {"row": i, "profile": None, "posts": [], "status": "none"} for i, _ in leads}
    by_url = {norm(u): i for i, u in leads}

    for b in range(0, len(leads), a.batch):
        chunk = leads[b:b + a.batch]
        urls = [u for _, u in chunk]
        print(f"batch {b//a.batch + 1}: {len(urls)} profiles")
        items, usd = run_actor(PROFILE_ACTOR,
                               {"urls": urls, "profileScraperMode": "Profile details no email ($4 per 1k)"}, tok)
        total_usd += usd
        for it in items:
            i = match_lead(norm(it.get("linkedinUrl") or it.get("url") or ""),
                           (it.get("publicIdentifier") or "").lower(), by_url)
            if i is not None:
                results[i]["profile"] = slim_profile(it)
        if a.with_posts:
            items, usd = run_actor(POSTS_ACTOR,
                                   {"targetUrls": urls, "maxPosts": POSTS_PER_PROFILE,
                                    "scrapeReactions": False, "scrapeComments": False}, tok)
            total_usd += usd
            for it in items:
                au = (it.get("author") or {}) if isinstance(it.get("author"), dict) else {}
                i = match_lead(norm(au.get("linkedinUrl") or ""), (au.get("publicIdentifier") or "").lower(), by_url)
                if i is not None and len(results[i]["posts"]) < POSTS_PER_PROFILE:
                    results[i]["posts"].append(slim_post(it))

    for i, res in results.items():
        res["status"] = "ok" if res["profile"] else ("partial" if res["posts"] else "none")
        (cache / f"row_{i}.json").write_text(json.dumps(res))
    got = sum(1 for r in results.values() if r["status"] != "none")
    print(f"done {len(leads)} profiles in {time.time()-t0:.1f}s | matched {got} | apify cost ${total_usd:.3f}")


if __name__ == "__main__":
    main()
