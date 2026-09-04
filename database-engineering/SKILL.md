---
name: database-engineering
description: >-
  Design, change, analyze, migrate, or operate relational databases. Trigger for schema design,
  constraints, indexes, SQL/query plans, migrations/backfills, locking/transactions, data
  integrity, backup/restore, or database-first performance work. Use build-backends for ordinary
  application persistence code.
---

# Database Engineering

Treat the database as a durable system of record with explicit invariants, access paths, migration compatibility, and recovery behavior. Prefer correctness and reversible evolution before clever query or schema optimizations.

## Activation Threshold

Use this skill when the primary deliverable is a database design, query/index analysis, schema or data migration, integrity repair plan, database-level concurrency decision, or operational database procedure.

Do not use it just because `build-backends` needs to add one application-owned column or transaction. Use `diagnose-bugs` first when the reported database symptom has an unknown cause. Use `secure-boundaries` when row/tenant access, sensitive data, credentials, or database privileges are part of the risk.

## Route Adjacent Work

- Public HTTP, event, or shared schema compatibility → `design-interfaces`.
- Application service, repository, or API implementation → `build-backends`.
- Unknown corruption, timeout, deadlock, or slow-path cause → `diagnose-bugs` until localized.
- Authentication, authorization, tenancy, secrets, or sensitive data → `secure-boundaries`.
- Rollout of a migration across deployed versions → `deploy-and-operate`.
- Behavior-preserving application cleanup around the data layer → `refactor-code`.

## Workflow

### 1. Recover the database contract

Inspect the smallest authoritative set of schema definitions, migrations, ORM mappings, query call sites, seed/reference data, deployment notes, and database/version configuration needed to understand the target.

Record:

```text
Database engine/version:
Source of schema truth:
Affected tables/queries:
Data volume and growth:
Read/write paths:
Integrity invariants:
Availability / downtime constraints:
Old/new application overlap:
Backup / recovery expectations:
```

Do not assume production row counts, index selectivity, query frequency, or engine settings from local development data.

### 2. State data invariants before structures

Define what must remain true independently of the ORM:

- identity and key semantics;
- required/optional/null distinctions;
- uniqueness and referential integrity;
- valid state/range constraints;
- ownership and lifecycle;
- ordering or version rules;
- concurrency/atomicity guarantees;
- retention, archival, or deletion behavior where material.

Prefer database constraints for invariants the database can enforce reliably. Keep application checks for user-facing validation and domain rules that cannot be expressed safely at the storage boundary.

Read [references/schema-and-integrity.md](references/schema-and-integrity.md) for modeling and constraint guidance.

### 3. Design access paths from real queries

Inventory the important query shapes before adding indexes. For each one, identify predicates, joins, ordering, cardinality, returned rows, write frequency, and latency sensitivity.

Use the database's real plan tooling when available. Do not infer plan quality only from SQL appearance. Avoid indexes whose only justification is a column being frequently mentioned in code.

Read [references/indexes-and-query-plans.md](references/indexes-and-query-plans.md). For PostgreSQL-specific decisions, read [references/postgresql.md](references/postgresql.md). For MySQL-specific decisions, read [references/mysql.md](references/mysql.md).

### 4. Plan schema and data changes as compatible stages

For deployed systems, separate:

```text
expand schema
↓
deploy compatible readers/writers
↓
backfill in bounded batches
↓
switch reads / enforce invariant
↓
contract old shape after the compatibility window
```

Define lock/scan risk, batch size, restartability, observability, failure recovery, and rollback/roll-forward constraints before touching large or critical tables.

Treat migration generators as candidate producers, not proof of a safe migration. Review generated operations and data effects manually.

Read [references/migrations-and-data-change.md](references/migrations-and-data-change.md).

### 5. Analyze transactions and concurrency at the invariant

Choose transaction boundaries around the state that must move atomically. Make isolation assumptions explicit and prefer database atomicity (constraints, conditional updates, compare-and-set, locks where justified) over check-then-act application races.

Document what concurrent winners/losers observe and how retries behave. Keep remote calls and user interaction out of long transactions.

### 6. Plan operations and recovery

For backup, restore, repair, or destructive maintenance, identify:

- exact target and environment;
- authority to make state changes;
- backup/restore point and verification;
- expected lock/resource impact;
- dry inspection versus real mutation;
- rollback or forward repair path;
- operator-visible evidence after completion.

Read [references/operations-and-recovery.md](references/operations-and-recovery.md).

Never execute production migrations, repairs, restores, destructive statements, or privilege changes without explicit authorization and a verified target.

### 7. Verify the smallest meaningful evidence

Use evidence appropriate to the risk:

1. Schema/static validation for definitions and migration ordering.
2. Focused integration tests for constraints, transaction behavior, and query semantics.
3. Query plans and representative measurements for performance claims.
4. Migration rehearsal on production-like volume when lock duration or backfill cost matters.
5. Restore or recovery rehearsal when the task claims recoverability.

Do not call a generated migration, successful syntax check, or empty development database proof of production safety.

## Handoff

Lead with the data invariant and database outcome. Include the changed schema/access path, compatibility stages, important locks/transactions, verification evidence, rollout dependency, and recovery path. Separate SQL or commands that were only prepared from actions actually executed.

## Completion Criteria

Database work is complete only when the target invariant and access paths are explicit, the migration or operational procedure is compatible and recoverable, the relevant database behavior has been verified with appropriate evidence, and unauthorized state-changing steps are clearly left for review rather than implied complete.
