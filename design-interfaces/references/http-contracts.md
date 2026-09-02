# HTTP and GraphQL Contract Reference

Read the relevant sections when the boundary is HTTP-facing.

## Table of contents

- Resource and operation design
- Status and error semantics
- Input and output schemas
- Collections, filtering, and pagination
- Partial updates and concurrency
- Idempotency, retries, and long-running work
- Caching and conditional requests
- Authentication, authorization, and rate limits
- Webhooks and callbacks
- GraphQL-specific considerations
- Compatibility review

## Resource and operation design

Prefer stable resource nouns and standard HTTP methods when resource semantics fit:

```text
GET    /tasks
POST   /tasks
GET    /tasks/{id}
PATCH  /tasks/{id}
DELETE /tasks/{id}
```

Use action endpoints when an operation is a real domain command rather than forced CRUD, such as `/orders/{id}:cancel`. Keep naming, casing, identifiers, timestamps, and envelopes consistent across sibling endpoints.

Define content type, encoding, maximum body size, timeout, cancellation, and request correlation behavior. Avoid encoding sensitive information in URLs when it will leak through logs or history.

## Status and error semantics

Use status codes consistently with the documented contract. Distinguish:

- `400` malformed or structurally invalid request.
- `401` missing or invalid authentication.
- `403` authenticated but not authorized.
- `404` missing resource or intentionally concealed existence.
- `409` state conflict, duplicate, or version mismatch.
- `422` well-formed but semantically invalid input when the API uses this distinction.
- `429` rate limited, with retry guidance when available.
- `5xx` server or dependency failure without internal leakage.

Use one error envelope, for example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request is invalid",
    "details": [{"field": "title", "reason": "required"}],
    "requestId": "req_123"
  }
}
```

Keep `code` stable for machines. Treat `message` as human-facing unless exact text is explicitly contractual. Document retryability and remediation for operational errors.

## Input and output schemas

- Reject invalid types, ranges, lengths, encodings, and unsupported enum values.
- Decide whether unknown fields are rejected or ignored and apply the rule consistently.
- Separate create, update, and response types.
- Use a standard timestamp and timezone representation.
- Define numeric precision, identifier format, nullability, and omitted-field behavior.
- Return only fields the consumer is permitted and needs to see.
- Validate third-party responses before mapping them into public output.

Do not reuse persistence models as public schemas merely for convenience.

## Collections, filtering, and pagination

Define:

- Default and maximum page size.
- Cursor or offset semantics.
- Stable sort order and deterministic tie-breaker.
- Allowed filter and sort fields.
- Search matching, case, locale, and tokenization behavior.
- Whether totals are exact, approximate, optional, or unavailable.
- Behavior when data changes between pages.

Prefer cursors for frequently changing or large collections. Bind cursor meaning to the filter and stable sort order. Treat cursors as opaque and validate them.

Avoid accepting arbitrary field names or expressions that leak storage structure or create injection and performance risks.

## Partial updates and concurrency

Define whether omitted, null, and empty values differ. For partial updates:

- Apply validation to the resulting state, not only individual fields.
- Reject immutable or unknown fields explicitly.
- Define whether operations are atomic.
- Prevent lost updates when material through entity versions, ETags, or conditional requests.
- Return the authoritative post-update representation or clearly document otherwise.

Use `PUT` only when full replacement semantics are intended. Use `PATCH` for documented partial changes; specify merge behavior instead of assuming it.

## Idempotency, retries, and long-running work

For retried writes, specify:

- Which operations are naturally idempotent.
- Whether an idempotency key is supported or required.
- Key scope, retention, and authentication binding.
- Whether the original response is replayed.
- What happens when the same key carries different input.
- How in-progress, failed, and expired keys behave.

Clients should retry only documented transient failures with bounded backoff and jitter. Servers should not encourage retries for validation or authorization errors.

For long-running work, consider `202 Accepted` with an operation resource. Define polling, cancellation, expiry, terminal states, and result retrieval.

## Caching and conditional requests

Define whether responses are public, private, or non-cacheable. Use cache keys and `Vary` correctly when content changes by authentication, locale, encoding, or headers.

Use ETags or last-modified validators when they improve read efficiency or concurrency safety. Specify stale behavior and invalidation expectations. Never cache one user's sensitive response for another consumer.

## Authentication, authorization, and rate limits

Document the authentication mechanism and required scopes or roles, but enforce authorization at the protected resource or action.

Define:

- Ownership and tenant isolation.
- Whether resource existence is concealed.
- Scope of credentials and delegation.
- Rate-limit dimension, quota window, response headers, and retry behavior.
- Audit expectations for privileged changes.

Avoid trusting tenant, owner, price, privilege, or role fields supplied by the caller when the server can derive them.

## Webhooks and callbacks

- Authenticate the sender and verify signatures against the raw payload when required.
- Define event identifier, type, version, creation time, and subject.
- Reject stale or replayed events when supported.
- Make handlers idempotent and safe for duplicate or out-of-order delivery.
- Acknowledge promptly; move slow work behind durable processing.
- Define retry schedule, timeout, delivery guarantees, and disablement behavior.
- Validate every field before using it in domain logic.

Never assume webhook delivery is exactly once.

## GraphQL-specific considerations

- Model domain concepts, not direct database access.
- Define nullability deliberately; non-null propagation can erase a large response subtree.
- Bound query depth, complexity, list sizes, and batching work.
- Avoid field-level authorization gaps and cross-tenant loaders.
- Use stable error extensions for machine-readable classification.
- Plan schema evolution through additive fields and deprecation metadata.
- Avoid breaking enum additions for clients that exhaustively switch without fallback; understand consumer language behavior.
- Control N+1 behavior without leaking loader implementation into the public schema.

## Compatibility review

Before changing an endpoint, check:

- Removed, renamed, or repurposed fields.
- Narrower accepted inputs or newly rejected unknown fields.
- New required fields or enum values.
- Changed defaults, ordering, pagination, status codes, error codes, or retry behavior.
- Changed nullability, encoding, time representation, or numeric precision.
- New side effects, authorization, rate limits, latency, or consistency behavior.
- Generated clients and cross-language serialization.

Prefer additive evolution, usage telemetry, a documented migration window, and removal criteria when consumers cannot move atomically.
