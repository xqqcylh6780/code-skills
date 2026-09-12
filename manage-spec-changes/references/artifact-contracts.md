# Artifact Contracts

Read this reference before creating or substantially revising lifecycle artifacts. These contracts
define the information each file must carry; they are not mandatory boilerplate. Omit irrelevant
sections and do not create empty files.

## Contents

1. Change directory and artifact selection
2. `change.json`
3. `proposal.md`
4. Behavioral delta specifications
5. `design.md`
6. `tasks.md`
7. `evidence.md`
8. Writing and identity rules

## 1. Change Directory and Artifact Selection

Default layout when the repository has no established equivalent:

```text
.agents/changes/
├── <active-change-id>/
│   ├── change.json
│   ├── proposal.md
│   ├── specs/
│   │   └── <capability>.md
│   ├── design.md
│   ├── tasks.md
│   └── evidence.md
└── archive/
    └── <completion-date>-<change-id>/
```

Canonical current specifications live at `.agents/specs/`, as described in
[`canonical-and-delta-specs.md`](canonical-and-delta-specs.md). When a repository already has an
equivalent layout, map these artifact roles onto it rather than creating parallel files.

Artifact selection:

| Artifact | Required when | Omit or combine when |
|---|---|---|
| `change.json` | Every durable change | Never omit; it is the machine-readable identity and state index |
| `proposal.md` | Every durable change | Never omit; compact changes may include specs within it |
| `specs/*.md` | Several requirements, capabilities, or consumers need stable behavioral detail | One compact change fits clearly in `proposal.md` |
| `design.md` | Architecture, interfaces, data, security, rollout, or meaningful alternatives affect correctness | The implementation follows an established local pattern with no material design choice |
| `tasks.md` | Work crosses sessions, boundaries, contributors, or ordered verification steps | One safe implementation action can be completed directly |
| `evidence.md` | Verification spans several requirements/checks or must survive handoff/archive | A compact change can record complete evidence in `proposal.md` |

Do not split a specification by source-code directory. Split by stable user or system capability so
requirements remain meaningful if implementation files move.

## 2. `change.json`

The manifest indexes lifecycle state, artifacts, touched boundaries, blockers, gaps, verification
identity, and canonical synchronization. Read
[`manifest-and-validation.md`](manifest-and-validation.md) for the complete schema and validator
contract. Do not duplicate narrative requirements into JSON.

Create the manifest before other durable artifacts so the change has one stable identity. Declare an
artifact only when its file exists; update status only after the corresponding lifecycle gate passes.

## 3. `proposal.md`

The proposal establishes why the change exists and what counts as accepted scope. Include:

```markdown
# <Outcome-oriented title>

Lifecycle metadata: `change.json`

## Problem and Evidence

What is wrong or newly needed, who or what is affected, and what evidence supports the claim.

## Desired Outcome

Observable result, without prematurely fixing the implementation.

## Governing Constraints

Links to adopted repository principles, policies, and instructions that materially constrain this
change, plus any required exception or compliance decision. Omit when ordinary repository
instructions are sufficient and no additional trace is useful.

## Scope

### In scope
- ...

### Out of scope
- ...

## Requirements Summary

| ID | Requirement | Priority | Source | Status |
|---|---|---|---|---|
| R-001 | ... | Must | User / repository / policy | Proposed / accepted / changed |

## Constraints and Quality Attributes

Compatibility, performance, accessibility, privacy, security, operational, dependency, or schedule
constraints that materially shape the solution.

## Success Criteria

Observable, technology-independent outcomes and how they can be assessed. Include only criteria that
add information beyond the detailed acceptance scenarios; do not invent numeric targets.

## Impact

Affected users, modules, contracts, stored data, integrations, operations, and documentation.

## Decisions and Open Questions

| ID | State | Decision or question | Evidence / owner / resolution condition |
|---|---|---|---|
| D-001 | Decided / Open / Rejected | ... | ... |

## Delivery and Verification Strategy

Vertical slices, rollout or rollback posture, and the kinds of evidence required for acceptance.
```

