---
name: manage-spec-changes
description: >-
  Coordinate consequential software changes when the user needs a spec-driven, traceable workflow
  with proposals, decisions, executable tasks, reconciliation, and evidence across sessions or
  owners. Do not trigger for ordinary feature work, single-file fixes, refactors, reviews, or tasks
  that only need a brief plan.
---

# Manage Spec Changes

Provide a lightweight but rigorous lifecycle around consequential changes. Keep the specification,
implementation plan, current work, and verification evidence mutually consistent without replacing
the specialist skills that perform design, implementation, testing, review, or deployment.

## Core Contract

- Scale the ceremony to the change. Durability and traceability are the purpose; document count is
  not.
- Treat artifacts as an evolving contract, not a one-time plan and not proof that work is complete.
- Preserve stable requirement IDs from proposal through verification. Trace every material behavior
  to implementation and evidence.
- Keep two distinct truths: canonical specifications describe currently effective behavior, while a
  change specification describes the accepted delta. Successful archival reconciles the delta into
  canonical truth.
- Reconcile artifacts when implementation reveals a changed assumption, boundary, or behavior.
  Never silently let the code become the only source of truth.
- Keep current execution state separate from durable change intent. Repository memory helps resume
  work; it does not replace the specification or evidence.
- Respect the user's authorization and repository instructions. This lifecycle never grants
  permission to implement, deploy, migrate data, write to a database, archive, or perform another
  external mutation that the request did not authorize.
- Use existing project conventions when they already provide an equivalent workflow. Extend the
  established change location instead of creating a competing artifact tree.
- Treat adopted repository principles and governance as inputs to every change. Reference their
  authoritative locations; do not create a parallel “constitution” merely to restate them.

## Activation Gate

Use the full lifecycle when at least one material reason makes persistent coordination valuable:

- Work will plausibly cross context windows, sessions, contributors, or handoffs.
- Several modules, applications, repositories, or independently owned boundaries must change in a
  coordinated way.
- The change affects an API, schema, event, configuration contract, authorization rule, stored data,
  migration, compatibility promise, release sequence, or rollback path.
- Requirements contain alternatives, unresolved decisions, staged delivery, or meaningful scope
  pressure.
- Verification must combine several kinds of evidence or prove important negative behavior.
- The user explicitly asks for a proposal/spec/design/task workflow, OpenSpec-like process, or
  durable audit trail.

Do not activate merely because more than one file will change, tests are needed, or the task sounds
important. For a small and well-specified change, state the observable outcome and verification path
in working context and continue with the relevant specialist skill.

For borderline cases, score the decision as a consistency aid:

| Signal | Weight |
|---|---:|
| Cross-session work or explicit handoff | +2 |
| Public/shared contract or configuration semantics | +2 |
| Stored-data migration or compatibility window | +3 |
| Security or tenancy boundary | +3 |
| Multiple applications, repositories, or independent owners | +2 |
| Staged rollout or rollback obligation | +2 |
| One localized, explicit behavior with focused verification | -3 |
| Private behavior-preserving refactor | -2 |

Use `1` or less as a strong signal to work directly, `2–4` for a compact change, and `5` or more for
the full lifecycle. Explain the deciding signals when the choice is not obvious. This score informs
judgment; explicit user intent and concrete risk still govern.

When the need is borderline, use a **compact change**: one `proposal.md` containing intent, scope,
requirements, and acceptance scenarios; add `tasks.md` or `evidence.md` only if they will actually be
used. Do not create empty placeholders.

## Locate the Change Store

Before creating anything:

1. Confirm the target repository or the common workspace only when the task genuinely spans several
   repositories.
2. Read applicable repository instructions and inspect focused evidence for an existing change,
   specification, RFC, ADR, plan, or OpenSpec convention.
3. Resume the matching active change when identity and scope agree. Do not create a second change
   because the title differs slightly.
4. Prefer, in order:
   - the repository's established specification/change location;
   - an existing OpenSpec or equivalent location already adopted by that repository;
   - `.agents/changes/<change-id>/` at the confirmed repository root.

When using the default layout, current behavior belongs in `.agents/specs/` and each active change
contains its delta under `.agents/changes/<change-id>/specs/`. Read
[references/canonical-and-delta-specs.md](references/canonical-and-delta-specs.md) before creating,
syncing, or removing canonical requirements.

