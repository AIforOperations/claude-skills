---
name: concept-engine-native-msl
description: Generate 50-100 lean ad concepts for Native MSL ads across any Your Brand product (SleepWell, QuitHabit, PetWell, and future brands). Takes raw research inputs (Reddit threads, YouTube comments, TikTok comments, winning ad copies, Commslayer tickets, Facebook comments) and outputs tight 1-3 sentence concepts that give the MSL writing skill maximum creative freedom. Trigger on "generate concepts," "concept bank," "concept engine," "mine concepts," "extract concepts," "create concepts from [source]," "concept batch," or any request to turn raw customer research into ad concept ideas. Also trigger when the user pastes Reddit threads, comment dumps, review screenshots, or any raw customer language and wants ad concepts derived from them. This skill handles the CONCEPT CREATION stage only. It does NOT write ad copy. The MSL writing skills (native-msl-sleep, native-msl-sleep-adhd, native-msl-quit, native-msl-pet) handle the actual ad writing from these concepts.
---

# CONCEPT ENGINE: Native MSL Ad Concept Generator

## WHAT THIS SKILL DOES

This skill turns raw customer research into lean, production-ready ad concepts. Each concept is a creative seed: just enough to give the MSL writing skill a narrator, a situation, and an emotional core. Everything else (the specific details, the life moments, the discovery scene, the mechanism bridge, the pacing) is generated during the writing stage by the MSL skill + the avatar's language bank.

**The cardinal rule: A concept is a SITUATION, not a SCRIPT.**

---

## WHY CONCEPTS MUST BE LEAN

Analysis of 200+ winning Native MSL ads across health, pet, emergency, beauty, food, and lifestyle niches reveals a consistent pattern: the best-performing ads were clearly written from concepts that were 1-3 sentences long. The narrative details that make ads convert (a grandmother's bread recipe box, a Marine's 30 push-ups every morning, a pharmacist whispering "off the record" at midnight) were invented during writing, not pre-planned in the concept.

**What over-specified concepts do to the output:**

1. **Kill authenticity.** Pre-scripted details ("she cries in the parking lot at 5:47am") read as stage directions when the writing skill tries to include them. The best ad details feel discovered, not inserted.

2. **Lock the narrative arc.** When the concept dictates the discovery vehicle ("While reviewing her own sleep study data, she notices her GABA levels mirror the pattern..."), the writing skill cannot let the narrator find the discovery naturally. The best discoveries in winning ads feel accidental: a sister mentioning something at Sunday roast, a pharmacist saying "off the record," receipts found in a mother's bathroom cabinet.

3. **Make every ad structurally identical.** If every concept has the same fields (authority + irony + data point + discovery vehicle + mechanism bridge), the skill produces ads with the same shape. Winning ads have wildly different narrative shapes: fear spirals, guilt stories, raw grief, casual lifestyle discoveries.

4. **Starve the narrator of a life.** Over-specified concepts contain only condition-relevant details. Winning ads give narrators full human lives. A tinnitus sufferer remembers his grandson's birthday candles. A blood pressure narrator remembers their dad coaching Little League. These life details do more selling work than any mechanism explanation because they make the reader think "I know this person." The writing skill invents these when given creative freedom. It cannot invent them when the concept is a cage.

---

## CONCEPT FORMAT

Every concept has two parts: the **core** (always required) and the **creative anchor** (optional but encouraged when the research gives you something too good to lose).

```
[NUMBER]. [SHORT TITLE]
[Archetype tag] | [Avatar if relevant]

[1-3 sentences. Who is the narrator. What situation are they in. What makes this impossible to ignore.]

>> [Optional creative anchor: a customer phrase, a belief, a paradox, a headline-worthy line, a specific behavioral detail, or a data point from the research that IS the concept's spark. This is the raw signal that the MSL writing skill can build around. Not a script. A seed.]
```

### WHAT A CREATIVE ANCHOR IS

The creative anchor is the piece of raw research that made you write this concept in the first place. It's the Reddit comment that stopped you scrolling. The customer phrase that captures the entire experience in 8 words. The paradox that would stop someone mid-scroll if it was the first line of an ad. The specific behavioral detail so precise that every person with this condition would think "how do they know that about me?"

**It is NOT:**
- A sample hook (the MSL skill writes hooks)
- A discovery vehicle ("she found out through...")
- A mechanism explanation
- An analytical note about why this concept works

