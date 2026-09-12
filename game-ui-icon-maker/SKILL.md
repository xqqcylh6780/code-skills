---
name: game-ui-icon-maker
description: >
  Generate consistent non-pixel 2D / 2.5D game UI icons such as menu, arrows, shop,
  inventory, settings, mail, quests, map, currency, skills, warnings, close/back buttons,
  and other small functional game interface icons. Prioritize small-size readability,
  silhouette clarity, style consistency, transparency, and coherent icon sets.
---

# Game UI Icon Maker

## Scope

Use this skill for non-pixel game UI icons and small interface graphics.

Typical targets:

- menu
- arrows
- back
- close
- confirm
- cancel
- shop
- backpack
- inventory
- settings
- mail
- quests
- map
- home
- profile
- chat
- notifications
- search
- lock / unlock
- warning
- info
- help
- plus / minus
- refresh
- download / upload
- currency icons
- coins
- gems
- energy
- health
- mana
- skill icons
- item icons
- equipment icons
- category icons
- navigation icons
- tab icons
- small button symbols
- other compact game-interface graphics

This skill is NOT for:

- character animation
- pets / NPC turnarounds
- environment art
- large scene illustrations
- Photoshop cleanup
- Spine
- Godot / Unity integration
- pixel art unless explicitly requested elsewhere

---

# Core Goal

The main goal is:

> Generate UI icons that remain immediately recognizable at small sizes and look like they belong to the same game.

Priority order:

1. Small-size readability
2. Clear silhouette
3. Functional meaning
4. Style consistency
5. Shape simplicity
6. Strong local contrast
7. Clean composition
8. Rendering polish

---

# Default Visual Style

Unless the user specifies another style, use:

> polished non-pixel 2D / 2.5D game UI icon, compact centered composition,
> crisp dark outline, clean cel shading, subtle dimensional highlights,
> strong silhouette, simple geometric shape language, premium mobile / indie game UI quality,
> readable at small size, not photorealistic.

If a reference icon or existing UI set is provided, its visual language takes priority.

---

# Small-Size Readability

Every icon must remain recognizable when reduced.

Prefer:

- one primary symbol
- one focal shape
- limited internal detail
- strong contour
- clear negative space
- simple lighting
- distinct foreground/background separation

Avoid:

- tiny decorative details
- thin fragile lines
- overly complex textures
- multiple competing subjects
- unnecessary perspective
- cluttered backgrounds

Rule:

> If the icon only works when viewed large, it is not a successful UI icon.

---

# Composition

Default icon composition:

- 1:1 square canvas
- centered subject
- generous safe margin
- no cropped edges
- visually balanced
- transparent background
- no text unless explicitly requested

Keep important shapes away from the outer edge.

For button icons, preserve enough breathing room for later placement inside UI containers.

---

# Icon Set Consistency

When generating multiple icons for the same game, preserve:

- outline thickness
- outline color
- corner roundness
- perspective
- lighting direction
- shadow hardness
- highlight style
- saturation
- material treatment
- level of detail
- visual weight
- padding
- overall scale

Rule:

> A menu icon, shop icon, backpack icon, and settings icon from one set should look designed together.

---

# Reference Image Workflow

When the user provides an existing icon or icon set:

1. Identify line thickness.
2. Identify camera angle.
3. Identify material depth.
4. Identify corner shape language.
5. Identify highlight style.
6. Identify shadow style.
7. Identify color intensity.
8. Match these traits in all new icons.

Do not copy unrelated imagery from the reference.

Use the reference as a style anchor, not as a content template.

---

# Functional Icon Mode

Use for navigation and system functions.

Examples:

- menu
- back
- close
- home
- settings
- search
- refresh
- lock
- warning

Requirements:

- instantly understandable
- simple silhouette
- minimal decoration
- no unnecessary depth
- strong directional clarity

For arrows:

- direction must be unmistakable
- use clean arrowhead geometry
- avoid decorative elements that weaken directionality

---

# Feature Icon Mode

Use for game features.

Examples:

- shop
- inventory
- quests
- map
- guild
- chat
- mail
- achievements

Requirements:

- one dominant metaphor
- simplified object design
- strong outline
- enough personality to feel game-specific
- no excessive scene detail

Examples:

Shop:
- storefront
- shopping bag
- coin + awning
- chest / merchant symbol

Inventory:
- backpack
- pouch
- chest
- satchel

