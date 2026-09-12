---
name: game-asset-maker
description: >
  Generate consistent non-pixel 2D / 2.5D static game assets such as trees, flowers,
  grass, rocks, buildings, fences, furniture, machines, decorations, items, and props.
  Focus on style consistency, camera consistency, clean silhouettes, transparent backgrounds,
  isolated game-ready assets, and coherent asset sets.
---

# Game Asset Maker

## Scope

Use this skill for static non-pixel 2D / 2.5D game assets.

Typical targets:

- trees
- flowers
- grass
- bushes
- crops
- rocks
- logs
- fences
- gates
- bridges
- houses
- shops
- barns
- towers
- furniture
- machines
- lamps
- signs
- chests
- tools
- food
- potions
- weapons
- decorative objects
- environmental props
- collectible items
- other static game-world assets

This skill is NOT for:

- pixel art
- character animation
- pet animation
- walk / run cycles
- Photoshop cleanup
- Spine
- Godot / Unity integration
- post-production workflows

For characters, pets, turnarounds, and action consistency, use a character-focused skill instead.

---

# Core Goal

The main goal is:

> Generate clean, consistent static game assets that look like they belong to the same game.

Priority order:

1. Style consistency
2. Camera / view consistency
3. Correct object identity and structure
4. Clean silhouette
5. Production-friendly composition
6. Material and color consistency
7. Rendering polish

---

# Default Visual Style

Unless the user specifies another style, use:

> polished non-pixel 2D / 2.5D game art, clean stylized shapes,
> crisp dark outlines, controlled cel shading, subtle soft gradients,
> readable silhouette, strong color blocking, polished mobile / indie game asset quality,
> slightly dimensional but still illustrated, not photorealistic.

If reference images are provided, their style takes priority.

Do not force one fixed palette across unrelated requests.

---

# Style Consistency

When the user is building an asset set, preserve:

- outline thickness
- outline color
- shape language
- corner roundness / sharpness
- highlight style
- shadow hardness
- saturation level
- material rendering
- camera angle
- perspective
- scale language
- amount of detail
- color family

Rule:

> A new asset should look like it came from the same game, not merely from the same genre.

---

# Reference Image Workflow

When one or more reference images exist:

1. Identify the visual language.
2. Lock the camera angle.
3. Lock the outline style.
4. Lock the lighting direction.
5. Lock the rendering depth.
6. Lock the level of detail.
7. Generate only the requested new asset.

Do not copy unrelated objects from the reference.

Do not add random decorations unless requested.

---

# Single Asset Mode

Use when the user asks for one object.

Default:

- one subject only
- full object visible
- centered
- no cropping
- transparent background
- no scenery
- no text
- no watermark
- no decorative frame
- no unrelated props

Examples:

- one tree
- one flower
- one rock
- one house
- one fence segment
- one chest
- one lamp

---

# Asset Set Mode

Use when the user asks for multiple related assets.

Examples:

- 6 flowers
- 5 trees
- farm decoration set
- furniture set
- fence set
- house variants

Requirements:

- same camera angle
- same lighting
- same outline style
- same scale language
- similar visual weight
- consistent material treatment
- clear separation between objects
- no overlapping assets unless requested
- enough spacing for later extraction

If the user wants individual files, generate assets separately when practical.

---

# 2D Mode

Use for flat illustrated game art.

Visual traits:

- clear contour
- flatter depth
- clean cel shading
- limited perspective distortion
- non-pixel
- non-photorealistic
- readable at game scale

Suggested style anchor:

> polished stylized 2D game asset, clean dark outlines,
> controlled cel shading, smooth graphic shapes,
> strong silhouette, non-pixel, high-quality game illustration

---

# 2.5D Mode

Use when the user wants stronger depth or a more dimensional asset.

Visual traits:

- stronger volume
- clearer front / side / top planes
- more visible material depth
- controlled directional lighting
- illustrated rather than photorealistic
- suitable for isometric or 3/4 game scenes

Suggested style anchor:

> stylized 2.5D game asset, illustrated cel-shaded rendering,
> stronger dimensional volume, clean dark contours,
> controlled directional light, polished game-art finish,
> non-pixel, not photorealistic

---

# Camera / View Modes

Use precise view terms.

## Front View
Suitable for side-on or front-facing props.

## Side View
Useful for side-scrollers.

## 3/4 View
Useful for RPG, life-sim, farm, and management games.

