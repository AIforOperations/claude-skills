# enrich_personalize

A Claude Code skill that turns a lead CSV into per-prospect cold-email openers. Each opener references one real, researched, personal fact about the prospect and reads like a friend wrote it: lowercase, under 9 words, no questions, no sales pitch. For example:

```
hey glenn, took over your dad's business in 1991, respect!
hey harry, tesco delivery driver to tile business owner, respect!
hey lewis, cu-plas started in a back street shed, wow!
```

The pipeline is cache-first: it bulk pre-fetches every prospect's LinkedIn bio (one cheap Apify run) and website pages (free parallel HTTP), then batched agents pick the best personal signal from the cache, verify it, write the opener, and an opus polish pass rewords weak phrasing or drops a lead rather than ship a soft line. Leads whose contact turns out to have left the company are dropped automatically with the reason recorded.

## What's in this folder

```
.claude/skills/enrich_personalize/   the skill (SKILL.md, references/, scripts/)
.claude/agents/lead-enricher.md      the worker agent the workflow calls
sample/leads_sample.csv              a tiny fake CSV for a no-cost smoke test
.env.example                         template for your API keys
```

## Prerequisites

Required:
- Claude Code with Workflow and sub-agent support
- Python 3 (standard library only, no pip installs)

Recommended:
- An Apify account token — powers the bulk LinkedIn bio pre-fetch, the skill's main signal source (~$4 per 1,000 profiles)

Optional:
- A Firecrawl API key, used only for sites that block a plain fetch

## Setup

### Option A: let Claude do it (recommended)

Clone this repo, open the folder in Claude Code, and say:

> Read README.md and set up the enrich_personalize skill in this workspace.

Claude will copy the `.claude` contents into place, ask you for your API keys and write them into `.env` (never committed), and run the smoke test. On every later run the skill checks this repo for a newer version and pulls it before starting.

### Option B: manual

1. Copy the `.claude` contents into your workspace:
   ```bash
   cp -R .claude/. /path/to/your-workspace/.claude/
   ```

2. Add your keys. Copy the template to your workspace root and fill it in:
   ```bash
   cp .env.example /path/to/your-workspace/.env
   ```
   The scripts load this `.env` at runtime, so it must sit at the root of the workspace you run Claude from.

3. Verify everything compiles:
   ```bash
   cd /path/to/your-workspace/.claude/skills/enrich_personalize
   python3 -m py_compile scripts/*.py && echo "python ok"
   ```

## Usage

Invoke the skill by name (`/enrich_personalize`) or by asking Claude to "personalize these leads" and pointing at a CSV. The flow is:

1. `scripts/prefetch_sites.py` bulk-fetches every prospect's homepage + about/team pages (free, ~30s per 100 leads).
2. `scripts/prefetch_linkedin.py` bulk-fetches every prospect's LinkedIn bio via one Apify run (~$4 per 1,000).
3. `scripts/build_workflow.py` generates the run script; the workflow then runs batched **enrich -> verify+write -> polish -> rescue** over the cache.
4. `scripts/write_lines.py` writes the openers back into the CSV, adding the `hey {name},` greeting and casual name/company columns.
5. `scripts/qa_lint.py` gates the result (no questions, no em-dash, no banned words, 9-word cap, greeting present).

Full step-by-step is in [.claude/skills/enrich_personalize/SKILL.md](.claude/skills/enrich_personalize/SKILL.md).

### Input

A CSV with contact + company columns. The scripts are schema-tolerant and accept the common scraper column names (`company_name`/`company`, `website`/`company_website`, `first_name`+`last_name` or `contact_name`, `contact_title`/`job_title`, `city`, `state`/`country`, `niche`/`industry`, `linkedin_url`/`linkedin`). A per-person LinkedIn URL column matters most: it is where the majority of kept signals come from.

### Output columns added

`personalization_v2` (the opener), `v2_qa_flag` (a note when a lead was dropped or polished), `casual_first_name`, `casual_company_name`. All greeting text is lowercase, including the name.

### Smoke test

```bash
cd .claude/skills/enrich_personalize
python3 scripts/prefetch_sites.py ../../../sample/leads_sample.csv --rows 1-3
```

The sample uses placeholder `example.com` sites, so it verifies the input format and the deterministic scripts. Real openers need real prospect data.

## What to expect

On a typical B2B list with LinkedIn URLs: roughly 78-80% of leads get a verified opener, ~6 minutes and ~18 agents per 100 leads. The rest are dropped with a recorded reason — no signal found, or a trap (contact left the company, wrong-person LinkedIn match, acquired/renamed firm). Dropped leads are deliberate: a blank opener beats a wrong one landing in a stranger's inbox.

## Tuning the voice

The rules live in plain markdown so you can edit them without touching code:
- [voice-rules.md](.claude/skills/enrich_personalize/references/voice-rules.md) — tone, the 9-word cap, banned words, the "soft opener" definition
- [signal-rules.md](.claude/skills/enrich_personalize/references/signal-rules.md) — what counts as a good signal and when to drop a lead

## What this skill does not do

It writes openers only. Email verification, list upload, and sending are deliberately left out. Bring your own tools for those.

## Costs and limits

Apify bills to your own account: ~$4 per 1,000 profiles for the bio pre-fetch. Firecrawl is called only as a last-resort fallback. Model usage runs through your Claude Code session (~9k tokens per lead). For lists over ~300 rows, run in slices of 100-200 and check the first slice before continuing.
