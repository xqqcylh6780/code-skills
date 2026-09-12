---
name: game-art-maker
description: >
  Generate consistent non-pixel 2D / 2.5D game characters and pets.
  Focus on character creation, turnarounds, multi-view consistency,
  and action poses such as walking, running, jumping, attacking,
  waving, raising a paw/hand/wing, sitting, sleeping, and similar motions.
---

# Game Art Maker

## Scope

This skill ONLY handles image generation for:

- Non-pixel 2D game art
- Stylized 2.5D game art
- Pets / companions
- Human / humanoid characters
- Character turnarounds / multi-view sheets
- Character consistency across images
- Walking / running / jumping / attacking / gesture poses
- Other requested character actions

This skill does NOT cover:

- Photoshop cleanup
- Layer separation
- Spine rigging
- Godot / Unity integration
- Export pipelines
- Sprite packing
- PSD production
- Post-processing workflows

Once the image is generated correctly, downstream editing belongs to other tools or workflows.

---

# Core Goal

The highest priority is:

> Generate the SAME character repeatedly without changing the character design.

Changing pose, direction, expression, or camera angle must NOT redesign the character.

Priority order:

1. Character identity consistency
2. Correct requested pose / action
3. Correct requested view / direction
4. Correct anatomy and body-part count
5. Consistent visual style
6. Clean silhouette and composition
7. Rendering polish

---

# Default Visual Style

Unless the user specifies another style, use:

> polished non-pixel 2D / 2.5D game art, clean stylized shapes,
> crisp dark outlines, controlled cel shading, subtle soft gradients,
> readable silhouette, compact game-ready proportions,
> strong color blocking, polished mobile / indie game character quality,
> slightly dimensional but still illustrated, not photorealistic.

Do not force a fixed color palette.

If a reference image is supplied, its style and palette take priority.

---

# Reference Image Consistency

When a reference image exists, treat it as the character's canonical design.

Preserve:

- species / character identity
- head-to-body ratio
- body proportions
- face shape
- eye shape and eye color
- mouth / beak / muzzle
- ears / horns / feathers / hair
- clothing
- armor structure
- accessory placement
- gem / emblem placement
- wing / tail structure
- main colors
- secondary colors
- outline style
- rendering style
- overall silhouette

Do not add new design elements unless requested.

Do not remove existing important design elements unless requested.

Rule:

> Change the pose or angle, not the character.

---

# Canonical Character Workflow

For a new character, prefer this sequence:

1. Generate one canonical character image.
2. User approves the design.
3. Use the approved image as the identity reference.
4. Generate additional views.
5. Generate action poses.
6. Continue using the same approved reference for future images.

Do not redesign the character for each request.

---

# Single Character / Pet Mode

Use when the user asks for one character or pet.

Default rules:

- one subject only
- full body visible
- centered composition
- no cropped feet, wings, ears, tails, horns, or accessories
- no extra characters
- no text
- no watermark
- transparent background when suitable
- clean silhouette

---

# Turnaround / Multi-View Mode

Use for requests such as:

- 三视图
- 四视图
- front / side / back
- character turnaround
- multi-angle reference

For 三视图, use:

- front view
- true side view
- back view

Optional if requested:

- 3/4 front
- 3/4 back

Requirements:

- same character in every view
- same proportions
- same scale
- same colors
- same clothing / armor
- same accessories
- same facial identity
- same tail / wing structure
- neutral pose
- no dramatic perspective
- no random redesign of hidden areas
- no text unless explicitly requested

Important:

> A side view must be a real side view, not another 3/4 view.

> A back view must preserve the established design and must not invent unrelated structures.

---

# Action Pose Mode

Use for:

- walk
- run
- jump
- attack
- wave
- raise hand
- raise paw
- raise wing
- sit
- sleep
- hurt
- victory
- skill cast
- dodge
- crouch
- idle

Rules:

- preserve character identity
- preserve colors
- preserve outfit / armor
- preserve accessories
- preserve body proportions
- keep full character visible
- use a readable key pose
- avoid unnecessary motion blur
- no new costume details
- no random weapon or prop unless requested

---

# Walk Pose

When the user asks for walking, use a readable walking key pose.

