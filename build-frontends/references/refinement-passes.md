# Targeted Frontend Refinement Passes

Use this reference when the user asks to improve an existing interface with a directional phrase such as “make it bolder,” “quiet this down,” “simplify it,” “polish it,” “harden it,” or “fix the typography.” Route the request to one primary pass so a focused refinement does not silently become a redesign.

## Contents

- [Classify the surface and scope](#classify-the-surface-and-scope)
- [Separate evaluation from editing](#separate-evaluation-from-editing)
- [Choose the primary refinement pass](#choose-the-primary-refinement-pass)
- [Run directional passes](#run-directional-passes)
- [Run capability passes](#run-capability-passes)
- [Use deterministic detectors carefully](#use-deterministic-detectors-carefully)
- [Finish in bounded evidence rounds](#finish-in-bounded-evidence-rounds)

## Classify the surface and scope

Classify what success means on this surface:

- **Persuade:** help a visitor understand, trust, decide, and act. Marketing, pricing, campaigns, and landing pages.
- **Operate:** help a user complete a task accurately and efficiently. Applications, dashboards, settings, tools, and editors.
- **Read:** help a reader find and understand information. Documentation, articles, guides, help, and changelogs.
- **Experience:** let the work or artifact lead. Portfolios, galleries, showcases, and immersive narratives.

Classify the requested change separately:

- **Evaluate:** inspect and report; do not edit.
- **Refine:** improve the incumbent design language within the named scope.
- **Enhance:** add one missing quality such as motion, color, or delight without changing the core concept.
- **Fix:** correct a concrete usability, resilience, responsive, performance, or copy problem.
- **Redesign:** replace the visual world or restructure the experience with explicit authorization.

The surface mode controls priorities; the change type controls authority. For example, an Operate surface that needs to be “bolder” should gain clearer hierarchy and stronger product-specific structure, not cinematic effects that obstruct work.

Resolve the target before editing:

- Named component, route, workflow, or page.
- What must remain unchanged.
- Whether copy, product behavior, information architecture, dependencies, and tokens are in scope.
- Evidence that defines success: an existing system, neighboring surface, reference, or user direction.

Treat “everything else stays the same” literally. If the requested result requires a new font, palette, dependency, primitive, or information architecture, explain the expansion and obtain authorization before proceeding.

## Separate evaluation from editing

Use the right evaluation pass; do not blend their outputs.

### Critique

Critique is rendered-experience judgment. It assesses:

- Purpose, comprehension, hierarchy, and cognitive load.
- Task or narrative flow.
- Emotional and brand fit.
- Product specificity and distinctiveness.
- Composition, typography, color, imagery, motion, and interaction character.
- Persona and context fit.

Critique from screenshots and real interaction. Support each conclusion with visible evidence. Do not present a source-code smell as a visual defect unless it affects the rendered experience.

### Audit

Audit is technical and verifiable. It assesses:

- Accessibility and semantic integrity.
- Responsive behavior, zoom, touch targets, and overflow.
- Performance, loading behavior, layout stability, and asset cost.
- Theming, tokens, and state consistency.
- Implementation integrity, dependencies, and console/runtime failures.

Keep automatic findings separate from verified defects. Inspect every material detector result in context and identify false positives.

### Polish

Polish edits an already-correct concept to reach release quality. Preserve the incumbent visual world, product behavior, factual copy, and everything outside scope. If the concept is fundamentally wrong, report that and recommend redesign instead of concealing one inside a polish pass.

Fix in this order:

1. Blocked tasks, data loss, misleading state, inaccessible paths.
2. Missing loading, empty, error, success, disabled, and permission states.
3. Flow, hierarchy, responsive behavior, and system drift.
4. Visual, copy, asset, and motion inconsistencies.
5. Dead code, accidental churn, and implementation cleanup.

Do not spend the time budget perfecting one corner while the primary path remains incomplete.

### Report severity

For an audit or critique, prioritize findings:

- **P0 Blocking:** prevents task completion, creates data loss, or makes a critical path inaccessible.
- **P1 Major:** materially harms comprehension, trust, accessibility, or success; fix before release.
- **P2 Minor:** creates friction or inconsistency but has a viable workaround.
- **P3 Polish:** visible refinement with low user impact.

For each finding, name the evidence, location, user impact, root cause, and smallest appropriate remedy. Include positive findings worth preserving. Avoid a long P3 list that hides the important work.

## Choose the primary refinement pass

Map natural-language requests to one primary pass:

| User intent | Primary pass | Preserve |
|---|---|---|
| “Make this more confident / bolder” | Amplify | Brand world, behavior, claims, and surrounding scope |
| “Calm this down / too loud” | Quiet | Personality, hierarchy anchors, and task clarity |
| “Simplify / strip it back” | Distill | Necessary capability, decision information, and access |
| “Polish / finish / ship-ready” | Polish | Concept, scope, behavior, and factual content |
| “Handle edge cases / productionize” | Harden | Normal path while expanding resilience |
| “Improve onboarding / empty state” | Onboard | Product truth and user autonomy |
| “Fix the wording / labels” | Clarify | Meaning, facts, voice, and legal constraints |
| “Improve typography” | Typeset | Content hierarchy and brand constraints |
| “Fix spacing / layout” | Layout | Information architecture and behavior unless authorized |
| “Needs more color” | Colorize | Semantic meaning, contrast, and established palette |
| “Add motion” | Animate | Task access, performance, and reduced-motion behavior |
| “Add personality” | Delight | Usability and the established visual world |
| “Make it extraordinary” | Overdrive | Product truth, control, fallbacks, and performance budget |
| “Make it responsive” | Adapt | Task priority and platform conventions |
| “Speed it up” | Optimize | Visible behavior unless a measured tradeoff is approved |

Use secondary passes only when required to complete the primary pass. For example, a layout pass may need a small typesetting correction, but it does not authorize a palette rewrite.

## Run directional passes

### Amplify

Diagnose why the target reads flat before adding effects:

- It does not use the system’s strongest motif or type hierarchy.
- Every element has equal weight.
- The composition lacks a decisive anchor.
- Density and pacing never create a peak.
- Evidence or imagery is too weak to support the intended claim.

Amplify what the system already owns. Make one decisive move, then reduce competition around it. Give the target a distinct rhythm while keeping it unmistakably part of the same product.

Run the skeleton test: remove the copy mentally and inspect the structure. If the composition becomes anonymous, larger text alone is carrying the boldness. Strengthen hierarchy, evidence, and spatial organization instead.

Do not introduce an unrelated color, font, effect, or motif merely because it is louder.

### Quiet

Identify the sources of visual competition:

- Too many saturated colors or contrast extremes.
- Multiple heavy anchors with no priority.
- Excessive layering, borders, shadows, gradients, or textures.
- Motion that competes with reading or task completion.
- Scale jumps and spacing changes that make every section perform.

Keep a small number of strong anchors. Reduce secondary contrast, color variety, decoration, and motion. Preserve the point of view; quiet design is precise, not absent.

On Persuade and Experience surfaces, retain enough drama to support the narrative. On Operate and Read surfaces, let the interface recede further into the task or content.

### Distill

Find the primary user goal and distinguish:

- Essential capability and decision information.
- Useful secondary information that can be disclosed progressively.
- Repetition, decoration, and implementation complexity that can be removed.

Simplify obstacles, not the domain. Prefer clearer grouping, fewer competing actions, smarter defaults, shorter paths, flatter containment, and less repeated explanation. Do not delete functionality, required information, accessibility affordances, or complex-domain detail without authorization.

For every removal, confirm where the displaced capability or information remains accessible. A visually minimal surface that hides necessary decisions is not simpler.

## Run capability passes

### Harden

Exercise the interface against adverse but realistic inputs and states:

- Long, short, missing, malformed, localized, right-to-left, and user-generated text.
- Zero, one, many, maximum, stale, partial, duplicated, and out-of-order data.
- Slow, offline, timeout, retry, permission-denied, conflict, and partial-success states.
- Double submission, interruption, back navigation, refresh, and session expiry.
- Keyboard-only, screen reader, zoom, reduced motion, high contrast, and coarse pointer.
- Slow images, failed images, late fonts, and constrained bandwidth.

Protect data and task continuity first. Make recovery actions specific and preserve user input whenever safe.

### Onboard

Optimize time to first value, not completion of a tutorial:

- Explain the immediate benefit and next meaningful action.
- Prefer contextual guidance and doing over introductory ceremony.
- Make optional tours skippable and resumable.
- Do not block experienced users with forced education.
- Design empty states around what will appear, why it matters, and how to create the first useful item.
- Measure activation through meaningful product outcomes rather than modal completion.

### Clarify

Audit visible language by function:

- Actions describe the result, not a vague verb.
- Navigation labels use the user’s vocabulary.
- Form labels remain visible; helper text answers likely uncertainty.
- Errors state what happened, what remains safe, and what the user can do.
- Empty and loading states set honest expectations.
- Permission messages explain the missing capability without exposing sensitive details.

Preserve factual claims, legal meaning, and established voice. Test localization expansion and avoid embedding meaning only in punctuation, capitalization, or idiom.

### Typeset

Separate two questions:

1. Is the typographic system coherent across roles, weights, measures, and states?
2. Does this particular composition use that system to create the right hierarchy and rhythm?

Fix the system at the token level and composition problems locally. Test real content, numerals, language coverage, font loading, wrap behavior, zoom, and narrow widths.

### Layout

Separate structural flow from local spacing. Establish a spatial thesis covering container model, grid, primary axis, density, and responsive transformation. Fix hierarchy and grouping before micro-adjusting gaps. Verify optical alignment as well as mathematical alignment.

### Colorize

Assign color a job: brand recognition, semantic state, hierarchy, navigation, data distinction, or emotional atmosphere. Add the smallest palette expansion that performs that job. Verify all themes and interaction states; never trade away contrast for color harmony.

### Animate

Write a one-sentence motion thesis and assign each animation a purpose: feedback, continuity, causality, hierarchy, orientation, or narrative. Use the existing runtime when possible. Keep motion interruptible, input-aware, performant, and reduced-motion safe.

### Delight and overdrive

Delight should reward a real moment: success, discovery, progress, personalization, or craft close inspection. Overdrive is appropriate only when spectacle is part of the product promise. Isolate expensive effects, provide fallbacks, preserve control, and prove the ordinary workflow remains excellent without them.

### Adapt and optimize

Adapt by task priority rather than shrinking the desktop. Recompose navigation, controls, tables, media, and information density for each input and viewport class. Optimize from measurements: identify the dominant cost, change the smallest causal area, and measure again. Do not remove visible behavior or quality based only on intuition.

## Use deterministic detectors carefully

If the project already contains a configured design detector or lint rule set, run it as part of the relevant audit or polish pass. Do not install a package, hook, browser extension, or project configuration merely because this reference mentions detectors.

For every finding:

1. Record the rule and exact location.
2. Inspect the rendered and product context.
3. Classify it as verified defect, intentional exception, or false positive.
4. Fix the root cause or document the narrow exception.
5. Re-run only the affected detector scope.

Detectors are good at repeatable signals such as line length, touch targets, skipped headings, hard-coded values, suspicious gradients, and known implementation patterns. They cannot establish product fit, emotional resonance, task success, or overall visual quality. A clean scan is evidence, not a design verdict.

## Finish in bounded evidence rounds

Use a bounded finishing loop by default:

1. Implement the coherent pass across the complete named path.
2. Gather desktop and mobile screenshots, interaction evidence, console state, and relevant detector/test results in one batch.
3. Fix all material findings together, ordered by severity and root cause.
4. Run one confirmation batch across the affected path.

Continue only when the confirmation reveals an unresolved material defect; do not start open-ended micro-polishing. Before handoff, inspect the source diff for accidental scope expansion, duplicate values, dead code, temporary artifacts, and unrelated formatting churn.