Quality rules:

- Describe the current state using verified evidence. Mark assumptions explicitly.
- Reference governing sources rather than copying them into a second policy document. Record any
  exception as a decision with an owner and acceptance condition.
- A requirement summary points to detailed specifications when they exist; it does not duplicate
  every scenario.
- Keep success criteria outcome-focused and verifiable. A test command, class name, or chosen
  framework is verification strategy, not a product success criterion.
- Record why an option was rejected only when that decision prevents later rediscovery.
- Do not write implementation tasks in the scope section.
- Keep machine state and change identity authoritative in `change.json`; do not maintain a second
  lifecycle-status field in prose.

## 4. Behavioral Delta Specifications

Use one file per stable capability. A specification describes observable behavior and invariants,
not a tour of planned classes or functions. Change specs describe deltas against current canonical
behavior and therefore use `ADDED`, `MODIFIED`, `REMOVED`, or `RENAMED` operation headings.

```markdown
# <Capability>

## MODIFIED

## Context and Boundary

Actors, entry points, owned state, upstream/downstream dependencies, and trust boundary if relevant.

## Requirements

### R-001: <Short requirement name>

The system SHALL <observable behavior or invariant>.

Rationale: <include only when the reason prevents misinterpretation>

#### SC-001-A: <Primary scenario>

- Given <starting state>
- When <event or action>
- Then <observable result>
- And <important invariant or side-effect constraint>

#### SC-001-B: <Failure or boundary scenario>

- Given ...
- When ...
- Then ...

## Cross-cutting Constraints

Only constraints shared by several requirements in this capability.

## Compatibility and Migration Semantics

Old/new behavior, versioning, stored-data transition, coexistence period, and removal condition when
relevant.
```

Requirement rules:

- Give every accepted requirement a stable `R-###` ID unique within the change. Preserve the ID when
  wording changes; create a new ID only for a distinct obligation.
- Use `SHALL` for required behavior, `SHOULD` for an accepted default with documented exceptions, and
  `MAY` for intentionally optional behavior. Do not use these words to disguise uncertainty.
- Give each scenario a stable ID derived from its requirement, such as `SC-003-A`.
- Cover primary success, permission denial, invalid input, failure, boundary, concurrency, recovery,
  and compatibility behavior only where distinct risk exists. Do not multiply equivalent scenarios.
- State absence of side effects when it is important: no row created, no event emitted, no secret
  logged, no partial state committed.
- Put measurable thresholds only where a credible measurement method exists.

When behavior changes after acceptance, mark the old statement as superseded in the decision history
or preserve it in version control; do not reuse its ID for unrelated behavior.

Read [`canonical-and-delta-specs.md`](canonical-and-delta-specs.md) for operation semantics, baseline
selection, synchronization, and conflict resolution.

## 5. `design.md`

Create design only when it carries decisions an implementer cannot safely infer from established
project conventions.

```markdown
# Design

## Verified Current State

Relevant components, flows, ownership, contracts, and limitations with source pointers.

## Decision Drivers

Requirements, risks, constraints, and operational needs that distinguish viable approaches.

## Considered Approaches

### A. <Approach>
- Fit:
- Benefits:
- Costs and risks:
- Reversibility:

### B. <Approach>
...

## Chosen Design

Components and responsibilities, request/event/data flow, state transitions, and invariants.

## Interfaces and Data

Public/shared contracts, validation, ownership, compatibility, persistence, transactions, and
migration semantics.

## Security and Failure Behavior

Trust boundaries, authorization, sensitive data, untrusted input, failure modes, retries,
idempotency, partial failure, and recovery.

## Operations and Delivery

Observability, rollout, rollback, feature flags, coexistence, cleanup, and support considerations.

## Requirement Mapping

| Requirement | Design element | Notes |
|---|---|---|
| R-001 | ... | ... |

## Decisions Deferred

Only decisions that do not block the next slice, with owner and resolution condition.
```

Do not invent several approaches when one follows directly from repository conventions. Conversely,
do not hide a consequential tradeoff merely to keep the file short.

