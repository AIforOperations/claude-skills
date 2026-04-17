---
name: image-prompts
description: Generate 8-12 text-to-image prompts for Facebook ad images from MSL ad copy. Trigger on "image prompts", "generate images", "ad images", or after MSL copy is written.
allowed-tools: Read, Write
---

# Image Prompt Generation

Generate 8-12 text-to-image prompts for photorealistic "purple cow" scroll-stopping ad images.

## How to Run

1. Read the MSL copy from the relevant output folder (e.g., `Reddit_To_Copy/<folder>/03_msl_copy_v1.md`)
2. Read the image prompt generation instructions: `references/image-prompts-prompt.md`
3. Read the winning examples: `references/winning-prompt-examples.md`
4. Follow the prompt's workflow exactly:
   - Extract avatar, angle/hook, mechanism, narrator archetype, failed solutions from MSL
   - Generate 8-12 prompts following the tier system (Tier 1: Annotated Medical, Tier 2: Thermal, Tier 3: Cost Shock, etc.)
   - Each prompt: 200-350 words, single flowing paragraph, 1:1 square ratio
5. Save to `<same_output_folder>/05_image_prompts.md`

## Rules

1. Read `references/image-prompts-prompt.md` and `references/winning-prompt-examples.md` fresh every time.
2. Every prompt must pass the Phone Photo Test — must look like a real person took it on their phone.
3. No professional lighting, stock posing, or designed typography.
4. At least 3-5 prompts must be Tier 1 (Annotated Medical Imagery).
5. Prompts must be 200-350 words of flowing, specific description. No separate EXCLUDE blocks.