Typical motion:

- one leg forward
- opposite leg back
- opposing arm / wing swing
- slight body shift
- stable head design
- readable foot placement

If a walk cycle is requested, prefer these key poses:

1. Contact
2. Down
3. Passing
4. Up

Keep:

- same scale
- same direction
- same character design
- same ground baseline

---

# Run Pose

When the user asks for running, use:

- stronger forward lean
- larger leg separation
- stronger arm / wing counter-swing
- clearer body compression / extension
- readable dynamic silhouette

If a run cycle is requested, prefer:

1. Reach / contact
2. Compression
3. Passing
4. Airborne / extension

Do not use heavy motion blur for animation reference images.

---

# Gesture / Raise Limb Pose

For requests such as:

- 举手
- 举爪子
- 举翅膀
- 挥手
- 指向某处

Keep the body design unchanged.

Only modify the relevant limb and supporting body posture.

For a single pose, use the clearest readable "hold" position.

---

# 2D Mode

Use when the user requests normal illustrated 2D.

Visual traits:

- clean contour
- strong silhouette
- flatter depth
- controlled cel shading
- illustrated appearance
- non-pixel
- non-photorealistic

Suggested style anchor:

> polished stylized 2D game character, clean dark outlines,
> controlled cel shading, readable silhouette, smooth graphic shapes,
> high-quality game illustration, non-pixel art

---

# 2.5D Mode

Use when the user requests 2.5D.

Visual traits:

- stronger form volume
- clearer light and shadow
- more dimensional material rendering
- illustrated rather than photorealistic
- still suitable for a game character asset

Suggested style anchor:

> stylized 2.5D game character, illustrated cel-shaded rendering,
> stronger dimensional volume, clean dark contours,
> controlled directional lighting, polished game-art finish,
> non-pixel, not photorealistic

---

# Camera / View Terms

Use precise view definitions:

## Front
Character faces the camera directly.

## 3/4 Front
Character rotated approximately 30–45 degrees.

## True Side
Profile view at approximately 90 degrees.

## Back
Back directly faces the camera.

## 3/4 Back
Rear three-quarter view.

Do not substitute one for another when the user requests a specific view.

---

# Background Rules

For isolated character / pet assets:

Prefer transparent background.

Do NOT use:

- checkerboard imitation
- scenery
- decorative frames
- random effects
- text
- logos
- watermarks

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
- no extra characters
- no extra limbs
- no extra wings
- no duplicate body parts
- no missing limbs
- no malformed anatomy
- no cropped extremities
- no random accessories
- no costume redesign
- no color drift
- no armor redesign
- no inconsistent proportions
- no identity drift
- no busy background

---

# Prompt Construction Logic

Build prompts in this order:

1. Character identity
2. Reference-image fidelity
3. Requested view
4. Requested action
5. 2D or 2.5D visual style
6. Character consistency constraints
7. Full-body composition
8. Background requirement
9. Negative constraints

Example internal structure:

```text
A single [character/pet].

Keep the exact same design as the provided reference:
[important identity traits].

View:
[front / true side / back / 3/4].

Action:
[walk / run / jump / raise paw / etc.].

Style:
polished non-pixel 2D / 2.5D game art,
clean dark contours, controlled cel shading,
readable silhouette, illustrated game rendering.

Preserve:
proportions, face, colors, costume, armor, accessories,
wing/tail structure, and all identifying design features.

Full body visible, centered, no cropping.
Transparent background.
No text, no extra limbs, no redesign, no identity drift.
```

Do not expose internal prompt-building logic unless the user asks for the prompt.

---

# Response Behavior

If the user asks to generate an image:

- generate the image directly
- use current-conversation reference images when available
- do not ask unnecessary questions when the request is already clear

If the user asks for a prompt:

- return a clean reusable image-generation prompt

If the user asks for multiple poses:

- preserve one canonical character reference
- keep view direction and scale consistent unless the user requests changes

---

# Final Rule

The skill exists for one purpose:

> Create the same non-pixel 2D / 2.5D game character or pet consistently across different views and actions.

Do not expand the skill into Photoshop, Spine, rigging, engine integration, or post-production.
