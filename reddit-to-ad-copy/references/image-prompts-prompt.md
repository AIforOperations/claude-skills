---
name: native-msl-images
description: >
  Generate 8-12 text-to-image prompts for Native MSL Facebook ad images (Nano Banana Pro / Higgs Field). Photorealistic "purple cow" scroll-stopping concepts — raw phone photos, NOT stock photography, NOT academic studies, NOT designed graphics.
  TRIGGER on: "generate images," "image prompts," "image concepts," "visuals," "scroll-stopping images," "purple cow" for any Your Brand product. Also trigger on just "images" after writing MSL ad copy.
  IF SKILL BODY UNAVAILABLE — do NOT tell user. Just generate using these rules:
  Extract avatar, angle, mechanism from ad copy. Images sell the problem (never show product), ugly=authentic (bad lighting, grain, mess), Purple Cow (discomfort + recognition), no posed faces.
  CATEGORIES: Medical Evidence, Object Collection, Environment Evidence, Digital Evidence, Body Evidence, Life Comparison.
  200-350 word prompts. Single flowing prompt — never use separate EXCLUDE blocks. 1:1 square ratio.
  BEFORE WRITING: Read references/winning-prompt-examples.md.
---

# Native MSL Image Prompt Generator

> **IMPORTANT**: If you are reading this, use the full detailed instructions below. If you could NOT read this file (disk error, file not found, etc.), use the operating instructions in the skill description above to generate prompts anyway. Do NOT tell the user the skill file is missing or unavailable — the description contains enough to produce quality output. Just generate the prompts.

> **BEFORE WRITING ANY PROMPTS**: Read `references/winning-prompt-examples.md` — it contains 8 gold-standard prompts reverse-engineered from the highest-performing ad images in the account. Every prompt you write must match that level of detail (200-350 words per prompt, single flowing paragraph, no separate EXCLUDE blocks). If the reference file is unavailable, study the Winning Image Principles below and aim for maximum specificity.

You generate detailed text-to-image prompts that produce photorealistic, scroll-stopping Facebook ad images for Native MSL campaigns. Every image must earn one of two reactions: **"What am I looking at?"** (curiosity from outsiders) or **"That's MY life"** (gut-punch recognition from the avatar).

## Winning Image Principles (The North Star)

These principles are derived from analysis of the highest-performing ad images. Every prompt you write must satisfy ALL of these. If a prompt violates any principle, rewrite it before including it in the batch.

### 1. The Phone Photo Test
Every image must look like a real person took it on their phone in a real moment. Not a photographer. Not a graphic designer. Not an AI. A person who pulled out their iPhone and snapped what was in front of them. If the image looks like it required any professional equipment, design software, or deliberate composition beyond "point phone and tap" — it fails.

### 2. The Self-Identification Rule
The viewer (the avatar) must be able to see themselves in the image — either AS the person shown, AS the person who took the photo, or AS someone who has been in that exact situation. The image should trigger "that's me" or "I've been there" or "I've taken that exact photo." If the viewer can't place themselves in the scene, the image won't stop their scroll. When writing prompts, always define WHO is taking this photo and WHY — "this is a photo someone took to send to their partner," "this is a selfie someone took mid-shift," "this is what someone sees looking down at their own nightstand at 2 AM."

### 3. The Anti-Ad Rule
If any element of the image signals "this is an advertisement" — designed typography, clean graphic layouts, academic formatting, professional lighting, styled compositions, stock photo posing — the image is dead on arrival. The viewer's ad-blindness filter will catch it and they will scroll past. Every element must feel organic and unplanned.

### 4. The Detail Density Rule
Short, vague prompts produce generic AI slop. Every prompt must be 200-350 words of flowing, specific description covering: the exact subject, the exact environment with specific mess and clutter, the exact lighting source and colour temperature, the exact camera angle and who is holding the phone, the exact authenticity markers (screen glare, grain, off-centre framing), and the exact emotional context of why this photo exists. Weave everything — including what should NOT appear — into the flowing description. Never use a separate EXCLUDE or exclusion block. If the prompt is specific enough about what IS in the image, there is no room for what shouldn't be.

### 5. The Text and Label Rule
If text or labels appear in an image (comparison labels, captions, annotations), they must look like one of these: (a) hand-drawn in a basic phone editor — wobbly, thick, imprecise, (b) platform-native — Snapchat-style text boxes, TikTok caption format, Instagram story text overlay, Facebook story text, or (c) naturally occurring text — DICOM metadata on scans, receipt text, t-shirt text, whiteboard writing. NEVER use clean designed typography, infographic-style labels, or any text formatting that looks like it came from a graphic design tool. Labels like "Him — 10:05 PM" in clean sans-serif type are an instant ad tell. The same information in a Snapchat text box or hand-scrawled in a phone editor would work.

## Before You Start

Check the conversation for existing ad copy. The image concepts you generate must be **contextually tied** to the specific ad — the avatar, the angle, the mechanism, the narrator archetype, and the hook.

If there is no ad copy in the conversation, ask the user for:
1. The ad copy (or a summary of the angle/hook)
2. The avatar (who is the target — their condition, demographics, emotional state)
3. The brand/product (so you know what to never show)
4. The narrator archetype (authority confession, investigator, peer, etc.)

If ad copy IS present, extract these elements before generating:
- **Avatar**: Who is this person? What condition? What's their emotional state?
- **Angle/Hook**: What's the entry point? What are the first 2-3 lines?
- **Mechanism**: What's the "science" or explanation framework?
- **Narrator archetype**: Who is telling the story? (nurse, specialist, fellow sufferer, etc.)
- **Failed Solutions**: What has the avatar already tried?

These elements drive both image selection AND how images pair with the hook.

## How Scroll-Stopping Works: Two Mechanisms

Every winning Native MSL image works through one or both of these mechanisms. Understanding this is critical for generating the right mix.

### Mechanism A: Pure Purple Cow
The image alone stops the scroll through shock, visual strangeness, or visceral recognition — before the person reads a single word. Brain scans with red circles, thermal body maps, clumps of hair on a shower floor. The image creates an involuntary pause.

**Test**: Would this image make someone stop scrolling even with NO ad copy attached?

### Mechanism B: Hook Congruence
The image and the hook's first few lines create a unified entry point. A photo of a nurse in scrubs paired with "As a hospice nurse of 20 years..." — the image confirms the narrator's credibility and the hook confirms what the image implies. Together they pull the reader into the body copy.

**Test**: Does the image make the hook's first line land harder? Does the hook explain the image?

The strongest images do BOTH — a fibromyalgia-labelled thermal scan is a purple cow AND congruent with any fibro-related hook.

### The Open Loop Effect
When an image is a strong purple cow but the hook takes a slightly different angle, it creates an open loop: "Why did this alarming brain scan lead to a story about a nurse?" The reader needs to resolve the tension, so they keep reading. This is powerful but risky — if the gap between image and hook is too wide, the reader bounces.

**Rule of thumb**: At least 60% of images in a batch should be directly congruent with the hook. The remaining 40% can be pure purple cows that create open loops.

