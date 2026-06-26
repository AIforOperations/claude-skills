# Signal rules (what to research, what to use)

The whole pipeline lives or dies on the signal. A great signal is **specific, personal, fresh, and non-business**.

## Priority ladder (use the highest you can verify)
1. **Personal bio quirk / hobby** — sings in a choir, competes in cow-horse, has a named pet, won a baking show, started in a garage. Strongest, most friend-toned.
2. **Founder / family / tenure story** — built the firm, runs their parent's company, started it on a kitchen table, "since 1991". Timeless, always safe.
3. **Community / board / charity / volunteer** — sits on a nonprofit board, flies charity missions, sponsors a local team.
4. **Recent LinkedIn post** — freshest possible signal, but only ~20% of these prospects post. Don't expect it.
5. **Owner replies to Google reviews by name** — behavioral, current, human. The most reliable Apify signal for this niche (more than LinkedIn).
6. **Local award / recognition** — only if within ~12 months.

## Avoid
- Pure business-service facts ("handles DRE filings", "manages 200 HOAs") — that is the firm, not the person.
- Negative reviews / low star ratings — never open on a wound.
- Anything stale (>~12 months) unless it is a timeless founder/tenure fact.
- Anything you cannot verify on a real source.

## When to drop (don't pad)
Drop a lead rather than ship a weak opener when it has **no fresh signal AND no personal signal AND is a weak-fit / low-rating firm**. A generic tenure line on a bad-fit lead is worse than no line — it reads as filler and wastes the send. Also drop any lead that ends up with a blank personalization.

## Which tool wins where (from the head-to-head test)
- **Free fetch + search** carries the majority. Use it first.
- **Firecrawl** wins when the signal is ON the site but unreachable by plain fetch (403, JS-rendered, truncated bios). It is a reliability upgrade, not a new source.
- **Apify premium** wins when the best signal is NOT on the site: a recent LinkedIn post, or an owner-reply on Google reviews. Weight Maps owner-replies over LinkedIn posts for this niche.

## Data hygiene (recurring, ~1 in 3 leads)
Verify and flag: wrong/missing contact name, role mismatch, same-name collisions, recent acquisition or domain redirect, founder deceased. Identify missing owners before writing a line. Never put the founding story in the wrong person's mouth.

## Confidence
H = verified on a primary source. M = corroborated via search snippet, not directly fetched. L = inferred or business-only. The verify stage drops anything that is not real, not personal, or not fresh.
