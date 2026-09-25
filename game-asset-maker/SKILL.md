---
name: game-asset-maker
description: Create non-pixel 2D or 2.5D static game-world assets such as plants, buildings, furniture, props, and items. Use for isolated objects or coherent asset sets; use game-ui-icon-maker for compact interface icons.
---

# Game Asset Maker

Create static game-world assets with consistent shape language, camera, scale, lighting, and materials. This skill covers image generation and prompt writing for objects placed in a scene or a character's hands. Character poses, pixel art, UI icons, engine integration, and post-production belong to other workflows.

## Choose the task

- For one object, generate one isolated, fully visible subject. Use a transparent background when it needs compositing; omit unrelated scenery, text, and props unless requested.
- For a set, variants, modular pieces, or complex plants/buildings, read [Asset sets and object checks](references/sets-and-asset-types.md). Keep objects distinct and provide separate files when requested and practical.
- Route an ambiguous item by intended use: a world object belongs here; a compact HUD, shop, toolbar, or inventory-slot image belongs to `game-ui-icon-maker`.
- When the user asks only for advice, a prompt, or planning, respond in text. Generate images when requested, without an unnecessary approval stage.

## Visual direction

Follow supplied references and project specifications first. Without them, use readable illustrated 2D or 2.5D game art with clean contours, controlled shading, and strong silhouette. A 2D request favors flatter shapes; 2.5D adds visible volume and directional lighting. Do not force a palette across unrelated requests.

Keep the project's established camera angle, outline treatment, scale language, detail density, and light direction. For an asset set, compare members together; matching genre alone does not establish a matching style.

## Generate and check

Use the available image-generation tool and current-conversation references. Specify the object's structure, requested view, reference style, composition, and background. Add negative constraints for likely mistakes such as malformed geometry, cropping, extra objects, or camera drift rather than using a generic exhaustive prompt.

Inspect the actual result for object identity, construction, silhouette, perspective, set consistency, and unwanted additions. If transparency was requested, verify the saved file's alpha channel and background pixels; a checkerboard or dark preview is not evidence of the file's alpha.

Deliver the actual images. Do not claim consistency or transparency without checking the produced files.
