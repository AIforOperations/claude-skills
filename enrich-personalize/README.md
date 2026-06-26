# enrich_personalize

A Claude Code skill that turns a lead CSV into per-prospect cold-email openers. Each opener references one real, researched, personal fact about the prospect and reads like a friend wrote it: lowercase, under 9 words, no questions, no sales pitch. For example:

```
hey will, rowed d1 crew at usd, respect!
hey wayne, named your grandson colt, love that!
hey joe, born, raised, and even mayor of burlingame, respect!
```

It researches each lead through a free -> Firecrawl -> Apify waterfall, verifies the signal is real and personal, writes the opener, and runs a final polish pass that rewords weak phrasing or drops a lead rather than ship a soft line.

## What's in this folder

```
.claude/skills/enrich_personalize/   the skill (SKILL.md, references/, scripts/, workflow/)
.claude/agents/lead-enricher.md      the worker agent the workflow calls
sample/leads_sample.csv              a tiny fake CSV for a no-cost smoke test
.env.example                         template for your API keys
```

## Prerequisites

Required:
- Claude Code with Workflow and sub-agent support
- Python 3 (standard library only, no pip installs)
- Node.js (the research workflow runs as JavaScript)

Optional but recommended (the skill still runs without them on the free WebFetch/WebSearch arm, just with a lower hit-rate):
- A Firecrawl API key, for sites that block a plain fetch
- An Apify account token plus the Apify MCP server, for premium signals (Google Maps owner-replies, LinkedIn posts)

## Setup

### Option A: let Claude do it

Open this folder in Claude Code and say:

> Read README.md and set up the enrich_personalize skill in this workspace.

Claude will copy the `.claude` contents into place, help you create your `.env`, register the Apify MCP server if you want it, and run the smoke test.

### Option B: manual

1. Copy the `.claude` contents into your workspace. This drops the skill into `.claude/skills/enrich_personalize` and the agent into `.claude/agents/lead-enricher.md` in one step:
   ```bash
   cp -R .claude/. /path/to/your-workspace/.claude/
   ```

2. Add your keys (optional). Copy the template to your workspace root and fill it in:
   ```bash
   cp .env.example /path/to/your-workspace/.env
   ```
   The `lead-enricher` agent loads this `.env` at runtime with `set -a; . ./.env; set +a`, so it must sit at the root of the workspace you run Claude from.

3. Register the Apify MCP server (only if you want the premium arm):
   ```bash
   claude mcp add apify --transport http https://mcp.apify.com \
     --header "Authorization: Bearer YOUR_APIFY_API_TOKEN"
   ```

4. Verify everything compiles:
   ```bash
   cd /path/to/your-workspace/.claude/skills/enrich_personalize
   python3 -m py_compile scripts/*.py && echo "python ok"
   node --check workflow/enrich.workflow.js && echo "workflow ok"
   ```

## Usage

Invoke the skill by name (`/enrich_personalize`) or by asking Claude to "personalize these leads" and pointing at a CSV. The flow is:

1. `scripts/prepare_leads.py` builds a work-list from your CSV (a row range, or every row missing an opener).
2. The workflow researches every lead in parallel: **enrich -> verify -> write -> polish**.
3. `scripts/write_lines.py` writes the openers back into the CSV, adding the `hey {name},` greeting and casual name/company columns.
4. `scripts/qa_lint.py` gates the result (no questions, no em-dash, no banned words, 9-word cap, greeting present).

Full step-by-step is in [.claude/skills/enrich_personalize/SKILL.md](.claude/skills/enrich_personalize/SKILL.md).

### Input

A CSV with at least: `company_name`, `website`, `city`, `state`, `contact_name`, `contact_title`, `niche`. The prepare step is schema-tolerant: it also accepts the common scraper column names (`company_website`, `company_city`, `company_state`, `first_name` + `last_name`, `job_title`, `industry`) and passes any person/company LinkedIn URLs through to the research.

### Output columns added

`personalization_v2` (the opener), `v2_qa_flag` (a note when a lead was dropped or polished), `casual_first_name`, `casual_company_name`.

### Smoke test

```bash
cd .claude/skills/enrich_personalize
python3 scripts/prepare_leads.py --csv ../../../sample/leads_sample.csv --rows 1-3 --out /tmp/leads.json
cat /tmp/leads.json   # should list 3 leads with all fields filled
```

The sample uses placeholder `example.com` sites, so it verifies the input format and the deterministic scripts. Real openers need real prospect data.

## How the polish pass works

After writing each opener, a final stage judges it and takes one action:
- **pass**: good line, left untouched (the default)
- **reword**: the fact is fine but the phrasing is clunky, rewritten cleanly
- **research**: the signal is weak, so one more research pass looks for something better
- **drop**: nothing better exists, so the lead ships with no opener rather than a soft one

## Tuning the voice

The rules live in plain markdown so you can edit them without touching code:
- [voice-rules.md](.claude/skills/enrich_personalize/references/voice-rules.md) — tone, the 9-word cap, banned words, the "soft opener" definition
- [signal-rules.md](.claude/skills/enrich_personalize/references/signal-rules.md) — what counts as a good signal and when to drop a lead

The example openers are tuned for real-estate and professional-services cold outreach, but the rules are general. Adjust the examples in those two files to fit your own niche.

## What this skill does not do

It writes openers only. Email verification, list upload, and sending are deliberately left out. Bring your own tools for those.

## Costs and limits

The workflow runs about 8 research agents at once (capped at the lesser of 16 and your CPU cores minus 2). Each lead does real web research, so a batch of 50 takes roughly 15 to 20 minutes. Firecrawl and Apify bill to your own accounts; the waterfall stops at the first strong signal to keep that spend low (in a typical run most leads are solved on the free arm before Firecrawl or Apify are ever called).
