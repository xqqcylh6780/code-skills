# PostgreSQL Notes

Authoritative source: https://www.postgresql.org/docs/current/

Use current PostgreSQL documentation when behavior depends on the deployed major version.

For connection-pool lifetime, RLS role checks, stable pagination, or concrete plan interpretation,
read [PostgreSQL access and isolation patterns](postgresql-patterns.md). Use only the relevant
section; it does not authorize executing SQL or changing provider configuration.

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

`EXPLAIN ANALYZE` executes the statement. Apply the active database execution policy to the full
statement, including called functions, before considering task-level authorization. Under a
read-only database policy, do not analyze a mutating statement by executing it, even on a test
database or with a planned rollback. Expensive production reads also need an understood target
and permitted resource impact. Prefer existing plans or permitted non-executing inspection when
execution is prohibited, and do not report estimated cost as observed latency.

Use PostgreSQL-specific capabilities such as partial indexes, expression indexes, `INCLUDE`, row locks, advisory locks, or concurrent index creation because the workload needs them, not merely because they exist.
