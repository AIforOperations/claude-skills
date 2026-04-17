# Reddit Research — First-Time Setup

Run this once before using the `/reddit-research` skill.

## Step 1: Install Python (if not already installed)

Check if Python 3 is available:
```bash
python3 --version
```

If not installed:
- **macOS:** `brew install python3` (requires Homebrew) or download from https://www.python.org/downloads/
- **Windows:** Download from https://www.python.org/downloads/

## Step 2: Set your Apify API key

Get a free API key from [apify.com](https://apify.com) and set it:

```bash
export APIFY_API_KEY=apify_api_xxxxx
```

Add this to your `~/.zshrc` or `~/.bashrc` so it persists across sessions.

## Step 3: Install required Python package

```bash
pip3 install certifi
```

That's the only dependency.

## Step 4: Verify everything works

```bash
python3 .claude/skills/reddit-research/scripts/reddit_scraper.py \
  --keywords "test" \
  --search \
  --max-posts 2 \
  --comments-per-post 2 \
  --output-dir Reddit_To_Copy/setup_test
```

If it prints "Done. X posts with Y comments saved", you're good. Delete the `setup_test` folder and start using `/reddit-research`.