**It IS:**
- A customer's own words: `>> "My brain treats 'finished thinking about it' as 'finished doing it'"`
- A belief the audience holds: `>> They believe silence should help sleep. For ADHD brains, silence is the worst possible environment.`
- A paradox: `>> Benadryl makes her MORE wired, not less. The sedative activates instead of sedating.`
- A behavioral detail: `>> Phone pickup count between 10pm and 2am: 127 times. She checked.`
- A headline-worthy phrase: `>> "I'm the dog." -- the moment a vet recognized her own pacing pattern in the anxious dogs she treats`
- A relationship moment: `>> Her husband falls asleep in 4 minutes. She's timed it. 4 minutes.`
- A research finding: `>> 60 nights tracked. Melatonin vs. no melatonin. 5 minutes difference. A rounding error.`
- A scene detail: `>> 3:17am, Walmart cereal aisle, pajama pants, box of Lucky Charms, no idea how she got there. Again.`

The anchor gives the MSL writing skill something concrete from the research to weave into the ad naturally. It's the difference between "write an ad about a pharmacist with ADHD" and "write an ad about a pharmacist with ADHD who stood behind her own counter and filled a melatonin prescription with her own name on it, knowing it wouldn't work before she opened the bottle." The second one has a creative anchor. The MSL skill can take that in any direction: it might become the hook, it might appear halfway through, it might become the emotional turning point. But it gives the writer a SEED that came from real human experience, not from fabrication.

**Multiple anchors are fine.** If the research gives you 2-3 details that all belong to the same concept, include them. Just keep each one tight (1 line max per anchor).

**Not every concept needs an anchor.** Some concepts are strong enough on situation alone. But when the research hands you a phrase or detail that IS the concept, don't strip it out in the name of leanness. That's throwing away the best part.

### THE BALANCE

The concept bank's job is to sit between raw research and finished ad copy. Too lean and the MSL skill is guessing. Too detailed and the MSL skill is locked into a script. The right balance:

- **Core (always):** Narrator + situation + emotional charge. 1-3 sentences.
- **Anchor (when available):** The research signal that sparked the concept. Customer phrase, paradox, belief, behavioral detail, or scene. 1-3 lines.
- **Never:** Sample hooks, discovery vehicles, mechanism explanations, "why this is new" analysis, production notes.

A concept with a strong anchor might be 4-6 sentences total. A concept without one might be 2 sentences. Both are correct. The anchor earns its place by carrying real research signal, not by adding analytical scaffolding.

### EXAMPLES OF GOOD CONCEPTS

These are reverse-engineered from real winning ads across multiple niches, now with creative anchors where the research provided them:

```
1. The Book Club Exile
Inherited Problem | Body Odor / Aging

Daughter's elderly mother gets silently excluded from her church book club because of a smell nobody will tell her about. The daughter already knew but couldn't face it.

>> The group leader called the next morning with that overly polite voice people use when they're about to say something they don't want to say.
>> "It's not the house. It never was. It's my mom. And everyone around her can smell it except her."
```

```
2. The Marine Who Survived Vietnam But Not the Flu
Peer Narrative | Immune Support

Wife lost her husband, a decorated Marine who survived three combat tours, to the flu. She'd told him to "give it another day" instead of going to the ER. Now she watches other wives post on Facebook about their husbands' "bad colds" and wants to reach through the screen.

>> "I said 'you're dismissed, Marine' because I didn't know what else to say to a man who survived a war but couldn't survive the flu."
```

```
3. The MiraLAX Dependency Spiral
Given-Up Narrator | Gut Health

Woman has been taking MiraLAX every single day for three years and is terrified of what happens if she stops. She tried quitting once, nothing happened for five days, and the panic sent her right back.

>> "I manage my bowel movements like a chemistry experiment. Measuring. Timing. Adjusting doses based on what happened yesterday and what I have planned tomorrow."
>> The laxative becomes the floor. She's terrified to remove it because without it she has nothing.
```

```
4. The Nail Salon Defector
Casual Lifestyle Discovery | Beauty

Woman hasn't been to a nail salon in 8 months. Her husband thinks she's been secretly going. Her sister showed up to Sunday roast with perfect nails and said one word: "wraps."

>> By day 4 she'd have a chip. By day 7, at least two nails lifting. By day 10, embarrassed to show her hands in meetings. £55 for ten days. Maybe.
```

