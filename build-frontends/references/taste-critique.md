# Taste Calibration and Design Critique

Use this reference for concept work, major redesigns, or any surface that is technically sound but still feels generic. It turns subjective taste into explicit constraints and a repeatable critique. It does not replace the product brief, an established design system, accessibility, or browser verification.

## Contents

- [Read the design situation](#read-the-design-situation)
- [Set three independent dials](#set-three-independent-dials)
- [Write a compact taste contract](#write-a-compact-taste-contract)
- [Create distinction without novelty theater](#create-distinction-without-novelty-theater)
- [Detect template-shaped output](#detect-template-shaped-output)
- [Critique the rendered interface](#critique-the-rendered-interface)
- [Redesign without erasing the product](#redesign-without-erasing-the-product)
- [Run the final taste review](#run-the-final-taste-review)

## Read the design situation

Before choosing a style, infer the design situation from evidence:

- Surface type: marketing page, portfolio, editorial page, dashboard, workflow, settings, commerce, documentation, or another product surface.
- Audience: their expertise, urgency, trust requirements, environment, and accessibility needs.
- Primary job: what the user must understand, decide, or complete.
- Brand evidence: existing logo, colors, typography, imagery, voice, and recognizable interaction patterns.
- Reference evidence: supplied screenshots, URLs, named products, and the particular qualities the user values in them.
- Content shape: amount of copy, data density, media availability, content hierarchy, and localization risk.
- Technical constraints: existing stack, components, dependencies, performance budget, and browser support.
- Risk constraints: regulated content, public-sector expectations, commerce trust, destructive actions, or accessibility-critical use.

Summarize the result internally in one sentence:

```text
This is a <surface> for <audience>, optimized for <primary job>, using a <tone> visual language while preserving <constraints>.
```

If two readings would produce materially different interfaces, ask one focused question. Otherwise choose the best-supported reading and proceed.

## Set three independent dials

Calibrate the interface with three independent scales. Do not treat higher values as better, and do not use fixed presets mechanically.

### Composition variance

How far the layout departs from predictable symmetry:

- **1-3, stable:** strong alignment, repeated modules, restrained overlap, familiar scan paths. Suitable for trust-heavy and task-heavy surfaces.
- **4-7, composed:** controlled asymmetry, varied spans and aspect ratios, occasional overlap, mixed section rhythms.
- **8-10, expressive:** unconventional cropping, deliberate imbalance, large negative zones, kinetic or editorial composition. Reserve for contexts where exploration supports the product.

High variance still needs a clear reading order and an explicit small-screen collapse. Random placement is not composition.

### Motion intensity

How much motion participates in comprehension and interaction:

- **1-3, quiet:** state feedback and essential transitions only.
- **4-7, responsive:** coordinated entrances, layout transitions, restrained scroll response, and clear state continuity.
- **8-10, cinematic:** choreographed storytelling, pinned sequences, spatial transitions, or rich canvas work when motion is central to the experience.

Every animation needs a job: explain hierarchy, preserve context, confirm input, reveal causality, or support narrative. If its only defense is that it looks premium, remove it. Honor reduced motion at every level.

### Information density

How much meaningful information appears per viewport:

- **1-3, spacious:** focused marketing, premium consumer, galleries, and editorial storytelling.
- **4-7, balanced:** everyday applications and content-rich pages.
- **8-10, compact:** monitoring, operations, analytics, expert tools, and comparison-heavy workflows.

Density is not the inverse of quality. Spacious products can be vague; compact products can be calm. Adjust type scale, grouping, control size, and navigation model together rather than changing padding alone.

Record the values with one sentence of justification:

```text
Variance 6 / motion 3 / density 8: a compact expert workflow with enough layout variation to separate decisions, but little ambient motion.
```

## Write a compact taste contract

For concept and redesign work, define these decisions before implementation:

```text
Design situation:
Variance / motion / density:
Base direction and restrained secondary influence:
Emotional target:
Signature idea:
Container and grid model:
Typography roles:
Palette and material roles:
Image or illustration treatment:
Shape and icon language:
Interaction character:
Hard exclusions:
Preservation constraints:
```

The contract should be specific enough to reject a plausible-looking but wrong design. Examples of useful exclusions include “no floating-card shell,” “no decorative metrics,” and “no animated background behind the form.” Avoid universal bans such as “never use Inter” or “never use centered layouts”; a pattern is wrong when it conflicts with the situation or is used without intent.

## Create distinction without novelty theater

Choose one signature idea that expresses the product, then let supporting elements stay disciplined. A signature idea may be:

- A layout behavior tied to the content model.
- A distinctive but legible typographic relationship.
- A product-derived visual motif.
- An interaction that makes an important state change easier to understand.
- A recognizable image treatment or data representation.
- A navigation or spatial model that fits the workflow.

Test the idea with three questions:

1. Does it communicate something specific about this product or audience?
2. Does it improve recognition, comprehension, or emotional fit?
3. Can it survive mobile, reduced motion, real content, and repeated use?

If not, it is novelty theater. Remove it before compensating with more decoration.

Build rhythm through contrast rather than constant spectacle:

- Alternate dense and quiet passages where the content supports it.
- Vary section composition without breaking the global grid.
- Give one element primary visual weight instead of making every block a feature.
- Use cards only for meaningful containment, selection, or elevation.
- Let imagery, type, data, and whitespace take turns carrying the composition.

## Detect template-shaped output

Treat these as diagnostic smells, not automatic violations. Ask whether the pattern follows the product or merely fills a familiar slot.

### Composition smells

- Centered hero, centered subcopy, two buttons, then three equal feature cards without a product-specific reason.
- Every section uses the same header, grid, card, and vertical spacing rhythm.
- Repeated left-image/right-copy zigzags that become predictable after the second use.
- Nested cards used to manufacture hierarchy that spacing and headings should provide.
- A default sidebar dashboard shell even when the workflow does not need persistent navigation.
- Bento or masonry layouts chosen before the content count and relationships are known.
- Large empty areas presented as premium spacing while key tasks fall below the fold.
- Eyebrows, numbered labels, pills, badges, and decorative metadata above every heading.

### Visual-language smells

- A fashionable palette, gradient, glass effect, or radius scale unrelated to the brand.
- Warm and cool neutrals mixed accidentally, or multiple competing accents.
- Type chosen from a fashionable shortlist rather than for language coverage, hierarchy, and brand fit.
- Every container has the same maximum rounding, border, and diffuse shadow.
- Icons from mixed families or cliché metaphors that add no information.
- Placeholder imagery whose subject, lighting, crop, and color treatment change from section to section.
- Fake dashboards, fake terminals, fabricated metrics, or decorative status indicators used as visual filler.

### Interaction smells

- Motion on every object, perpetual loops, parallax, or cursor-following effects with no informational role.
- Hover-only discovery for primary content or actions.
- Identical hover scaling on every clickable surface regardless of meaning.
- Animated entrances that delay access to content.
- Motion libraries added for a single transition that CSS or the existing stack already handles.

### Content smells

- Generic brand names, people, testimonials, statistics, awards, or customer logos invented to make the page feel complete.
- Abstract marketing verbs where concrete product behavior should be described.
- Repeated section labels that restate what the heading already says.
- Every heading written in the same cadence or title case.
- Copy shaped to fit a composition at the cost of meaning, accuracy, or localization.

When a smell is present, diagnose the root problem before replacing the pattern. For example, a generic card grid may actually reflect weak information grouping, missing imagery, or equal visual priority—not a card styling problem.

## Critique the rendered interface

Critique the running interface, not just source code. Use screenshots at representative wide and narrow viewports.

### First-glance test

Look for five seconds, then answer:

- What is this surface for?
- What is the first action or idea?
- What feels branded or product-specific?
- What is visually competing with the primary task?

If the answers are unclear, fix hierarchy and content before polish.

### Silhouette and scan-path test

Temporarily ignore color and details:

- Does the page have a recognizable large-scale composition?
- Is the intended reading order visible from grouping, scale, and position?
- Do adjacent sections have distinct jobs and rhythms?
- Are text blocks shaped for readable line lengths rather than arbitrary geometry?
- Does the mobile order preserve task priority?

### System-coherence test

Check whether the interface speaks one visual language:

- Typography roles and weights are consistent without flattening hierarchy.
- Spacing follows a rhythm while allowing optical correction.
- Color roles are semantic and accents are controlled.
- Radius, borders, elevation, imagery, and icons share a coherent character.
- Controls expose hover, focus-visible, active, disabled, pending, error, and success states as relevant.
- Motion timing and easing belong to the same interaction character.

### Reality test

Replace ideal content with adverse cases:

- Long labels, localization expansion, missing media, and multiline values.
- Empty, loading, permission-denied, offline, error, and partial-data states.
- Keyboard-only navigation, 200% zoom, reduced motion, and coarse pointer.
- Small phone, intermediate width, ordinary laptop, and wide screen.
- Slow image loading and late font loading.

A concept that only looks good with curated placeholder content is not a finished interface.

## Redesign without erasing the product

Classify the redesign before editing:

- **Preserve:** modernize within the existing brand and architecture.
- **Evolve:** keep the recognizable system while replacing weak patterns.
- **Overhaul:** create a new visual language while preserving agreed content and product behavior.

Capture a baseline:

- Representative screenshots and viewport sizes.
- Routes, navigation labels, anchor targets, and primary workflows.
- Brand tokens, fonts, imagery, icons, shape language, and motion character.
- Content hierarchy, conversion paths, forms, and important states.
- Accessibility behavior, analytics hooks, SEO metadata, and public URLs.
- Existing strengths worth preserving and concrete problems to retire.

Diagnose root causes before proposing fixes. Separate:

- Structural problems: information architecture, task flow, hierarchy, responsive model.
- System problems: inconsistent tokens, type scale, spacing, shapes, color roles, states.
- Surface problems: individual component styling, asset quality, or microcopy.

Apply redesign work in risk-aware order:

1. Preserve or repair task flow and information hierarchy.
2. Establish tokens, typography, container model, and spacing rhythm.
3. Recompose the highest-value surfaces.
4. Normalize component states and interaction behavior.
5. Improve imagery, material treatment, and motion.
6. Polish optical alignment and micro-details.

Do not silently change URLs, route structure, primary navigation labels, form field semantics, analytics identifiers, legal text, brand marks, or established copy voice. Visual modernization does not authorize product, content, or tracking changes.

Compare before and after at the same content, state, viewport, and scroll position. A redesign succeeds when it improves clarity, task completion, coherence, and brand expression—not merely when it looks newer.

## Run the final taste review

Score each dimension as **0 = unresolved**, **1 = acceptable but generic or inconsistent**, or **2 = deliberate and convincing**:

| Dimension | Question |
|---|---|
| Product specificity | Could this interface belong to an unrelated product after changing the logo? |
| Hierarchy | Is the primary idea or task unmistakable at first glance? |
| Composition | Does the large-scale layout create a controlled scan path and useful rhythm? |
| Typography | Do type choices, line lengths, wraps, weights, and hierarchy fit the content? |
| Color and material | Are palette, surfaces, imagery, and depth coherent and purposeful? |
| Component language | Do shapes, icons, controls, and states feel like one system? |
| Motion | Is motion motivated, coherent, performant, and reduced-motion safe? |
| Responsive behavior | Does each viewport feel composed rather than mechanically collapsed? |
| Accessibility | Can users perceive, understand, navigate, and operate the interface? |
| Content integrity | Is visible copy specific, accurate, complete, and free of invented claims? |
| State completeness | Are realistic success, empty, loading, error, and edge states handled? |
| Finish | Are there unresolved alignment, wrapping, overflow, contrast, or asset issues? |

Resolve every 0. Rework any 1 that affects the primary task, the signature idea, accessibility, or visible polish. Do not chase a perfect score by adding decoration; simplification is often the correct fix.