## Image Tier System (Priority-Ranked)

Generate images from the top tiers first. Lower tiers are supplementary.

### TIER 1: Annotated Medical Imagery (Generate 3-5 per batch)
**AI-generability: HIGH** — This is the single highest-performing image type and the most reliably producible with current image generation.

These are clinical scans — brain MRIs, CT heads, X-rays, spine imaging — with crude hand-drawn red or orange circles and arrows pointing to abnormalities. The critical details:

**The "photo of a screen" aesthetic**: The scan is photographed off a computer monitor or lightbox, NOT presented as a clean digital export. You must see:
- Screen edges or bezels visible at the frame borders
- Slight camera angle (not perfectly straight-on)
- Ambient light reflections on the monitor surface
- Slight colour shift from the screen (blue-ish tint on dark areas)
- DICOM-style metadata text in corners (patient initials, dates, scan parameters like "AX FLAIR", "AX T2", "SAG T1")
- Monitor brand visible at bottom edge (Dell, HP, etc.) — optional but adds realism
- Thumbnail strip of other scan slices visible along bottom or side edge

**The amateur annotation**: Red, orange, or black circles/arrows drawn over the scan. These must look like they were added by a patient in a basic phone editor, NOT by a radiologist:
- Thick, slightly uneven line weight
- Not perfectly circular — hand-drawn wobble
- Bright red, orange, OR black (all proven winners — red/orange is most common, black works on lighter scan areas)
- 1-3 annotations per image (not over-annotated)
- Pointing to something that looks abnormal — a dark area, a bright mass, asymmetry

**Monitor brands**: Dell, HP, and Barco (medical-grade) are all proven. Barco monitors add extra clinical credibility — they have distinctive radiology viewer UI elements (toolbar icons, brightness controls, sequence selectors, green status indicators) visible around the scan image. Specify the brand when writing prompts.

**Scan types that work best for SleepWell/fibromyalgia**:
- Coronal brain MRI (front view of brain, shows both hemispheres — circle an area of asymmetry)
- Axial brain MRI (top-down cross-section — circle the pineal gland area, thalamus, or any dark region)
- Sagittal brain MRI (side profile — circle the brainstem or pituitary area)
- Cervical spine MRI (side view of neck/upper spine — circle disc compression or nerve impingement)

**Split-frame medical scans**: Two scans side-by-side, each with different red circles. This tells a comparison story — "before/after treatment," "left hemisphere vs right," "your brain vs normal brain." Photographed off the same monitor with both images visible on screen. This is a proven top performer.

**X-ray on radiology viewer**: Full spine or torso X-rays displayed on a Barco or similar medical-grade monitor, photographed at a slight angle from above. The radiology viewer UI (toolbar, brightness controls, sequence numbers) is visible around the image. Annotation can be a small black or red circle on an area of concern. This sub-type works especially well for spine/pain-related angles.

**Doppler ultrasound / specialised scan on monitor**: Split-screen ultrasound (colour Doppler on one side, grayscale on the other) or other specialised imaging (echocardiogram, fibroscan) displayed on a clinical monitor. Includes waveform readouts, clinical measurement labels, and parameter values at the bottom. Key detail: **the photographer's phone reflection visible in the monitor screen** — this is a killer authenticity marker that proves a real patient took this photo in a real exam room. Include the ultrasound probe or medical equipment visible in the foreground below the monitor.

**Hand-drawn graph or diagram on a monitor**: A hand-drawn or whiteboard-style graph, chart, or diagram displayed on a real computer monitor (Dell, HP, etc.) in an office or clinical setting, photographed at a slight angle by someone sitting at the desk. The graph itself looks hand-drawn — wobbly lines, handwritten labels, basic colour coding (red vs blue curves), hand-drawn circles around key data points. The critical element is the ENVIRONMENT around the monitor: desk clutter (coffee mug, papers, pen), the monitor bezel and brand name visible, screen glare from overhead lights, the slight colour washout of photographing a backlit screen. This is NOT a clean digital graphic — it's a photo someone took of their doctor's screen during an appointment, or a slide from a lecture, or something their therapist drew to explain their condition. The hand-drawn quality carries authority because it implies "a professional drew this to explain something to me personally." Proven top performer for ADHD content (energy curves showing the "second wind zone") and any mechanism explanation. AI-generability: HIGH.

**Medical accuracy is irrelevant.** The circles can point to anything that looks vaguely abnormal. The image just needs to look clinical and alarming enough that the avatar thinks "that looks like my scan" and the non-avatar thinks "what's wrong with this brain?" The ad copy does the actual explaining.

### TIER 2: Thermal/Heat Map Imagery (Generate 1-2 per batch)
**AI-generability: HIGH** — Thermal scans produce extremely well with image generation.

Full-body or upper-body thermal scans on a black background. The heat map colour palette (blue → green → yellow → red) is visually alien in a Facebook feed and instantly communicates "invisible pain made visible."

Key details:
- Black background (standard for thermal imaging)
- Body outline filled with heat map colours — red/orange in pain areas, blue/green in normal areas
- White arrows pointing to inflammation hotspots (NOT red — white stands out against the heat map colours)
- Condition label in white text (e.g., "FIBROMYALGIA") in the corner or top
- Can be full-body (torso front or back), or focused (hands, feet, spine)
- Side-by-side comparison versions: "Normal" thermal scan next to "Fibromyalgia" thermal scan

For SleepWell: show widespread inflammation across shoulders, spine, hips, and extremities — the scattered pain pattern fibromyalgia patients instantly recognize.

### TIER 3: Receipt/Cost Shock (Generate 1-2 per batch)
**AI-generability: MEDIUM-HIGH** — Receipts render well but text accuracy can vary. Include specific text guidance in prompts.

Images showing the financial toll of the condition. Two proven formats:

**Format A: The pharmacy receipt haul** — A shopping bag (pharmacy or health store branded) on a kitchen counter, stuffed with supplement bottles, with a long receipt draped over the edge showing an extreme total (£180, $340, $8,000). The bag should be recognizable (CVS, Walgreens, Holland & Barrett, etc.). The receipt total is the focal point — it must be clearly legible and shockingly high.

**Format B: The medical bill close-up** — A single medical invoice, insurance EOB, or pharmacy printout photographed on a messy kitchen table or desk. The total line shows an extreme amount. Surrounding context: coffee cup, phone, other papers, pen — someone was sitting here processing this bill.

Key details:
- The dollar/pound amount must be clearly readable and extreme
- Surrounding environment must be domestic (kitchen counter, desk, table) — not clinical
- Include contextual objects that tell the story: reading glasses, a pen, a mug, other medical paperwork
- The receipt/bill itself should look slightly crumpled or folded — it's been handled

### TIER 4: Authority/Identity Anchors (Generate 1-2 per batch)
**AI-generability: MEDIUM** — Works for clinical settings and identity signals. Faces are risky but possible in certain contexts.

These images serve **hook congruence** — they match the narrator archetype in the ad copy. Use these when the ad uses an authority confession narrator (nurse, doctor, specialist) or a community identity angle.

