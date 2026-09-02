---
name: build-frontends
description: >-
  Design, implement, improve, or browser-verify user-facing web interfaces. Use for pages,
  applications, dashboards, landing pages, components, forms, navigation, responsive layouts,
  accessibility, screenshot or wireframe implementation, visual polish, and redesigns. Preserve
  an established design system when one exists. Do not use for backend-only work, non-visual
  business logic, or contract design without a user-facing implementation.
---

# Build Frontends

Deliver a frontend that works as a product surface, not merely code that compiles. Establish a
specific visual direction, implement the complete user path, inspect the rendered result, and
correct material defects before handoff.

## Choose the Mode

Choose one mode before editing:

- **Preserve:** focused work inside an established design system.
- **Extend:** a new surface that must feel native to an existing product.
- **Concept:** a new product or interface without a settled visual language.
- **Redesign:** an intentional visual or structural change to an existing surface.
- **Audit:** evidence-backed UX, visual, responsive, or accessibility review without edits unless
  the user asks for fixes.

Do not turn a focused request into a redesign. Do not invent a new visual language when the
repository or supplied reference already establishes one.

### Focused-change fast path

For an obvious copy, CSS, template, or isolated component change, inspect the smallest relevant
source area, make the edit, run at most one focused check when useful, and stop. Do not create a
design brief, launch a browser, add tests, or load design references unless the result genuinely
depends on them or the user requests them.

## Route Supporting Guidance

Load only the references needed for the current work:

- New visual identity, typography, color, composition, imagery, motion, or interface copy:
  [visual-direction.md](references/visual-direction.md).
- No established style, or a need to compare concrete design directions:
  [style-directions.md](references/style-directions.md).
- A project or supplied reference includes `DESIGN.md`, or the user wants to adapt one:
  [design-md.md](references/design-md.md).
- Concept work, major redesign, or output that still feels generic:
  [taste-critique.md](references/taste-critique.md).
- Requests such as polish, simplify, amplify, quiet, harden, onboard, typeset, animate, adapt, or
  optimize: [refinement-passes.md](references/refinement-passes.md).
- Component boundaries, state ownership, forms, responsive architecture, rendering, or
  performance: [frontend-engineering.md](references/frontend-engineering.md).
- Implementing or polishing text wrapping, reading measure, or numeric alignment:
  [typography-recipes.md](references/typography-recipes.md).
- Implementing or polishing nested surfaces, icon alignment, depth, or small controls:
  [surface-recipes.md](references/surface-recipes.md).
- Implementing or polishing press feedback, icon swaps, or enter/exit transitions:
  [motion-recipes.md](references/motion-recipes.md).
- Forms, dialogs, menus, focus, dynamic content, charts, media, or accessibility verification:
  [accessibility.md](references/accessibility.md).
- Material visual or interaction verification: [browser-qa.md](references/browser-qa.md).

Use `diagnose-bugs` for failures with an unknown cause, `test-behavior-first` for deterministic
behavior changes with a practical test seam, `design-interfaces` for public contracts, and
`secure-boundaries` when the interface handles identity, privileges, secrets, uploads, payments,
or untrusted content.

## Execute the Frontend Loop

### 1. Recover the local product contract

Inspect the smallest set of relevant files and, when available, the current rendered surface.
Identify:

- framework, routing, styling, state, data, and test conventions;
- page shell, components, tokens, fonts, icons, assets, and nearby surfaces;
- primary user, task, content, states, responsive constraints, and supplied references;
- acceptance evidence: source inspection, tests, screenshots, or browser workflows.

For material visual work, look for a relevant project-owned or user-supplied `DESIGN.md` without
turning a focused-change task into broad discovery. Read only the applicable file; when found,
follow [design-md.md](references/design-md.md) before choosing or changing the visual direction.

Reuse the repository's components and tokens when they fit. Preserve server rendering, hydration,
caching, supported browsers, and existing data-flow patterns unless the user requests a change.

### 2. Commit to a design direction

For material Concept or Redesign work, write a compact internal design contract before coding:

```text
Product and primary user:
Primary task and content hierarchy:
Visual direction and one signature idea:
Typography, color, geometry, density, and motion:
Responsive and accessibility constraints:
Evidence required for completion:
```

If the direction is unsettled, compare two concise candidates and select the one that best fits the
product, audience, and content. When there is no established system or approved visual reference,
use the bundled design-intelligence search to inform the choice:

```text
python <skill-root>/scripts/design-intelligence/search.py "<product audience task tone density>" --design-system -f markdown -p "<project>"
```

Treat results as candidates, not authority. Reject recommendations that conflict with the product,
brand, accessibility, font availability, or implementation constraints. Do not persist generated
design-system files unless the user requests that artifact.

### 3. Implement a complete vertical slice

Build the primary path end to end before multiplying components or decorative detail.

- Keep shells as composition glue and give components meaningful ownership boundaries.
- Separate remote data, domain state, URL state, and transient presentation state by lifecycle.
- Prefer semantic native elements, explicit variants, and repository-native icons.
- Centralize repeated visual decisions in existing tokens, CSS variables, or theme primitives.
- Make every visible control work; do not ship decorative filters, fake buttons, or misleading data.
- Include the relevant loading, empty, populated, validation, error, disabled, pending, and success
  states.
- Handle long content, localization expansion, narrow viewports, and large or small data sets where
  they materially affect the surface.

### 4. Inspect the rendered interface

For a new surface, redesign, material layout change, or runtime-dependent interaction, use the
repository's existing development command and a real browser when the task authorization permits.
Do not install dependencies or replace the project's tooling merely to perform verification.

Check the primary workflow at narrow, intermediate, and wide widths as relevant. Inspect hierarchy,
wrapping, overflow, focus, keyboard use, state transitions, console errors, and relevant network
failures. Capture screenshots for visual work and compare them with supplied references or the
design contract.

If the application cannot be run within the granted permissions or available environment, say so
and distinguish source-verified behavior from unverified runtime behavior.

### 5. Critique once, then correct

After the first meaningful render, perform one deliberate correction round:

- Does the first glance reveal the primary action and content hierarchy?
- Does the silhouette look product-specific rather than template-shaped?
- Are typography, spacing, color, geometry, imagery, and motion one coherent system?
- Are controls, data, and states believable and complete?
- Is mobile intentionally reflowed rather than squeezed?
- Are focus, labels, contrast, reduced motion, and semantic structure adequate?

Fix material mismatches before polishing minor details. For major Concept or Redesign work, use the
scored review in `references/taste-critique.md` and resolve every zero-score dimension.

### 6. Verify proportionately

Inspect verification scripts and their relevant hooks for side effects before running the
repository's focused checks; a command named `build` can also migrate data or publish output.
Respect the user's database and execution restrictions. For changes to routing, asset paths,
SSR/hydration, or build configuration, follow the served-build check in
[browser-qa.md](references/browser-qa.md) when safe and available.
Protect the critical rendering path: avoid unnecessary dependencies, duplicate fetching, obvious
waterfalls, unbounded rendering, layout-shifting media, and premature performance abstractions.

## Hard Quality Gates

Do not hand off material interface work with:

- clipped, overlapping, horizontally scrolling, or broken primary content;
- lorem ipsum, placeholder boxes, invented product claims, or obviously rough seeded data;
- inert controls or missing core workflow states;
- generic card grids, excessive pills, arbitrary gradients, or decoration unrelated to the brief;
- missing keyboard access, invisible focus, unlabeled controls, or color-only state communication;
- mobile behavior that is only a compressed desktop layout;
- implementation-caused console errors;
- a claimed visual match that was never rendered and inspected;
- a passing build presented as the only evidence of visual quality.

## Handoff

Lead with the implemented outcome. Briefly state the chosen mode and direction, primary interactions,
responsive and accessibility evidence, browser workflows or screenshots checked, focused code
checks, and any remaining runtime limitation. Do not emit an empty checklist or repeat this workflow.

Material frontend work is complete only when the primary path works, the rendered result has been
inspected when permitted, and material visual, responsive, interaction, and accessibility defects
found during that inspection have been corrected.
