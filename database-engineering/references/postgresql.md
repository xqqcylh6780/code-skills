# PostgreSQL Notes

Authoritative source: https://www.postgresql.org/docs/current/

Use current PostgreSQL documentation when behavior depends on the deployed major version.

## Useful areas to verify

- indexes and index types;
- `EXPLAIN` / `EXPLAIN ANALYZE`;
- transaction isolation and explicit locking;
- constraints and foreign keys;
- concurrent index operations;
- vacuum/analyze and planner statistics;
- backup/restore tooling;
- partitioning and replication when actually used.

## Guardrails

`EXPLAIN ANALYZE` executes the statement. Do not use it on consequential writes or expensive production queries without explicit authorization and an understood target.

Use PostgreSQL-specific capabilities such as partial indexes, expression indexes, `INCLUDE`, row locks, advisory locks, or concurrent index creation because the workload needs them, not merely because they exist.
