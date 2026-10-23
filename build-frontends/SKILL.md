---
name: build-frontends
description: >-
  Build, fix, or review browser UI in React, Vue, Next.js, or HTML/CSS. Use for
  做网页、截图还原、页面不好看、布局样式、交互、响应式 and accessibility. Includes rendered verification; excludes
  uni-app/native apps and scraping.
---
# Build Frontends

Build the requested browser UI in the repository's existing frontend stack. Preserve the local design system,
framework, routing, state, styling, and test conventions. Use the smallest workflow that proves the requested
outcome; a frontend task does not automatically require a redesign, a browser session, or every design reference.

## Route Before Editing

- Browser-only React/Vue/Next/Vite/HTML/CSS UI -> stay in this skill.
- Native Android Kotlin/Java, Compose/Views, lifecycle, permissions, or packaging -> `build-mobile-apps`.
- uni-app, Flutter, React Native, and mini-program implementation are outside these two build skills.
  Follow the actual project's conventions and relevant platform guidance; do not apply Android or browser
  assumptions merely because one deployment target is mobile or H5.
- Unknown-cause UI/runtime failure -> `diagnose-bugs` first.
- Public/shared API or reusable contract change -> `design-interfaces`.
- Authentication, authorization, uploads, payments, secrets, or other trust boundaries -> `secure-boundaries`.
- Performance measurement/optimization as the primary goal -> `performance-engineering`.
- Browser automation without a frontend code change -> `playwright`.
- Requested dependency version transition or upgrade assessment -> `upgrade-dependencies`;
  use this skill for the resulting UI adaptations.

When framework details matter, read [web-stack-routing.md](references/web-stack-routing.md) and preserve the
stack already present in the repository.

## Choose the Smallest Work Mode

### Focused change

Use for a specific copy, CSS, spacing, icon, template, or isolated component edit.

1. Inspect only the owning source and nearby conventions.
2. Make the smallest coherent edit.
3. Run one focused check only when it adds evidence.
4. Stop.

Do **not** create a design brief, run design-intelligence, add dependencies, launch a browser, or expand scope
unless the requested result actually depends on it.

### Product implementation

Use for a new page/component/flow or a material behavior/layout change.

1. Recover the local frontend contract.
2. Implement one complete user path with real states.
3. Verify the changed boundary proportionately.
4. Correct observed material defects and recheck the affected behavior; stop when the outcome is proven.

### Visual redesign / screenshot implementation

Use when the user explicitly asks to redesign, restyle, modernize, match a screenshot/wireframe, or create a new
visual direction. Load only the visual references needed below. Render and inspect the result before claiming
visual fidelity.

### Audit

Use for UX, responsive, accessibility, or visual review without edits unless the user asks for fixes. Report
specific evidence, not generic design advice.

## Load References Only When Needed

- Framework, component/state ownership, forms, rendering, CSS architecture, responsive behavior:
  [frontend-engineering.md](references/frontend-engineering.md).
- React/Vue/Next/Vite detection and stack-preservation rules:
  [web-stack-routing.md](references/web-stack-routing.md).
- React request waterfalls, server deduplication, bundle cost, or measured render problems:
  [react-performance.md](references/react-performance.md).
- Reusable React components, coordinated parts, or controlled-state API decisions:
  [react-composition.md](references/react-composition.md).
- Next.js routing, RSC, cache, metadata, or hydration APIs that depend on the installed version:
  [nextjs-versioned-guidance.md](references/nextjs-versioned-guidance.md).
- Existing or explicitly requested shadcn/ui integration:
  [shadcn-integration.md](references/shadcn-integration.md).
- Vue reactive ownership, computed/watch decisions, or async watcher cleanup:
  [vue-reactivity.md](references/vue-reactivity.md).
- TypeScript runtime-data boundaries, narrowing, state variants, or generic relationships:
  [typescript-boundaries.md](references/typescript-boundaries.md).
- New visual identity, screenshot implementation, composition, typography, color, imagery, or motion:
  [visual-direction.md](references/visual-direction.md).
- No established visual language and a real need to compare design directions:
  [style-directions.md](references/style-directions.md).
- Existing or requested `DESIGN.md`: [design-md.md](references/design-md.md).
- Product facts versus visual direction, or explicitly requested comparable UI alternatives:
  [design-context-and-variants.md](references/design-context-and-variants.md).
- Major redesign that still feels generic: [taste-critique.md](references/taste-critique.md).
- User explicitly asks to polish/simplify/amplify/quiet/harden/typeset/animate/adapt:
  [refinement-passes.md](references/refinement-passes.md).