Use a short, stable, lowercase hyphenated change ID describing the outcome, such as
`enforce-export-permissions`. Do not encode an implementation choice that may change. For unrelated
repositories, keep full artifacts in each repository; use workspace-level state only for the shared
goal and integration decisions.

## Artifact Graph

Create artifacts on demand according to these dependencies:

```text
canonical specs ──baseline──> change.json + proposal.md
                                  |
                                  +--> delta specs/*.md
    |
    +---------------------------> design.md          when architecture or tradeoffs are material
                                   |
                     delta specs --+--> tasks.md     when execution needs durable decomposition
                                             |
                                             +--> implementation and reconciliation
                                                            |
                         proposal + delta specs + code ------+--> evidence.md
                                                                      |
                                          canonical sync + validator --+--> archive
```

The graph describes information dependencies, not mandatory phases. Draft independent artifacts in
parallel when useful, but do not claim an artifact is ready while required upstream decisions remain
unresolved. Read [references/artifact-contracts.md](references/artifact-contracts.md) before creating
or substantially revising change artifacts.

Every durable change also has a machine-readable `change.json`. Read
[references/manifest-and-validation.md](references/manifest-and-validation.md) before creating or
changing the manifest, entering `READY` or later, or running the validator.

Read
[references/principles-clarification-and-convergence.md](references/principles-clarification-and-convergence.md)
when a new or revised change needs a governance check, material ambiguity must be resolved before
planning, or implementation needs a convergence pass against its accepted artifacts.

## Operating Modes

Choose the mode that matches the current request and change state. Do not force a new change through
all earlier modes again.

### Start

Establish change identity, inspect nearby behavior, decide whether full or compact artifacts are
justified, and write the smallest proposal that makes intent and boundaries reviewable. When the
problem or scope is materially ambiguous, use `shape-project` to resolve it; this skill persists the
result and manages its later evolution.

Identify the repository's governing sources before accepting requirements. Audit ambiguity across
scope, actors, ownership, failure behavior, compatibility, and acceptance. Infer safe defaults and
record assumptions; ask only about decisions whose plausible answers materially change the result.
Resolve blocking ambiguity in the authoritative spec before `READY` rather than leaving placeholder
questions for implementers.

Search active manifests for overlapping `touches` before declaring the change ready. An overlap is a
coordination signal: resolve ownership, ordering, or compatible design; do not assume separate
directories make the work independent.

### Continue

Read repository task state first when present, then the change proposal and only the downstream
artifacts needed for the next incomplete action. Check volatile facts in the repository rather than
trusting stale state. Report conflicts before overwriting another contributor's decision or work.

### Fast-forward

When the user asks to prepare everything needed for implementation and the decisions are already
clear, produce proposal, specifications, conditional design, and executable tasks in dependency
order without pausing between documents. Stop for a user decision only when it would materially
change behavior, compatibility, data ownership, security, cost, or irreversible work.

### Apply

Implement only when the user requested implementation. Select the relevant specialist skills for
the affected boundaries. Work from executable tasks, but prioritize the specification and latest
accepted decisions over stale task wording. Record actual verification rather than checking off a
task based on code presence.

### Reconcile

Update upstream artifacts as soon as implementation evidence invalidates them. Classify the change:

- **Clarification:** wording becomes more precise without changing observable behavior; update the
  affected artifact and continue.
- **Design adjustment:** implementation structure changes while requirements remain stable; update
  `design.md` and dependent tasks.
- **Requirement change:** behavior, failure semantics, compatibility, scope, or quality threshold
  changes; update specs, impact analysis, design/tasks, and request a user decision when the change
  exceeds accepted intent.
- **Scope discovery:** necessary adjacent work appears; keep it out, stage it, or seek scope approval.
  Do not silently absorb it.

Express accepted behavior changes as `ADDED`, `MODIFIED`, `REMOVED`, or `RENAMED` deltas against the
canonical specification. Do not edit canonical truth early merely to make an active proposal appear
already accepted.

Read [references/lifecycle-and-reconciliation.md](references/lifecycle-and-reconciliation.md) for
state transitions, readiness rules, stale-artifact handling, and resumption behavior.

### Verify

Verify three independent properties:

1. **Completeness:** every in-scope requirement, scenario, task, migration, and cleanup obligation has
   a disposition.
2. **Correctness:** implementation and tests demonstrate the specified positive, negative, boundary,
   compatibility, and operational behavior.
3. **Coherence:** proposal, specs, design, tasks, code, tests, and user-visible behavior agree.

