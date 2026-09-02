---
name: test-behavior-first
description: >-
  Implement behavior with a witnessed red-green-refactor loop. Use when the user requests TDD,
  when a reproduced defect needs a regression test, or when a high-value domain rule, public
  contract, state transition, authorization outcome, concurrency rule, or other material invariant
  has a practical automated seam. Do not activate for every ordinary code change, or for open-ended
  diagnosis, static styling, copy, pure configuration, generated artifacts, or low-value tests.
---

# Test Behavior First

Use tests to define and prove observable behavior. Work in small vertical slices: specify one behavior, witness a meaningful failure, implement the minimum change, refactor under green tests, and repeat.

## Activation Threshold

Use this strict workflow only when at least one condition holds:

- The user explicitly requests TDD or test-first development.
- A reproduced defect needs a durable regression guard.
- The change protects a material invariant whose failure would affect users, data, security,
  compatibility, concurrency, or a public contract.
- Repository policy or accepted implementation criteria explicitly require a test-first proof.

Do not invoke it solely because deterministic behavior is being edited or because a test could be
written. Ordinary implementation can still include focused tests without requiring a witnessed
RED or the full red-green-refactor ceremony.

## Core Rules

- Discover the repository's real test contract before choosing commands or locations.
- Derive expected values independently from the implementation.
- Test through a stable public seam, not private call structure.
- Require a meaningful RED; compilation, setup, fixture, or environment failures do not prove missing behavior.
- Keep GREEN minimal without intentionally poor design.
- Refactor only while behavior remains protected.
- Report what ran, what passed, what was skipped, and what remains untested.

## Workflow

### 1. Discover the Test Environment

Inspect the smallest set of repository sources that establishes:

- Language, build system, package manager, and checked-in wrappers.
- Test frameworks, configuration, naming, locations, fixtures, and helpers.
- Focused-test and affected-test commands.
- CI workflows and merge-gating commands.
- Existing tests nearest the behavior being changed.
- Constraints such as containers, services, browser runtimes, database setup, or generated code.

Prefer repository scripts and wrappers over guessed global commands. Do not assume `npm test`, `pytest`, or a full-suite command without evidence.

If the harness is already failing for an unrelated reason, establish that baseline before adding a test. Do not attribute pre-existing failures to the new behavior.

### 2. Write the Behavior Contract

Translate the request into observable examples:

```text
Given <relevant starting state>
When <public action occurs>
Then <observable result or side effect>
And <important invariant remains true>
```

Cover the smallest useful set:

- Primary success path.
- Relevant boundary or invalid input.
- Error and recovery behavior.
- Important state transition or side effect.
- Compatibility behavior for existing consumers when changing a contract.

Do not invent unrelated requirements. Surface ambiguity only when different interpretations would materially change public behavior.

### 3. Choose the Verification Seam

Use the lowest-cost seam that faithfully observes the contract and the highest stable boundary needed to catch the changed risk.

Typical choices:

- Pure unit for deterministic rules and transformations.
- Module/service for a stable capability composed of collaborators.
- API, command, database, or event contract for boundary behavior.
- Component/browser for rendering, accessibility, and interaction.
- End-to-end only when wiring across systems is the risk.

Use more than one seam only when each covers a distinct risk. Read [references/test-quality.md](references/test-quality.md) for seam selection, doubles, determinism, database/API/browser patterns, property tests, snapshots, and failure diagnosis.

### 4. Plan One Vertical Slice

Choose one behavior that can move completely from failing proof to working implementation. Identify:

```text
Behavior:
Public seam:
Independent expected result:
Focused command:
Expected RED reason:
Minimal production surface:
Adjacent regression risk:
```

Avoid writing a large batch of speculative tests before any implementation. A small batch is acceptable only when it defines one coherent contract and gives clearer diagnostics than separate cycles.

### 5. RED — Prove the Test Is Sensitive

Write a focused test that reads as a behavioral specification. Arrange only necessary state, perform one public action, and assert the meaningful result.

Run the narrowest command and inspect the failure. A valid red state must:

