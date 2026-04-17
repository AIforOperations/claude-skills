# Reddit to Ad Copy — Setup & Reference

Open this folder in your IDE with Claude Code. The skills are ready to go after the one-time setup in `.claude/skills/reddit-research/SETUP.md`.

## How to Use

Type `/reddit-research` and describe what you want to scrape. Examples:
- "Scrape r/ADHD and r/adhdwomen for melatonin complaints"
- "Find what people say about sleep supplements on Reddit"
- "Mine Reddit for fibro morning pain discussions"

Claude will scrape, generate ad concepts, and write MSL copy. After the copy is written, it'll ask if you want headlines and image prompts.

You can also run each skill separately:
- `/headline-gen` — generate headlines from an existing MSL ad
- `/image-prompts` — generate image prompts from an existing MSL ad

## Output

Everything saves to `Reddit_To_Copy/` in topic-named folders.

## What You Can Change

### Apify API Key
Set via environment variable:
```bash
export APIFY_API_KEY=apify_api_xxxxx
```

### Default Scrape Size
Same file, search for `--max-posts` and `--comments-per-post`:
```
default=5   ← posts per search
default=10  ← comments per post
```

You can also override these per-run by telling Claude (e.g., "get me 20 posts with 15 comments each").

### Your Prompts & Frameworks
All your prompt files live in `references/`. Edit them anytime — Claude reads them fresh each run.