- Typography, surfaces, or motion details only when that exact issue matters:
  [typography-recipes.md](references/typography-recipes.md),
  [surface-recipes.md](references/surface-recipes.md), or
  [motion-recipes.md](references/motion-recipes.md).
- Accessibility-sensitive forms/dialogs/menus/focus/dynamic content:
  [accessibility.md](references/accessibility.md).
- Material rendered behavior or visual verification:
  [browser-qa.md](references/browser-qa.md).

Do not read the full reference set by default.

## Frontend Execution Loop

### 1. Recover the local contract

Inspect the smallest useful set of files. Identify the actual framework, router, styling system, state/data
patterns, component library, design tokens, icons/assets, build/test commands, and nearby screens. Reuse them.
Do not introduce a new framework, state library, CSS methodology, icon library, or component system for one task.

For an existing product, match its conventions before applying generic aesthetic preferences. For a new product,
make the first screen the requested usable experience rather than inventing a marketing landing page unless the
user actually asked for one.

For material visual work, check the user-selected reference and the applicable project-root or
surface-scoped `DESIGN.md` before inventing a direction. Follow [design-md.md](references/design-md.md)
when one exists; do not scan unrelated directories or load multiple brand catalogs. If no direction
is established, use [visual-direction.md](references/visual-direction.md) to form a compact internal
design contract. Skip this discovery for focused changes that do not depend on visual direction.

### 2. Build one complete slice

Implement the primary user path before multiplying abstractions or decoration.

- Give components meaningful ownership boundaries; do not split by arbitrary line count.
- Keep remote data, URL state, domain state, and transient presentation state at appropriate owners.
- Use semantic native controls where possible and the repository's existing component/icon system.
- Include the states that matter: loading/pending, empty/no-results, validation/error, disabled, success, and
  permission state when relevant.
- Make visible controls real. Do not ship decorative filters, fake buttons, placeholder interactions, or invented
  product claims.
- Preserve long text, localization expansion, narrow widths, keyboard use, and dense/large data where material.
- Avoid generic generated-UI habits when they conflict with the product: card-inside-card layouts, every section as
  a floating card, excessive pills, arbitrary gradients, or oversized marketing typography inside work surfaces.

### 3. Verify proportionately

Use source/type/lint/test/build checks only when they prove the changed boundary and after inspecting their scripts
for side effects.

Use a real browser for a new page, screenshot-driven implementation, redesign, material layout change, or runtime
interaction where rendering is part of correctness. Follow [browser-qa.md](references/browser-qa.md). Check the
relevant narrow/intermediate/wide widths, the primary workflow, overflow/wrapping, keyboard/focus, console errors,
and failed network states that the change can affect.

Do not install browser tooling or dependencies merely to satisfy this skill. If runtime verification is unavailable,
state what was source-verified and what remains unverified.

### 4. Correct material defects, recheck, then stop

For material UI work, inspect the rendered result and fix issues that change hierarchy, usability,
responsive behavior, accessibility, or obvious visual fidelity before minor polish. After each
material fix, recheck the affected scenario and viewport; one correction pass is not a cap on
fixing known defects. Stop when the requested outcome is proven, without speculative redesign or
repeating unchanged checks. If verification is blocked or fixes stop producing new evidence,
report the remaining mismatch and blocker instead of looping or claiming completion.

## Design-Intelligence Guardrail

The bundled design-intelligence scripts are **not** a default step. Use them only for a new visual direction or redesign when
there is no settled design system or approved visual reference and comparison would materially improve the result:

```text
python <skill-root>/scripts/design-intelligence/search.py "<product audience task tone density>" --design-system -f markdown -p "<project>"
```

Treat results as candidates, never as authority. Do not persist generated design-system artifacts unless requested.

## Hard Stops

Do not hand off material frontend work with:

- clipped, overlapping, or accidental horizontally scrolling primary content;
- inert primary controls or missing recovery for an affected workflow;
- missing keyboard access, visible focus, labels, or semantic structure where relevant;
- a mobile layout that merely squeezes desktop content and destroys task priority;
- implementation-caused console errors;
- a claimed screenshot/design match that was never rendered and inspected;
- a passing build presented as proof of visual quality.

## Completion

Lead with the implemented outcome and only the evidence that matters: affected route/component, checks actually run,
rendered/browser evidence when used, and any remaining runtime limitation. Stop when the requested path works and the
changed boundary has been verified proportionately.