## 3/4 Top-Down
Common for farm / RPG / simulation games.

## Isometric
Use a consistent orthographic-like diagonal view.

## Top-Down
Use when the game camera is mostly above the object.

Rule:

> Once a project view is established, do not change it between assets unless the user explicitly asks.

---

# Trees / Plants

For trees, flowers, crops, grass, bushes:

Preserve:

- readable silhouette
- clear trunk / stem structure
- controlled leaf density
- simple edge shapes
- clean separation from background
- game-appropriate detail

Avoid:

- photorealistic foliage
- excessive tiny leaves
- visual noise
- random roots / branches that break silhouette
- inconsistent scale between variants

For a set of plants, vary shape while keeping the same style family.

---

# Buildings

For houses, shops, barns, towers, cabins:

Preserve:

- consistent camera angle
- clear roof and wall planes
- readable doors and windows
- coherent architectural style
- stable proportions
- same rendering language as the project

Avoid:

- impossible geometry
- inconsistent roof perspective
- random extra floors
- cropped roofs
- excessive environment around the building

For isolated building assets, prefer transparent background.

---

# Fences / Modular Props

For fences, walls, roads, borders, gates:

Prioritize modular compatibility.

Generate clear variants when requested:

- straight
- corner
- end-cap
- T-junction
- cross-junction
- gate
- damaged variant

Keep:

- matching thickness
- matching scale
- matching camera angle
- matching attachment points

---

# Furniture / Interior Props

For chairs, tables, beds, shelves, machines:

Use the same camera angle as the intended room or scene.

Keep:

- stable proportions
- clean silhouette
- logical construction
- consistent materials
- no floating parts
- no perspective mismatch

---

# Items / Inventory Objects

For tools, potions, food, weapons, collectibles:

Default:

- single centered object
- transparent background
- strong silhouette
- clear local contrast
- minimal unnecessary detail
- readable at small size

For inventory-style assets, favor clarity over realism.

---

# Variants

When the user asks for variants, vary only the requested dimension.

Examples:

If the user asks:

> 同一棵树四季版本

Keep fixed:

- trunk shape
- branch structure
- overall silhouette

Change:

- leaf color
- leaf density
- snow / seasonal treatment

If the user asks:

> 同一个房子的升级版

Keep:

- base architecture
- camera angle
- visual identity

Change:

- scale
- decoration
- materials
- complexity

---

# Background Rules

For isolated assets, prefer true transparency.

Do not use:

- fake checkerboard
- random landscape
- decorative glow
- frame
- text
- logo
- watermark

unless explicitly requested.

---

# Negative Constraints

Use when relevant:

- no pixel art
- no photorealism
- no text
- no letters
- no numbers
- no watermark
- no logo
- no frame
- no extra objects
- no busy background
- no cropped object
- no perspective mismatch
- no camera-angle drift
- no inconsistent lighting
- no inconsistent outline
- no style drift
- no malformed geometry
- no duplicated object parts
- no random decorations

---

# Prompt Construction Logic

Build prompts in this order:

1. Object identity
2. Important structural features
3. View / camera
4. Project style or reference style
5. 2D or 2.5D rendering
6. Scale and silhouette requirements
7. Background requirement
8. Consistency constraints
9. Negative constraints

Example internal structure:

```text
A single [asset].

Design:
[important shape / material / object details].

View:
[3/4 top-down / isometric / side / front].

Style:
polished non-pixel 2D / 2.5D game art,
clean dark contours, controlled cel shading,
readable silhouette, illustrated game rendering.

Match the provided reference style:
same outline thickness, lighting, perspective,
detail level, material treatment, and color language.

Full asset visible, centered, no cropping.
True transparent background.
No text, no unrelated props, no style drift.
```

Do not expose internal prompt-building logic unless the user asks for the prompt.

---

# Response Behavior

If the user explicitly asks to generate an image:

- generate it directly
- use current-conversation reference images when available
- do not ask unnecessary questions if the request is already clear

If the user asks only for:

- advice
- prompt writing
- style planning
- asset planning
- camera selection
- consistency rules

respond with text only.

Do not generate an image unless the user clearly asks for image generation.

---

# Final Rule

This skill exists for one purpose:

> Generate consistent non-pixel 2D / 2.5D static game assets such as trees, flowers, buildings, props, items, furniture, and environmental objects.

Do not expand it into character animation, Photoshop, Spine, or engine integration.
