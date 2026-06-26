# Voice rules (binding)

Every opener line must pass all of these. `scripts/qa_lint.py` enforces the mechanical ones.

1. **All lowercase.** Including the name in the greeting: `hey margo, ...`.
2. **One specific researched fact.** If you deleted the company/person, the line should stop making sense. Generic praise ("impressive firm", "industry leader") fails.
3. **No question marks. No leading-question format.** Statements only. `"you compete in reined cow horse, that's wild!"` not `"you compete in reined cow horse? that's wild!"`. This rule has been broken before at scale; the linter rejects any `?`.
4. **Under 9 words** in the signal core. The greeting `hey {name},` and the trailing casual closer (`, that's super cool!`) do not count toward the 9.
5. **Not salesy.** No mention of your service, software, a meeting, a call, or "we help". The line is a human reaction to their fact, never a pitch.
6. **Casual closer only where the line is flat.** Add a short closer (`, that's super cool!`, `, love that!`, `, respect!`, `, wow!`, `, that's amazing!`) when the line would otherwise read flat. Do NOT add one when the verb already carries warmth (`loved your...`, `love that...`). Vary the closer across a batch so it does not read as a template.
7. **Recent signals only.** Awards, recognitions, news, and posts must be from the last ~12 months (2025-2026, prefer 2026). Never frame a 3+-year-old item as current ("noticed you're a..."/"congrats on...") — it reads as low-effort. If the only signal is old, use a timeless founder/tenure/hobby fact instead, or drop the lead.
8. **No em-dashes, no AI filler.** Banned: seamlessly, leverage, robust, streamline, elevate, empower, unlock, comprehensive, optimize, transformative, etc. (full list in qa_lint.py).
9. **Legacy, not corporate.** When someone runs a family firm a parent founded, frame it as warmly carrying the legacy forward ("carrying on what your dad started"), never transactionally ("running your dad's company", "worked every role in your dad's firm").
10. **Plain words for charities/programs.** Describe what a charity or initiative does in human words; never drop a brand/program name that reads as a product or random phrase. "you help feed houston kids", not "you partner with kids meals".

## Greeting + casual name convention
Final personalization = `hey {casual_first_name}, {line}` (lowercase).

`casual_first_name`: the name a friend uses. Already-casual names stay (Margo, Andrew, Amy). Formal names collapse to the common short form (Jeffrey -> Jeff, Steven -> Steve, William -> Bill). The `lead-enricher` agent returns the name the person actually goes by; trust that over a generic guess. `scripts/casual.py` has a conservative fallback map. When unsure, keep the full name and flag it.

`casual_company_name`: the short spoken form. Drop legal suffixes (Inc., LLC, PC, LLP), drop a leading "The", drop a tagline after `-`/`|`/`(`, drop a trailing generic "Group/Companies" when a distinctive brand remains, fix acronym casing. Examples:
- `The Helsing Group` -> `Helsing`
- `Mmi- Mcclure Management Inc.` -> `MMI`
- `Criterion - Medical Equipment Planning...` -> `Criterion`
- `The Avalon Management Group, Inc.` -> `Avalon Management`
- `Zed Condos` -> `ZED` (override), `Omni Community Management, Llc` -> `OMNI Community Management` (override)
Two extra rules from prior campaigns: **avoid repeating a word** the line already uses, and **don't shout 5+ letter brands** (only true short acronyms stay all-caps).

## Soft openers (the polish stage auto-fixes these)
A line can pass every mechanical rule above and still be **soft** — weak enough that it should not ship as-is. Two kinds:
1. **Clunky phrasing.** The fact is fine but the wording is awkward to say aloud. `hey ivan, you live in the socal open water, respect!` -> reword to `hey ivan, you dive and paddle socal's open water, love that!`.
2. **Weak signal.** Generic tenure on a name-only bio (`built your arcadia firm back in 2004`), a line built on an unverified or wrong contact, or anything not genuinely personal. Re-research for a better personal fact; if none exists, **drop** (better no line than a soft one).

The workflow's polish stage does this automatically and records `polish reword` / `polish research` / `polish drop` in the flag. When writing by hand, apply the same bar.

## Good vs bad
- GOOD: `hey bill, just learned you sing in a men's choir, that's super cool!`
- GOOD: `hey margo, loved your hoa pros podcast take on hiring.` (no closer; verb carries it)
- BAD: `hey amy, a fourth-generation salinas native? that's roots.` (leading question)
- BAD: `we help firms like yours automate dre filings end-to-end.` (salesy, business, too long)
- BAD: `hey nik, congrats on that 2021 award!` (stale)