- Execute the intended test.
- Reach the intended behavior seam.
- Fail because the requested behavior is absent or wrong.
- Produce a diagnostic message consistent with the assertion.

If it passes immediately:

1. Check whether the behavior already exists.
2. Mutate the setup or assertion to confirm sensitivity.
3. Check whether the wrong code path, skipped test, loose matcher, or stale artifact is involved.

If it fails for setup, syntax, import, fixture, or environment reasons, repair the test harness first; do not call that RED.

For a bug fix, preserve evidence that the regression test fails against the defective state before applying the repair.

### 6. GREEN — Implement the Behavior

Change only the production surface necessary for the current contract. Reuse existing architecture and conventions. Avoid speculative flags, abstractions, compatibility paths, and generalized frameworks not demanded by the behavior.

Run the focused command and inspect actual execution counts, skips, retries, warnings, and output—not only the exit code.

If several implementation attempts fail, stop guessing. Reclassify the problem with `diagnose-bugs`: localize the failure, test hypotheses, and return to GREEN after the causal issue is understood.

### 7. REFACTOR — Improve Without Changing Behavior

With the focused test green:

- Improve names and express invariants.
- Remove meaningful duplication.
- Simplify control flow and data ownership.
- Move validation or side effects to the correct boundary.
- Consolidate test helpers only when they improve readability.

Keep tests green after each meaningful edit. Do not broaden product behavior during refactoring; start another RED cycle for any new behavior.

### 8. Expand by Risk, Not Habit

Add the next example only when it covers a distinct risk: boundary value, authorization outcome, concurrency rule, retry or idempotency, data migration, error mapping, accessibility interaction, or compatibility constraint.

Avoid combinatorial test matrices without a risk model. Use table-driven or property-based tests when many cases share one invariant; keep a few named examples for readability.

### 9. Verify in Widening Rings

After the final slice, run:

1. New and changed focused tests.
2. Tests for directly affected consumers and contracts.
3. Relevant type checks, lint, build, migration, or browser checks.
4. Full suite only when repository policy or blast radius requires it.

For user-interface behavior, verify the real runtime when unit or component tests cannot prove layout, focus, browser APIs, network integration, or accessibility. For integrations, use a contract or sandbox check when mocks could drift.

Do not repeat an unchanged command merely for reassurance. A rerun is useful only after relevant code, state, environment, seed, or timing changed.

## Quality Guardrails

- Assert outputs, errors, public state transitions, durable side effects, rendered results, and contractual events.
- Avoid private methods, internal call order, incidental SQL, framework plumbing, or exact implementation structure.
- Prefer real implementations, then fakes, then stubs; use interaction mocks only at costly, nondeterministic, or unsafe boundaries.
- Keep tests deterministic by controlling time, randomness, locale, identifiers, network, and mutable state.
- Wait for observable conditions instead of fixed sleeps.
- Keep each test independently understandable; repetition is acceptable when abstraction would hide intent.
- Use snapshots only for small, intentionally reviewed structures.
- Never skip, disable, weaken, or rewrite an assertion merely to achieve green.
- Never derive the expected result with the same algorithm used by production code.
- Never claim coverage of behavior that did not execute.

## When Strict Test-First Is Impractical

State the reason and choose the strongest substitute when behavior cannot be exercised before implementation, such as:

- Hardware- or vendor-only paths.
- One-time migrations where rollback is unsafe.
- Visual exploration before a stable expectation exists.
- Legacy code with no test seam and excessive setup cost.

Prefer characterization tests, contract tests, invariant assertions, a deterministic verification script, or a documented manual scenario. Keep the implementation scoped and disclose the residual risk. Do not create a low-value test solely to satisfy process.

## Output Format

Return:

```text
Behavior: examples implemented
RED evidence: why the test failed before implementation
GREEN evidence: focused commands and outcomes
Refactor: structural changes made under protection
Broader verification: affected checks and runtime validation
Exceptions: tests not run, skipped paths, or residual risk
```

## Completion Criteria

Completion requires a witnessed meaningful RED for new behavior or regression, passing focused tests after implementation, directly affected checks, and no silently skipped or disabled coverage.