```
5. The 16-Year Medication Sentence
Inherited Problem + Promise-Frame | Blood Pressure

Narrator watched their father deteriorate on blood pressure medication for 16 years: the cough that never stopped, the swollen ankles, the exhaustion that turned him into a ghost. Now they see the same numbers on their own monitor and refuse to follow the same path.

>> "His blood pressure? 'Controlled.' Sitting at 134/86. Not fixed. Controlled."
>> He used to coach Little League and take them for ice cream. Energy for days. On the medication he was asleep by 7:30.
```

```
6. The Pharmacist at Midnight
Peer Discovery + Physical Setting | Sleep (ADHD)

Woman standing in a 24-hour pharmacy at midnight buying melatonin for the 13th time, knowing it won't work. The pharmacist behind the counter says, off the record: "I sell 200 bottles of that a month to people who look just like you. It's not going to work."

>> "At 2am, desperation looks exactly like a pink pill you already know won't work."
```

```
7. The Vet Who Recognized the Pattern
Authority Confession | Sleep (ADHD)

Veterinarian who noticed anxious dogs respond better to calming supplements than sedatives. Sedatives knock them out but they wake up worse. The supplements just stop the pacing. One night pacing her own kitchen she recognized the pattern.

>> "I'm the dog."
```

### EXAMPLES OF BAD CONCEPTS (what NOT to produce)

**Over-specified narrative (this is a script, not a concept):**
> "A sleep lab technician spends every shift wiring patients up to polysomnography machines and reading their brainwave data -- yet she hasn't had a full night's sleep herself in 4 years. She was diagnosed with ADHD at 31 and realized her brain's 'night shift' wasn't insomnia in the clinical sense -- it was GABA depletion from a dopamine-starved brain scrambling for stimulation after dark. She discovers that 31 micro-arousals per night (she tracked her own data) aren't caused by too much brain activity but by too LITTLE inhibitory neurotransmitter."

This names the mechanism, dictates the discovery, specifies the data point. The writing skill is locked into a script.

**Correct version:**
> Sleep lab technician with ADHD. Wires patients up to sleep study machines every shift but hasn't slept through the night herself in years. She knows the handouts she gives patients are useless for brains like hers.
> >> "The sleep hygiene handout I give my patients three times a day? I wrote it. It doesn't work on my brain. I know because I've tried it every night for 4 years."

The anchor carries a real detail (the handout she wrote herself) without dictating the story structure or naming the mechanism.

**Mechanism explanation disguised as a concept:**
> "Challenges the core assumption most ADHD people have about their nighttime brain activity. The brain doesn't race because it has too much energy -- it races because it's starving for stimulation. The GABA brake pedal is empty..."

This has no person in a situation. It's an educational framework, not a concept.

**Correct version:**
> Everything you do at 2am, the scrolling, the reorganizing, the replaying that weird thing from 2019, isn't your brain having too much energy. It's your brain begging for something it can't find.
> >> "Your brain isn't overstimulated at night. It's starving." -- This paradox reframe is the entire scroll-stop.

The paradox statement itself IS the creative anchor. The MSL skill wraps any narrator around it.

**Anchor that's actually a sample hook (too much, crosses the line):**
> >> "I've hooked up 4,200 patients to sleep study machines in the last 6 years. I've read more polysomnography data than most neurologists. Last Tuesday I cried in the parking lot at 5:47am because I hadn't slept more than 3 hours myself in I don't even remember how long."

That's 3 full hook lines. It's a script. The MSL skill should write the hook.

**Correct anchor version:**
> >> She's hooked up thousands of patients but hasn't slept through the night herself. The irony: she MEASURES sleep for a living.

This gives the creative spark without writing the hook.

---

## INPUT TYPES & EXTRACTION PROTOCOLS

This skill accepts multiple input types. The extraction method varies by source, but the output is always the same: lean concepts.

### INPUT TYPE 1: REDDIT THREADS / COMMENT DUMPS

The richest source. When the user pastes a Reddit thread or collection of comments:

**Step 1: Silent Extraction (do NOT show this to the user unless asked)**

Scan every comment and internally categorize. Pay special attention to material that could serve as **creative anchors** -- the phrases, details, and moments that are too good to paraphrase:

