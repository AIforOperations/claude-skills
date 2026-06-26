export const meta = {
  name: 'enrich-personalize',
  description: 'Per lead: research one personal signal, verify it, draft a friend-to-friend opener line',
  phases: [
    { title: 'Enrich', detail: 'free -> Firecrawl -> Apify waterfall per lead' },
    { title: 'Verify', detail: 'adversarially check each signal is real, personal, fresh' },
    { title: 'Write', detail: 'draft a lowercase, non-salesy opener (no greeting)' },
    { title: 'Polish', detail: 'auto-fix soft openers: reword clunky phrasing, re-research or drop weak signals' },
  ],
}

// args may arrive as an array, an object with .leads, or a JSON string
// (the harness can stringify a large inline value) — normalize all three.
let _a = args
if (typeof _a === 'string') { try { _a = JSON.parse(_a) } catch (e) { _a = [] } }
const leads = Array.isArray(_a) ? _a : (_a && _a.leads) || []
if (!leads.length) { log('no leads passed in args'); return [] }

const SIGNAL = {
  type: 'object',
  additionalProperties: false,
  required: ['signal', 'source', 'confidence', 'arm'],
  properties: {
    contact_name: { type: 'string', description: 'verified full name (identify if missing)' },
    first_name: { type: 'string', description: 'the name they actually go by' },
    signal: { type: 'string', description: 'one specific verifiable PERSONAL fact' },
    source: { type: 'string', description: 'url' },
    confidence: { type: 'string', enum: ['H', 'M', 'L'] },
    arm: { type: 'string', enum: ['free', 'firecrawl', 'apify-maps', 'apify-linkedin', 'none'] },
    flag: { type: 'string', description: 'name/role/same-name/acquisition/deceased issue, or empty' },
  },
}

const VERDICT = {
  type: 'object',
  additionalProperties: false,
  required: ['keep', 'is_real', 'is_personal', 'is_fresh', 'reason'],
  properties: {
    keep: { type: 'boolean' },
    is_real: { type: 'boolean' },
    is_personal: { type: 'boolean', description: 'about the person/firm story, not a business-service fact' },
    is_fresh: { type: 'boolean', description: 'true unless it leans on something >~12mo old that is not a timeless founder/tenure fact' },
    reason: { type: 'string' },
  },
}

const LINE = {
  type: 'object',
  additionalProperties: false,
  required: ['line'],
  properties: {
    line: { type: 'string', description: 'opener WITHOUT greeting; all lowercase; no question mark; <=9 words; casual closer only if otherwise flat' },
  },
}

const POLISH = {
  type: 'object',
  additionalProperties: false,
  required: ['action', 'line'],
  properties: {
    action: { type: 'string', enum: ['pass', 'reword', 'research', 'drop'] },
    line: { type: 'string', description: 'final opener WITHOUT greeting; lowercase; no question mark; <=9 word core; casual closer only if flat. Empty string when action=drop.' },
    signal: { type: 'string', description: 'the fact the final line is built on (the new one if you researched)' },
    source: { type: 'string', description: 'url of the new signal when action=research, else empty' },
    note: { type: 'string', description: 'one short reason for the action' },
  },
}

const VOICE = [
  'Write ONE cold-email opener line built from the signal. HARD RULES (a line breaking any rule is invalid):',
  '- all lowercase',
  '- references the specific signal, friend-to-friend tone',
  '- NO question mark and NO leading-question format (statements only)',
  '- under 9 words (the "hey <name>," greeting is added later, do NOT include it)',
  '- not salesy: no mention of a service, software, meeting, call, or "we help"',
  '- add a short casual closer (", that\'s super cool!", ", love that!", ", respect!", ", wow!", ", that\'s amazing!") ONLY if the line is otherwise flat; if the verb already carries warmth ("loved your...", "love that...") add no closer',
  '- recent signals only: never frame a 3+-year-old award/news as current ("noticed you\'re a..."/"congrats on..."); only use fresh items, else a timeless founder/tenure/hobby fact',
  '- family firm a parent founded: frame as carrying the legacy forward warmly ("carrying on what your dad started"), never corporate ("running your dad\'s company", "worked every role in your dad\'s firm")',
  '- charities/programs in plain words, never a brand/program name that reads as a product ("you help feed houston kids", not "you partner with kids meals")',
  '- no em-dashes; no filler words (seamlessly, leverage, robust, streamline, elevate, empower, unlock, comprehensive, optimize, transformative)',
].join('\n')