## 6. `tasks.md`

Tasks are an execution contract organized by observable slices and dependencies, not a flat file
checklist.

```markdown
# Execution Plan

## Readiness

Status: READY | READY WITH DECISIONS | BLOCKED
Blocking decisions: none | D-...

## Slice S1: <Observable outcome or retired risk>

Exit condition: <specific behavior/evidence that ends the slice>
Dependencies: <other slice/task/decision IDs or none>
Rollback/recovery: <when material>

- [ ] T-001 <Concrete implementation or investigation action>
  - Covers: R-001, SC-001-A
  - Likely locations: <verified files/modules, only when useful>
  - Verification: <focused check and expected evidence>
  - Notes: <ownership/interface constraints, only when useful>

- [ ] T-002 ...

## Final integration obligations

- [ ] T-... compatibility, migration, documentation, cleanup, release, or manual validation work
```

Task rules:

- Each task must produce an observable change, decision, or evidence. Avoid vague tasks such as
  “handle edge cases” or “finish backend.”
- Map tasks to requirement/scenario IDs. A task may cover several requirements, but every accepted
  requirement must have a path to evidence.
- Order by dependencies, vertical value, uncertainty, and risk. Avoid decomposing every change into
  “models, services, controllers, tests” layers when an end-to-end slice is practical.
- Include expected verification at planning time, but replace expectation with actual results in
  `evidence.md`.
- Mark a task complete only after its behavior or artifact exists and its focused verification has a
  recorded disposition. Code written is not enough.
- Add newly discovered work using a new task ID. Do not rewrite completed history to make the plan
  look prescient.
- During a post-implementation convergence pass, append a `Convergence` slice only when a real
  implementation gap needs work. Leave `tasks.md` unchanged when no gap exists. Reconcile an
  incorrect requirement or design at its authoritative source instead of appending a task that
  forces code to match a known-wrong artifact.

## 7. `evidence.md`

Evidence records what was actually checked and how it supports acceptance.

```markdown
# Verification Evidence

Verification status: PASS | PASS WITH ACCEPTED GAPS | FAIL | BLOCKED
Verified revision/state: <commit, diff identity, or precise working-tree scope when available>
Verified environment: <relevant runtime/configuration; no secrets>

## Traceability

| Requirement / scenario | Tasks | Implementation | Evidence | Result |
|---|---|---|---|---|
| R-001 / SC-001-A | T-001 | `path:line`, symbol, migration, config | test/check/manual observation | Pass / Fail / Blocked |

## Checks Run

### V-001: <Check name>

- Command or method:
- Scope and environment:
- Expected:
- Observed:
- Result:
- Limitations:

## Manual or External Verification

Steps, observer, environment, observed result, and retained artifact where applicable.

## Contradiction Review

Differences found between proposal, specs, design, tasks, code, tests, and actual behavior; include
their resolution or accepted disposition.

## Residual Risks and Gaps

| ID | Risk or gap | Impact | Disposition | Owner / follow-up |
|---|---|---|---|---|

## Final Scope

Delivered, deferred, removed, and user-accepted gaps.
```

Record concise outputs or durable artifact paths, not enormous logs. A command exit code alone is
insufficient when it does not show what behavior was exercised.

## 8. Writing and Identity Rules

- Use Markdown that remains understandable without special tooling.
- Use repository-relative paths in durable artifacts unless an absolute path is itself material.
- Prefer stable IDs to paragraph references. Never renumber accepted IDs solely for neatness.
- Timestamp decisions only when timing matters; version control already provides ordinary history.
- Separate fact, user decision, assumption, proposal, and observed evidence.
- Link to source evidence and authoritative repository documents instead of copying large passages.
- Never store credentials, secrets, sensitive production data, full terminal transcripts, or
  speculative findings presented as facts.
- Keep artifacts sufficient for an unfamiliar implementer to continue without replaying the entire
  conversation, but remove repetition that creates multiple competing statements of the same rule.
- Run the bundled validator at lifecycle gates, but do not treat structural validity as behavioral
  proof.