- **Situations:** Specific moments, scenes, events described. "I was standing in the pharmacy at midnight buying melatonin again." "My daughter asked why mommy is always tired." "I caught myself pacing the kitchen at 1am doing the same circuit my mother does."

- **Quotable phrases (HIGH PRIORITY for anchors):** Lines that capture the entire experience in a few words. These often work as headlines or hook openers on their own. "My brain treats 'finished thinking about it' as 'finished doing it.'" "I'm the dog." "The quieter the world gets, the louder my brain becomes." "Too tired to sleep." When you find these, FLAG THEM. They are the most valuable output of the extraction because they carry authenticity the MSL skill cannot fabricate.

- **Paradoxes:** Experiences that contradict conventional wisdom. "Coffee calms me down." "Exercise makes me MORE wired." "I can nap anywhere during the day but can't sleep at night." "Benadryl makes me more awake." These are scroll-stoppers AND creative anchors. A paradox stated in the customer's own words is often the entire concept.

- **Beliefs stated as certainties:** "My brain is just wired differently." "There's a golden window in the morning and if I miss it the day is done." "Silence is worse than noise for falling asleep." These are powerful anchors because the audience recognizes their own unspoken beliefs being said out loud. The MSL skill can open an ad with a belief statement and immediately have the reader's trust.

- **Failed solutions with emotional charge:** Not just "melatonin didn't work" but "I've bought melatonin 13 times knowing it won't work because I don't know what else to buy." The emotional charge around the failure matters more than the failure itself. The specific NUMBER of times, the KNOWING it won't work, the buying it ANYWAY -- these details are anchors.

- **Behavioral micro-details (HIGH PRIORITY for anchors):** Not "scrolling phone" but "picked it up, put it down, picked it back up, 47 times." Not "can't sleep" but "opened the fridge, closed it, opened my phone, closed it, opened the fridge again." The hyper-specific behavioral loop is what makes the reader think "how do they know I do that?" These details are often stronger anchors than any phrase because they're VISIBLE. The MSL skill can build an entire opening scene around one behavioral micro-detail.

- **Relationship moments:** NOT for use as primary entry (0/3 win rate for relationship destruction), but as secondary beats and anchors. "My partner falls asleep in 4 minutes. I've timed it." "My husband thinks I've been secretly going to the salon." "I don't talk about anything serious with my wife after 8pm." These are powerful ANCHORS even when they shouldn't be the concept's primary entry.

- **Identity statements:** "My brain is either on full chat or in a state of sleep -- there is no middle." "I am so tired of being fully aware and still completely useless." These become narrator voices AND anchors. When someone states their identity this precisely, it's a concept seed.

- **Frequency markers:** How common is this experience? If 6+ comments describe the same situation, it's universal. Universal = safe. Niche = risky but potentially high-reward if the niche is large enough.

- **Inherited patterns:** "My mother was the same way." "I'm watching myself become my father." "Three generations of women in my family can't sleep." These are the highest-converting emotional structures across all niches.

- **Professional ironies:** "I'm a sleep coach who can't sleep." "I'm a pharmacist filling prescriptions I know don't work." "I'm a psychologist and my own techniques don't work on me." These are authority confession seeds. The irony itself is the anchor.

**Step 2: Rank by Concept Potential**

Not every extracted data point becomes a concept. Rank by:

1. **Universality:** How many people will read this and think "that's me"? A situation described by 1 person that 10,000 people share beats a situation described by 50 people that only 200 share.

2. **Visual specificity:** Can you SEE the scene? "Standing in Target at 11pm holding a candle I don't need" is visual. "Struggling with insomnia" is not.

3. **Paradox strength:** Does it contradict what people believe? "Your brain isn't overstimulated, it's starving" contradicts everything the audience has been told. Paradoxes stop scrolls.

4. **Emotional charge:** Does reading it produce a physical reaction? Guilt, recognition, fury, dark humor, grief? If it's intellectually interesting but emotionally flat, it won't convert.

5. **Narrator potential:** Can a specific, credible person tell this story? The best concepts have a narrator whose life makes the story inevitable. A pharmacist buying melatonin she knows won't work. A sleep coach scrolling at 2am. A daughter finding her mother's sleep journal from 1992.

