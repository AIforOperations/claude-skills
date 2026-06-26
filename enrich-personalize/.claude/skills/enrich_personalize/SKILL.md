---
name: enrich_personalize
description: Enrich a lead CSV with one researched personal signal per prospect and write a short, friend-to-friend cold-email opener (lowercase, under 9 words, no questions) starting with "hey {casual first name},". Use when asked to personalize a lead list, add opener lines, or enrich prospects for cold outreach.
allowed-tools: Bash, Read, Write, Workflow, Agent
---

# enrich_personalize

Turns a lead CSV into per-prospect cold-email openers. Each line references one real, researched, personal fact and reads like a friend wrote it.

The voice rules and the signal rules live in `references/` so they never drift between runs. Read them before generating any line. The parallel research runs through a workflow that uses the `lead-enricher` agent.

## Inputs
A CSV with at least: `company_name`, `website`, `city`, `state`, `contact_name`, `contact_title`, `niche`. `prepare_leads.py` is schema-tolerant: it also accepts the leads-finder / `scrape_leads` column names (`company_website`, `company_city`, `company_state`, `first_name`+`last_name`, `job_title`, `industry`) and passes the person + company LinkedIn URLs through to the research agent. Output columns added: `personalization_v2`, `v2_qa_flag`, `casual_first_name`, `casual_company_name`.

## Run it

1. **Read the rules first:** `references/signal-rules.md` and `references/voice-rules.md`. These are binding.

2. **Pick the leads.** Build the work-list JSON:
   ```bash
   python3 scripts/prepare_leads.py --csv <CSV> --rows 26-69 --out /tmp/leads.json    # or omit --rows to take every row whose personalization_v2 is empty
   ```

3. **Fan out the research (workflow).** Read `/tmp/leads.json`, then launch the workflow with that array as `args`:
   `Workflow({ scriptPath: "<skill>/workflow/enrich.workflow.js", args: <parsed leads array> })`
   The workflow runs enrich -> verify -> write -> **polish** per lead in parallel, returns an array of
   `{row, contact_name, first_name, signal, source, confidence, arm, flag, keep, line}`. `line` has NO greeting.
   The **polish** stage auto-fixes soft openers (see Conventions): rewords clunky phrasing, re-researches a weak
   signal for something better, or drops it. The action is recorded in `flag` (`polish reword` / `polish research` / `polish drop`).
   Pass the work-list inline as the `args` array; the workflow also tolerates a stringified array.
   Workflows spend tokens and can spawn many agents, so confirm with the user before launching on a large list.

4. **Save the result** to `/tmp/signals.json` (the array, lines without greeting).

5. **Write the CSV** (adds greeting + casual columns, backs up first):
   ```bash
   python3 scripts/write_lines.py --csv <CSV> --signals /tmp/signals.json
   ```

6. **Gate on QA.** This must pass before the file is considered done:
   ```bash
   python3 scripts/qa_lint.py --csv <CSV> --rows 1-50    # scope to the slice you ran; omit --rows to check the whole file
   ```
   For any FAIL, fix the line (re-run that single lead, or hand-edit the signal entry) and re-run steps 5-6.

## Conventions
- Greeting format: `hey {casual_first_name}, {line}` — all lowercase. `write_lines.py` adds it; never bake it into the line.
- Casual name + casual company derivation: `scripts/casual.py` (nickname map + company shortener). Pass a `casual_first_name` / `casual_company_name` override in the signals entry when the auto-rule is wrong (e.g. ConsensYs, OMNI, ZED).
- Rows with no contact get no greeting; leave them flagged. Rows with templated/unverifiable bios get a blank line and a flag, never a guessed personalization.
- **Never keep a blank-personalization lead in the final/send list.** Drop it (or hold until a real signal is found) before upload.
- **Soft openers are auto-fixed** by the workflow's polish stage. A line is "soft" when it is technically valid but weak: (a) **clunky phrasing** that is awkward to say aloud (`you live in the socal open water`), (b) a **weak signal** — generic tenure on a name-only bio, or built on an unverified/wrong contact, or not genuinely personal. Polish rewords (a), re-researches (b) for a better personal fact, and drops it if nothing better exists. It defaults to leaving good lines untouched. A polished or dropped line carries `polish reword` / `polish research` / `polish drop` in its `flag`.

## Sources / tools
`references/sources.md` has the Firecrawl endpoints + key location and the Apify actor IDs.