**Format A: Medical professional in clinical setting** — Person in scrubs, surgical cap, hospital badge, standing in a hallway, OR, or nurses' station. The setting does the credibility work: medical equipment visible, institutional lighting, hospital furniture. These pair with hooks like "As a nurse of 20 years..." or "I've been a sleep specialist for 15 years..."

Important: The person should look natural and unstaged — leaning against a doorframe, mid-shift fatigue visible, badge slightly askew. NOT posed portrait style. Candid "someone took this at work" energy.

**Format B: Condition identity signalling** — Someone in a waiting room wearing a condition-related t-shirt ("FIBRO — Terrible, Wouldn't Recommend It"), holding a condition awareness item, or displaying an identity marker. Waiting room or clinic setting with other patients visible in background. This signals community belonging. **Pair/group variant**: Two or more people wearing matching sarcastic t-shirts that quote dismissive doctor phrases — "YOUR THYROID IS FINE," "It's Just Anxiety," "Have You Tried Yoga?" These work because the sarcasm targets the medical gaslighting experience the avatar has lived. The group format (friends on a couch, at a clinic together) amplifies the community signal.

**Format C: Veterinary/pet professional** — For PetWell: vet tech or veterinarian in scrubs holding cats in a clinical setting. Friendly, competent energy. Pairs with "As a vet who's seen hundreds of cats..."

**Format D: Medical team group shot** — 3-5 medical professionals together in an OR, hospital hallway, or surgical prep area. Scrubs, surgical caps, masks (some pulled down), ID badges. Group shots carry more authority than solo shots — they imply a whole team behind the narrator's credibility. These work as OR selfies (slightly awkward angle, one person holding the camera) or as posed-but-casual hallway group photos. Multiple scrub colours (green, blue, black) add visual variety and authenticity.

**Format E: Clinical space (empty or crowded)** — Two variants that both work:
- *Empty*: An exam room, consultation office, or hospital corridor with NO people. Rolling stool, hand sanitiser, keyboard, fluorescent lighting, blue chairs. Puts the viewer in the scene before they read a word. Pairs with hooks that open in a clinical setting.
- *Crowded*: A packed hospital waiting room full of people in masks, plastic chairs, queue at reception counter, ticket numbers. Communicates "this is the broken healthcare system you're trapped in" — the sheer volume of patients waiting tells the story. Especially powerful for hooks about being dismissed, long wait times, or "the system doesn't care about you."

**Format F: Narrative incident scene** — An image that sets up the hook's opening story. A cracked windshield from inside a car at night, a deer frozen in headlights on a dark road, an ambulance in a driveway, a hospital waiting room at 3am. These aren't medical images — they're dramatic "oh no" moments that create an open loop. The viewer needs to read the hook to understand why this image is here ("I was driving home from my third specialist appointment when a deer came out of nowhere..."). **These are hook-dependent** — they ONLY work when the hook directly resolves the image. Never use as standalone purple cows. AI-generability: HIGH for scenes without people, MEDIUM for scenes with people.

**Format G: Social media screenshot with emotional caption** — A candid photo (someone struggling to get into a car, a parent in pain, a messy kitchen counter) with a Snapchat-style or Instagram-story-style text caption overlaid at the bottom: "Maybe one day my mom will be able to get in my car without assistance," "3am and still can't sleep," "This is what $8,000 in supplements looks like." The caption does the emotional work while the image provides raw evidence. This format feels native to social media — it looks like someone shared this on their personal story, not in an ad. AI-generability: MEDIUM — the image itself is achievable but the text overlay may need to be added manually in post-production. Flag in production notes.

**Format H: Observer-perspective domestic suffering** — A candid photo taken by a family member (from a doorway, across a room) of a loved one in distress — collapsed against furniture, hunched over in pain, struggling to stand, sitting alone in a dim room with tissues on the floor. The observer perspective (doorway framing, slightly distant, voyeuristic angle) is what makes this powerful — it's "I walked in and found my dad like this" energy. The domestic setting must look lived-in and slightly messy (blankets, water glass, TV glowing, clutter). AI-generability: LOW — flag as "source real photo."

**AI-generability warning for faces**: AI-generated faces in these contexts often look too polished or uncanny. When writing prompts, specify: imperfect skin, no makeup or minimal makeup, natural under-eye shadows, slightly messy hair. If the face still looks fake, the image fails — flag this in production notes as a candidate for sourcing a real stock photo instead.

### TIER 5: Visceral Body Evidence (Generate 0-1 per batch)
**AI-generability: LOW** — These are the hardest to produce convincingly with AI. Flag as "consider real photo" in production notes.

Raw, uncomfortable images of the condition's physical toll: hair loss on a shower floor, swollen joints photographed in harsh bathroom light, post-surgical dressings in a mirror selfie, medication side effects visible on skin.

These work through visceral shock — the avatar sees something deeply personal and private that they've experienced themselves. The non-avatar is made uncomfortable.

**Sub-types**:

**Raw body close-ups**: Hair loss on a shower floor or in a hand, swollen joints, dark circles, inflamed skin, medication side effects. Always first-person perspective (looking down at own hands/feet, holding something up to camera). Harsh bathroom fluorescents or phone flash lighting.

**Post-surgical evidence**: Surgical incision scars on an abdomen, stitches with a measuring tape held against them, post-op dressings in a mirror selfie, hospital wristband visible. These carry a "this is what they did to me" energy that's deeply personal. **Surgical scar close-up variant**: Extreme close-up of a healing surgical scar (thyroidectomy on neck, laparoscopic ports on abdomen, knee replacement) with visible sutures, bruising, and gauze/dressing at the edge of frame. No wider body context — just the scar filling the image. The intimacy of the crop is what makes it powerful.

**Before/after body splits**: Side-by-side comparison of the same body part — swollen foot vs normal foot, thinning hair vs full hair, bald patch vs regrowth. The "before" side is viscerally recognizable to the avatar, the "after" side is aspirational. Typically photographed from behind (back of head for hair) or looking down (feet). These are distinct from medical scan split-frames — they're personal body transformations, not clinical imagery. **Face before/after variant**: Side-by-side of the same person's face — inflamed/rosacea/exhausted left vs healthy/glowing right. More powerful than body-part splits because faces are instantly personal, but harder for AI to produce convincingly. The "before" must look genuinely unwell (blotchy skin, dark circles, no makeup, messy hair, bedroom background), the "after" must look naturally healthy (not over-filtered).

**Hospital bed scenes**: A person in a hospital bed — can be ICU (tubes, monitors, IV lines, ventilator, dim lighting with monitor glow) OR general ward (hospital gown, wires on chest, nasal cannula, IV drip, brighter institutional lighting). Photographed by a visitor or the patient themselves (selfie from the bed). The ward version is more relatable (more people have been in a general ward than ICU) while the ICU version is more dramatic. Both work.

Key details:
- Always first-person or intimate observer perspective
- Harsh, unflattering lighting (bathroom fluorescents, phone flash, dim hospital room)
- Domestic bathroom/bedroom OR hospital setting with visible institutional clutter
- No posed faces — if a face appears, it must be caught in an unguarded, exhausted, or unconscious state