**Step 3: Generate Concepts**

Turn the highest-ranked extractions into lean concepts following the format above.

### INPUT TYPE 2: YOUTUBE / TIKTOK / INSTAGRAM COMMENTS

Same extraction logic as Reddit, but these sources tend to be:
- Shorter (extract situations and paradoxes, less narrative depth)
- Higher signal-to-noise ratio for DESIRES and FAILED SOLUTIONS
- Often contain product-specific language ("I tried X brand and it didn't work")
- Comments on competitor content reveal what the audience WISHES the content had said

Extract the same categories. Weight toward paradoxes and failed solutions, which tend to be more concentrated in video comments.

### INPUT TYPE 3: WINNING AD COPIES (Own Account or Competitors)

When the user provides winning ad copies as input:

**DO NOT clone the concept.** Instead, extract:

- **The narrative shape:** Is it a fear spiral? A casual discovery? A guilt story? A professional confession? A generational pattern? The SHAPE is transferable to new concepts.

- **The narrator-to-situation ratio:** How much of the ad is the narrator's life vs. the condition? Winning ads are typically 60% human story, 30% mechanism, 10% product. If your concepts are producing ads with different ratios, adjust.

- **The emotional entry point:** What feeling does the first paragraph create? Fear? Recognition? Curiosity? Guilt? Humor? This is the concept's emotional DNA.

- **What the concept must have been:** Reverse-engineer the concept from the finished ad. It's almost always 1-2 sentences. Write that down. That's the format your concepts should match.

Then generate NEW concepts that share the narrative shape and emotional entry point but with completely different narrators, situations, and specifics.

### INPUT TYPE 4: COMMSLAYER / CUSTOMER SERVICE TICKETS

Customer support conversations contain:
- Real objections (pre-purchase and post-purchase)
- Exact language around pain points ("I've tried everything and nothing works")
- Specific product-usage scenarios that reveal the customer's real life
- Complaint patterns that reveal what the audience expected vs. what they got

Extract situations and language. These become concepts rooted in customer reality, not Reddit projection.

### INPUT TYPE 5: FACEBOOK AD COMMENTS (Own Ads)

