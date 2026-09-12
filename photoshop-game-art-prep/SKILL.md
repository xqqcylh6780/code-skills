---
name: photoshop-game-art-prep
description: >
  Prepare an existing non-pixel 2D / 2.5D game character for later Spine-style skeletal animation.
  Default to a minimal body-part breakdown: one complete character plus only the essential movable body parts.
  Preserve the source character exactly and never add expression sheets, turnarounds, animation frames, or unnecessary accessory breakdowns unless explicitly requested.
---

# Photoshop Game Art Prep

## Purpose

This skill has one job:

> Turn one approved character image into a minimal, clean body-part breakdown suitable for later Photoshop layer preparation and Spine rigging.

The default output is NOT a full character design sheet.

The default output contains only:

1. One complete reference character.
2. The essential separated body parts required for skeletal animation.

Do not add unrelated content.

---

# DEFAULT MODE — MINIMAL_SPINE_PARTS

If the user says any of the following:

- Spine 拆分
- Spine 拆分图
- 最简拆分
- 身体部件拆分
- 拆开给 Spine 用
- 动画拆件
- 角色拆件

use `MINIMAL_SPINE_PARTS` by default.

This mode is strict.

---

# Output Must Contain Only

## A. Complete character

Include exactly one complete character as the assembly reference.

Requirements:

- same character as source
- same pose unless user requests otherwise
- same proportions
- same costume
- same colors
- same view
- full body visible
- no cropping

## B. Essential body parts

For a humanoid character, default to:

- head
- torso / body

- left upper arm
- left forearm
- left hand

- right upper arm
- right forearm
- right hand

- left thigh
- left shin
- left foot

- right thigh
- right shin
- right foot

Optional only when clearly needed for independent motion:

- scarf
- cape
- tail
- long hair mass
- wing_L
- wing_R

Do not split fixed clothing, belts, pouches, armor ornaments, gems, badges, or small decorations unless the user explicitly asks.

---

# What Must NOT Appear

In `MINIMAL_SPINE_PARTS`, do NOT generate:

- expression sheet
- extra facial expressions
- separate eyes
- separate eyebrows
- separate mouth
- separate ears
- separate hair strands
- front / side / back turnaround
- 3/4 turnaround
- walk-cycle frames
- run-cycle frames
- action references
- pose references
- extra full-body poses
- animation timeline
- weapon variants
- accessory inventory
- color palette
- labels
- captions
- explanatory text
- decorative panels
- UI framing
- unrelated props

Unless explicitly requested by the user, these are forbidden.

---

# Canonical Source Rule

The provided character image is the ONLY canonical source.

All separated parts must look as though they were physically taken from that exact character.

Preserve exactly:

- face
- hairstyle
- hair color
- eye style
- skin tone
- body proportions
- head-to-body ratio
- clothing
- armor
- scarf
- cape
- gloves
- boots
- belts
- pouches
- decorative motifs
- colors
- line style
- shading style
- camera angle

Rule:

> Separate the character. Do not redesign the character.

Do not invent alternate clothing.
Do not simplify the costume into a new costume.
Do not recolor.
Do not change the art style.
Do not change the character's age or body type.

---

# Part Integrity

Every separated part must be complete enough to animate.

A body part must NOT look like a random visible crop from the source.

Examples:

- upper arm should include enough hidden shoulder area to rotate under the torso
- forearm should include enough elbow overlap
- hand should include enough wrist overlap
- thigh should continue under the torso
- shin should continue under the thigh
- foot should overlap the shin
- neck should continue under the head
- cape/scarf attachment area should include enough hidden artwork for rotation

Principle:

> Hidden overlap is better than exposed holes.

---

# Hidden Area Reconstruction

When the source image contains overlapping parts, reconstruct what is hidden.

Examples:

- arm covers torso
- cape covers shoulder
- scarf covers chest
- thigh overlaps coat
- hand overlaps clothing
- hair covers neck

The reconstructed area must match the original style and color.

Do not leave:

- holes
- transparent gaps
- hard cut edges
- duplicated outlines
- broken clothing shapes

---

# Outline Rule

For stylized art with dark outlines:

- preserve the original line weight
- avoid double outlines at joints
- do not place a visible hard outline inside a hidden joint unless it should really be visible
- reconstruct clean hidden contours

The assembled parts should visually match the original complete character.

---

# Layout Rule

When generating a breakdown sheet:

- put the complete character on one side
- put separated parts on the other side
- keep every separated part isolated
- do not overlap separated parts
- leave generous spacing
- keep parts large enough to inspect
- use a plain or transparent background
- do not add text unless requested

Recommended structure:

```text
┌─────────────────┬──────────────────────────────┐
│                 │ head                         │
│                 │ torso                        │
│                 │ arm_L_upper / forearm / hand │
│ COMPLETE        │ arm_R_upper / forearm / hand │
│ CHARACTER       │ thigh_L / shin_L / foot_L    │
│                 │ thigh_R / shin_R / foot_R    │
│                 │ scarf / cape if needed       │
│                 │                              │
└─────────────────┴──────────────────────────────┘
```

This is a body-part sheet, not a design presentation board.

---

# Do Not Over-Split

The default goal is the MINIMUM useful number of parts.

Bad:

```text
eye_L
eye_R
mouth
eyebrow_L
eyebrow_R
hair_01
hair_02
hair_03
belt_buckle
gem
badge
pouch_strap
boot_buckle
...
```

Good:

```text
head
torso

arm_L_upper
arm_L_lower
hand_L

arm_R_upper
arm_R_lower
hand_R

thigh_L
shin_L
foot_L

thigh_R
shin_R
foot_R

scarf
cape
```

Only split something further if the user explicitly wants that part to animate independently.

---

# Pets / Creatures

For pets or non-humanoid characters, use the same minimal philosophy.

Example:

- complete character
- head
- body
- left front limb / wing
- right front limb / wing
- left rear leg
- right rear leg
- left foot if needed
- right foot if needed
- tail
- optional movable accessory

Do not force humanoid anatomy onto animals.

---

# Photoshop Layer Preparation

If the user asks how to build the PSD after receiving the breakdown:

Use one PSD per character.

Suggested layer structure:

```text
00_REFERENCE
  original_locked

01_HEAD
  head

02_BODY
  torso

03_ARM_L
  upper_arm_L
  forearm_L
  hand_L

04_ARM_R
  upper_arm_R
  forearm_R
  hand_R

05_LEG_L
  thigh_L
  shin_L
  foot_L

06_LEG_R
  thigh_R
  shin_R
  foot_R

07_CLOTH
  scarf
  cape
```

Do not create extra layers without a functional reason.

---

# Background

For separated parts:

- prefer true transparency
- never imitate transparency with a checkerboard pattern
- no scenery
- no decorative background
- no glow
- no shadow plate unless explicitly requested

---

# Prompt Construction for Minimal Breakdown

When generating a minimal breakdown, internally enforce:

```text
Use the provided character as the sole canonical reference.

Create a minimal Spine body-part breakdown sheet.

Show exactly:
- one complete character
- head
- torso
- left upper arm
- left forearm
- left hand
- right upper arm
- right forearm
- right hand
- left thigh
- left shin
- left foot
- right thigh
- right shin
- right foot
- scarf and cape only if they need independent motion

Every separated part must preserve the exact original design, colors,
proportions, clothing, outline style, and shading.

Reconstruct hidden joint areas so each part can rotate without exposing holes.

No expressions.
No turnaround views.
No walk or run frames.
No action poses.
No extra accessories.
No labels.
No text.
No redesign.
No extra character.
```

Do not expose this internal prompt unless the user asks for the prompt.

---

# Quality Checklist

Before considering the result acceptable, verify:

- exactly one complete reference character
- only essential body parts are present
- no expression sheet
- no turnaround sheet
- no animation frames
- no extra poses
- no extra accessories
- source identity is preserved
- costume is unchanged
- colors are unchanged
- body proportions are unchanged
- view is unchanged
- parts are not cropped
- hidden joint areas are reconstructed
- parts do not overlap one another on the sheet
- no obvious holes
- no duplicated joint outlines
- no unnecessary micro-parts

If any forbidden extra content appears, regenerate with stricter constraints.

---

# Response Behavior

If the user explicitly asks to generate a breakdown image:

- use the current source character image
- generate only the minimal body-part sheet
- do not add explanatory sections
- do not add labels unless requested

If the user only asks how to split the character:

- answer in text
- do not generate an image

If the user asks for a more detailed facial or cloth rig later:

- add only the explicitly requested extra parts

---

# Final Rule

Default behavior:

> COMPLETE CHARACTER + ESSENTIAL BODY PARTS ONLY.

No design sheet.
No expression sheet.
No turnaround.
No action sheet.
No animation frames.
No unnecessary micro-parts.