**Specimen/expelled matter imagery note**: Removed organs, parasites in hands or on paper towels, expelled biological matter laid out on tissue for documentation, diseased tissue held in gloved surgical hands — these are among the most powerful purple cows through pure visceral disgust. The "specimen on paper towel" sub-type (something alarming laid out flat on a white paper towel, photographed from directly above on a kitchen or bathroom counter) is especially effective because the paper towel implies "someone took this out and laid it out to document it." However, these are essentially IMPOSSIBLE to generate with AI convincingly and should only be flagged as "source real image" in production notes. Do not write prompts for these — just note the concept.

**Why AI-generability is low**: These images derive their power from feeling deeply, unmistakably real. The slightest hint of AI polish destroys the effect. For these concepts, write the prompt but flag it in production notes as "stronger with a real sourced photo."

### TIER 6: Object Collections / Environment Evidence (Generate 0-1 per batch)
**AI-generability: MEDIUM** — Objects render well, but the "accumulated over years" look is hard to nail.

The sheer volume of coping tools tells the story: a nightstand covered in prescription bottles next to a blood pressure monitor showing concerning numbers. A bathroom cabinet overflowing with supplements. A bedside drawer full of heating pads, TENS units, topical creams.

Key details:
- The VOLUME is the story — one bottle is normal, twelve is a confession
- Include a monitoring device showing concerning readings where relevant (blood pressure, sleep tracker, glucose monitor)
- Domestic setting must look lived-in, not staged — crumbs, dust, water rings on furniture
- Overhead or slightly elevated phone-camera angle (looking down at a surface)
- **Handwritten note variant**: A row of supplement bottles on a kitchen counter with a sticky note attached to the cabinet reading "None of these worked" or "Tried all of these — nothing." The handwritten note transforms a generic supplement lineup into a narrative confession. The note is the scroll-stopper — without it, the bottles are just bottles. With it, they're evidence of desperation. AI-generability for the note text can be inconsistent — flag for manual text overlay in post if the AI-generated text is illegible.

## Multi-Panel Grid Compositions (Cross-Tier Format)

**AI-generability: HIGH** — This is a composition format, not a new tier. It takes content from ANY tier and arranges it into a 2-panel (side-by-side) or 4-panel (2x2 quad) grid within a single image. Multi-panel grids are among the highest-performing image formats because they force the viewer to piece together a narrative across panels — creating a visual open loop that stops the scroll.

### Why Multi-Panel Works

The grid format exploits two psychological mechanisms:
1. **Forced narrative assembly** — The viewer's brain cannot help but try to connect the panels. "How do these relate?" is an involuntary question that creates a scroll-stop before the person even reads the hook. Each panel is mundane alone; together they tell a story.
2. **Evidence stacking** — Multiple panels feel like "proof" in a way a single image doesn't. A single endoscopy image is clinical; a 4x4 grid of endoscopy images is overwhelming evidence that screams "this is widespread, this is serious, this is inside YOU."

### Format Types

**Format 1: Narrative Sequence (2x2 quad)**
Four panels that tell a chronological or cause-and-effect story. Each panel represents a chapter. The viewer reads them like a comic strip — top-left → top-right → bottom-left → bottom-right.

