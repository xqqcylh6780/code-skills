# Specialist Result Contract

Read this reference before delegating or routing an active durable change to an implementation,
design, diagnostic, testing, review, performance, security, database, or deployment skill, and when
reconciling its result.

## Purpose

Specialist skills retain their own methods and output formats. This contract supplies the lifecycle
fields needed to trace their real result back to the active change. It does not authorize additional
work or require a specialist to claim evidence it did not obtain.

## Input Envelope

Provide only the relevant subset:

```text
Change ID:
Lifecycle status:
Authorized task IDs:
Requirement/scenario IDs:
Accepted design constraints:
Affected boundaries:
Expected evidence:
Known unrelated changes or failures:
Scope and permission limits:
```

Do not send the entire artifact tree when one requirement, task, and source boundary are sufficient.
The specialist must still read its own applicable instructions and repository evidence.

## Result Envelope

Normalize the result into:

```text
Change ID:
Task IDs addressed:
Requirement/scenario IDs addressed:
Outcome:
Files or boundaries changed:
Implementation evidence:
Verification performed and observed result:
Artifacts or decisions produced:
Deviation from accepted spec/design:
New scope or dependency discovered:
Residual risk or unverified behavior:
Recommended lifecycle transition:
```

Omit empty fields, but never omit a known deviation, blocked verification, new scope, or residual
risk. “Addressed” does not mean “fully satisfied”; the outcome and evidence determine that.

## Interpretation Rules

- Update `tasks.md` only for tasks actually completed with their required evidence disposition.
- Update `evidence.md` with observed checks, not the specialist's confidence statement.
- If the specialist changes observable behavior or a recorded boundary, run reconciliation from the
  earliest affected artifact.
- If it discovers unrelated defects, record them as out of scope or request expansion; do not absorb
  them silently.
- If it reports pre-existing failures, preserve the distinction between baseline and introduced
  regressions.
- If it performed a planning-only or read-only task, do not represent implementation as changed.
- If its verification subject cannot be identified, do not advance into successful terminal status.

## Skill-Specific Minimums

| Specialist | Lifecycle result that matters |
|---|---|
| `shape-project` | Accepted requirements, exclusions, assumptions, decisions, first slice, readiness |
| `design-interfaces` | Contract semantics, compatibility, consumers, migration/deprecation obligations |
| `build-frontends` / `build-mobile-apps` / `build-backends` | Implemented behavior, changed boundaries, focused runtime/test evidence |
| `database-engineering` | Data ownership, integrity, migration/backfill SQL or plan, locking, rollback, unexecuted external actions |
| `secure-boundaries` | Security invariants, denial behavior, trust-boundary changes, validation evidence |
| `test-behavior-first` | RED cause, GREEN evidence, covered scenarios, skipped/unverified behavior |
| `diagnose-bugs` | Proven causal chain, affected requirement, evidence, whether repair was authorized |
| `review-changes` | Findings mapped to requirement/task/boundary and disposition |
| `performance-engineering` | Workload, baseline, target, measurements, variance, regression result |
| `deploy-and-operate` | Artifact identity, rollout/health evidence, rollback readiness, external actions actually performed |

## Handoff Quality Gate

Before accepting a specialist result, confirm:

- It addresses the assigned scope and identifies the actual subject examined or changed.
- Claims are supported by repository, runtime, test, or external evidence appropriate to the risk.
- Requirement and task mappings are plausible rather than added mechanically.
- Deviations and newly discovered scope are visible.
- No unauthorized external action is implied.
- The recommended lifecycle transition follows the manifest state gates and validator result.

