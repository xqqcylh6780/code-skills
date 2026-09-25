---
name: game-art-maker
description: Create non-pixel 2D or 2.5D game characters and pets, including 日系 Q 版角色, consistent turnarounds, and action poses. Use pixel-art-maker for pixel sprites.
---

# Game Art Maker

Create character images that preserve the same design when the view, pose, or expression changes. This skill covers image generation and prompt writing for characters and pets; it does not cover rigging, engine integration, sprite packing, or post-production.

## Choose the task

- For one character or pet, produce the requested image directly. Default to one full-body subject with an uncropped silhouette and an isolated background when the asset needs compositing.
- For a turnaround, multi-view sheet, action pose, or cycle reference, read [Views and actions](references/views-and-actions.md). A single-pose request stays a single pose.
- For an existing character, use the supplied image or established design as the identity anchor. Preserve proportions, face, colors, costume, accessories, and distinctive anatomy; change only what the user requests.
- When the user asks only for a prompt or advice, answer in text. Generate an image when the user asks for an image, without requiring an extra design-approval stage unless they requested phased review.

## Visual direction

Follow the user's style and reference images first. Without a reference, use readable stylized 2D or 2.5D game art: clean contour, clear silhouette, controlled shading, and coherent color blocking. A 2D request favors flatter graphic shapes; 2.5D adds form volume and directional lighting while remaining illustrated. Do not force a fixed palette or add unrequested costume details.

Keep the requested camera angle exact. Check anatomy and body-part count, especially for wings, tails, hands, and feet. Avoid extra characters, unrelated props, text, or scenery unless requested.

### 日系 Q 版游戏角色

When the user asks for this style, follow their reference's proportions and shape language. Typical cues are a large expressive head on a compact body, simplified facial features, crisp contours, broad flat color areas, and a few hard-edged cel shadows. Keep costume details legible at sprite size. Do not replace this with an adult-proportion anime illustration, painterly rendering, or the angular comic-book look of a different cartoon reference.

If the character will later be split for Spine, favor a relaxed pose with visible, separated limbs and clothing edges that can conceal joints, such as sleeve cuffs, hems, and boot collars. This guides the source drawing; use the spine-image-parts workflow for the actual layer cuts and motion checks.

## Generate and check

Use the available image-generation tool and current-conversation references. State the character identity, requested view and action, relevant style, composition, and background requirement. Use negative constraints only for likely failures; do not substitute a long stock prompt for the user's specific design.

Inspect the result for identity drift, pose readability, missing or extra parts, cropping, and mismatched view. For an asset requested with transparency, inspect the saved file's alpha channel and confirm background pixels outside the subject are transparent. A dark or checkerboard preview alone does not establish whether the file is transparent.

Deliver the actual image. Do not claim that a set is consistent or transparent without checking the produced files.
