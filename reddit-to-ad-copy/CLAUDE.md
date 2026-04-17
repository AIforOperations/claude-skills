# CLAUDE.md

## Workspace

This is a Reddit-to-ad-copy research workspace. All output goes to `Reddit_To_Copy/`.

## Products & Avatars

Configure your products and target avatars here. Example structure:

### Example Product — Sleep Gummies
- **Price:** $39 (NEVER mention in ad copy)
- **Form:** Gummies
- **Guarantee:** 60-day money-back
- **Ingredients:** Magnesium Glycinate (350mg), L-Theanine (200mg), 5-HTP (200mg), Valerian Root (600mg), Passionflower (400mg)
- **Key differentiator:** Melatonin-free

**Avatars:**
- **ADHD** (primary) — Female 30+, diagnosed or self-identified. Tone: self-deprecating, wry, "one of us."
- **Fibromyalgia** — Morning pain is the primary angle. Tone: suffering, determination.
- **Anxious Insomniac** — 3AM wake-ups, racing thoughts.

Add your own products and avatars following this format.

## Skills

- `/reddit-research` — Scrape Reddit via Apify, generate ad concepts, and write MSL ad copy
- `/headline-gen` — Generate 3-5 Facebook ad headlines from MSL copy
- `/image-prompts` — Generate 8-12 text-to-image prompts from MSL copy

## Workflow Chaining

After `/reddit-research` completes Stage 3 (MSL copy is written), ask:

> "Ad copy is done. Want me to generate headlines and image prompts for this ad?"

Each skill can also be invoked independently at any time.

## Output Convention

All output goes to `Reddit_To_Copy/<folder_name>/`

Folder naming: `adhd_melatonin/`, `fibro_morning_pain/`, `quit_smoking_cravings/`

## Shared References

All prompt references live in `references/` at the project root. Skills read from there.

## Rules

1. **Preserve exact language.** Never paraphrase Reddit quotes. The value is in verbatim words.
2. **Confirm before scraping.** Always show the planned subreddits/keywords and wait for approval.
3. **No pausing between scrape and concepts.** Once raw data is scraped, immediately generate concepts and present the Top 10.
4. **Pause before writing copy.** Always ask which concept to develop before writing MSL copy.
5. **Pause before headlines/images.** Always ask after MSL copy is done.
