# Execution Plan Reference

Use this reference after project shaping reaches `READY` or `READY WITH DECISIONS` and the user
needs a file-level plan that another agent, session, or developer can execute without rediscovering
the design.

## Contents

- [Planning boundary](#planning-boundary)
- [Plan header](#plan-header)
- [Task sizing](#task-sizing)
- [Task template](#task-template)
- [Cross-task consistency](#cross-task-consistency)
- [Verification and handoff](#verification-and-handoff)
- [Plan failures](#plan-failures)

## Planning boundary

Start from an approved brief, requirements ledger, or explicit user direction. Preserve its scope,
non-goals, exact values, compatibility decisions, and acceptance criteria. If a required decision
remains open for the first task, return to shaping instead of hiding it inside implementation.

Map the files and ownership boundaries before writing tasks:

- Files to create, modify, migrate, generate, or remove.
- Responsibility of each changed file or module.
- Public interfaces and stored state affected.
- Existing tests, fixtures, scripts, and documentation that prove the behavior.
- Dependencies between tasks and any rollout or cleanup ordering.

Do not invent paths or signatures. Inspect the repository and mark genuinely new names as planned
decisions.

## Plan header

Begin with:

```text
Goal:
Source brief or requirements:
Observable completion outcome:
Architecture summary:
Global constraints:
Out of scope:
Compatibility and migration posture:
Verification strategy:
```

Copy exact project-wide values—versions, limits, names, formats, copy, platform requirements—into
global constraints so later tasks do not reinterpret them.

## Task sizing

Make each task an independently reviewable vertical increment. A task should deliver observable
behavior or retire a concrete implementation risk and should own its test or verification cycle.

Keep setup, configuration, generated artifacts, and documentation with the behavior that requires
them. Split tasks when one could be accepted or rejected without its neighbor, not merely because
the work touches another technical layer.

Do not force a universal duration. Prefer the smallest task that preserves meaningful context,
coherent behavior, and a stable verification boundary.

## Task template

Use:

```text
Task N — <observable outcome>

Purpose:
Requirements covered:

Files:
- Create: exact/path
- Modify: exact/path and relevant symbol or region
- Test: exact/path
- Generate or migrate: exact/path, when applicable

Interfaces:
- Consumes: existing or earlier-task signatures, schemas, events, state, or files
- Produces: exact signatures, schemas, events, state, or files later tasks rely on

Implementation:
1. Concrete change with relevant names, behavior, and invariants.
2. Error, denial, recovery, compatibility, and cleanup behavior where material.
3. Integration or wiring required to make the behavior reachable.

Verification:
- Focused command or runtime scenario:
- Expected evidence:
- Expected failure evidence before the change, when applicable:
- Directly affected checks:

Exit condition:
Rollback or recovery:
```

Include code or pseudocode only when it resolves an otherwise ambiguous algorithm, contract, or
wiring decision. Do not fill the plan with code that an implementer can derive safely from existing
project patterns.

## Cross-task consistency

Before handoff, check:

1. Every acceptance criterion maps to at least one task and verification step.
2. Every produced interface is defined before a later task consumes it.
3. Names, types, paths, fields, errors, events, and configuration values agree across tasks.
4. The test described for each task can actually reach its implementation.
5. Migration, mixed-version operation, rollout, rollback, and cleanup are ordered when relevant.
6. No task silently expands a non-goal or contradicts a global constraint.

Fix inconsistencies in the plan before execution. Do not rely on an implementer to reconcile two
conflicting task descriptions.

## Verification and handoff

Specify the narrowest command or scenario that proves each task, followed by affected integration,
build, browser, migration, or security checks proportional to risk. State expected outcomes, not
only command names.

Finish the plan with:

```text
Execution order:
Safe parallelism, if any:
Decisions that block later tasks:
First task to execute:
Final acceptance checklist:
Residual risks:
```

Do not assume another session retains conversational context. Point it to the brief, plan, exact
files, and authoritative project instructions.

## Plan failures

Reject or revise a plan containing:

- `TBD`, `TODO`, “implement later,” or an unresolved decision required by the first task.
- “Add validation,” “handle edge cases,” “write tests,” or “update docs” without naming the
  behavior and evidence.
- Paths, symbols, commands, or dependencies that were guessed rather than inspected.
- File-layer batches that postpone all observable behavior until the end.
- Tests that assert implementation structure instead of the required behavior.
- Repeated code blocks where a contract, invariant, or existing repository pattern is sufficient.
- A success claim based only on task completion rather than acceptance evidence.
