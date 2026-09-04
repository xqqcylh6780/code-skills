---
name: build-backends
description: >-
  Build or modify server-side product behavior in Python, Java, or the repository's existing
  backend stack. Trigger for handlers, services, jobs, persistence, transactions, queues,
  caching, integrations, retries, idempotency, concurrency, or observability. Use database-
  engineering when the database itself is the primary task.
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
- Use `database-engineering` when schema modeling, indexes, query plans, large migrations, database
  integrity, backup/restore, or database-level operations are themselves the task.
- Use `diagnose-bugs` when the causal chain of an existing failure is unknown or disputed.
- Use `secure-boundaries` for authentication, authorization, sensitive data, untrusted input,
  uploads, webhooks, or privileged effects.
- Use `test-behavior-first` for requested TDD, a reproduced defect's regression guard, a material
  invariant with a practical test seam, or repository-required test-first proof. Ordinary feature
  tests do not by themselves require strict RED/GREEN routing.
- Use `deploy-and-operate` when release artifacts, deployment configuration, rollout, target-runtime
  operations, rollback, or recovery are the requested deliverable or a necessary authorized change.
  A local build or focused runtime check used only to verify a feature stays in this skill.
- Use `refactor-code` when the primary goal is internal structural improvement with unchanged
  observable behavior.
- Use `performance-engineering` when measurement, profiling, throughput, latency, resource, or
  capacity improvement is itself the primary outcome.

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
transactions, application-owned schema changes, queues, caching, concurrency, idempotency, and
recovery.

Detect the repository's existing backend language and stack before loading framework guidance. Preserve
that stack unless the user explicitly requests a migration.

For Python backends, start with [Python backend](references/stacks/python-backend.md), then load only
the relevant narrower references such as [FastAPI](references/stacks/fastapi.md),
[Pydantic](references/stacks/pydantic.md), [SQLAlchemy](references/stacks/sqlalchemy.md), or
[Alembic](references/stacks/alembic.md).

For Java backends, start with [Java backend](references/stacks/java-backend.md), then load only the
technologies actually present: [Spring Boot](references/stacks/spring-boot.md),
[Spring Security](references/stacks/spring-security.md),
[JPA/Hibernate](references/stacks/jpa-hibernate.md), [MyBatis](references/stacks/mybatis.md),
[Flyway/Liquibase](references/stacks/flyway-liquibase.md),
[Maven/Gradle](references/stacks/maven-gradle.md), and
[JUnit/Testcontainers](references/stacks/junit-testcontainers.md).

Cross-stack references such as [relational databases](references/stacks/relational-databases.md),
[Redis](references/stacks/redis.md), and [WebSockets](references/stacks/websocket.md) remain available.
Do not load every reference for a task, and do not migrate Python to Java or Java to Python merely because
another reference is available.

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
