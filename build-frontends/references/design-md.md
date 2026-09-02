# Using DESIGN.md

Use a `DESIGN.md` as structured visual evidence: it can define atmosphere, tokens, typography,
component treatment, layout, motion, responsiveness, and guardrails. It does not replace source
inspection, user requirements, interaction behavior, accessibility, or browser verification.

## Discover the Applicable Contract

Check for `DESIGN.md` only when the task materially depends on visual direction. Prefer, in order:

1. a file or design reference explicitly selected by the user;
2. the project-owned `DESIGN.md` applicable to the edited surface;
3. an external or example `DESIGN.md` chosen as inspiration.

Do not load a catalog of alternatives when one relevant file is already selected. Do not blend
multiple brand systems by default. If multiple project-owned files could apply, use the closest
scope that actually governs the surface and note any material ambiguity.

## Classify Before Applying

Determine whether the file is:

- **Current contract:** describes the existing product and should guide Preserve or Extend work.
- **Target contract:** describes an approved redesign or new direction.
- **Reference:** analyzes another product or brand and supplies ideas rather than requirements.

When the document and implemented product disagree, do not silently treat either as authoritative.
Use the task mode, source evidence, and latest user request to decide whether the difference is
drift to repair, a pending migration, or an unsuitable reference.

## Convert It into Implementable Decisions

Extract only what affects the current surface:

- semantic color roles and contrast relationships, not merely a list of hex values;
- available font families, fallbacks, scale, measure, weight, and line-height;
- spacing, geometry, borders, elevation, imagery, and icon treatment;
- component states, hierarchy, density, and interaction feedback;
- breakpoint intent, reflow behavior, touch targets, focus, and reduced motion;
- explicit do/don't guidance and the signature idea that makes the direction recognizable.

Map repeated decisions into the repository's existing tokens and component variants. Do not create
a second token system when the established one can express the direction. Treat numeric values as
inputs to validate, not mandatory constants when content, platform, or accessibility requires an
adjustment.

## Adapt External Brand References

Preserve the design principles that fit the user's product while replacing brand-specific content.
Do not copy trademarks, logos, proprietary fonts, screenshots, product claims, or distinctive
assets without supplied rights and files. Use available project-native fonts and assets, and keep
the product's own information architecture and content hierarchy.

Reject or adjust reference rules that conflict with:

- the user's explicit requirements or an established project design system;
- readable contrast, visible focus, keyboard use, reduced motion, or touch usability;
- available assets, supported browsers, performance, localization, or framework constraints;
- the actual content and primary task of the surface.

Record the adapted result in the compact design contract used by the frontend loop. Do not persist
a new or rewritten `DESIGN.md` unless the user requests that artifact.

## Verify the Translation

Compare the rendered interface against the adapted contract, not just the source reference's
colors. Check hierarchy, density, typography, geometry, imagery, states, and responsive behavior.
State which parts were preserved, adapted, or omitted when those choices materially affect the
result.
