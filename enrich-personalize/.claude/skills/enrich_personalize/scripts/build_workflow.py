#!/usr/bin/env python3
"""Generate the enrichment run script (batched architecture).

Pipeline the generated workflow runs:
  Enrich       sonnet med  1 agent / 10 leads   reads pre-fetched cache, live fallback for thin ones
  VerifyWrite  sonnet med  1 agent / 15 signals judgment + opener line in one pass (may Read cache)
  Polish       opus   med  1 agent / 40 lines   batched QA: pass/reword/tag-for-research/drop
  Rescue       sonnet med  1 agent / lead       tools-on re-research, ONLY polish-tagged rows

Keep-rule: any legit verified reasonable personal fact is a keep, including plain
founder/tenure facts. Drop only: wrong person / left company, stale non-timeless,
political/religious, negative, unverifiable.

Usage: python3 build_workflow.py <leads.csv> --rows 1-100 [--cache-dir ./enrich_cache] [-o run.workflow.js]
"""
import csv, json, argparse
from pathlib import Path

ENRICH_BATCH = 10
VW_BATCH = 15
POLISH_BATCH = 40

COLS = dict(
    company=("company_name", "company"),
    website=("website", "company_website", "domain"),
    first=("first_name",), last=("last_name",),
    contact=("contact_name",),
    title=("contact_title", "job_title", "title"),
    city=("city", "company_city"), state=("state", "company_state", "country"),
    niche=("niche", "industry"),
    linkedin=("linkedin_url", "linkedin", "person_linkedin_url"),
)


def pick(row, key):
    for c in COLS[key]:
        if c in row and (row[c] or "").strip():
            return row[c].strip()
    return ""


VOICE = r"""Write ONE cold-email opener line built from the signal. HARD RULES (a line breaking any rule is invalid):
- all lowercase
- references the specific signal, friend-to-friend tone
- NO question mark and NO leading-question format (statements only)
- under 9 words (the "hey <name>," greeting is added later, do NOT include it)
- not salesy: no mention of a service, software, meeting, call, or "we help"
- add a short casual closer (", that's super cool!", ", love that!", ", respect!", ", wow!", ", that's amazing!") ONLY if the line is otherwise flat; if the verb already carries warmth ("loved your...", "love that...") add no closer
- recent signals only: never frame a 3+-year-old award/news as current; only fresh items, else a timeless founder/tenure/hobby fact
- family firm a parent founded: frame as carrying the legacy forward warmly, never corporate
- charities/programs in plain words, never a brand/program name that reads as a product
- no em-dashes; no filler words (seamlessly, leverage, robust, streamline, elevate, empower, unlock, comprehensive, optimize, transformative)"""

