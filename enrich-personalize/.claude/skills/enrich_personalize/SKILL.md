---
name: enrich_personalize
description: Enrich a lead CSV with one researched personal signal per prospect and write a short, friend-to-friend cold-email opener (lowercase, under 9 words, no questions) starting with "hey {casual first name},". Use when asked to personalize a lead list, add opener lines, or enrich prospects for cold outreach.
allowed-tools: Bash, Read, Write, Workflow, Agent
---

# enrich_personalize

Turns a lead CSV into per-prospect cold-email openers. Each line references one real, researched, personal fact and reads like a friend wrote it.

The voice rules and the signal rules live in `references/` so they never drift between runs. Read them before generating any line.

## Check for updates first

Before every run, check whether the skill repo has a newer version and pull it automatically:

```bash
git -C <repo-root> fetch --quiet && git -C <repo-root> status -sb | head -1
# if behind: git -C <repo-root> pull --ff-only
```

If the pull brings changes, re-read this SKILL.md before continuing — the pipeline may have changed.

## First-run setup

If `.env` does not exist in the workspace root (or `APIFY_API_TOKEN` is not set in the environment), STOP and ask the user for keys before doing anything else:

1. **APIFY_API_TOKEN** (strongly recommended) — powers the bulk LinkedIn bio pre-fetch, the skill's main signal source (~$4 per 1,000 profiles). Get it at https://console.apify.com/account/integrations
2. **FIRECRAWL_API_KEY** (optional) — used only when a prospect's site blocks a plain fetch AND LinkedIn gave nothing. The skill runs without it, just with a slightly lower yield. Get it at https://www.firecrawl.dev

Write the keys the user provides into `.env` in the workspace root (copy `.env.example`). Never commit `.env`, never print the key values back, and never hardcode keys anywhere.

Then run a smoke test on the bundled sample before touching real data:

```bash
python3 <skill>/scripts/prefetch_sites.py sample/leads_sample.csv --rows 1-3
```

## Inputs

A CSV with contact + company columns. All scripts are schema-tolerant and accept common name variants: `company_name`/`company`, `website`/`company_website`, `first_name`+`last_name` or `contact_name`, `contact_title`/`job_title`, `city`, `state`/`country`, `niche`/`industry`, `linkedin_url`/`linkedin`. A per-person LinkedIn URL column dramatically raises yield — most kept signals come from it.

## Run it

The pipeline is cache-first: bulk pre-fetch everything once with cheap deterministic scripts, then let batched agents read the cache instead of fetching the web per lead.

1. **Read the rules:** `references/signal-rules.md` and `references/voice-rules.md`. Binding.

2. **Pre-fetch websites** (free, ~30s per 100 leads):
   ```bash
   python3 <skill>/scripts/prefetch_sites.py <CSV> --rows 1-100 --cache-dir ./enrich_cache
   ```

3. **Pre-fetch LinkedIn bios via Apify** (~$4 per 1,000 profiles, ~1 min per 100):
   ```bash
   set -a; . ./.env; set +a
   python3 <skill>/scripts/prefetch_linkedin.py <CSV> --rows 1-100 --cache-dir ./enrich_cache
   ```
   Skip this step only if the CSV has no LinkedIn column or the user declines the cost.

4. **Generate and launch the workflow:**
   ```bash
   python3 <skill>/scripts/build_workflow.py <CSV> --rows 1-100 --cache-dir ./enrich_cache -o ./run.workflow.js
   ```
   Then `Workflow({ scriptPath: "<abs path>/run.workflow.js" })`. Stages: batched enrich (sonnet, 1 agent/10 leads, reads cache, live fallback only for thin caches) -> batched verify+write (sonnet, 1/15, judgment + opener in one pass) -> batched polish (opus, 1/40, no tools) -> targeted rescue (sonnet + tools, only polish-tagged rows, typically <5%).
   Expect roughly 78-80% of leads kept, ~9k tokens per lead, ~6 min per 100 leads. Workflows spend tokens and spawn agents, so confirm with the user before launching on a large list. For lists over ~300 rows, run in slices of 100-200 and confirm the first slice looks right before continuing.

5. **Save the result** array to `/tmp/signals.json`.

6. **Write the CSV** (adds greeting + casual columns, backs up first):
   ```bash
   python3 <skill>/scripts/write_lines.py --csv <CSV> --signals /tmp/signals.json
   ```

7. **Gate on QA.** Must pass before the file is done:
   ```bash
   python3 <skill>/scripts/qa_lint.py --csv <CSV> --rows 1-100
   ```
   For any FAIL, fix the line (re-run that single lead or hand-edit the signal entry) and re-run steps 6-7.

## Conventions

- Greeting format: `hey {casual_first_name}, {line}` — all lowercase, including the name. `write_lines.py` adds it; never bake it into the line.
- Casual name + casual company derivation: `scripts/casual.py` (nickname map + company shortener). Pass a `casual_first_name` / `casual_company_name` override in the signals entry when the auto-rule is wrong.
- Keep-rule: any legit, verified, reasonable personal fact is a keep — including plain founder/tenure facts ("MD since 2005"). A plain-but-true fact beats no personalization. Drop only: wrong person / left the company, stale (>~12mo) and not timeless, politically or religiously charged, negative, or unverifiable.
- Dropped rows keep their reason in the flag column (`verify rejected: ...`, `no signal`). **Never keep a blank-personalization lead in the final send list**, and never re-run leads whose flag shows a wrong-person/left-company trap — those are dead, not retryable.
- Model roles are fixed and load-bearing: sonnet for enrich/verify/write/rescue, opus for polish. Do not downgrade enrich or verify to haiku (misses wrong-person traps) and do not drop stage effort below medium for judgment stages.

## Sources / tools

`references/sources.md` has the Firecrawl endpoints and the Apify actor IDs the pre-fetch scripts use.