Use repository-appropriate checks only after inspecting their entry points and side effects. A
passing test suite is supporting evidence, not automatic proof of coverage or product correctness.
Read [references/verification-and-archive.md](references/verification-and-archive.md) before final
verification or archival.

After implementation has run against the current task set, perform a convergence pass: compare the
present code and behavior with governing constraints, accepted requirements, design decisions, and
tasks. If genuine implementation gaps remain, append traceable remediation tasks and return to
`ACTIVE`; if an artifact is wrong, reconcile its authoritative source first. A clean pass does not
rewrite tasks and is necessary but not sufficient evidence for completion.

For the default artifact format, run `scripts/validate_change.py <change-directory>` at readiness,
before claiming successful verification, and after canonical synchronization. Use
`--strict-conflicts` when unresolved overlap must block progression and `--json` when another tool
needs structured results. Treat validator success as a necessary structural gate, not a substitute
for behavioral verification.

### Archive

Archive only after the completion gate passes or the user explicitly accepts documented residual
gaps. For successful changes, apply and verify the accepted delta against canonical specifications
before moving the change directory. Preserve the accepted artifact set and final evidence as a
durable decision record. Never use archive to hide abandoned, superseded, or incomplete work; label
those outcomes explicitly.

## Relationship to Repository Memory

Keep these roles distinct:

| Location | Purpose | Must not become |
|---|---|---|
| `.agents/PROJECT_CONTEXT.md` | Verified stable project facts and conventions | A history of individual changes |
| `.agents/TASK_STATE.md` | Current objective, completed work, blockers, and exact next action | The authoritative requirements document |
| `.agents/changes/<id>/` | Durable intent, behavior, decisions, execution contract, and evidence | A terminal transcript or scratchpad |

When multi-step work remains unfinished, update task state according to repository instructions and
point it to the active change ID. Summarize outcomes and the exact next action; do not duplicate full
specifications or logs into task state.

## Specialist Skill Routing

This skill owns lifecycle integrity, not every technical decision. Route work to specialist skills
when their trigger is met:

- `shape-project` for unresolved product framing, scope, and acceptance criteria.
- `design-interfaces` for public/shared contracts and compatibility semantics.
- `build-frontends`, `build-mobile-apps`, or `build-backends` for product implementation.
- `database-engineering` for database-first schema, integrity, query, or migration work.
- `secure-boundaries` for trust boundaries and sensitive effects.
- `test-behavior-first` when TDD is requested or a material invariant needs a witnessed regression
  guard.
- `diagnose-bugs` when the causal chain is still unknown.
- `review-changes`, `performance-engineering`, or `deploy-and-operate` when their distinct work is
  requested or required by the accepted change.

Load only the skills that apply. Keep lifecycle artifacts updated with their results instead of
copying those skills' instructions into this one.

When a durable change is active, give each specialist the change ID and relevant requirement,
scenario, and task IDs. Normalize its result using
[references/specialist-result-contract.md](references/specialist-result-contract.md) so that
implementation, verification, deviations, and newly discovered scope can be reconciled without
depending on a particular skill's prose format.

## Status Communication

Lead user updates with the current outcome or blocker. For ongoing lifecycle work, make these facts
recoverable without dumping the entire artifact set:

```text
Change:
Lifecycle status:
What became true:
Artifacts changed:
Evidence obtained:
Decision or blocker:
Exact next action:
```

Omit empty fields. Distinguish proposed behavior, accepted behavior, implemented behavior, and
verified behavior; never use “done” for all four.

## Completion Criteria

The lifecycle is complete only when:

- The delivered scope and explicit exclusions are unambiguous.
- Every accepted requirement and scenario has a disposition and traceable evidence.
- Material design, compatibility, data, security, migration, rollout, rollback, and cleanup decisions
  are reflected where relevant.
- No known contradiction remains between durable artifacts and actual behavior.
- Verification commands and meaningful observed results are recorded, including blocked or manual
  checks.
- Residual risks, deferred work, and user-accepted gaps are explicit.
- The change manifest passes structural validation, including active-change overlap disposition.
- Each successful delta is reflected in canonical specifications and recorded in `canonicalSync`.
- Current task state no longer points to an unfinished action for this change.
- The final status is one of `COMPLETED`, `COMPLETED WITH ACCEPTED GAPS`, `SUPERSEDED`, or
  `ABANDONED`, and archival preserves that outcome without implying more evidence than exists.
