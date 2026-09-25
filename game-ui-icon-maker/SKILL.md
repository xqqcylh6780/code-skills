---
name: game-ui-icon-maker
description: Create non-pixel 2D or 2.5D game interface icons for navigation, features, resources, skills, and inventory. Use when small-size readability and coherent UI sets matter; use game-asset-maker for objects placed in the game world.
---

# Game UI Icon Maker

Create icons that communicate their function at the intended UI size and belong to the same visual family. This skill covers image generation and prompt writing for interface graphics, including button symbols; it does not cover scene art, character animation, pixel art, or engine integration.

## Choose the task

- For one icon, choose one clear symbol and generate an isolated image. Default to a square composition with safe padding and a transparent background when the icon will be composited into UI.
- For a themed icon, set, complete button, or normal/hover/pressed/disabled/selected/locked states, read [Icon workflows](references/icon-workflows.md). Generate a complete button only when requested; otherwise supply the bare icon.
- Route an ambiguous item by intended use: a compact HUD, inventory-slot, shop, or toolbar symbol belongs here; a world object belongs to `game-asset-maker`.
- When the user asks only for advice, a prompt, or UI planning, respond in text. Generate images when requested.

## Visual direction

Follow the supplied UI style or reference set first. Without one, use clean non-pixel 2D or 2.5D illustrated icons with strong silhouette, clear negative space, controlled contrast, and limited internal detail. 2.5D may add material volume but must remain readable as an icon.

Keep outline width/color, perspective, lighting, corner language, visual weight, and padding consistent across a set. Avoid tiny details, fragile strokes, competing subjects, unnecessary text, and decorative backgrounds unless the user requests them.

## Generate and check

Use the available image-generation tool and current-conversation references. Specify the icon function, dominant metaphor, target display size, style, composition, and background. Do not rely on a long stock prompt to resolve an ambiguous symbol.

Inspect the output at its intended UI size as well as full size. Check meaning, direction, cropping, contrast, and consistency with neighboring icons. For a transparent asset, verify the saved file's alpha channel and background pixels rather than judging the preview alone. For state variants, verify the base symbol stays aligned and recognizable.

Deliver the actual images. Do not claim readability, consistency, or transparency without checking the produced files.
