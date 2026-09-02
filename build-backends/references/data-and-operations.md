# Data and Operations

Use this reference when a change crosses persistence, queues, caches, concurrency, or runtime
operations. Treat durability and recovery as part of the feature, not as an afterthought.

## Persistence and transactions

- Give each aggregate or data owner one write path and state the invariant it protects.
- Keep repository interfaces expressed in domain terms; do not leak ORM sessions, query builders,
  or vendor-specific rows into services.
- Use a transaction for the smallest set of reads and writes that must change atomically. Enforce
  uniqueness and critical constraints in the database as well as in application checks.
- Make isolation, lock scope, timeout, and retry-on-serialization-failure behavior explicit.
  Avoid long transactions around remote calls or user interaction.
- Decide whether reads may be stale, whether writes require read-your-writes, and how replicas or
  eventual-consistency lag is surfaced.

## Schema changes and authorization

Plan additive, backwards-compatible steps when old and new code overlap: introduce nullable or
dual-readable fields, backfill in bounded batches, switch reads/writes, then remove obsolete data
only after the compatibility window. Include indexes, constraints, rollback, and backfill
observability in the plan.

Database administration is outside this skill's execution authority. Never run migrations, seeds,
repairs, destructive statements, or production writes without explicit user authorization. In a
read-only environment, inspect metadata and produce SQL text only, with assumptions for the user to
review and execute. Do not call a dry run proof of a state change.

## Jobs and queues

Assume delivery is at least once unless a stronger guarantee is documented. A durable job should
carry a stable operation ID, attempt count, schema/version, and enough context to retry safely.

- Persist the state transition or outbox record before acknowledging the triggering work.
- Make the handler idempotent; use a deduplication record, unique operation ID, or compare-and-set.
- Bound retries with backoff and jitter. Classify permanent failures, quarantine poison messages,
  and expose dead-letter/replay controls.
- Set visibility/lease time longer than the expected work or renew it safely. Do not acknowledge
  before durable side effects complete.
- Support cancellation and graceful shutdown: stop intake, finish or requeue owned work, and emit
  an unambiguous outcome.

If publishing and database commit must appear together, use an outbox or equivalent durable handoff
and make the relay replay-safe. Never claim exactly-once effects merely because a queue suppresses
one duplicate delivery.

## Caching

For each cache, document key namespace and tenant scope, value version/serialization, TTL, negative
cache policy, invalidation owner, stale-read policy, and behavior after eviction or backend outage.
Cache only data that can tolerate the stated freshness. Prevent stampedes with request coalescing,
leases, jittered expiry, or bounded stale-while-revalidate. Do not use cache presence as an
authorization decision or as the sole record of a durable operation.

## Concurrency and idempotency

Replace check-then-act sequences with an atomic update, compare-and-set, unique constraint, or
properly scoped lock. State what happens when two requests race and how the loser observes the
winner. Keep lock ordering consistent and bound lock waits to avoid deadlocks and queue collapse.

For retriable commands, choose an idempotency key scope and retention window. Store a request
fingerprint so a reused key with different intent is rejected; record in-flight, success, and
failure outcomes; return the original result where safe. Expire records only after the operation
cannot be replayed into a conflicting state.

## Runtime and recovery

Expose health/readiness signals that reflect required dependencies without making liveness depend on
every transient vendor. Bound memory, body size, concurrency, queue depth, and remote fan-out.
Emit alerts for saturation, retry storms, dead letters, stale outbox rows, and failed state
transitions. Document rollback, replay, reconciliation, and operator-visible evidence for partial
failure. Verify these paths with the narrowest authorized test or sandbox available.
