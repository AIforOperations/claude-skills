#!/usr/bin/env python3
"""
Reddit Scraper via Apify (trudax/reddit-scraper-lite)

Pulls Reddit posts + comments from specified subreddits and keywords.
Outputs raw JSON + formatted Markdown.

Usage:
    python3 reddit_scraper.py \
        --subreddits "ADHD,adhdwomen" \
        --keywords "can't sleep,racing thoughts" \
        --max-posts 5 \
        --comments-per-post 10 \
        --output-dir ./output
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
import ssl
import certifi
from datetime import datetime, timezone
from pathlib import Path

try:
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = ssl.create_default_context()
    CTX.check_hostname = False
    CTX.verify_mode = ssl.CERT_NONE

ACTOR_ID = "trudax~reddit-scraper-lite"
APIFY_BASE = "https://api.apify.com/v2"

# Set your Apify API key: export APIFY_API_KEY=apify_api_xxxxx
APIFY_API_KEY = os.environ.get("APIFY_API_KEY", "")


def build_start_urls(subreddits, keywords, sort="relevance", time_filter="month"):
    """Build Apify start URLs from subreddits and keywords."""
    urls = []
    subs = [s.strip().lstrip("r/") for s in subreddits.split(",")]
    kws = [k.strip() for k in keywords.split(",")]

    for sub in subs:
        for kw in kws:
            encoded_kw = urllib.parse.quote(kw)
            url = f"https://www.reddit.com/r/{sub}/search/?q={encoded_kw}&restrict_sr=1&sort={sort}&t={time_filter}"
            urls.append({"url": url})

    return urls


def run_actor(api_key, start_urls, searches, max_posts, comments_per_post):
    """Run the Apify actor and return dataset items.
    Uses startUrls mode (subreddit-specific) or searches mode (global), not both.
    """
    if searches:
        max_items = max_posts * (1 + comments_per_post) * len(searches)
        payload = {
            "searches": searches,
            "searchType": "Posts",
            "sort": "relevance",
            "time": "month",
            "maxItems": max_items,
            "maxPostCount": max_posts,
            "maxComments": comments_per_post,
            "proxyConfiguration": {"useApifyProxy": True},
        }
    else:
        max_items = max_posts * (1 + comments_per_post) * len(start_urls)
        payload = {
            "startUrls": start_urls,
            "maxItems": max_items,
            "maxPostCount": max_posts,
            "maxComments": comments_per_post,
            "proxyConfiguration": {"useApifyProxy": True},
        }

    input_data = json.dumps(payload).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    mode = "global search" if searches else f"{len(start_urls)} subreddit URLs"
    print(f"Running Apify actor ({mode})...")
    print(f"Max posts: {max_posts}, comments per post: {comments_per_post}")

    # Step 1: Start the actor run (async)
    run_url = f"{APIFY_BASE}/acts/{ACTOR_ID}/runs"
    req = urllib.request.Request(run_url, data=input_data, headers=headers, method="POST")

    try:
        resp = urllib.request.urlopen(req, context=CTX, timeout=30)
        run_data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        print(f"ERROR: Apify API returned HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Network error connecting to Apify: {e.reason}", file=sys.stderr)
        sys.exit(1)

    run_id = run_data["data"]["id"]
    dataset_id = run_data["data"]["defaultDatasetId"]
    print(f"Actor run started (ID: {run_id}). Waiting for results...")

    # Step 2: Poll until the run finishes
    import time
    poll_url = f"{APIFY_BASE}/actor-runs/{run_id}"
    max_wait = 600  # 10 minutes max
    waited = 0
    poll_interval = 5

    while waited < max_wait:
        time.sleep(poll_interval)
        waited += poll_interval

        try:
            poll_req = urllib.request.Request(poll_url, headers={"Authorization": f"Bearer {api_key}"})
            poll_resp = urllib.request.urlopen(poll_req, context=CTX, timeout=15)
            status_data = json.loads(poll_resp.read().decode())
        except Exception:
            continue  # retry on transient errors

        status = status_data["data"]["status"]
        if status == "SUCCEEDED":
            print(f"Actor finished in {waited}s.")
            break
        elif status in ("FAILED", "ABORTED", "TIMED-OUT"):
            print(f"ERROR: Actor run {status}.", file=sys.stderr)
            sys.exit(1)
        else:
            if waited % 15 == 0:
                print(f"  Still running... ({waited}s elapsed)")
    else:
        print(f"ERROR: Actor did not finish within {max_wait}s.", file=sys.stderr)
        sys.exit(1)

    # Step 3: Download dataset items
    dataset_url = f"{APIFY_BASE}/datasets/{dataset_id}/items?format=json"
    try:
        ds_req = urllib.request.Request(dataset_url, headers={"Authorization": f"Bearer {api_key}"})
        ds_resp = urllib.request.urlopen(ds_req, context=CTX, timeout=60)
        data = json.loads(ds_resp.read().decode())
        return data
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        print(f"ERROR: Failed to download results: HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Network error downloading results: {e.reason}", file=sys.stderr)
        sys.exit(1)


def filter_data(items):
    """Separate posts and comments, filter out AutoModerator. Keep all posts."""
    posts = []
    comments = []

    for item in items:
        if item.get("username", "").lower() == "automoderator":
            continue

        if item.get("dataType") == "post":
            posts.append(item)
        elif item.get("dataType") == "comment":
            comments.append(item)

    seen_ids = set()
    unique_posts = []
    for p in posts:
        pid = p.get("id") or p.get("parsedId")
        if pid and pid not in seen_ids:
            seen_ids.add(pid)
            unique_posts.append(p)

    unique_posts.sort(key=lambda x: x.get("upVotes", 0), reverse=True)

    return unique_posts, comments


def format_markdown(posts, comments, subreddits, keywords):
    """Format posts and comments into readable markdown."""
    lines = []
    lines.append("# Reddit Raw Data")
    lines.append(f"**Subreddits:** {subreddits}")
    lines.append(f"**Keywords:** {keywords}")
    lines.append(f"**Pulled:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | **Source:** Apify (trudax/reddit-scraper-lite)")
    lines.append(f"**Total:** {len(posts)} posts, {len(comments)} comments")
    lines.append("")

    for i, post in enumerate(posts, 1):
        ups = post.get("upVotes", 0)
        num_comments = post.get("numberOfComments", 0)
        if ups >= 100 or num_comments >= 50:
            engagement = "HIGH ENGAGEMENT"
        elif ups >= 20 or num_comments >= 10:
            engagement = "MEDIUM ENGAGEMENT"
        else:
            engagement = "LOW ENGAGEMENT"

        lines.append("---")
        lines.append(f"## Post {i}: {post.get('title', '[No title]')}")
        lines.append(
            f"**Author:** u/{post.get('username', 'unknown')} | "
            f"**Subreddit:** {post.get('communityName', 'unknown')} | "
            f"**Upvotes:** {ups} | "
            f"**Comments:** {num_comments} | "
            f"**Date:** {post.get('createdAt', '')[:10]} | "
            f"**[{engagement}]**"
        )
        lines.append(f"**URL:** {post.get('url', '')}")
        lines.append("")

        body = post.get("body", "").strip()
        if body:
            for bline in body.split("\n"):
                lines.append(f"> {bline}")
        else:
            lines.append("> [No text body — image/link post]")
        lines.append("")

        post_id = post.get("id")
        post_comments = [c for c in comments if c.get("postId") == post_id]

        if post_comments:
            lines.append(f"### Comments ({len(post_comments)} scraped)")
            lines.append("")
            for j, c in enumerate(post_comments, 1):
                author = c.get("username", "unknown")
                cup = c.get("upVotes", 0)
                cbody = c.get("body", "").strip()
                lines.append(f"**Comment {j}** — u/{author} ({cup} upvotes):")
                for cline in cbody.split("\n"):
                    lines.append(f"> {cline}")
                lines.append("")

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Reddit Scraper via Apify")
    parser.add_argument("--subreddits", default="", help="Comma-separated subreddit names (e.g., 'ADHD,adhdwomen'). If empty, uses global search mode.")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords (e.g., 'can\\'t sleep,racing thoughts')")
    parser.add_argument("--search", action="store_true", help="Force global search mode (ignores --subreddits)")
    parser.add_argument("--sort", default="relevance", choices=["relevance", "hot", "top", "new", "comments"], help="Sort order (default: relevance)")
    parser.add_argument("--time-filter", default="month", choices=["hour", "day", "week", "month", "year", "all"], help="Time filter (default: month)")
    parser.add_argument("--max-posts", type=int, default=5, help="Max posts per search (default: 5)")
    parser.add_argument("--comments-per-post", type=int, default=10, help="Comments per post (default: 10)")
    parser.add_argument("--output-dir", required=True, help="Output directory for results")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    api_key = APIFY_API_KEY
    if not api_key:
        print("ERROR: APIFY_API_KEY not set. Run: export APIFY_API_KEY=apify_api_xxxxx", file=sys.stderr)
        sys.exit(1)

    use_search = args.search or not args.subreddits.strip()
    start_urls = []
    searches = []

    if use_search:
        searches = [k.strip() for k in args.keywords.split(",")]
        print(f"Mode: Global search ({len(searches)} queries)")
        for s in searches:
            print(f"  \"{s}\"")
    else:
        start_urls = build_start_urls(args.subreddits, args.keywords, args.sort, args.time_filter)
        print(f"Mode: Subreddit search ({len(start_urls)} URLs)")
        for u in start_urls:
            print(f"  {u['url']}")

    raw_items = run_actor(api_key, start_urls, searches, args.max_posts, args.comments_per_post)
    print(f"Apify returned {len(raw_items)} items")

    posts, comments = filter_data(raw_items)
    print(f"After filtering: {len(posts)} posts, {len(comments)} comments")

    if not posts:
        print("WARNING: No posts found. Try different keywords or subreddits.", file=sys.stderr)

    json_path = output_dir / "01_raw_data.json"
    with open(json_path, "w") as f:
        json.dump(raw_items, f, indent=2)
    print(f"Raw JSON saved: {json_path}")

    subreddit_label = args.subreddits if args.subreddits.strip() else "Global search"
    md_content = format_markdown(posts, comments, subreddit_label, args.keywords)
    md_path = output_dir / "01_raw_data.md"
    with open(md_path, "w") as f:
        f.write(md_content)
    print(f"Formatted MD saved: {md_path}")

    metadata = {
        "subreddits": args.subreddits,
        "keywords": args.keywords,
        "sort": args.sort,
        "time_filter": args.time_filter,
        "max_posts": args.max_posts,
        "comments_per_post": args.comments_per_post,
        "total_items_returned": len(raw_items),
        "posts_after_filter": len(posts),
        "comments_after_filter": len(comments),
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "actor": ACTOR_ID,
    }
    meta_path = output_dir / "metadata.json"
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Metadata saved: {meta_path}")

    print(f"\nDone. {len(posts)} posts with {len(comments)} comments saved to {output_dir}/")


if __name__ == "__main__":
    main()
