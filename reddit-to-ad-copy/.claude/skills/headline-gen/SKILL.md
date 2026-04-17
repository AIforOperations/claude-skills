---
name: headline-gen
description: Generate 3-5 Facebook ad headlines from MSL ad copy. Trigger on "headlines", "generate headlines", "headline variations", or after MSL copy is written.
allowed-tools: Read, Write
---

# Headline Generation

Generate 3-5 Facebook ad headlines from a completed MSL ad.

## How to Run

1. Read the MSL copy from the relevant output folder (e.g., `Reddit_To_Copy/<folder>/03_msl_copy_v1.md`)
2. Read the headline generation prompt: `references/headline-gen-prompt.md`
3. Follow the prompt's workflow exactly:
   - Extract avatar, angle, mechanism, authority, constraint, discovery channel from the MSL
   - Select 3-5 headline formulas (default: 2-3 Formula 1, 1 Formula 2, 1 Formula 3-4)
   - Write headlines (27 char target, max 40)
   - Present with format: `[Headline] — [Formula #] ([Blocks]) — [XX chars]`
4. Save to `<same_output_folder>/04_headlines.md`

## Rules

1. Read `references/headline-gen-prompt.md` fresh every time. Do not rely on memory.
2. Headlines must NOT reveal the mechanism, mention product name, price, or guarantee.
3. At least 2 headlines must use Formula 1 (Authority + Concealment Verb + Condition).
4. At least 2 headlines must end with ellipsis (..).
5. Authority in headline must match the MSL narrator.