Comments on your own winning ads contain:
- "This is literally me" identification moments (tells you what resonated)
- "But what about X?" objections (tells you what's missing)
- Personal stories shared in response to the ad (these ARE concepts, told by real customers)
- Skepticism patterns ("sounds too good to be true" + what specifically triggers the skepticism)

Mine the personal stories. Real customer stories shared in comments are pre-validated concepts.

---

## ARCHETYPE TAGS

Tag every concept with its primary archetype. These are the proven structural patterns:

**TIER 1 (default to these):**
- `Authority Confession` -- Professional who has/treats the condition confesses they were wrong or couldn't help themselves. Win rate: 4/4+.
- `Inherited Problem` -- Narrator watches a family member suffer, then faces the same fate. #1 tracked-spend archetype cross-niche.
- `Combined` -- Two archetypes stacked (Authority + Inherited is the ultra-winner structure). Highest structural strength.

**TIER 1.5 (proven cross-niche, scale well):**
- `Promise-Frame` -- "If you have X, you're gonna be pissed when you hear these 3 things." Templatable. 7 cross-niche winners.
- `Paradox Command` -- "STOP doing X." Highest scroll-stop rate. Validates the audience against conventional advice.

**TIER 2 (creative diversification):**
- `Peer Discovery` -- Narrator meets someone in a PHYSICAL setting who shares the solution. Converts well, doesn't scale on Facebook. Physical settings only (digital = 0 purchases).
- `Given-Up Narrator` -- Someone on the edge of surrender. Maximum empathy.
- `Data Proof` -- Raw data makes invisible suffering visible. Screen time reports, sleep tracker data, lab results.
- `Casual Lifestyle Discovery` -- Low-stakes, "huh, that worked" energy. Sister at Sunday roast. Friend at coffee.

**DEAD (never use):**
- Relationship destruction as primary entry (0/3)
- Digital discovery settings (0 purchases)
- Failed authority types: dentist, chiropractor, OT, anesthesiologist, school nurse (0/5)
- Hook swaps / ITN onto existing ad bodies (0/4)
- Cannabis/MJ angles (0/1)
- Listicle format for authority confessions (0 wins)
- "Works every night" promises (credibility killer)
- Sedation language ("knocks you out")
- Lecturing about screen time (community rage trigger)
- Sleep hygiene as primary solution (rage trigger)
- Willpower framing ("just try harder")

---

## CONCEPT DISTRIBUTION

When generating a full bank of 100 concepts:

- Authority Confession: 25
- Inherited Problem: 15
- Combined Archetypes: 20
- Promise-Frame: 10
- Paradox Command: 10
- Peer Discovery (physical settings): 10
- Sub-Avatar / Comment-Sourced Expansion: 10

When generating a smaller batch (10-25 concepts), weight heavily toward Tier 1 (Authority Confession and Combined), with 2-3 Paradox Commands for scroll-stop diversification.

---

## AVATAR-SPECIFIC NOTES

These are brief mechanism/tone references so concepts are correctly oriented. The MSL writing skill contains the full mechanism details.

### ADHD (SleepWell)
- **Mechanism name:** GABA Brake Pedal. Brain is too LOW by evening, not too high. Racing thoughts = brain scanning for stimulation.
- **Tone:** Self-deprecating humor, wry, slightly chaotic. "One of us" energy. Never lecture.
- **Key paradoxes to mine:** Coffee calms me down. Silence is worse than noise. Exercise makes me more wired. I can nap during the day but not at night. Benadryl makes me MORE awake. I'm most productive at 11pm.
- **Melatonin-free positioning:** Essential. This audience is specifically anti-melatonin.

### Fibromyalgia (SleepWell)
- **Mechanism name:** Serotonin Pain Gate. MORNING PAIN is the primary angle, not nighttime.
- **Tone:** Suffering, determination, rage at the system. Validation-first.
- **Key language:** "Flu every day," "beaten with a steel pipe," "taking a shower = climbing Mt Everest," "good day = run errands then bed for a day."

### Smoking/Vaping Cessation (QuitHabit)
- **Mechanism name:** Ritual Gap. The hand-to-mouth ritual is the addiction, not just nicotine.
- **Tone:** Non-judgmental. No shame. Acknowledge the ritual is genuinely comforting.

### Cat Dental Health (PetWell)
- **Mechanism name:** Biofilm Barrier. Bacteria hide under a protective shield that brushing can't reach.
- **Tone:** Worried but proactive cat parent. Guilt about not knowing sooner.

### New Avatars (when exploring)
- When generating concepts for avatars without established mechanisms (perimenopause, bruxism, shift workers, anxiety/insomnia), tag the concept with `[NEW AVATAR -- mechanism TBD]`. The concept should still have a narrator and situation. The mechanism connection gets built when the MSL skill writes the ad.

---

## CREATIVITY GUIDELINES

The extraction process surfaces what's REAL. The concept generation process adds what's CREATIVE. Here's how:

**1. Combine sources that don't obviously connect.**
A Reddit comment about pacing the kitchen at 2am + a winning ad about a veterinarian recognizing anxiety patterns in dogs = "Veterinarian with ADHD, pacing her own kitchen at 1am, recognizes the same pattern she treats in anxious dogs who pace at night."

**2. Transplant situations across demographics.**
A mother finding dental bills in her mom's bathroom cabinet (gum recession ad) becomes a daughter finding a sleep journal from 1992 in her mother's closet (ADHD sleep ad). The STRUCTURE (physical artifact reveals generational pattern) transfers. The details change completely.

**3. Flip the observer.**
If the Reddit comment says "my partner falls asleep in 5 minutes and it makes me furious," the concept isn't about the partner. It's about the fury. But ANOTHER concept could be: the partner who starts learning about ADHD to be supportive and realizes THEY have it too.

**4. Find the scene nobody has used.**
Winning ads use: gym saunas, pharmacies at midnight, school pickup lines, airport gates at 4am, 24-hour laundromats, Walmart cereal aisles at 3am, hotel bars at conferences. These are PHYSICAL places where the avatar would actually be at an unusual hour. When generating peer discovery concepts, imagine: where is this person at 2am? Where are they at their lowest? Where would they encounter someone with the same brain?

**5. Test the "written about me" standard.**
Every concept must pass: "If the ideal customer read just the first two lines of the ad this concept would produce, would they think 'this was written about me specifically'?" If the concept is too broad ("woman who can't sleep"), it fails. If it's too narrow ("left-handed pharmacist in Nebraska"), it fails. The sweet spot: specific enough to trigger recognition, universal enough that thousands identify.

---

## OUTPUT STRUCTURE

When generating concepts, present them as a clean numbered list. Group by archetype category with a single-line header. No analytical scaffolding. No "why this works" explanations. No production notes. Concepts with creative anchors use the `>>` prefix for anchor lines.

```
## AUTHORITY CONFESSION (25 concepts)

1. [Title]
Authority Confession | [Avatar]

[1-3 sentences]

>> [Creative anchor from research -- customer phrase, paradox, behavioral detail, belief, or scene detail]
>> [Optional second anchor if the research gives you another strong signal]

2. [Title]
Authority Confession | [Avatar]

[1-3 sentences]

[No anchor needed if the situation is strong enough on its own]

...
```

After all concepts, include ONE summary section:

```
## TOP 10 PRIORITY CONCEPTS

[List the 10 concepts with highest conversion potential. One line each explaining why: "Universal identification + untested narrator type" or "Paradox strength + proven archetype" etc.]
```

---

## WORKFLOW

**When the user provides raw research (Reddit threads, comments, etc.):**

1. Read everything silently. Do NOT output the extraction unless asked.
2. Confirm avatar and product: "Generating [ADHD/Fibro/etc.] concepts for [SleepWell/QuitHabit/etc.]. How many concepts? Full bank (100) or focused batch (10-25)?"
3. Generate concepts in the format above.
4. Present the Top 10 priority list.

**When the user provides winning ad copies:**

1. Read the ads silently.
2. Reverse-engineer the concepts (1-2 sentences each).
3. Ask: "Want me to generate new concepts that share these narrative shapes but with fresh narrators and situations?"
4. If yes, generate new concepts inspired by the structural patterns, not the specific content.

**When the user says "generate concepts" without providing input:**

1. Ask what input they have: "What research do I have to work with? Reddit threads, customer comments, winning ads, or should I work from the existing language bank in the MSL skill?"
2. If they say "use existing language bank," pull from the bundled Reddit extraction in the relevant MSL skill (e.g., `references/reddit-extraction-march-2026.md` in the ADHD skill) and generate concepts from that data.

**When the user provides a specific scenario or idea:**

1. Treat it as a concept seed. Generate 5-10 variations that explore different narrators, archetypes, and emotional angles around that seed.
2. Present them as options, not a single expansion.

---

## WHAT THIS SKILL DOES NOT DO

- Does NOT write ad copy (use the MSL writing skills for that)
- Does NOT generate full sample hooks (but creative anchors may contain phrases that COULD become hook elements -- that's fine, the MSL skill decides how to use them)
- Does NOT specify discovery vehicles (the MSL skill invents these during writing)
- Does NOT explain mechanisms (the MSL skill handles mechanism education)
- Does NOT rate production difficulty (irrelevant at concept stage)
- Does NOT explain "why this is new to Facebook" (analytical scaffolding that doesn't improve the concept)
- Does NOT generate image prompts (use the native-msl-images skill)
- Does NOT generate headlines (use the headline-gen skills)

## WHAT THIS SKILL DOES THAT RAW RESEARCH DOESN'T

Raw research gives you comments. This skill gives you concepts with creative anchors. The difference:

- **Raw research:** "I can fall asleep in any meeting but can't sleep at night"
- **Concept without anchor:** "Woman who can nap anywhere during the day but can't sleep at 11pm in her own bed."
- **Concept with anchor:** "Woman who can nap anywhere during the day but can't sleep at 11pm in her own bed with blackout curtains and white noise and every 'perfect sleep condition' in place. >> 'At 3pm on a Tuesday I could nap standing up. At 11pm my brain runs a marathon.'"

The concept adds the narrator's situation. The anchor preserves the research's specificity and emotional charge. Together they give the MSL writing skill the creative freedom to build a full ad while keeping one foot planted in real customer experience.

---

## VERSION NOTES

- **V1.0** -- April 2026
- Created based on analysis of 200+ winning Native MSL ads across health, pet, emergency, beauty, food, lifestyle niches
- Core finding: winning ads are written from 1-3 sentence concepts, not detailed blueprints
- Replaces the Concept Bank Generation Master Prompt V1.0 (March 2026) which produced over-specified concepts
