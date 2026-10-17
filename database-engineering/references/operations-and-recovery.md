# Operations and Recovery

Use this reference for backup, restore, repair, reconciliation, and database-level operational changes.

## Before a state-changing operation

First check the active workspace policy. If database access is read-only, the steps below describe
the operator's runbook: prepare SQL/procedures and proposed verification, but do not execute a
restore, repair, backfill, permission change, or mutating rehearsal through a script or test.
Writing an authorized migration/runbook file does not authorize applying it.

Confirm:

- exact environment/cluster/database;
- operator authority;
- maintenance/downtime expectations;
- backup or restore point;
- target data scope;
- command semantics on the actual engine/version;
- rollback or forward repair plan;
- post-operation verification.

## Backup is not recovery until restore is proven

A backup policy should define retention, encryption/access, failure detection, restore procedure, and recovery objectives appropriate to the system. Where recovery matters, rehearse restoring into an isolated target and verify application-readable data rather than only archive creation.

## Data repair

Prefer a deterministic repair predicate and bounded affected set. Record before/after counts and keep the repair restartable where possible. For consequential repair, prepare the statement/script first and separate review from execution.

## Destructive changes

For drops, truncation, bulk delete/update, restore-overwrite, privilege changes, or irreversible conversions:

- require explicit authorization;
- verify the exact target immediately before execution;
- avoid wildcard or environment-inferred targets;
- capture enough evidence to explain what changed;
- state when rollback is impossible and use a forward recovery plan instead.
