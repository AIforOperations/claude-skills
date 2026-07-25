#!/usr/bin/env python3
"""Bulk pre-fetch of lead websites (homepage + about/team/leadership pages).

No model tokens, no paid APIs. Plain parallel HTTP. Output: <cache-dir>/site/row_<n>.json
  {"row": n, "status": "ok|thin|blocked|no_website", "pages": {url: text}, "chars": int}

Usage: python3 prefetch_sites.py <leads.csv> [--rows 1-100] [--workers 24] [--cache-dir ./enrich_cache]
"""
import csv, json, re, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
SUBPAGES = ["about", "about-us", "team", "our-team", "meet-the-team", "leadership", "our-story", "history"]
MAX_CHARS_PER_PAGE = 6000
WEBSITE_COLS = ("website", "company_website", "domain", "company_domain", "url")


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip, self.links = [], 0, []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1
        if tag == "a":
            self.links.append(dict(attrs).get("href") or "")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip and d.strip():
            self.parts.append(d.strip())


def fetch(url, timeout=15):
    req = Request(url, headers={"User-Agent": UA, "Accept-Language": "en;q=0.9"})
    with urlopen(req, timeout=timeout) as r:
        raw = r.read(600_000)
    return raw.decode("utf-8", "ignore")


def clean(html):
    p = Text()
    try:
        p.feed(html)
    except Exception:
        pass
    return re.sub(r"\s+", " ", " ".join(p.parts))[:MAX_CHARS_PER_PAGE], p.links


def do_lead(row, website):
    out = {"row": row, "status": "no_website", "pages": {}, "chars": 0}
    if not website:
        return out
    base = website if website.startswith("http") else "http://" + website
    try:
        home, links = clean(fetch(base))
    except Exception as e:
        out["status"] = "blocked"
        out["error"] = str(e)[:200]
        return out
    if home:
        out["pages"][base] = home
    cand = [urljoin(base, h) for h in links
            if any(s in (h or "").lower() for s in ("about", "team", "leadership", "our-story", "history", "who-we-are", "meet"))]
    if not cand:
        cand = [urljoin(base + "/", s) for s in SUBPAGES[:4]]
    seen, fetched = set(), 0
    for u in cand:
        u = u.split("#")[0].rstrip("/")
        if u in seen or u == base.rstrip("/") or fetched >= 3:
            continue
        seen.add(u)
        try:
            txt, _ = clean(fetch(u, timeout=12))
            if len(txt) > 300:
                out["pages"][u] = txt
                fetched += 1
        except Exception:
            pass
    out["chars"] = sum(len(v) for v in out["pages"].values())
    out["status"] = "ok" if out["chars"] > 1500 else ("thin" if out["chars"] > 0 else "blocked")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--rows", help="1-based data-row range like 1-100", default=None)
    ap.add_argument("--workers", type=int, default=24)
    ap.add_argument("--cache-dir", default="./enrich_cache")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.csvfile)))
    col = next((c for c in WEBSITE_COLS if c in rows[0]), None)
    if not col:
        raise SystemExit(f"no website column found (looked for {WEBSITE_COLS})")
    lo, hi = (1, len(rows))
    if a.rows:
        lo, hi = (int(x) for x in a.rows.split("-"))
    todo = [(i, (r.get(col) or "").strip()) for i, r in enumerate(rows, 1) if lo <= i <= hi]
    cache = Path(a.cache_dir) / "site"
    cache.mkdir(parents=True, exist_ok=True)
    t0, stats = time.time(), {}
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(do_lead, i, w): i for i, w in todo}
        for f in as_completed(futs):
            res = f.result()
            (cache / f"row_{res['row']}.json").write_text(json.dumps(res))
            stats[res["status"]] = stats.get(res["status"], 0) + 1
    print(f"done {len(todo)} leads in {time.time()-t0:.1f}s -> {stats}")


if __name__ == "__main__":
    main()
