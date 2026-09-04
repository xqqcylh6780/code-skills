---
name: refactor-code
description: >-
  Improve internal code structure while preserving observable behavior. Trigger for extraction,
  decomposition, moving responsibilities, dependency cleanup, reducing duplication, clarifying
  boundaries, or legacy-code restructuring when behavior should not change. Route behavior
  changes to the relevant build/design skill.
---

# Refactor Code

Change structure in small protected steps while keeping the system's observable contract stable. Use evidence to preserve behavior; do not hide new product decisions inside cleanup.

## Activation Threshold

Use this skill when the requested result is primarily internal maintainability or architecture improvement and user-visible/shared behavior is intended to remain unchanged.

If behavior must change, route to the relevant build or interface skill. If existing behavior is wrong for an unknown reason, use `diagnose-bugs` before refactoring. If the user only wants findings, use `review-changes`.

## Route Adjacent Work

- New/changed public contract → `design-interfaces`.
- New product behavior → `build-frontends`, `build-mobile-apps`, or `build-backends`.
- Unknown defect → `diagnose-bugs`.
- Security boundary redesign → `secure-boundaries`.
- Strict regression-first proof when valuable → `test-behavior-first`.
- Read-only assessment → `review-changes`.

## Workflow

### 1. Define the behavior-preservation boundary

State exactly what should remain unchanged and what structural problem should improve.

Inspect callers, public interfaces, tests, configuration, persistence effects, events, logs/metrics relied on operationally, and supported runtimes. Avoid calling a behavior “internal” if another module/service/tool observes it.

Record:

```text
Structural problem:
Observable behavior to preserve:
Public/shared boundaries:
Current test/verification seams:
Known unsupported or legacy behavior:
Target structural outcome:
```

### 2. Establish a trustworthy baseline

Use the narrowest existing tests or reproducible scenarios that cover the behavior. Where legacy code has no practical seam, add characterization tests or another stable observation before large structural movement.

Read [references/refactoring-loop.md](references/refactoring-loop.md).

Do not weaken tests to make a refactor pass. If baseline behavior is already failing, separate that fact and do not silently repair it inside the refactor.

### 3. Identify ownership and seams

Find the smallest structural issue that creates change cost:

- responsibility mixed across boundaries;
- dependency cycle;
- duplicated domain policy;
- transport/storage/framework details leaking inward;
- large file/service with unrelated reasons to change;
- mutable shared state or unclear lifecycle;
- obsolete path proven unreachable or unsupported.

Read [references/module-and-dependency-boundaries.md](references/module-and-dependency-boundaries.md) for module movement and dependency cleanup.

### 4. Apply one reversible transformation

Prefer small moves such as:

```text
rename for meaning
extract function/value
move function/type to its owner
extract a stable collaborator
introduce an adapter at a leaking boundary
replace duplicated policy with one owner
simplify a conditional under tests
remove a proven dead branch
```

Keep each step small enough that a failure has a short suspect list. Do not combine dependency upgrades, formatting sweeps, feature flags, and architectural migration unless they are necessary to the requested refactor.

### 5. Verify after each material step

Run the focused protection seam, then widen only when a changed boundary requires it. Inspect output, not only exit status.

For a large legacy refactor, use [references/legacy-code.md](references/legacy-code.md) and prefer strangler/adapter seams over a rewrite when behavior cannot be safely reproduced all at once.

### 6. Remove temporary compatibility only when safe

If the refactor introduced a temporary adapter, dual path, or compatibility shim, remove it only after all known callers have migrated and the old path is no longer needed for rollback or supported runtime compatibility.

### 7. Stop at the requested structural outcome

Do not keep cleaning unrelated files because the codebase now looks inconsistent. Record adjacent debt separately unless the user expands scope.

## Handoff

Lead with the structural improvement and the behavior-preservation evidence. Mention moved ownership/dependency direction, tests or characterization checks used, temporary compatibility that remains, and any behavior that could not be proved.

## Completion Criteria

A refactor is complete when the requested structural problem is materially improved, observable behavior remains protected by credible evidence, no accidental public contract change was introduced, and the work stops without bundling unrelated modernization or feature changes.