TEMPLATE = '''export const meta = {{
  name: 'enrich-personalize-v2',
  description: 'Batched enrich/verify-write (sonnet), batched opus polish, targeted rescue',
  phases: [
    {{ title: 'Enrich', detail: '1 agent per 10 leads: read caches, pick best personal signal each', model: 'sonnet' }},
    {{ title: 'VerifyWrite', detail: '1 agent per 15: judge signal + write opener in one pass', model: 'sonnet' }},
    {{ title: 'Polish', detail: 'batched final QA: pass/reword/tag-for-research/drop', model: 'opus' }},
    {{ title: 'Rescue', detail: 'tools-on re-research, only polish-tagged rows', model: 'sonnet' }},
  ],
}}

const LEADS = {leads_json}
const VOICE = {voice_json}
const ENRICH_OUT = {enrich_json}
const VW_OUT = {vw_json}
const POLISH_OUT = {polish_json}
const RESCUE = {rescue_json}
const EB = {enrich_batch}, VB = {vw_batch}, PB = {polish_batch}

const byRow = new Map(LEADS.map((l) => [l.row, l]))
const chunk = (arr, n) => {{ const c = []; for (let i = 0; i < arr.length; i += n) c.push(arr.slice(i, i + n)); return c }}
const leadMeta = (l) => JSON.stringify({{ row: l.row, company: l.company, contact: l.contact, title: l.title, city: l.city, state: l.state, website: l.website, linkedin: l.linkedin, li_cache: l.li_cache, site_cache: l.site_cache }})

// ---- stage 1: batched enrich ----
const enrichRes = await parallel(chunk(LEADS, EB).map((batch, bi) => () => agent(
  `You research ${{batch.length}} B2B prospects and return the single best PERSONAL signal for EACH, for friend-to-friend cold-email openers.\\n\\n` +
  'For EVERY prospect: Read its two cache files (LinkedIn bio/about/experience/volunteering + website about/team pages), then pick the best PERSONAL signal ' +
  '(bio quirk/hobby > founder/family/tenure story > community/volunteer role > local recognition). A plain founder/tenure fact IS acceptable when nothing richer exists. ' +
  'AVOID pure business-service facts when anything personal is available.\\n' +
  'ONLY if a prospect\\'s caches are empty/thin: do ONE quick live pass for that prospect (WebSearch the person, WebFetch the site). Firecrawl only if the site cache says blocked AND LinkedIn cache is empty. No Apify (already pre-fetched).\\n' +
  'Watch for traps and note them in flag: person left the company / works elsewhere now, same-name collisions, deceased founders. Never invent a fact; if nothing verifiable, arm=none, confidence=L.\\n\\n' +
  'PROSPECTS:\\n' + batch.map(leadMeta).join('\\n') + '\\n\\nReturn one entry for EVERY row listed.',
  {{ label: `enrich:b${{bi + 1}}`, phase: 'Enrich', agentType: 'lead-enricher', model: 'sonnet', effort: 'medium', schema: ENRICH_OUT }},
)))
const signals = []
for (const r of enrichRes.filter(Boolean)) for (const s of r.signals || []) if (byRow.has(s.row)) signals.push(s)
for (const l of LEADS.filter((l) => !signals.some((s) => s.row === l.row)))
  signals.push({{ row: l.row, signal: '', source: '', confidence: 'L', arm: 'none', flag: 'enrich returned nothing for this row' }})
log(`enrich: ${{signals.filter((s) => s.arm !== 'none').length}}/${{LEADS.length}} signals found`)

// ---- stage 2: batched verify+write ----
const vwRes = await parallel(chunk(signals.filter((s) => s.arm !== 'none'), VB).map((batch, bi) => () => agent(
  `You do TWO jobs for EACH of ${{batch.length}} cold-email signals: (1) adversarial verify, (2) if kept, write the opener line.\\n\\n` +
  'VERIFY - this is JUDGMENT, not research. No web tools. You MAY Read the listed cache files to confirm the claimed fact actually appears in the cited material. ' +
  'KEEP any legit, verified, reasonable personal fact - including plain founder/tenure facts; a plain-but-true fact beats no personalization. ' +
  'DROP ONLY when: wrong person / left the company (per flag or cache), stale (>~12mo) AND not a timeless founder/tenure/hobby fact, politically or religiously charged, negative, or unverifiable against cache and flags.\\n\\n' +
  'WRITE - for every kept signal:\\n' + VOICE + '\\n\\n' +
  'ITEMS:\\n' +
  batch.map((s) => {{ const l = byRow.get(s.row); return JSON.stringify({{ row: s.row, company: l.company, contact_expected: l.contact, signal: s.signal, source: s.source, confidence: s.confidence, flag: s.flag || 'none', li_cache: l.li_cache, site_cache: l.site_cache }}) }}).join('\\n') +
  '\\n\\nReturn a verdict for EVERY row listed (keep=false rows: empty line, give reason).',
  {{ label: `vw:b${{bi + 1}}`, phase: 'VerifyWrite', model: 'sonnet', effort: 'medium', schema: VW_OUT }},
)))
const vmap = new Map()
for (const r of vwRes.filter(Boolean)) for (const v of r.results || []) vmap.set(v.row, v)
const done = signals.map((s) => {{
  const base = {{ row: s.row, contact_name: s.contact_name || '', first_name: s.first_name || '',
    signal: s.signal, source: s.source, confidence: s.confidence, arm: s.arm }}
  if (s.arm === 'none') return {{ ...base, keep: false, line: '', flag: (s.flag || '') + '; no signal' }}
  const v = vmap.get(s.row)
  if (!v) return {{ ...base, keep: false, line: '', flag: (s.flag ? s.flag + '; ' : '') + 'verify-write returned no verdict' }}
  if (!v.keep) return {{ ...base, keep: false, line: '', flag: (s.flag ? s.flag + '; ' : '') + 'verify rejected: ' + (v.reason || '') }}
  return {{ ...base, keep: true, line: v.line, flag: s.flag || '' }}
}})
const keptRows = done.filter((x) => x.keep && x.line)
log(`verify+write: ${{keptRows.length}}/${{LEADS.length}} lines kept`)

// ---- stage 3: batched opus polish ----
const polishOut = await parallel(chunk(keptRows, PB).map((ch, ci) => () => agent(
  'FINAL POLISH pass on a batch of cold-email openers. For EACH item pick ONE action. Default to pass - only act on a clear problem.\\n' +
  '- pass: reads smoothly AND built on a specific verified fact (plain founder/tenure facts are fine)\\n' +
  '- reword: fact solid, phrasing clunky/unnatural -> rewrite cleanly, SAME fact\\n' +
  '- research: the fact looks wrong-person / contradicted per the flag -> tag it; a separate agent will re-research. Return the original line.\\n' +
  '- drop: no salvageable fact -> empty line\\n\\n' + VOICE + '\\n\\nITEMS:\\n' +
  ch.map((x) => JSON.stringify({{ row: x.row, line: x.line, fact: x.signal, flag: x.flag || 'none' }})).join('\\n') +
  '\\n\\nReturn a verdict for EVERY row listed.',
  {{ label: `polish:b${{ci + 1}}`, phase: 'Polish', model: 'opus', effort: 'medium', schema: POLISH_OUT }},
)))
const pmap = new Map()
for (const p of polishOut.filter(Boolean)) for (const v of p.results || []) pmap.set(v.row, v)
for (const x of keptRows) {{
  const v = pmap.get(x.row)
  if (!v || v.action === 'pass') continue
  if (v.action === 'reword' && v.line) {{ x.line = v.line; x.flag = (x.flag ? x.flag + '; ' : '') + 'polish reword' }}
  else if (v.action === 'drop') {{ x.keep = false; x.line = ''; x.flag = (x.flag ? x.flag + '; ' : '') + 'polish drop: ' + (v.note || '') }}
  else if (v.action === 'research') x._rescue = true
}}

// ---- stage 4: targeted rescue ----
const rescueRows = keptRows.filter((x) => x._rescue)
log(`rescue pass: ${{rescueRows.length}} rows tagged`)
if (rescueRows.length) {{
  await parallel(rescueRows.map((x) => () => {{
    const l = byRow.get(x.row)
    return agent(
      'The current fact for this prospect was judged WEAK or wrong. Do ONE more research pass (free web -> Firecrawl if needed) for a better PERSONAL fact, then write a fresh line from it. If nothing better exists, action=drop.\\n\\n' +
      VOICE + '\\n\\n' +
      `weak fact: ${{x.signal}}\\ncurrent line: ${{x.line}}\\nflag: ${{x.flag || 'none'}}\\n` +
      `company: ${{l.company}} | ${{l.contact}} | ${{l.title}} | ${{l.city}}, ${{l.state}} | ${{l.website}} | ${{l.linkedin}}`,
      {{ label: `rescue:r${{x.row}}`, phase: 'Rescue', agentType: 'lead-enricher', model: 'sonnet', effort: 'medium', schema: RESCUE }},
    ).then((r) => {{
      if (!r || r.action === 'drop' || !r.line) {{ x.keep = false; x.line = ''; x.flag = (x.flag ? x.flag + '; ' : '') + 'rescue drop' }}
      else {{ x.line = r.line; x.signal = r.signal || x.signal; x.source = r.source || x.source; x.flag = (x.flag ? x.flag + '; ' : '') + 'polish research' }}
    }})
  }}))
}}

log(`done: ${{done.filter((x) => x.keep).length}}/${{LEADS.length}} usable`)
return done
'''

