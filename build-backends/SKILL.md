---
name: build-backends
description: >-
  Implement or modify server-side product behavior across request handlers, services, domain
  logic, persistence adapters, transactions, jobs, queues, caching, integrations, errors,
  observability, concurrency, and idempotency. Use for an actual backend change or focused
  operational hardening, not for generic code review, contract design alone, unexplained defects,
  frontend-only work, or pure database administration.
---

# Build Backends

Build reliable server behavior by tracing one vertical path from an entry boundary through
application and domain logic to persistence or an integration, then to an observable outcome.
Keep authorization, consistency, failure behavior, and operational effects explicit.

## Activation Threshold

Use this skill when the requested outcome requires changing or deliberately hardening executable
server-side behavior. Do not activate it merely because a reviewed diff contains backend files or
because another task mentions an API, database, or service. Route review-only work to
`review-changes`, unknown failures to `diagnose-bugs`, and public contract decisions to
`design-interfaces`.

## Use this skill for

- Services, domain rules, command/query handlers, controllers, resolvers, and webhooks.
- Repositories, persistence adapters, transactions, migrations needed by an application change,
  and cache boundaries.
- Workers, scheduled jobs, queues, retries, dead-letter handling, and graceful shutdown.
- External API or event integrations, typed errors, structured telemetry, concurrency, and
  idempotent processing.
- Focused backend tests and risk-matched operational checks.

Route adjacent work deliberately:

- Use `design-interfaces` before changing a public HTTP, GraphQL, event, job, or module contract.
- Use `diagnose-bugs` when the causal chain of an existing failure is unknown or disputed.
- Use `secure-boundaries` for authentication, authorization, sensitive data, untrusted input,
  uploads, webhooks, or privileged effects.
- Use `test-behavior-first` when the requested behavior has a practical automated test seam.

## Workflow

### 1. Establish the local boundary

Inspect repository instructions, runtime and entrypoints, module conventions, configuration,
existing tests, migrations, queues, deployment notes, and neighboring implementations. Trace the
relevant request, event, or job through handler → application service → domain → repository or
adapter → response/acknowledgement. Record the caller, actor and tenant, data sensitivity,
consistency and transaction needs, latency/resource limits, retry semantics, and rollback path.

Preserve the repository's architecture and supported runtime. Do not add dependencies,
infrastructure, or compatibility layers without a concrete need. Check authorization before
starting services, installing packages, running migrations/seeds, or changing database state.
Without that authority, inspect safely and hand back SQL text only for database changes; do not
execute it or imply that a state-changing check was performed.

### 2. State behavior and invariants

Write a small Given/When/Then set for the primary success, relevant invalid or unauthorized input,
failure/retry behavior, and important side effects. Make explicit:

- Domain invariants and allowed state transitions.
- Input normalization, ownership/tenant checks, and output/error categories.
- Transaction and consistency boundaries, ordering, duplicate handling, and eventual consistency.
- Timeouts, cancellation, retry and backoff rules, idempotency scope, and observability signals.

If a behavior changes an observable contract, pause for `design-interfaces`; do not smuggle a new
contract into private implementation work. If the expected behavior is unclear because of a
failure, diagnose it before editing.

### 3. Implement one vertical slice

- Validate and canonicalize untrusted input at the boundary; authorize before resource access.
  Pass an explicit actor/tenant context into application code.
- Keep application services orchestration-focused and domain rules independent of transport and
  persistence frameworks where practical.
- Hide storage and vendor details behind repositories or adapters. Put transactions around the
  invariant they protect; never rely on a cache for correctness.
- Map domain outcomes to transport responses at one boundary. Use stable error categories,
  preserve causes for internal telemetry, and avoid leaking secrets or sensitive data.
- Give every external call a deadline, cancellation path, bounded retry policy, response
  validation, and a duplicate/partial-failure strategy. Make webhook processing replay-safe.
- Treat jobs as at-least-once unless the infrastructure proves otherwise: persist state before
  acknowledgement, make retries and poison messages visible, and support safe shutdown.
- Define cache key scope, freshness, invalidation, stampede protection, and behavior on misses or
  stale data. Use compare-and-set, unique constraints, locks, or other atomic operations instead
  of check-then-act races.
- Design idempotency around a durable key and request fingerprint; record in-flight, success, and
  failure outcomes with an expiry policy appropriate to the operation.
- Emit structured logs, metrics, and traces with correlation context and bounded cardinality.
  Redact secrets and unnecessary personal data; make saturation, retries, and terminal failures
  actionable.

Read [references/backend-quality.md](references/backend-quality.md) for layering, error and
integration patterns, observability, and verification seams. Read
[references/data-and-operations.md](references/data-and-operations.md) for persistence,
transactions, schema changes, queues, caching, concurrency, idempotency, and recovery.

### 4. Verify in widening rings

Choose the cheapest seam that proves each risk, then widen only when a distinct boundary is
affected:

1. Focused domain/service/handler tests for rules, validation, authorization, error mapping, and
   side effects.
2. Repository, integration, worker, or contract tests for transaction behavior, vendor adapters,
   retries, duplicate delivery, cache invalidation, and durable acknowledgements.
3. Type checks, lint, build, migration checks, or static analysis for changed modules.
4. Authorized sandbox/runtime checks when source and tests cannot prove wiring, timeouts, or
   deployment behavior.

Control time, randomness, identifiers, and external responses. Assert outcomes and invariants,
not private call order. Inspect execution counts, skips, retries, warnings, and logs; do not treat
an exit code alone as evidence. Never start a service, install a dependency, or write to a database
just to obtain verification without user authority. Record unrun checks and residual risk.

## Handoff

Lead with the changed vertical path and observable outcome. Mention only the relevant contract,
authorization, transaction or data ownership, failure and retry behavior, job/cache/concurrency
semantics, telemetry, focused checks, and rollback or recovery notes. Do not emit an empty checklist
for concerns that do not apply.
