# Migrations and Data Change

Treat schema migration, application rollout, and data backfill as one compatibility problem.

## Expand / migrate / contract

Prefer staged changes when old and new application versions may overlap:

1. Add the new representation without breaking old readers/writers.
2. Deploy code that can tolerate both shapes.
3. Backfill existing data in bounded, restartable batches.
4. Observe completeness and errors.
5. Switch authoritative reads/writes.
6. Add stricter constraints only after data satisfies them.
7. Remove old fields or paths after the rollback/compatibility window closes.

## Review generated migrations

Autogeneration can identify candidate schema differences but cannot prove intent, lock duration, data conversion safety, renamed-object semantics, or production cost. Inspect every generated migration.

For large tables, consider:

- whether an operation rewrites or scans the table;
- lock type and expected duration;
- index creation strategy supported by the engine;
- batching and throttling;
- replication/redo/binlog pressure;
- transaction size;
- resumability after interruption.

## Data backfills

A durable backfill should have:

```text
selection cursor/key:
batch bound:
idempotent update rule:
progress signal:
retry behavior:
invalid-row handling:
completion query:
```

Do not mix a long backfill with an application deployment command unless the repository deliberately owns that orchestration.
