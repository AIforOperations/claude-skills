---
name: reddit-research
description: Scrape Reddit via Apify, generate ad concepts, and write MSL ad copy. Trigger on "reddit research", "scrape reddit", "mine reddit", "reddit to ads", or any request involving Reddit data for ad creation.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebSearch
---

# Reddit Research Pipeline

Scrape Reddit → Generate concepts → Write MSL ad copy.

## Stage 1: SCRAPE

### Two Modes

**Mode A — Subreddit search (preferred when subreddits are obvious):**
```bash
python3 .claude/skills/reddit-research/scripts/reddit_scraper.py \
  --subreddits "ADHD,adhdwomen" \
  --keywords "can't sleep,racing thoughts" \
  --output-dir Reddit_To_Copy/<folder_name>
```

**Mode B — Global search (when subreddits are unclear or not mentioned):**
```bash
python3 .claude/skills/reddit-research/scripts/reddit_scraper.py \
  --search \
  --keywords "ADHD supplements sleep" \
  --output-dir Reddit_To_Copy/<folder_name>
```

### Choosing the Mode

1. **User specifies subreddits** → Mode A. Use their subreddits directly.
2. **Topic found in `subreddit_map.md`** → Mode A. Use the mapped subreddits.
3. **Topic NOT in the map** → Run the Subreddit Discovery process (see below), then Mode A.
4. **Discovery fails or topic is too broad** → Mode B (global search).

### Keyword Rules (CRITICAL)

When YOU are choosing keywords (not the user):

1. **Broad, common words.** "sleep", "melatonin", "can't sleep" will return results. "ADHD-induced-insomnia-supplement-failure" will not.
2. **1-3 words max per keyword.** Reddit search works best with short terms.
3. **Multiple short keywords** instead of one long phrase. Use `--keywords "sleep,supplements,melatonin"` not `--keywords "ADHD sleep supplement problems"`.
4. **No jargon or compound phrases** that real users wouldn't type.
5. **Limit total search URLs.** Each subreddit x keyword combination = 1 URL. Keep total URLs under 6 to avoid Apify timeouts. Use max 2-3 subreddits with 1-2 keywords. If you need broader coverage, run multiple smaller scrapes.

### Zero Results Protocol

If a scrape returns 0 posts:
1. Tell the user: "No results for [keywords] in [subreddits]. Trying broader terms."
2. Broaden keywords — drop modifiers, use root words. "magnesium glycinate sleep" → "magnesium", "sleep supplements"
3. If subreddit search returned nothing, try global search as fallback.
4. If still nothing after 2 attempts, ask the user what terms their audience actually uses.

Never retry the same failing keyword.

### Defaults

| Param | Default | Notes |
|---|---|---|
| --max-posts | 5 | Posts per search. User can override. |
| --comments-per-post | 10 | Comments are where the gold language lives. |
| --sort | relevance | Options: relevance, hot, top, new, comments |
| --time-filter | month | Options: hour, day, week, month, year, all |

If the user wants more or fewer posts, pass it as a CLI argument (e.g., `--max-posts 20`). Do NOT edit the script to change defaults.

### Output Folder Naming

All output goes to `Reddit_To_Copy/<folder_name>/`. Name the folder after the keywords or topic:
- `adhd_melatonin/`
- `fibro_morning_pain/`
- `quit_smoking_cravings/`

If a folder already exists, append a number: `adhd_melatonin_2/`, `adhd_melatonin_3/`

### Engagement Tags

The script tags every post in the output:
- **[HIGH ENGAGEMENT]** — 100+ upvotes or 50+ comments
- **[MEDIUM ENGAGEMENT]** — 20+ upvotes or 10+ comments
- **[LOW ENGAGEMENT]** — below those thresholds

No posts are dropped. Tags tell Stage 2 what to prioritize.

## Stage 2: ANALYZE (Concept Engine)

**This runs immediately after Stage 1. No pause.**

1. Read the scraped data: `<output_dir>/01_raw_data.md`
2. Read the concept engine prompt: `references/concept-engine-prompt.md`
3. Silently absorb the language, pain points, paradoxes, failed solutions, exact phrases. Prioritize HIGH ENGAGEMENT posts.
4. Generate concepts following the archetype distribution from the prompt.
5. Write the full concept bank to `<output_dir>/02_concepts.md`
6. Present the Top 10 priority concepts to the user with conversion rationale.

### Output Format

```
# Ad Concepts — [Avatar] / [Product]
**Source:** [subreddits scraped]
**Generated:** [date]
**Total concepts:** [count]

---

## Top 10 Priority Concepts

[numbered list with archetype tag, title, concept, and conversion rationale]

---

## Full Concept Bank

[all concepts in numbered format with archetype tags]
```

## Stage 3: WRITE COPY (Native MSL)

**Pause here. Ask the user which concept to develop.**

1. Read the MSL writing prompt: `references/msl-adhd-prompt.md`
2. Read the language bank: `references/msl-adhd-reddit-extraction.md`
3. Read the selected concept from `02_concepts.md`
4. Follow the MSL prompt's full workflow: select narrator, generate 10+ hooks, present for selection, write complete ad (1200-2000 words)
5. The ad must read as one continuous story — no visible section breaks
6. Write to `<output_dir>/03_msl_copy_v[N].md`
7. Tell the user where the file was saved and show a brief summary of the ad (narrator, hook format, word count)

## Workflow Summary

```
1. User gives input → check subreddit_map.md → if new topic, web search for subreddits
2. Confirm subreddits/keywords with user
3. Scrape → immediately generate concepts → present Top 10
4. User picks concept → write MSL ad copy
5. Update subreddit_map.md if new topic produced good results
6. (CLAUDE.md handles chaining to headlines/image prompts)
```

## Subreddit Discovery

### Step 1: Check the map
Read `subreddit_map.md` (in this skill folder). If the topic matches an existing entry, use those subreddits.

### Step 2: New topic — web search
If the topic is NOT in the map:
1. Web search: "best subreddits for [topic]" or "reddit communities for [topic]"
2. Pick 2-4 most relevant, active subreddits
3. Confirm with the user: "I found r/X, r/Y, r/Z for this topic. Look good?"
4. If user corrects ("use r/A instead"), use their picks

### Step 3: Update the map
After the scrape returns good data (not 0 results), add the new entry to `subreddit_map.md`:
```
## [Topic Name] (added YYYY-MM-DD)
- **Subreddits:** r/X, r/Y, r/Z
- **Keywords:** keyword1, keyword2
- **Notes:** [how it was found — web search, user suggested, etc.]
```

Do NOT update the map if:
- The scrape returned 0 results (bad subreddit picks)
- The user said the results were off-topic
- It was a one-off search the user won't repeat

## Rules

1. Preserve exact language. Never paraphrase Reddit quotes.
2. Confirm subreddits/keywords before scraping.
3. No pause between scrape and concepts. Go straight through.
4. Pause before writing MSL copy. Always ask which concept.
5. After MSL copy is saved, stop. CLAUDE.md handles chaining to headlines/image prompts.
6. AutoModerator comments are filtered by the script automatically.
