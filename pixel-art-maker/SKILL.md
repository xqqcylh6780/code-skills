---
name: pixel-art-maker
description: >
  Create, modify, or guide the creation of pixel game assets, including scenes,
  tiles, characters, props, UI icons, animations, and sprite sheets. Supports precision drawing,
  layered source files, and export verification via Aseprite MCP. Suitable for
  pixel art production, step-by-step tutorials, and asset specification alignment;
  not for general illustration or game logic programming.
---

# Pixel Art Maker

Transform user descriptions into clean, editable, game-ready pixel assets. Prioritize authentic pixel structure, deliberate cluster design, and clear development stages. Never apply a generic "pixelate" filter over a smooth illustration and call it pixel art.

## 1. Identify the Task Type

- **Tiles**: Ground, grass, dirt, water, foliage, paths, walls, borders, corners, and terrain transitions.
- **Initial Outline**: Focus strictly on exterior silhouette, primary volumes, and essential internal structural lines. Do not add full color or micro-textures prematurely.
- **Final Render**: Build directly upon the confirmed outline using the identical canvas size, scale, perspective, and pose. Complete the palette, shadows, highlights, and selective material textures.
- **Stage Comparison**: When the user requests a progression review, provide an aligned preview showing "Outline → Base Colors → Final Render", while retaining independent files for each phase.
- **Game Asset Set**: Establish project-wide baselines (tile size, character frame size, pivot/anchor points, animation directions, layer structure, palette, and export rules) before mass-producing individual assets.

### Default Baseline
When specifications for a small standalone sprite are not provided, default to **32×32 pixels**, **transparent background**, **limited palette**, **crisp hard edges**, and **no anti-aliasing**, choosing a clear perspective that best identifies the subject. For example, "draw a cat" should be executed directly without asking the user to confirm an outline first. Top-down orthographic characters may default to **32×48**. Derive scene and UI dimensions from their intended use rather than applying the small-sprite default. Reuse previously confirmed project specs without re-asking. Only ask a clarifying question if missing details would fundamentally break production or cause major rework.

## 2. Choose the Production Path

- **Aseprite MCP**: Use native canvas, layers, and pixel tools when the user specifies Aseprite, requests drawing inside an active window, or when the task environment provides Aseprite MCP. Prioritize this path for exact dimensions, editable layers, animations, and tiles. Read [Aseprite MCP Workflow](references/aseprite-workflow.md) first.
- **Image Generation**: When exploring concepts or when the user explicitly requests image generation, use the environment's image tools following [Generation & Editing Patterns](references/generation-patterns.md). Generated images cannot be assumed to meet strict pixel-grid specifications without verification and post-processing.
- **Explanation & Tutorial**: When the user asks about techniques, software operations, or art theory, explain clearly without generating files or modifying documents.
- **Tool Grounding**: Verify available tools and parameters beforehand. Never assume functions from workspace source code are active tools. If a tool is unavailable, explain limitations truthfully rather than faking execution.

### Live Visible Drawing
When the user or project has configured an **Aseprite Live** workflow, keep the drawing process visible in the active window by default (unless batch processing or end-result only is explicitly requested):
- Break drawing into small, discrete, visible calls: Silhouette/Blockout → Base Colors → Shading/Volume → Detailing & Cleanup.
- For animations, draw key poses first, then in-between frames sequentially, refreshing the view to display each newly drawn frame.
- Do not generate the entire piece in a single monolithic script, and never generate the final result in secret only to toggle layers on and off to simulate drawing.
- Provide brief progress notes between phases and continue without pausing for unnecessary confirmations. See [Aseprite MCP Workflow](references/aseprite-workflow.md) for execution details.

## 3. Pixel Game Projects

When working on a complete pixel game, character animations, sprite sheets, or cohesive environment sets, refer to [Game Asset Specifications](references/game-asset-spec.md).
- For a character requested in multiple directions or with animation, also follow [Directional Character Workflow](references/character-workflow.md). Establish one reusable character design before expanding views or actions; verify identity and alignment across the set. A single-pose request stays a single pose unless the user asks for more.
- For a background or playable environment, follow [Scene Workflow](references/scene-workflow.md); distinguish a composed scene from reusable map parts before drawing.
- For a prop with multiple states, directions, or actions, follow [Prop State Workflow](references/prop-state-workflow.md); keep its footprint and identity consistent across variants.
- For a pixel UI icon set or interactive UI components, follow [Pixel UI Set Workflow](references/ui-set-workflow.md); check the family at its intended display size. A single icon request stays a single icon.
- Reuse existing project specs whenever available.
- For new projects lacking specs, propose a concise baseline table and confirm only decisions that block mass production.
- **Scope Boundary**: This skill is strictly responsible for visual assets, animation frames, naming, slicing layout, and import parameters. Engine scripting (character controllers, movement physics, event handlers, tilemap loaders, combat logic) belongs to game development workflows, not this skill.

## 4. Production Pipeline

