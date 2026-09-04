# Routing Examples

## Should trigger

- “Design the tables, foreign keys, unique constraints, and indexes for this marketplace.”
- “This PostgreSQL query is slow; inspect the plan and recommend indexes.”
- “Plan a zero-downtime migration for a 200M-row table.”
- “Check whether this schema can represent invalid order states.”
- “Write and verify a backup/restore rehearsal plan for this database.”

## Should not trigger

- “Add a normal users endpoint that saves a record using the project's existing repository.” → `build-backends`.
- “The API sometimes returns 500 after a database call and we do not know why.” → `diagnose-bugs` first.
- “Design the response shape of the public orders API.” → `design-interfaces`.
- “Review this PR containing a migration.” → `review-changes` unless implementation changes are requested.
- “Prevent one tenant from reading another tenant's rows.” → `secure-boundaries` owns the trust-boundary analysis.

## Conflict cases

- “Add a required column and deploy it with no downtime.” → `database-engineering` designs the compatible change; `deploy-and-operate` owns rollout sequencing; `build-backends` owns application compatibility code.
- “Fix a duplicate-payment race caused by two concurrent DB writes.” → begin with `diagnose-bugs` if causality is unproven, then combine `build-backends`, `database-engineering`, and `secure-boundaries` as the proven boundary requires.
- “Move a repository from one ORM abstraction to another without changing behavior.” → `refactor-code`; use database references only for storage invariants affected by the refactor.
