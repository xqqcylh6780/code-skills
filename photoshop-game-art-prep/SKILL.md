---
name: photoshop-game-art-prep
description: >
  Prepare AI-generated 2D / 2.5D game characters and pets in Photoshop for later animation.
  Focus on clean cutout, layer separation, reconstruction of hidden body areas, transparent background,
  consistent layer naming, overlap-safe joints, and PSD organization suitable for later skeletal animation.
---

# Photoshop Game Art Prep

## Scope

This skill ONLY handles Photoshop preparation of already-generated 2D / 2.5D game characters or pets.

Use it for:

- removing the background
- cleaning edges
- separating body parts into layers
- rebuilding hidden areas behind overlapping parts
- preparing overlap-safe joints
- organizing a clean PSD
- naming layers consistently
- preserving the original character design
- preparing artwork for later animation software

This skill does NOT handle:

- generating new character designs
- changing the visual style
- creating animation in Spine
- Godot / Unity integration
- sprite-sheet packing
- game-engine export pipelines

The goal is simple:

> Turn one finished character image into a clean, editable, animation-ready Photoshop document.

---

# Highest Priority

Preserve the original character.

Do not redesign:

- face
- body proportions
- colors
- armor
- clothing
- accessories
- gems / emblems
- wings
- tail
- silhouette

Photoshop work should separate and reconstruct the existing design, not invent a new one.

Priority order:

1. Preserve character identity
2. Clean separation of body parts
3. Reconstruct hidden areas correctly
4. Maintain enough overlap around joints
5. Clean transparent edges
6. Clear layer organization
7. Non-destructive editing where practical

---

# Default Workflow

Use this sequence:

1. Open the original character image.
2. Duplicate the original as a locked backup layer.
3. Remove the background.
4. Identify the minimum useful animation parts.
5. Separate those parts into independent layers.
6. Reconstruct body areas that were hidden by overlapping parts.
7. Add extra overlap around joints.
8. Clean masks and edges.
9. Name and group layers consistently.
10. Save the master PSD.

Do not over-split the character unless the intended animation requires it.

---

# Recommended Part Strategy

For a simple pet or mascot, start with:

- head
- body
- left arm / wing
- right arm / wing
- left leg
- right leg
- left foot
- right foot
- tail

Optional separate parts:

- mouth / beak
- eyes
- eyelids
- ears
- hair
- helmet
- chest armor
- gems
- cape
- weapon
- floating ornament

Rule:

> Split only parts that need to move independently.

A simple character should not become 50 unnecessary layers.

---

# Layer Naming

Use clear stable names.

Recommended naming:

```text
00_REFERENCE

HEAD
  head_base
  eye_L
  eye_R
  mouth
  head_armor

BODY
  body_base
  chest_armor
  chest_gem

ARM_L
  arm_L

ARM_R
  arm_R

LEG_L
  leg_L
  foot_L

LEG_R
  leg_R
  foot_R

TAIL
  tail
```

For animals, replace `arm` with the actual anatomy where useful:

- wing_L
- wing_R
- paw_L
- paw_R

Use `_L` and `_R` consistently.

---

# Background Removal

For isolated assets:

- remove all background pixels
- preserve antialiased contour edges
- avoid white halos
- avoid dark halos
- keep semi-transparent edge pixels where needed
- inspect at 100% and 200% zoom

Do not paint a fake checkerboard background.

The PSD should contain real transparency.

---

# Separating Parts

Each moving body part should become its own layer.

When separating:

- preserve the original silhouette
- avoid deleting pixels needed by neighboring parts
- use masks before destructive erasing when possible
- keep the original layer untouched as backup
- check the separated result against the source image

After separation, temporarily move each part away from the body to verify that it is complete.

---

# Hidden Area Reconstruction

This is the most important step.

When one body part covers another in the original image, the hidden part must be reconstructed before animation.

Examples:

- wing covers torso
- arm covers chest
- leg overlaps body
- tail sits behind body
- head covers neck
- armor covers body

