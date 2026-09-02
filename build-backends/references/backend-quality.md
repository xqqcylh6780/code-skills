# Backend Quality

Use this reference when implementing service logic, handlers, adapters, integrations, errors, or
telemetry. Keep the implementation's ownership boundaries visible in code and tests.

## Layer a vertical path

| Boundary | Owns | Keep out |
| --- | --- | --- |
| Transport/handler | Decode, validate, authenticate, authorize, map response | Domain rules, SQL, vendor protocol details |
| Application service | Use-case orchestration and transaction choice | HTTP framework state, presentation formatting |
| Domain | Invariants, state transitions, deterministic policies | ORM entities, network calls, request objects |
| Repository/adapter | Persistence or vendor protocol, timeout/cancellation plumbing | Caller-specific policy and authorization |
| Worker/consumer | Decode, deduplicate, invoke use case, acknowledge or retry | Hidden infinite retries, best-effort side effects |

Keep one clear composition root for wiring. Pass explicit context (actor, tenant, deadline,
correlation ID) rather than reaching for ambient globals. Return domain results or typed failures;
translate them to a transport shape only at the boundary.

## Validate and authorize at entry

- Parse and normalize once into a trusted internal type; reject ambiguous formats and impossible
  combinations early.
- Authenticate before loading protected resources. Authorize against the requested resource and
  tenant, not merely against a route or caller-supplied identifier.
- Apply size, depth, rate, and time limits where untrusted input can consume resources.
- Treat vendor responses, queue payloads, webhook bodies, and deserialized data as untrusted too.

Do not log raw credentials, tokens, payment data, or full personal records. Redact at the logging
boundary and prefer stable identifiers or hashes with a documented retention policy.

## Model errors deliberately

Use a small internal taxonomy such as validation, unauthenticated, forbidden, not-found,
conflict/already-processed, dependency-unavailable, rate-limited, and unexpected. Attach a safe
client message, machine-readable category, retryability, and original cause where useful. Map each
category once at the outer boundary; avoid catching broad exceptions and silently turning them into
success. Preserve enough context for operators without exposing implementation or secret data.

## Integrate with deadlines

For every network or vendor call, define a deadline, cancellation behavior, bounded retries with
backoff/jitter, and a response/schema check. Retry only operations known to be safe or protected by
an idempotency key. Distinguish timeout, refusal, malformed response, rate limit, and server error
so callers and metrics can react correctly. Handle partial success explicitly; do not hide an
external side effect behind a transaction that cannot include it.

For webhooks and event consumers, authenticate the sender where applicable, tolerate duplicates
and reordering, persist the processing decision before acknowledgement when required, and expose
replay/dead-letter paths to operators.

## Make telemetry useful

Emit structured events at meaningful boundaries: request/job received, validation or authorization
outcome, state transition, dependency call, retry, cache decision, acknowledgement, and terminal
failure. Include correlation and operation identifiers, duration, outcome, and bounded reason
codes. Metrics should distinguish success, expected rejection, retry, and terminal failure; traces
should propagate across queues and integrations. Avoid high-cardinality user input and secrets.

## Match tests to the boundary

| Risk | Strongest economical seam |
| --- | --- |
| Pure rule or state transition | Deterministic unit test |
| Service orchestration and error policy | Service test with real domain and narrow fakes |
| Input/auth/error mapping | Handler or API contract test |
| Query, transaction, constraint, serialization | Repository/integration test with an authorized fixture |
| Vendor timeout/retry/response drift | Adapter test plus sandbox/contract check when available |
| Worker retry, duplicate, ordering, acknowledgement | Worker test with controlled clock and queue fake |
| Logs, metrics, traces | Structured-output assertions at one boundary |

Control clocks, randomness, IDs, and vendor responses. Assert durable outcomes, emitted categories,
and invariants rather than private methods or incidental SQL. If an environment cannot safely run a
needed integration, state the exact unverified risk and provide a user-run command or SQL handoff.