Quest:
- scroll
- marker
- exclamation symbol only when explicitly requested

---

# Currency / Resource Icon Mode

Use for:

- coin
- gem
- energy
- health
- mana
- tickets
- tokens

Requirements:

- very strong silhouette
- simple internal shape
- readable at very small size
- suitable for repeated use beside numbers
- visually distinct from one another

Avoid making multiple resources too similar in color and silhouette.

---

# Skill Icon Mode

Use for:

- attack skills
- buffs
- debuffs
- elemental abilities
- spells
- passive skills

Requirements:

- one clear ability concept
- strong central effect
- high contrast
- simplified effect shapes
- restrained particles
- readable at small size

Possible structure:

- central symbol
- one supporting elemental/effect motif
- controlled glow
- no complex full-scene illustration

---

# Item / Equipment Icon Mode

Use for:

- weapons
- armor
- potions
- food
- tools
- collectibles

Default:

- one item only
- 3/4 or front view
- centered
- clean silhouette
- transparent background
- no character holding the item
- no scenery

---

# 2D Mode

Use when the user asks for flat illustrated icons.

Visual traits:

- flatter shading
- graphic shapes
- clear contour
- low visual noise
- high readability
- non-pixel
- non-photorealistic

Suggested style anchor:

> clean stylized 2D game UI icon, crisp dark outline,
> simple cel shading, compact centered composition,
> strong silhouette, high small-size readability

---

# 2.5D Mode

Use when the user wants stronger volume.

Visual traits:

- slightly deeper lighting
- stronger material volume
- subtle top/side planes
- controlled highlights
- still icon-like, not scene-like
- illustrated rather than photorealistic

Suggested style anchor:

> stylized 2.5D game UI icon, compact dimensional form,
> clean dark contour, controlled cel-shaded volume,
> premium mobile game UI rendering, readable at small size

---

# Background Rules

Default:

- true transparent background

Do not use:

- fake checkerboard
- scene background
- decorative frame
- text
- watermark
- logo

unless explicitly requested.

If the user asks for an icon inside a button, treat the button shape as part of the requested asset.

---

# Button Icon Mode

If the user asks for a complete button rather than a bare icon:

Preserve:

- clear button silhouette
- readable foreground symbol
- sufficient contrast
- consistent padding
- consistent corner radius
- same visual depth across a button set

Generate the complete button only when requested.

Otherwise generate the icon alone.

---

# Variants

When the user asks for states or variants:

Examples:

- normal
- hover
- pressed
- disabled
- selected
- locked

Keep the same base geometry.

Change only:

- brightness
- saturation
- glow
- shadow depth
- highlight intensity
- overlay indicator

Do not redesign the icon between states.

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
- no busy background
- no extra objects
- no tiny unreadable details
- no thin fragile lines
- no inconsistent perspective
- no style drift
- no excessive glow
- no clutter
- no cropped edges
- no inconsistent padding
- no mismatched outline thickness

---

# Prompt Construction Logic

Build prompts in this order:

1. Icon function
2. Core visual metaphor
3. 2D or 2.5D style
4. Existing UI/reference style
5. Readability requirements
6. Composition
7. Background
8. Consistency constraints
9. Negative constraints

Example internal structure:

```text
A single [shop / menu / arrow / backpack] game UI icon.

Core symbol:
[clear visual metaphor].

Style:
polished non-pixel 2D / 2.5D game UI icon,
crisp dark outlines, controlled cel shading,
compact readable form, premium mobile game quality.

Match the provided reference set:
same outline thickness, perspective, lighting,
detail level, padding, and color language.

1:1 centered composition.
Large readable silhouette.
True transparent background.
No text, no watermark, no extra decoration,
no style drift, no tiny unreadable details.
```

Do not expose the internal prompt structure unless the user asks for the prompt.

---

# Response Behavior

If the user explicitly asks to generate an image:

- generate it directly
- use current-conversation references when available
- keep the icon isolated unless the user requests a set or button

If the user asks only for:

- advice
- prompt writing
- UI planning
- icon set planning
- naming
- style rules

respond with text only.

Do not generate an image unless the user clearly asks for image generation.

---

# Final Rule

This skill exists for one purpose:

> Generate clean, consistent, non-pixel 2D / 2.5D game UI icons that remain clear and recognizable at small sizes.

Do not expand it into character animation, environment art, Photoshop, Spine, or engine integration.