If a wing is raised later, the torso behind it must already exist.

Rule:

> Every moving part should reveal complete artwork behind it.

Do not leave empty holes hidden under limbs.

---

# Joint Overlap

Do not cut exactly at visible joint boundaries.

Leave extra artwork under the neighboring part.

Examples:

- shoulder should extend under torso / arm overlap
- thigh should continue under body
- foot should overlap leg
- neck should extend under head
- tail root should continue behind body

Recommended principle:

> Hidden overlap is better than exposed gaps.

The overlap should be large enough to support moderate rotation without revealing holes.

---

# Cleaning Seams

After separating and reconstructing:

- move parts through small test rotations
- test ±15°
- test ±30° where reasonable
- inspect for gaps
- inspect for duplicated outlines
- inspect for sudden contour breaks

If a seam appears:

- extend the hidden artwork
- soften or remove duplicated contour lines
- repaint the joint transition

---

# Outline Handling

For stylized characters with dark outlines:

Avoid double outlines at joints.

Example:

A wing resting on the torso may have an outline on both layers.
When the wing rotates, the torso outline hidden underneath may become visible unnaturally.

Solution:

- keep the visible contour on the foreground part
- reconstruct the hidden base shape without unnecessary internal outline
- paint only the contour that should appear when exposed

Maintain the same line weight as the source art.

---

# Eyes and Facial Parts

Separate facial features only when needed.

For simple animation:

- head can remain one layer

For blinking / expression:

- eye_L
- eye_R
- eyelid_L
- eyelid_R
- mouth / beak

Do not separate facial features unnecessarily if no facial animation is planned.

---

# Armor and Accessories

Separate armor only if it needs independent movement.

Keep fixed armor merged with its parent body part when practical.

Examples:

- helmet fixed to head -> may stay with head
- chest plate fixed to torso -> may stay with body
- dangling charm -> separate
- cape -> separate
- floating crystal -> separate

Avoid excessive fragmentation.

---

# Non-Destructive Editing

Prefer:

- layer masks
- smart objects when useful
- grouped layers
- backup source layer
- adjustment layers for global corrections

Avoid destroying the only copy of the source image.

Always keep a locked original reference layer.

---

# Canvas and Resolution

Do not resize unnecessarily.

Keep the source resolution unless there is a clear production reason to change it.

Ensure:

- enough empty canvas around moving parts
- no cropped ears / feet / wings / tails
- transparent outer area
- character remains centered enough for easy later use

---

# Final PSD Structure

Recommended final document:

```text
00_REFERENCE
  original_locked

01_HEAD
  head_base
  eye_L
  eye_R
  mouth

02_BODY
  body_base
  chest_armor

03_LEFT
  wing_L
  leg_L
  foot_L

04_RIGHT
  wing_R
  leg_R
  foot_R

05_OTHER
  tail
  cape
  accessory
```

Not every character needs every folder.

Keep the structure simple.

---

# Quality Check

Before considering the Photoshop preparation complete, verify:

- background is truly transparent
- no white / dark halo
- no important part is cropped
- each moving part is on its own layer
- hidden body areas are filled
- joints have enough overlap
- no accidental holes appear when moving limbs
- no double outlines appear at joints
- layer names are clear
- left / right naming is consistent
- the original reference is preserved
- the character still matches the source exactly

---

# User Guidance Behavior

If the user provides a character image and asks how to split it:

1. Identify the minimum useful parts.
2. Explain which parts should remain merged.
3. Explain which hidden areas must be reconstructed.
4. Provide a recommended PSD layer tree.
5. Avoid unnecessary complexity.

If the user asks about a specific action, tailor the split to that action.

Example:

For only "raise wing":

- body
- wing_L
- wing_R
- head
- legs

may be enough.

For "walk + run + jump":

separate legs and feet individually.

---

# Final Rule

This skill does one job:

> Prepare a finished 2D / 2.5D character image in Photoshop so its parts can move later without gaps, broken outlines, or design drift.

Do not expand this skill into image generation, Spine animation, or game-engine work.