phase('Enrich')
const out = await pipeline(
  leads,
  (lead) => agent(
    'Research this prospect and return the single best PERSONAL signal.\n' +
    `company: ${lead.company}\nwebsite: ${lead.website}\n` +
    `city/state: ${lead.city || ''}, ${lead.state || ''}\n` +
    `contact: ${lead.contact || 'NONE on file - identify the owner/principal'}\n` +
    `title: ${lead.title || ''}\nniche: ${lead.niche || ''}` +
    (lead.linkedin ? `\nlinkedin (person): ${lead.linkedin}` : '') +
    (lead.company_linkedin ? `\nlinkedin (company): ${lead.company_linkedin}` : ''),
    { label: `enrich:r${lead.row}`, phase: 'Enrich', agentType: 'lead-enricher', schema: SIGNAL },
  ),
  (sig, lead) => sig ? agent(
    'Adversarially check this signal for a friend-to-friend cold opener. ' +
    'Default keep=false if it is generic/business-only, unverifiable, negative, ' +
    'or leans on something stale (>~12 months) that is not a timeless founder/tenure fact.\n' +
    `company: ${lead.company}\nsignal: ${sig.signal}\nsource: ${sig.source}\nconfidence: ${sig.confidence}`,
    { label: `verify:r${lead.row}`, phase: 'Verify', schema: VERDICT },
  ).then((v) => ({ ...sig, row: lead.row, verdict: v })) : null,
  (sig, lead) => {
    if (!sig) return { row: lead.row, keep: false, line: '', flag: 'enrichment returned nothing' }
    const base = {
      row: lead.row, contact_name: sig.contact_name || '', first_name: sig.first_name || '',
      signal: sig.signal, source: sig.source, confidence: sig.confidence, arm: sig.arm,
    }
    if (sig.verdict && sig.verdict.keep) {
      return agent(`${VOICE}\n\nsignal: ${sig.signal}`,
        { label: `write:r${lead.row}`, phase: 'Write', schema: LINE })
        .then((l) => ({ ...base, flag: sig.flag || '', keep: true, line: l.line }))
    }
    const why = sig.verdict ? sig.verdict.reason : 'no verdict'
    return { ...base, keep: false, line: '', flag: (sig.flag ? sig.flag + '; ' : '') + 'verify rejected: ' + why }
  },
  // POLISH: final auto-fix pass on each kept line. Default pass; reword clunky
  // phrasing; re-research a weak signal for something better; drop if nothing.
  (written, lead) => {
    if (!written || !written.keep || !written.line) return written
    return agent(
      'You are doing a final POLISH pass on ONE cold-email opener. Default to PASS - only act on a clear problem.\n\n' +
      'Pick ONE action:\n' +
      '- pass: the line reads smoothly AND is built on a specific, personal, fresh fact. Return it unchanged.\n' +
      '- reword: the fact is solid but the phrasing is awkward, clunky, or unnatural to say aloud. Rewrite cleanly with the SAME fact, no new research.\n' +
      '- research: the fact is weak (generic tenure on a name-only bio, tied to an unverified/wrong contact per the flag, or not genuinely personal). Do ONE more research pass (free -> Firecrawl -> Apify) for a better PERSONAL fact, then write a fresh line from it.\n' +
      '- drop: the fact is weak and one more research pass turns up nothing better. Return an empty line.\n\n' +
      VOICE + '\n\n' +
      `current line: ${written.line}\n` +
      `fact it is built on: ${written.signal || ''}\n` +
      `research flag / known issues: ${written.flag || 'none'}\n` +
      `prospect: ${lead.company} | ${lead.contact || ''} | ${lead.title || ''} | ${lead.city || ''}, ${lead.state || ''} | ${lead.website || ''}` +
      (lead.linkedin ? ` | ${lead.linkedin}` : ''),
      { label: `polish:r${lead.row}`, phase: 'Polish', agentType: 'lead-enricher', schema: POLISH },
    ).then((p) => {
      if (!p || p.action === 'pass') return written
      if (p.action === 'drop' || !p.line) {
        return { ...written, keep: false, line: '', flag: (written.flag ? written.flag + '; ' : '') + 'polish drop: ' + (p.note || 'weak signal') }
      }
      return {
        ...written, line: p.line,
        signal: p.signal || written.signal, source: p.source || written.source,
        flag: (written.flag ? written.flag + '; ' : '') + 'polish ' + p.action + (p.note ? ': ' + p.note : ''),
      }
    })
  },
)

const final = out.filter(Boolean)
const kept = final.filter((x) => x.keep).length
const polished = final.filter((x) => /polish (reword|research)/.test(x.flag || '')).length
const pdropped = final.filter((x) => /polish drop/.test(x.flag || '')).length
log(`done: ${kept}/${leads.length} usable; polish fixed ${polished}, dropped ${pdropped}`)
return final
