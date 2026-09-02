# Visual Direction and Product Design

Read when creating or materially revising visual identity. Skip for focused changes inside an established design system unless the change exposes an unresolved visual decision.

## Table of contents

- Ground the direction in the product
- Create a compact direction plan
- Use hierarchy and composition
- Design typography deliberately
- Build a functional color system
- Use spacing, containers, and geometry
- Choose imagery, icons, and illustration
- Use motion with purpose
- Write interface copy
- Avoid template defaults
- Review the direction before implementation

## Ground the direction in the product

Define the product's subject, audience, environment, and primary task. Draw visual language from the subject's real materials, instruments, data, processes, culture, and vocabulary.

Ask:

- What should users notice first?
- What should the interface make easy or trustworthy?
- Is the product editorial, operational, analytical, transactional, playful, luxurious, technical, institutional, or something else?
- Which visual quality would be inappropriate even if fashionable?
- What content or interaction is uniquely characteristic of this product?

A distinctive interface is not necessarily loud. It is specific. A restrained system can be memorable through proportion, typography, pacing, or one characteristic interaction.

## Create a compact direction plan

Before implementation, describe:

```text
Design thesis: one sentence connecting product and visual behavior
Canvas and surface character:
Typography roles:
Layout model and content rhythm:
Signature element:
Component geometry:
Imagery/icon treatment:
Motion cues:
Explicit anti-patterns for this project:
```

Choose one coherent direction. Avoid averaging several incompatible inspirations into a vague style.

For alternative concepts, vary structural ideas—not just accent colors. Compare information hierarchy, composition, density, typography, imagery, and interaction model.

## Use hierarchy and composition

Make structure express information priority:

- Give the primary task or message one obvious focal point.
- Use scale, position, whitespace, contrast, grouping, and alignment before adding decoration.
- Let important content occupy meaningful space; do not give every block equal visual weight.
- Vary rhythm across long pages while preserving grid and token consistency.
- Use cards only where bounded objects or actions need containment.
- Use bands, lists, tables, rails, canvases, full-bleed media, or open whitespace when they better match the content.
- Keep the first viewport complete enough to orient the user without crowding it.

Structural devices must encode something true. Numbers imply sequence or quantity; badges imply classification or status; dividers imply grouping; tabs imply peer views. Do not use them as filler.

## Design typography deliberately

Define roles rather than selecting a fashionable font in isolation:

- Display or editorial voice.
- Body reading voice.
- Interface/control voice.
- Data/monospace role when relevant.

Specify family and fallback, size, weight, line height, tracking, casing, and responsive behavior. Use a limited scale with clear relationships.

Review:

- Heading wrapping at realistic widths.
- Body measure and reading rhythm.
- Control labels, table text, captions, helper text, and dense chrome.
- Numeric alignment and tabular figures where data comparison matters.
- Font loading, fallbacks, and layout shift.
- Language coverage and longer localized strings.

Do not rely on browser-default typography for controls. Do not use decorative type at sizes or densities where it becomes hard to read.

## Build a functional color system

Define semantic roles:

- Canvas and elevated surfaces.
- Primary and secondary text.
- Borders and separators.
- Accent and interactive states.
- Success, warning, error, and informational states.
- Focus indication and selection.

Use contrast and hierarchy, not many unrelated colors. Validate important text and non-text contrast. Provide non-color cues for status.

Avoid defaulting to purple/indigo, warm cream, neon-on-black, or muted gray simply because they are common generated aesthetics. Use them only when the brief supports them.

For light and dark themes, design each as a system; do not mechanically invert colors. Preserve hierarchy, contrast, elevation, imagery treatment, and semantic meaning.

## Use spacing, containers, and geometry

Build from a consistent spacing scale while allowing optical adjustment where needed. Define:

- Page gutters and maximum readable widths.
- Section spacing and internal component density.
- Grid columns, gaps, and alignment lines.
- Radius hierarchy.
- Border and shadow purpose.
- Stable media aspect ratios.

Avoid identical large padding everywhere, deeply nested rounded containers, or shadows on every surface. Geometry should communicate grouping, hierarchy, and interaction.

## Choose imagery, icons, and illustration

Use imagery when it carries product meaning, emotional tone, explanation, or evidence. One strong image system is usually better than many unrelated decorative assets.

For supplied references, preserve crop logic, lighting, background interaction, and framing—not only subject matter.

Use the existing icon family when possible. Match metaphor, filled versus outline style, stroke weight, optical size, corner treatment, baseline, and state behavior. Do not substitute approximate text glyphs for interface icons.

Use ImageGen for central raster concepts and assets when it materially improves the product. Keep navigation, forms, buttons, labels, tables, and other interactive UI code-native. Request transparent or background-matched assets when layering is required.

## Use motion with purpose

Motion should clarify hierarchy, causality, continuity, feedback, or spatial relationships.

- Prefer one orchestrated moment over many unrelated animations.
- Keep interaction feedback immediate.
- Use consistent duration and easing roles.
- Avoid delaying primary tasks for decorative entrances.
- Preserve state and focus through transitions.
- Respect `prefers-reduced-motion`; provide a meaningful low-motion result.

Do not animate layout properties unnecessarily when transforms or opacity can express the same effect more smoothly.

## Write interface copy

Write from the user's side of the screen:

- Name actions by their result: `Save changes`, `Publish`, `Send invitation`.
- Keep an action's vocabulary consistent through confirmation and status messages.
- Use labels for recognition, helper text for necessary guidance, and examples only when they teach format.
- Make error messages say what happened and how to recover without exposing internals.
- Make empty states explain the situation and offer the next relevant action.
- Use sentence case and concise active language unless brand requirements specify otherwise.

Avoid filler slogans, vague adjectives, redundant subtitles, and internal technical vocabulary.

## Avoid template defaults

Question these patterns rather than banning them universally:

- Hero eyebrow, giant headline, two buttons, and generic dashboard mockup.
- Repeated three-column feature cards.
- Bento grids without information hierarchy.
- Purple gradients, glass panels, excessive glow, or maximum rounding.
- Pills and badges used as decoration.
- Fake metrics, logos, testimonials, or activity feeds.
- Oversized icons in every card.
- Alternating text/image sections repeated mechanically.
- Warm off-white plus serif display chosen without product justification.
- Decorative numbering where content is not sequential.

Use any of these when they truthfully serve the brief. The problem is automatic use, not the component itself.

## Review the direction before implementation

Ask:

- Could this design belong unchanged to a different product?
- Does the visual thesis reinforce the primary task?
- Is there one memorable decision rather than many competing effects?
- Is the information hierarchy clear without decoration?
- Does typography carry an intentional voice at all levels?
- Are real content and difficult states represented?
- Is the direction practical to implement responsively and accessibly?
- Which element can be removed without losing meaning?

Revise generic or unsupported decisions before coding. During implementation, preserve the chosen system while allowing necessary accessibility and responsive adaptations.
