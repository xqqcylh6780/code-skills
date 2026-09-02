# Interface Patterns Beyond HTTP

Use the sections matching the boundary being designed.

## Table of contents

- Modules and libraries
- Components and UI props
- Commands and CLIs
- Configuration and environment
- Schemas and persistence boundaries
- Events, queues, and jobs
- State machines
- Third-party adapters
- Compatibility and deprecation

## Modules and libraries

Define ownership, lifecycle, mutation, concurrency, and cleanup:

- Who constructs and disposes the resource?
- Is the interface synchronous, asynchronous, cancellable, or streaming?
- Are returned values owned copies, immutable views, or mutable shared state?
- Is the module thread-safe or reentrant?
- Which errors are recoverable and stable for callers?
- Which implementation details must remain hidden?

Prefer cohesive capabilities over getters and setters that expose internal representation. Avoid boolean parameter lists; use named options or distinct operations. Keep domain identifiers and variants explicit when accidental interchange is costly.

For libraries, minimize mandatory dependencies and global state. Define supported runtime versions, initialization, shutdown, and resource limits. Preserve source, binary, and behavioral compatibility appropriate to the ecosystem.

## Components and UI props

Treat props and events as a public interface:

- Separate controlled and uncontrolled behavior clearly.
- Define initial/default value versus current value.
- Keep event payloads domain-focused rather than exposing DOM/framework internals unnecessarily.
- Distinguish loading, empty, error, disabled, read-only, and permission-denied states.
- Preserve accessibility names, focus behavior, keyboard operation, and semantic roles.
- Avoid mutually inconsistent booleans; use variants or a state model.
- Define composition and styling extension points without exposing fragile internal selectors.

Do not add a prop for every incidental implementation choice. Prefer a smaller semantic API that supports the intended composition patterns.

## Commands and CLIs

Define:

- Command and subcommand grammar.
- Positional arguments versus named options.
- Defaults, environment/config precedence, and interactive behavior.
- Exit codes and classification of errors.
- stdout for requested results and stderr for diagnostics.
- Stable machine-readable output separate from human output.
- Non-interactive mode, confirmation rules, cancellation, and signal behavior.
- Idempotency and dry-run semantics for mutations.

Avoid prompting when input is non-interactive unless explicitly requested. Never make a destructive default. Quote examples for target shells and do not expose secrets in command history or process arguments.

## Configuration and environment

Treat configuration as a versioned input schema:

- Type, allowed values, defaults, units, and precedence.
- Required versus optional settings.
- Secret versus non-secret values.
- Startup validation and failure behavior.
- Dynamic reload semantics and consistency.
- Deprecation and migration of keys.

Reject ambiguous or dangerous values early. Normalize once into a typed internal configuration. Avoid scattered reads of environment variables and hidden fallback chains.

## Schemas and persistence boundaries

Separate public contract from storage representation. Define:

- Identity, uniqueness, ownership, nullability, precision, and time semantics.
- Referential integrity and deletion behavior.
- Concurrency and transaction rules.
- Forward and backward application compatibility during migrations.
- Data retention, archival, and deletion.

Use expand-migrate-contract for incompatible storage changes:

1. Add compatible storage and dual-read/write behavior only when needed.
2. Backfill with checkpoints, idempotency, and verification.
3. Switch reads after adoption is proven.
4. Remove old fields only after rollback and compatibility windows close.

Do not equate a database constraint with the full domain contract; validate and map errors at the owning boundary.

## Events, queues, and jobs

Define an event envelope with stable identifiers, event type, schema version, subject, occurrence time, producer, and correlation/causation IDs as needed.

Specify:

- At-most-once, at-least-once, or best-effort delivery.
- Ordering scope and partition key.
- Acknowledgement and visibility timeout.
- Retry schedule and terminal/dead-letter behavior.
- Idempotency and deduplication window.
- Schema compatibility and unknown-event behavior.
- Sensitive-data and retention rules.

Events should describe facts that occurred. Commands request actions and may be rejected. Do not blur the two when consumers need different semantics.

For jobs, define submission acknowledgement, progress, cancellation, timeout, terminal states, result retention, and repeated-submission behavior.

## State machines

Use an explicit state model when valid operations depend on lifecycle:

```text
state + event -> next state + side effects
```

List allowed transitions, guards, authorization, idempotency, terminal states, and compensating actions. Reject impossible transitions rather than silently coercing them. Test every critical transition and repeated event.

## Third-party adapters

Place vendor SDKs and payloads behind an adapter owned by the application. The adapter should:

- Validate external responses.
- Translate vendor errors into stable domain categories.
- Apply bounded timeout and retry policy.
- Handle pagination, rate limits, duplicate responses, and partial failure.
- Prevent vendor types from spreading through domain code.
- Expose capability gaps explicitly rather than fabricating success.

Add contract tests against a sandbox or recorded schema when drift is material. Treat documentation examples as hints until verified against the actual supported version.

## Compatibility and deprecation

Before deprecating, identify consumers and measure usage when possible. Communicate replacement, rationale, migration steps, deadlines, and behavior after the deadline.

Use warnings or metadata that reach the actual consumer channel. Keep the compatibility window long enough for known consumers and operational constraints. Define removal criteria based on adoption evidence, not only a calendar date.

Do not leave deprecated interfaces indefinitely without ownership and a removal plan; they remain part of the support surface.