ENRICH_OUT_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["signals"],
    "properties": {"signals": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["row", "signal", "source", "confidence", "arm"],
        "properties": {
            "row": {"type": "integer"},
            "contact_name": {"type": "string"}, "first_name": {"type": "string"},
            "signal": {"type": "string", "description": "one specific verifiable PERSONAL fact"},
            "source": {"type": "string"},
            "confidence": {"type": "string", "enum": ["H", "M", "L"]},
            "arm": {"type": "string", "enum": ["cache-linkedin", "cache-site", "free", "firecrawl", "none"]},
            "flag": {"type": "string"},
        }}}},
}
VW_OUT_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["results"],
    "properties": {"results": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["row", "keep", "line"],
        "properties": {
            "row": {"type": "integer"}, "keep": {"type": "boolean"},
            "line": {"type": "string", "description": "opener WITHOUT greeting; empty when keep=false"},
            "reason": {"type": "string", "description": "why dropped; empty when kept"},
        }}}},
}
POLISH_OUT_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["results"],
    "properties": {"results": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["row", "action", "line"],
        "properties": {
            "row": {"type": "integer"},
            "action": {"type": "string", "enum": ["pass", "reword", "research", "drop"]},
            "line": {"type": "string"}, "note": {"type": "string"},
        }}}},
}
RESCUE_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["action", "line"],
    "properties": {
        "action": {"type": "string", "enum": ["replaced", "drop"]},
        "line": {"type": "string"}, "signal": {"type": "string"}, "source": {"type": "string"},
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--rows", required=True, help="1-based data-row range like 1-100")
    ap.add_argument("--cache-dir", default="./enrich_cache")
    ap.add_argument("-o", "--out", default="./run.workflow.js")
    a = ap.parse_args()
    lo, hi = (int(x) for x in a.rows.split("-"))
    cache = Path(a.cache_dir).resolve()
    rows = list(csv.DictReader(open(a.csvfile)))
    leads = []
    for i, r in enumerate(rows, 1):
        if not (lo <= i <= hi):
            continue
        contact = pick(r, "contact") or (pick(r, "first") + " " + pick(r, "last")).strip()
        leads.append({
            "row": i, "company": pick(r, "company"), "website": pick(r, "website"),
            "contact": contact, "title": pick(r, "title"),
            "city": pick(r, "city"), "state": pick(r, "state"),
            "niche": pick(r, "niche"), "linkedin": pick(r, "linkedin"),
            "li_cache": str(cache / "linkedin" / f"row_{i}.json"),
            "site_cache": str(cache / "site" / f"row_{i}.json"),
        })
    js = TEMPLATE.format(
        leads_json=json.dumps(leads), voice_json=json.dumps(VOICE),
        enrich_json=json.dumps(ENRICH_OUT_SCHEMA), vw_json=json.dumps(VW_OUT_SCHEMA),
        polish_json=json.dumps(POLISH_OUT_SCHEMA), rescue_json=json.dumps(RESCUE_SCHEMA),
        enrich_batch=ENRICH_BATCH, vw_batch=VW_BATCH, polish_batch=POLISH_BATCH,
    )
    Path(a.out).write_text(js)
    print(f"wrote {a.out}: {len(leads)} leads (rows {lo}-{hi}), {len(js)/1024:.0f} KB")


if __name__ == "__main__":
    main()