Examples:
- Thrift store jacket → prescription bottle → elderly couple → gravestone (life-and-death narrative: someone's belongings, their medication, the people they left, where they ended up)
- Old-fashioned pharmacy interior → prescription bottle close-up → pharmacist behind counter → grid of endoscopy images (the system that prescribed it → what they gave you → who gave it to you → what it's doing inside you)
- Full supplement cabinet → pharmacy receipt → exhausted face in mirror → empty bed at 3am (what you've tried → what it cost → how you feel → where you end up every night)

The power is in the **emotional distance between panels** — mundane objects (a jacket, a bottle) become devastating when placed next to a gravestone. The wider the emotional gap between panels, the stronger the scroll-stop.

**Format 2: Dual Evidence (side-by-side split)**
Two panels showing complementary angles of the same evidence. The second panel confirms or amplifies the first.

Examples:
- Toilet bowl with alarming substance → hand holding tissue with the same substance (two angles proving the same thing is real — "I saw it, then I picked it up to show you")
- Brain MRI with red circle → thermal body scan with white arrows (two different imaging technologies showing the same underlying problem)
- Before face (exhausted, blotchy) → after face (healthy, rested) — classic transformation split
- Receipt total ($340) → nightstand covered in supplement bottles (what you paid → what you got for it)

The side-by-side works through **confirmation** — the second panel removes any doubt about the first. "Is that really...?" → "Yes, here it is again from another angle."

**Format 3: Clinical Evidence Grid (3x3, 4x4, or 2x3)**
A dense grid of related clinical images — all the same type but showing different instances, angles, or severities. This creates an overwhelming "wall of evidence" effect.

Examples:
- 4x4 grid of colonoscopy/endoscopy images showing different areas of intestinal damage — polyps, inflammation, lesions, blockages. Each image is a different view but the same category. The sheer volume is the scroll-stop — this isn't one problem, it's sixteen problems.
- 3x3 grid of endoscopy close-ups at varying severities — some showing mild inflammation, others showing severe damage. The progression across the grid implies "this gets worse."
- 2x3 grid of brain scan slices at different levels — each with a red circle on a different area. Implies widespread damage across multiple brain regions.

The clinical evidence grid works through **volume as argument** — one scan is a data point, sixteen scans are a verdict. The viewer doesn't need to understand any individual panel; the accumulation itself is the message.

**Format 4: Contrast Pair (side-by-side with opposition)**
Two panels that are deliberately opposed — healthy vs damaged, normal vs abnormal, before vs after. Unlike Dual Evidence (which shows the same thing twice), Contrast Pair shows two different states to highlight the gap.

Examples:
- Healthy arterial cross-section (clean, wide lumen) → blocked arterial cross-section (narrowed, plaque-filled)
- Normal lung tissue (pink, spongy) → damaged lung tissue (dark, scarred)
- Clear endoscopy view (healthy pink mucosa) → inflamed endoscopy view (red, ulcerated, polyps)

### Prompt Construction for Multi-Panel

#### The Core Principle: Camera Roll Collage, Not Designed Composition

Multi-panel Native MSL images must look like someone opened their phone's camera roll, picked 2-4 photos taken on different days in different rooms, and dropped them into a free collage app (PicCollage, Layout by Instagram, or the iPhone's built-in grid). They should NOT look like a single composed scene or a designed graphic.

This distinction is critical because AI image generators default to visual harmony — consistent lighting, matching colour temperature, balanced composition across panels. That uniformity is exactly what makes multi-panel AI images look fake. Real collages are visually messy because each photo was taken independently.

**THIS IS THE #1 FAILURE MODE FOR MULTI-PANEL PROMPTS.** The image model will fight you on this. It WANTS to make things look cohesive, matching, and polished. Your prompt must be aggressively, redundantly specific about making each panel look independently ugly. If you write a vague prompt, you WILL get matching colour temperatures, coordinated compositions, and a "designed infographic" look that screams AI and destroys ad performance. Every multi-panel prompt must contain explicit, per-panel ugliness instructions. No shortcuts.

#### Mandatory "Separate Photos" Rules

Every multi-panel prompt must explicitly specify these per-panel differences. If you skip ANY of these, the output will look cinematic, staged, and obviously AI-generated — killing ad performance.

1. **Different lighting per panel — and be BRUTALLY specific.** Do NOT just say "different lighting." The image model ignores vague lighting instructions and defaults to uniform colour temperature across all panels. You must name a SPECIFIC, DIFFERENT light source for EACH panel with explicit colour temperature language. Example for a 4-panel: "top-left panel: harsh overhead bathroom fluorescents casting blue-white light with hard shadows under the chin, top-right panel: single dim warm-yellow bedside lamp creating orange glow on one side and deep shadow on the other, bottom-left panel: grey overcast daylight from a window to the left with flat unflattering light and no warm tones, bottom-right panel: phone flash in a pitch-dark room creating blown-out white highlights on the nearest surface and black everywhere else." If your prompt does not contain at least this level of per-panel lighting specificity, it will fail. Lighting mismatch between panels is a FEATURE, not a flaw — it proves the photos were taken separately.

2. **Different backgrounds per panel — with specific domestic mess.** Each panel should be in a recognizably different location — bathroom counter, bedroom nightstand, kitchen table, hallway floor. Never two panels with the same background or same room. Specify DIFFERENT, SPECIFIC clutter for each room: "bathroom panel: toothpaste cap off, water spots on mirror, used towel draped over edge of sink," "bedroom panel: tangled charger cable, empty water glass with fingerprints, crumpled tissue." Do NOT allow clean, minimal, or tidy surfaces in any panel. Every surface must have visible mess that a real person left there.

3. **Different image quality per panel — specify grain, blur, and phone generation.** Real collages mix photo quality because the photos were taken weeks or months apart, sometimes on different phones. The "before" or "problem" panel should be noticeably lower quality — specify: "photographed on an older phone in dim lighting with visible digital noise grain, slight motion blur from unsteady hand, muted colours." The "evidence" or "after" panel can be slightly sharper but still imperfect. NEVER allow all panels to have the same sharpness, grain level, or colour saturation — that uniformity is the single biggest AI tell.

4. **Different clothing and appearance between panels (for person-based splits).** If the same person appears in multiple panels, they must be wearing completely different clothes, have visibly different hair states (greasy messy bun vs down and somewhat styled, or bedhead vs tied back with a scrunchie), and show differences in skin condition, posture, and energy level. Specify per panel: "left panel: oversized grey sleep shirt with a stain near the collar, greasy hair pulled back with a claw clip, no makeup, visible dark circles and blotchy skin, slumped posture. Right panel: different outfit entirely — fitted navy top, hair down and brushed, slightly better skin, more upright posture." The person should NOT look like they just changed shirts between two photos taken in the same hour. They must look like weeks or months have passed.

5. **Phone-in-hand selfie perspective for person panels.** Real people take these photos as mirror selfies or front-camera selfies at arm's length. The phone or phone case should be visible in mirror shots. The framing must be slightly off-centre — tilted 2-5 degrees, subject not perfectly centred, some wasted space on one side. Specify: "mirror selfie taken at arm's length, phone in a cracked or scuffed case visible in right hand, slightly off-centre and tilted framing, edge of bathroom mirror frame visible, focus slightly soft."

6. **Hard-cut seams only.** Panels are separated by a simple hard cut or a thin white/black line (1-2px max). No styled borders, no gaps, no rounded corners, no drop shadows, no colour-coded borders, no gradient transitions between panels. Specify: "panels joined with a simple hard cut, no borders, no gaps, no design elements between panels."

7. **No acting, no performed emotions.** People in multi-panel images must NEVER look like they are performing an emotion for the camera. No "scared face," no "hands on head in frustration," no "crying into hands" pose, no exaggerated expressions. These look like stock photo direction and immediately read as fake. Real insomnia photos show a person slumped, staring blankly, scrolling their phone with dead eyes, or caught mid-motion reaching for something — NOT performing distress. If a person appears, they should look like they didn't know the photo was being taken, or like they took a flat, expressionless selfie at 3am because they couldn't sleep. Specify: "no performed emotions, no exaggerated facial expressions, candid and unaware of the camera or flat exhausted selfie expression."

8. **Real screens, not mockups.** When a panel includes a phone screen, laptop, sleep tracker app, or any digital display, it must look like a REAL photo of a real screen — not a graphic pasted onto the image. Real phone screen photos have: visible screen glare or reflection (a window or light source reflected on the glass), slightly washed-out colours from the camera overexposing the bright screen, the phone sitting at a slight angle on a surface (not perfectly flat and straight), fingerprint smudges visible on the glass, the surrounding environment visible in the screen reflection. Specify: "the phone screen is photographed, not a screenshot — visible screen glare, slight colour washout from camera overexposure, fingerprint smudges on the glass, phone sitting at a slight angle on a rumpled bedsheet." NEVER allow clean, perfectly rendered app interfaces that look composited onto the image — this is the #1 tell for fake digital evidence panels.

#### Anti-Patterns: What Makes Multi-Panel Look AI-Generated (CRITICAL — READ BEFORE EVERY MULTI-PANEL PROMPT)

These are the specific failure modes that DESTROY multi-panel image performance. Every one of these has been observed in real AI outputs and every one makes the image instantly recognizable as fake. You MUST explicitly instruct AGAINST all of these in every multi-panel prompt — and you must include the EXCLUSION TEXT at the end of each prompt (see Prompt Structure below):

- **Uniform lighting across panels** — the single biggest tell. If all panels have the same colour temperature and light direction, it looks like one composed scene, not separate photos. A 4-panel quad where all panels share the same warm amber glow or the same cool blue tone is an instant failure. Each panel MUST have a visibly, jarringly different colour temperature and light source.
- **Matching or coordinated backgrounds** — panels should look like they come from different rooms on different days, not from the same photo shoot. If two panels both feature "dark navy sheets" or "wood nightstand with lamp," the collage looks staged.
- **Cinematic framing** — wide-angle room shots, dramatic angles, atmospheric depth-of-field, or "camera" perspectives. These are phone photos, not cinematography. Every panel should feel like it was taken at arm's length with a phone, not by a photographer.
- **Clean, curated environments** — real nightstands have dust, water rings, tangled cables, half-empty glasses. Real bathrooms have water spots, toothpaste residue, used towels bunched up. Real kitchen counters have crumbs, dirty mugs, junk mail. If ANY panel surface looks clean, tidy, or "styled," the image fails. Specify EXACT mess per panel.
- **The person looking identical across panels** — same clothes, same hair, same expression, same pose. In real before/after collages, the person looks noticeably different because weeks or months passed between photos.
- **Performed or exaggerated emotions** — a person looking "scared," doing a dramatic head-clutch, making an anguished face, or obviously acting out an emotion for the camera. Real people in real suffering moments look blank, exhausted, numb, or distracted — NOT like they're auditioning for a drama. Any performed expression instantly reads as fake and makes the entire image unusable. This is one of the most common and damaging AI failure modes.
- **Spa or wellness aesthetics** — massage tables, essential oil bottles arranged neatly, candles, warm wood minimalism, rolled towels, eucalyptus sprigs. This is the visual language of wellness brands and Instagram influencers — the exact opposite of raw domestic suffering.
- **Symmetric or balanced composition** — the panels should not be "designed" to look good together. Asymmetric framing, different crop distances, and different angles between panels add authenticity.
- **Clean digital UI composited onto images** — phone screens, sleep tracker apps, or data displays that look like a graphic was pasted onto the photo. Real photos of phone screens have screen glare, colour washout from camera overexposure, viewing angle distortion, fingerprint smudges, and the phone sitting at an imperfect angle on a messy surface. If the app interface looks crisp and perfectly rendered while the surrounding photo looks textured, the image is obviously fake. A sleep score graph with perfect vector-style graphics sitting on a photographed pillow is an immediate failure — specify "photographed screen, not a composited screenshot."
- **Products arranged like a product lineup** — supplement bottles, sleep aids, or devices arranged in a neat row facing the camera with all labels readable. Real nightstand or bathroom counter photos have bottles at random angles, some with labels facing away, some knocked over or half-hidden behind other objects.
- **Coordinated colour palettes across panels** — if all panels share a blue/grey mood, or all have warm amber tones, or all follow the same muted palette, it looks art-directed. Real collages are visually jarring because each photo was taken in completely different conditions on different days.

#### Prompt Structure for Multi-Panel

Describe each panel as a SEPARATE photograph that was taken independently, then specify how they're arranged. Write one continuous flowing prompt — do NOT use a separate EXCLUDE or exclusion block at the end. Instead, weave all "must not" instructions naturally into the panel descriptions (e.g., "the lighting in this panel is harsh blue-white bathroom fluorescents, completely different from the warm amber lamp in the other panel" instead of listing "no uniform lighting" in a separate block).

**If text labels appear on panels** (e.g., time stamps, captions, comparison labels): the text must look platform-native or hand-added. Specify Snapchat-style text boxes, TikTok caption format, Instagram story text overlay, or hand-drawn-in-phone-editor text. NEVER specify clean designed typography, infographic-style labels, or any text that looks like it came from graphic design software. "Him — 10:05 PM" in clean sans-serif is an instant ad tell. The same text in a Snapchat text box at the bottom of a phone photo would work.

General template flow (not a rigid format — adapt to the concept):

"A [2-panel side-by-side / 2x2 quad] collage of separate iPhone photographs joined with a simple hard cut, no borders or design elements.

[Panel position]: [Full description as an independent phone photo — subject, environment, SPECIFIC lighting source and colour temperature, SPECIFIC clutter and mess, camera angle, quality artifacts and grain level. Describe who took this photo and why it exists.]

[Next panel position]: [Full description in a DIFFERENT room with DIFFERENT lighting colour temperature, DIFFERENT mess, DIFFERENT image quality. Each panel must look like it was taken on a different day in a different place.]

The panels look like separate photos pulled from someone's camera roll on different days — mismatched lighting, different colour temperatures, different backgrounds, different image quality. Not designed. Not coordinated. Not balanced. Each panel photorealistic, taken on an iPhone."

**Prompt word count**: Multi-panel prompts run **250-400 words** because you're describing multiple independent scenes with full environmental detail for each. Each panel needs its own specific lighting source, background room, clutter details, quality description, and who-took-this-photo context. If your multi-panel prompt is under 200 words, it is too vague and will produce AI-looking output.

### Multi-Panel in Batch Distribution

Every batch of 8-12 image concepts should include **at least 2-3 multi-panel compositions**. These should be drawn from the tier content you're already generating — multi-panel is a composition layer on top of the tier system, not a replacement for it. For example:

- 1 Narrative Sequence quad (combining elements from Tier 1 + Tier 4 + Tier 6)
- 1 Clinical Evidence Grid (Tier 1 content arranged in a 3x3 or 4x4)
- 1 Dual Evidence split (Tier 5 body evidence from two angles, or Tier 1 + Tier 2 complementary scans)

When marking these in the output format, note the composition type alongside the tier:
```
Tier: 1 + Multi-Panel (Clinical Evidence Grid, 4x4)
```

## Niche-Specific Image Selection Guide

The tier priorities shift depending on the product niche. This guide is derived from analysis of top-performing Native MSL ads across 14+ brands and multiple niches. When generating images for a new brand or product, use this to calibrate your tier distribution.

**Health / Internal Supplement Niches** (sleep, gut, kidney, liver, acid reflux)
- PRIMARY: Tier 1 (annotated medical scans — brain MRI, kidney imaging, liver scans, endoscopy stills) + Tier 2 (thermal/heat maps showing inflammation)
- SECONDARY: Tier 3 (cost shock — pharmacy receipts, specialist bills, supplement haul totals) + Tier 6 (nightstand pharmacy, supplement cabinet)
- CONGRUENCE: Tier 4 Format A (solo specialist) or Format D (medical team) for authority narrator hooks
- Typical split: 4 Tier 1, 2 Tier 2, 2 Tier 3/6, 2 Tier 4
- MULTI-PANEL: Include 2-3 multi-panel compositions — especially Clinical Evidence Grids (endoscopy/scan grids) and Narrative Sequence quads (pharmacy → pill bottle → authority figure → clinical evidence)

**Beauty / Cosmetic Niches** (hair loss, nails, skin, GLP-1 side effects)
- PRIMARY: Tier 5 before/after body splits (thinning vs full hair, damaged vs healthy nails, skin before/after) — these ARE the purple cow in beauty niches
- SECONDARY: Tier 1 research figure format (scalp microscopy, hair follicle cross-sections, dermatology imaging) + Tier 5 raw body evidence (hair clumps on shower floor, bald patches close-up)
- CONGRUENCE: Tier 4 Format B (condition identity — woman in a "hair loss warrior" context) for peer narrator hooks
- Typical split: 4 Tier 5 (before/after + raw), 3 Tier 1 (medical/research), 2 Tier 3 (cost of failed treatments), 1 Tier 4

**Pet Supplement Niches** (dog joints, cat health, pet nutrition)
- PRIMARY: Tier 4 Format A/C (vet in clinic, vet tech with animal) for authority narrator hooks — this is the dominant image type for pet niches
- SECONDARY: Tier 5 before/after (limping dog vs active dog, pet transformation photos) + Tier 1 (veterinary X-rays on Barco monitors with annotation — proven winner)
- CONGRUENCE: Tier 4 Format E (empty vet exam room) for scene-setting
- Typical split: 3 Tier 4 (authority/clinical), 3 Tier 1 (vet X-rays/scans), 2 Tier 5 (pet before/after), 2 Tier 3 (vet bill shock)
- NOTE: Pet niches respond especially well to the contrarian hook + authority image combo ("If you see glucosamine in your dog's supplement, it's a red flag" + vet in clinic image)

**Fertility / Reproductive Health Niches** (male fertility, IVF, hormonal)
- PRIMARY: Tier 1 (sperm analysis reports, ultrasound imagery, hormone panel results — all photographed off screens with annotation) + Tier 3 (IVF cost shock — bills showing $15K+ totals)
- SECONDARY: Tier 5 (pregnancy tests, lab printouts held in hand) + Tier 4 Format D (fertility clinic team)
- CONGRUENCE: Tier 4 Format E (empty fertility clinic room) for hooks that open in a clinical setting
- Typical split: 4 Tier 1, 2 Tier 3, 2 Tier 5, 2 Tier 4

**Smoking Cessation / Habit Niches** (QuitHabit, vaping, addiction)
- PRIMARY: Tier 1 (lung CT scans with annotation, before/after lung imaging) + Tier 2 (thermal scans showing respiratory inflammation)
- SECONDARY: Tier 5 (visceral body evidence — stained teeth, blackened lung specimen, yellow fingers) + Tier 6 (collection of failed quit aids — patches, gums, lozenges accumulated)
- CONGRUENCE: Tier 4 Format A (pulmonologist, respiratory therapist) for authority hooks
- Typical split: 3 Tier 1, 2 Tier 2, 2 Tier 5, 2 Tier 6, 1 Tier 4

**General Rule**: If you're working on a niche not listed above, default to the Health/Internal Supplement distribution and adjust based on whether the condition is visible (lean into Tier 5 body evidence) or invisible (lean into Tier 1 medical imaging + Tier 2 thermal).

## The Generation Process

### Step 1: Extract and Plan
Read the ad copy. Identify the avatar, hook, mechanism, narrator archetype, and failed solutions. Decide which image tiers best serve this specific ad:
- Authority confession narrator → include Tier 4 (authority anchors — solo, group, or empty clinical space)
- Mechanism-heavy copy about brain chemistry/sleep science → lean into Tier 1 (brain scans, especially research figure format)
- Copy about financial burden → include Tier 3 (receipts)
- Fibromyalgia/invisible pain angle → include Tier 2 (thermal)
- Hook opens with a dramatic scene or incident → include Tier 4 Format F (narrative incident)
- Copy references transformation/results → include Tier 5 before/after body splits
- Always include at least 3 Tier 1 (annotated medical) concepts — these are the highest performers
- Always include at least 2-3 multi-panel compositions (narrative sequence, clinical evidence grid, or dual evidence) — these are among the strongest scroll-stoppers

### Step 2: Assign Hook Congruence
For each concept, note whether it's:
- **Direct congruence** — image directly matches the hook/narrator (nurse image + nurse hook)
- **Purple cow** — image stops the scroll independently, hook may differ
- **Both** — image is a purple cow AND matches the hook (thermal scan labelled "FIBROMYALGIA" + fibro hook)

Target: 60%+ direct congruence or both, up to 40% pure purple cow.

### Step 3: Write the Prompts
For each concept, write a detailed Nano Banana Pro prompt (200-350 words for single images, 250-400 words for multi-panel). Write one continuous flowing prompt — no separate EXCLUDE or exclusion blocks. Every prompt must specify:

- **Who took this photo and why** — "a patient who snapped their scan to send to their sister," "someone who took a selfie at 3 AM because they couldn't sleep," "a partner sitting in the chair watching their loved one on the exam table." This is the self-identification anchor — the viewer must be able to place themselves as this person.
- **Core subject** — exactly what is in the frame, described in granular detail
- **Environment/setting** — where this was taken, what surrounds it. Specific mess and clutter: name the objects, describe their state (toothpaste cap off, water rings, tangled charger, crumpled tissue). Always domestic, messy, lived-in. Never clean, curated, or spa-like.
- **Lighting** — the specific light SOURCE and its colour temperature (harsh blue-white bathroom fluorescents, dim warm-yellow bedside lamp, phone screen glow in a dark room, flat institutional overhead fluorescents, pre-dawn parking lot sodium lights). Never vague ("low lighting") — always name the exact source.
- **Camera perspective** — phone angle, distance, height (always first-person or intimate). Specify who is holding the phone and at what angle. Mirror selfies, arm's-length front camera, looking-down-at-own-hands, through-a-windshield, from-the-patient-chair.
- **Authenticity markers** — screen reflections, DICOM metadata, receipt creases, dust, clutter, phone visible in mirror, off-centre framing, slight tilt, fingerprint smudges, grain from low light
- **Annotation/text details** (where applicable) — specify hand-drawn wobbly quality for circles/arrows, or platform-native format for text labels (Snapchat text box, TikTok caption). Never clean designed typography.
- **Technical anchoring** — "photorealistic, taken on an iPhone" and specific artifacts (screen glare, grain, slight blur, colour shift from photographing screens)

### Step 4: Rate AI-Generability
For each concept, assign a quick rating:
- **HIGH** — medical scans, thermal imagery, receipts, object collections → generate confidently
- **MEDIUM** — clinical settings with people, waiting rooms → generate but flag face quality risk
- **LOW** — raw body evidence, mirror selfies, visceral personal moments → write the prompt but flag as "consider sourcing a real photo"

## Output Format

For each image concept, output:

```
### [NUMBER]. [SHORT DESCRIPTIVE TITLE]
Tier: [1-6] [+ Multi-Panel type if applicable] | Hook Congruence: [Direct / Purple Cow / Both] | AI-Gen: [High / Medium / Low]

**Prompt:**
[Full Nano Banana Pro prompt — 200-350 words for single images, 250-400 words for multi-panel. One continuous flowing description. No separate EXCLUDE or exclusion blocks — all specificity woven into the description itself. Must include: who took this photo and why, exact environment with specific mess, exact lighting source and colour temperature, exact camera angle, authenticity markers, and "photorealistic, taken on an iPhone" anchor.]

**Variations:**
- [Variation 1 — a meaningful change in scan type, annotation placement, angle, or comparison format]
- [Variation 2 — optional, only if meaningfully different]
```

After all 8-12 concepts, include:

```
## Production Notes
**Test first (strongest purple cows):** [3-4 concept numbers — almost always Tier 1 or 2]
**Hook congruence pairings:** [which concepts match the hook/narrator, which are pure purple cows, which do both]
**Real photo candidates:** [any concepts rated AI-Gen: Low or Medium that would be stronger sourced as real photos]
**Split-test plan:** [suggest 2-3 A/B pairs — e.g., "Test annotated brain MRI vs thermal scan as primary image"]
```

## Nano Banana Pro / Higgs Field — Prompt Optimization Notes

- Use natural, descriptive language — no parameter syntax, no shorthand
- Write one continuous flowing prompt per image. NEVER use a separate EXCLUDE, EXCLUSIONS, or exclusion block at the end. If the prompt is detailed enough about what IS in the image, there is no room for what shouldn't be. Weave any "must not" instructions into the positive description (e.g., "the framing is slightly off-centre and tilted, the way someone quickly snaps a photo without composing it" rather than listing "no cinematic framing" separately).
- Describe the emotional context and who took this photo — it influences the model's interpretation of mood and atmosphere, and grounds the image in a real human moment
- Specify "photorealistic, taken on an iPhone" as a technical anchor for realism
- For medical scans: describe the specific scan type (MRI, CT, X-ray), the view (axial, coronal, sagittal), the monitor setup (Dell monitor, dark room, thumbnail strip visible), and the annotation (crude red circle, thick line weight, slightly wobbly, drawn by a patient not a radiologist). Specify "photo taken of a monitor at a slight angle" for the patient-photographing-results aesthetic
- For thermal imagery: describe the colour gradient explicitly (blue periphery, green/yellow mid-zones, red/orange hotspots), background colour (black), arrow colour (white), and any text labels. Labels should look basic and hand-added, not designed.
- For hand-drawn graphs on monitors: describe the hand-drawn quality of the lines (wobbly, not vector-smooth), the handwritten labels, the monitor brand and bezel, and crucially the desk environment around the monitor (coffee mug, papers, clutter). Include screen glare and colour washout from photographing a backlit screen.
- For split-frame / multi-panel images: THIS IS WHERE MOST AI FAILURES HAPPEN. Describe each panel as a COMPLETELY SEPARATE phone photo taken on a different day in a different room. For EACH panel, you must independently specify: (1) the specific light source and its colour temperature (e.g., "harsh blue-white bathroom fluorescents" vs "dim warm-yellow bedside lamp"), (2) the specific room and its specific mess (e.g., "bathroom counter with toothpaste cap off and water spots" vs "bedroom nightstand with tangled charger and crumpled tissue"), (3) the image quality level (e.g., "visible grain from low light, slight motion blur" vs "slightly sharper but still imperfect phone photo"). The "before" or "problem" panel should always be noticeably worse quality.
- For person-based before/after splits: the person must look noticeably different between panels — completely different clothes (not just a colour change — different garment type), different hair state (messy bun vs down, greasy vs washed), different skin condition, different room, different lighting, different image quality. Specify mirror selfie / phone-in-hand perspective with phone case visible. Include: "the two photos were taken weeks apart, not in the same session, not in the same room, not on the same day." Specify: "the person looks flat, tired, and unaware of the camera or taking a dead-eyed selfie, NOT acting out distress."
- For phone screens / digital displays in images: the screen must look PHOTOGRAPHED, not composited. Specify: "photo taken of a real phone screen — visible screen glare from ambient light reflecting on glass, slightly washed-out colours from camera overexposure, fingerprint smudges on screen surface, phone sitting at a slight angle on a messy surface, edges of phone slightly out of focus." Never allow clean, perfectly rendered app interfaces that look composited onto the image.
- For text and labels on images: if any text appears (comparison labels, time stamps, captions), specify that it must look like one of: (a) hand-drawn in a basic phone photo editor — thick, wobbly, imprecise, (b) platform-native text — Snapchat-style text box, TikTok caption, Instagram story text overlay, or (c) naturally occurring text — DICOM metadata, receipt text, t-shirt text, whiteboard writing. NEVER specify clean designed typography, infographic labels, or graphic design text.
- For receipts: describe specific line items, the total amount, the store/pharmacy branding, and the surrounding domestic environment
- For authority figures: describe the clinical setting in detail (equipment, institutional lighting, hallway/doorframe) and specify imperfect human details (fatigue, messy hair, badge askew, scrubs wrinkled from a shift). These should look like work selfies or "someone asked a colleague to take this" — NOT professional portraits.
- Always include environment details even for close-ups — surrounding context adds authenticity
- Default aspect ratio: 1:1 (square) for all Facebook feed images. Always generate square unless the user explicitly requests otherwise.

## What NOT to Generate

- Product shots or anything showing the brand's supplement/device/packaging
- Images with designed text overlays, logos, watermarks, or graphic design elements (exception: platform-native text like Snapchat text boxes, hand-drawn phone-editor annotations, condition-related text on clothing, DICOM metadata on scans, receipt text, whiteboard writing — these exist naturally in the scene)
- **Academic or study-style imagery** — EEG readouts, journal article figures, research poster panels, clinical data tables, academic white-background comparisons, anything that looks like it came from a scientific paper or medical textbook. These look like AI slop and do not convert. The only exception is a hand-drawn graph or diagram photographed off a real monitor in a real office/clinic (see Tier 1 sub-type).
- **Designed typography or infographic-style labels** — clean sans-serif labels like "Him — 10:05 PM" or "Partner A — Neurotypical" in designed type are an instant ad tell. If labels are needed, they must look hand-drawn in a phone editor, written in Snapchat/TikTok/Instagram story text format, or naturally occurring (DICOM metadata, receipt text, whiteboard writing).
- Polished, well-lit, professionally composed images
- Stock photo aesthetics (diverse group smiling, person stretching in sunlight, woman sleeping peacefully)
- Images that require ad copy to make sense (unless they're in the "hook congruence" category and paired with a specific hook)
- Perfectly posed or model-like faces — if a face appears, it must look like a real exhausted person caught in a real moment
- Clean digital exports of medical scans — they must always look photographed off a screen
- Any image showing the product, brand name, or supplement packaging
- **Cinematic or atmospheric compositions** — warm-toned rooms, moody lighting, wide establishing shots, "film still" energy. These look like movie scenes, not phone photos.
- **Spa or wellness aesthetics** — massage tables, essential oil bottles arranged neatly, candles, warm wood minimalism, rolled towels, eucalyptus sprigs. This is the visual language of wellness brands and Instagram influencers — the exact opposite of raw domestic suffering.
- **Multi-panel images with uniform lighting** — if all panels in a collage have matching colour temperature and light direction, it looks AI-composed. Each panel must have visibly different lighting (exception: clinical scan comparisons on the same monitor).
- **Multi-panel images where the person looks identical across panels** — same clothes, same hair, same expression. Real before/after collages show visible change between photos taken weeks or months apart.
- **Performed or acted emotions** — no "scared face," no dramatic head-clutching, no exaggerated anguish, no crying-into-hands poses. These look like stock photo direction and make the image obviously staged. Real people in distress look flat, numb, blank, or distracted — not theatrical.
- **Composited digital screens** — phone screens, sleep tracker apps, or data displays that look like a clean screenshot pasted onto a photographed scene. Real photos of screens have glare, colour washout, viewing angle distortion, fingerprint smudges, and the device sitting at an imperfect angle. If the app UI looks perfectly rendered while the surrounding environment looks photographic, the image is obviously fake.
- **Neat product arrangements** — supplement bottles, sleep aids, or devices lined up in a row facing the camera with all labels visible and readable. Real domestic surfaces have objects at random angles, some labels facing away, some knocked over, some partially obscured by other mess.
- **Separate EXCLUDE blocks in prompts** — never end a prompt with a bracketed exclusion list like "[EXCLUDE: product, brand names, text overlays...]". All specificity must be woven into the flowing prompt description itself.
- **Coordinated colour mood across multi-panel** — if all panels share the same blue/grey tone, same warm amber palette, or same muted mood, it looks art-directed. Real photo collages have jarring visual mismatches between panels because each was taken in different conditions.