When actively drawing or demonstrating Aseprite operations, refer to [Artist Workflow & Operations](references/artist-workflow.md), following the standard order: **Silhouette/Structure → Values/Lighting → Materials → Pixel Cleanup**.

1. **Deconstruct Subject**: Extract core subject, camera perspective, pixel dimensions, color palette, primary light source direction, background requirements, and delivery format.
2. **Silhouette & Footprint**: Establish ground footprint and exterior silhouette first, placing the largest masses before adding any internal details.
3. **Values & Base Color**: Verify silhouette readability at 100% scale, apply base flat colors, and sculpt form with grouped value steps (shadows and highlights). Only halt for review if the user explicitly requested phased approvals; otherwise, treat the confirmed outline as a rigid constraint and proceed.
4. **Consistency**: The final render must strictly preserve the verified outline's geometry, proportions, perspective, and orientation. If an outline is flawed, fix the structural silhouette before adding polish.
5. **Tool Execution**: Draw directly at the target pixel resolution in Aseprite. When utilizing generated reference images, only perform integer nearest-neighbor downscaling if pixels are uniformly aligned to the logical grid. Scaling is never a substitute for manual pixel cleanup and must not introduce blurring or anti-aliasing.
6. **Export & Verify**: Export original-resolution PNGs along with an integer-scaled preview (e.g., 4× or 8× nearest neighbor). Inspect the rendered images visually, correct defects, and run quality checks before delivery. For Aseprite workflows, save the actual layered `.aseprite` file.

*Phased execution rule*: If the user requests "step by step" or "one at a time", deliver only the requested stage without jumping ahead.

## 5. Tile Rules

For tile-related tasks, follow the "Tile Design" section in [Pixel Specs & Quality Checklist](references/pixel-spec.md).

- **Isolated Output by Default**: For standalone tile requests, deliver each tile type as an independent image; do not pack grass, dirt, props, and walls into a single unsliced sheet unless requested. For a scene request, deliver the composed scene and only the reusable parts requested.
- **Tileset Sheets**: Create packed tilesets or overview sheets only when explicitly requested, while keeping individual source tiles available.
- **Seamless Continuity**: Verify top-to-bottom and left-to-right edges for seamless ground tiles. For terrain transitions, provide clear sets (centers, edges, outer corners, inner corners, and variations).
- **Layer Separation**: Separate decorative overlays (grass clumps, flowers, rocks, tree stumps) onto transparent background layers rather than baking them permanently into base terrain.
- **Consistency**: Maintain uniform light angle, palette, pixel density, outline thickness, and viewing angle across the entire tile set.

## 6. Outline Rules

- Use clean, 1-pixel hard edges. On small canvases, avoid mechanically outlining every internal crease in black.
- Ensure the silhouette is immediately recognizable at 100% native zoom before drawing internal details.
- Strictly avoid anti-aliasing, semi-transparent feathered edges, blur, smooth gradients, or stray single-pixel noise.
- Use a transparent background for standalone sprites, props, and UI symbols that need compositing. A finished scene background may be opaque. If an outline is difficult to see against a transparent canvas, provide an optional checkerboard preview without replacing the transparent master.
- When animating character movement, ground contacts and torso/pelvis weight shifts should move coherently; never shift half a sprite mechanically to simulate walking.

## 7. Final Art Rules

- Place flat base colors beneath the outline layer, then build depth with limited shading and highlight ramps.
- Stick to a single consistent light source. Most materials require 3 value steps (base, shadow, highlight), with a 4th step only when necessary for extreme reflections or deep cavities.
- Sculpt form with cohesive **pixel clusters**; avoid single-pixel noise (salt-and-pepper dithering) and photographic micro-textures.
- Avoid **banding** (parallel lines hugging outlines) and **pillow shading** (shading edges inwards regardless of lighting).
- Polish readability without silently altering the approved outline design. If shape adjustments are unavoidable, update the outline and clarify the change.

## 8. Delivery Format

Default deliverables:
- Native-resolution PNG(s), transparent where the asset needs compositing;
- Original native pixel resolution;
- Layered `.aseprite` source file (when using Aseprite MCP; if using other tools that cannot produce native source files, state this clearly—never rename a flat PNG to `.aseprite`);
- An integer-scaled (nearest neighbor) enlarged preview for easy viewing;
- Clear, descriptive filenames (e.g., `grass_center_32.png`, `farmer_outline_32.png`, `farmer_final_32.png`).

Do not substitute a textual description or mockup diagram for an actual image. When the user asks for graphics, provide the actual files. If the user asks "no text" or "images only", generate assets without in-canvas labels, banners, or titles, and keep chat responses strictly minimal.

## 9. Quality Verification

Before delivering assets, review and execute the checklist in [Pixel Specs & Quality Checklist](references/pixel-spec.md).
- Validate dimensions, color count, and alpha channels programmatically or via file metadata.
- Visually inspect exported previews for silhouettes, cluster coherence, double-pixels ("doubles"), jaggies, and seamless wrapping.
- A tool execution returning `success` does not guarantee artistic or technical correctness. Only report checks that were genuinely performed.
