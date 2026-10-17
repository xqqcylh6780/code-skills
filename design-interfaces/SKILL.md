---
name: design-interfaces
description: >-
  Design or evolve public/shared API, event, CLI, config, library, or component contracts: inputs,
  errors, compatibility, and migration. Excludes private implementation details.
---

# Design Interfaces

Design the observable contract before the implementation. Make valid use straightforward, invalid states difficult to represent, failures predictable, and future evolution possible without coordinated rewrites.

## Activation Threshold

Use this skill only when a caller outside the changed implementation owns a dependency on the
contract, or when an existing observable behavior must evolve safely. A handler, component,
configuration value, schema, or function is not automatically a shared interface. For ordinary
private implementation work, follow repository conventions without producing a separate contract
design deliverable.

## Select the outcome and work size

- **Design/advice only:** specify the affected contract, examples, consumer impact, and proposed
  checks. Do not edit implementation or create tests merely to complete the design.
- **Design and implementation:** settle the contract decisions needed for the requested change,
  update its authoritative artifact, and continue into the implementation skill without asking
  again for an already-authorized change.

For a small compatible extension following an established convention, inspect the current contract
and actual consumers, define the delta and absence/default/error semantics that change, then use a
representative example and focused compatibility check. Skip unrelated sections below; a new
optional field does not by itself need an ADR, versioning plan, or separate design document.

Use the broader workflow for a new interface, breaking change, or material semantic ambiguity.
Record decisions in the project's existing types/schema/specification instead of duplicating them
across new artifacts. A breaking change still needs explicit consumer and migration analysis.

## Design Principles

- Start from consumer tasks and invariants, not storage tables or framework primitives.
- Expose the smallest coherent capability that lets consumers complete a use case.
- Treat every observable behavior as a potential dependency: shapes, defaults, ordering, timing, side effects, error categories, and retry behavior.
- Keep transport and implementation details behind adapters.
- Validate untrusted data at entry and convert it to trusted internal types once.
- Prefer additive evolution, explicit deprecation, and one supported contract over long-lived parallel variants.
- Pair every contract with executable examples or tests.

## Workflow

### 1. Define the Boundary and Consumers

Identify:

- Who calls or observes the interface: people, modules, services, automation, third parties, and operational tooling.
- Which use cases must be completed atomically or independently.
- Which system owns validation, state, authorization, retries, and error translation.
- Which behaviors already exist and may have accidental consumers.
- Expected scale, latency, consistency, availability, and compatibility constraints.

Create a consumer table when several callers differ:

| Consumer | Goal | Required data/operation | Failure handling | Compatibility constraint |
|---|---|---|---|---|

Do not design from hypothetical future consumers unless a concrete extension pressure exists.

### 2. Write Contract Invariants

State what must always be true:

- Valid inputs and canonical representation.
- Output shape and meaning.
- Allowed state transitions.
- Authorization and ownership rules.
- Side effects and transactional boundaries.
- Ordering, uniqueness, consistency, and concurrency rules.
- Idempotency, retry, timeout, cancellation, and duplicate behavior.
- Privacy, retention, and observability expectations when relevant.

Prefer invariants that can be tested. If the contract cannot explain an empty, invalid, duplicate, partial, delayed, or repeated operation, it is incomplete.

### 3. Model the Domain, Not the Transport

Choose names and types that reflect consumer concepts. Separate:

- Create/update input from stored/output representation.
- Domain identifiers from interchangeable strings or numbers when confusion is costly.
- Variants with discriminated unions or explicit state machines.
- Optional, omitted, empty, and null semantics.
- Domain errors from transport codes and human messages.

Avoid exposing database rows, ORM objects, framework request types, SDK responses, internal timestamps, or incidental call sequencing without a consumer need.

### 4. Minimize and Shape the Surface

Prefer a small number of cohesive operations over many shallow primitives that force callers to coordinate internal steps.

For each operation define:

```text
Name and purpose:
Inputs and validation:
Output and guarantees:
Errors and retryability:
Side effects and atomicity:
Authorization:
Ordering/consistency:
Idempotency/cancellation:
Observability:
```

Make the common path convenient and dangerous or ambiguous behavior explicit. Use safe defaults, bounded collections, and named options instead of positional booleans or overloaded meanings.

### 5. Design Success and Failure Together

Define success, empty, partial, conflict, invalid, unauthenticated, unauthorized, missing, rate-limited, unavailable, timeout, and internal failure outcomes as relevant.

Use one predictable error strategy:

- Stable machine-readable code or type.
- Safe human-facing message.
- Structured details only when consumers can act on them.
- Retryability or remediation guidance when useful.
- Correlation identifier for operational diagnosis when appropriate.

Do not leak stack traces, queries, internal paths, secrets, dependency details, or cross-tenant information. Do not make consumers parse prose to determine behavior.

### 6. Define Collection and Mutation Semantics

For collections, specify limits, pagination, stable ordering, tie-breaking, filters, search semantics, field selection, and whether totals are exact or available.

For writes, specify validation timing, uniqueness, concurrency control, partial-update semantics, idempotency, duplicate handling, and transaction boundaries. Distinguish omitted, null, and empty values explicitly.

Read [references/http-contracts.md](references/http-contracts.md) for HTTP status and method semantics, pagination, conditional requests, caching, idempotency keys, webhooks, and GraphQL considerations.

### 7. Design Non-HTTP Interfaces Deliberately

Read [references/interface-patterns.md](references/interface-patterns.md) when designing modules/libraries, component props, CLIs, configuration, schemas, events, queues, jobs, state machines, or third-party adapters.

Keep async interfaces explicit about acknowledgement, delivery, ordering, retry, deduplication, poison messages, and schema evolution. Keep module interfaces explicit about ownership, lifecycle, mutation, thread safety, and resource cleanup.

### 8. Plan Evolution and Migration

Inventory current observable behavior and affected consumers before changing an established contract.

Classify the change:

- **Compatible additive:** new optional field, operation, or variant that old consumers safely ignore.
- **Conditionally compatible:** changed default, new error, tighter validation, ordering, performance, or authorization behavior.
- **Breaking:** removed/renamed field, narrower input, new required value, changed type or meaning, incompatible state transition, or changed side effect.

Prefer additive changes and tolerant readers without silently accepting invalid data. When a breaking change is necessary, define adoption telemetry, migration steps, compatibility window, deprecation signal, rollback constraints, and removal criteria.

Avoid multiple long-lived versions unless consumer isolation cannot be achieved through adapters or staged migration.

### 9. Produce Examples Before Implementation

Write representative examples for:

- Normal success.
- Minimum and maximum valid input.
- Empty result.
- Invalid input.
- Authorization failure.
- Conflict, duplicate, or concurrency outcome.
- Retry/idempotency behavior.
- Old and new consumer behavior during migration.

Examples should be concrete enough to become contract tests. Derive them from the contract, not the implementation.

### 10. Prepare the Implementation Boundary

Describe the stable internal capability that should sit behind the contract. HTTP handlers, GraphQL
resolvers, CLI parsers, queues, storage, and third-party SDKs should translate into and out of that
capability rather than leak transport or vendor types into domain behavior.

Specify where external data is parsed and validated, where errors are translated, and which adapter
owns third-party response validation. Do not modify private implementation merely to complete a
contract-design-only request. When implementation is also requested, route the resulting contract
to `build-backends`, `build-frontends`, `build-mobile-apps`, or `database-engineering` as appropriate.

### 11. Prove and Document the Contract

For implementation work, add or update contract tests for inputs, outputs, errors, authorization,
side effects, retries, compatibility, and state transitions that change. For design-only work,
provide the proposed examples and checks without creating or modifying tests.

When edits are requested, update the authoritative artifact in the same change: type definitions,
schema, OpenAPI/GraphQL description, CLI help, configuration schema, event schema, examples, or
protocol documentation. For advice-only requests, identify the artifact and proposed delta.

Verify a representative real consumer when generated types, SDKs, serialization, or cross-language behavior could differ from the source schema.

## Review Guardrails

- Do not expose framework, persistence, or vendor types without a consumer requirement.
- Do not mix error shapes or success envelopes across sibling operations.
- Do not add unbounded list operations.
- Do not add retries to non-idempotent effects without duplicate semantics.
- Do not change defaults, ordering, nullability, precision, authorization, or latency silently.
- Do not overload one field with several meanings or use booleans where a future state may be needed.
- Do not force consumers to reconstruct domain operations from low-level primitives.
- Do not accept unknown fields silently when doing so would hide client mistakes or weaken security.
- Do not use third-party payloads without schema and semantic validation.

## Handoff

For requested edits, update the authoritative contract artifact; for advice only, describe the
proposed delta. Lead with the consumer-visible outcome. Summarize
only the relevant owners, inputs, guarantees, errors, state and side effects, authorization,
compatibility classification, migration plan, examples, verification, and unresolved risks. Do
not manufacture sections for concerns that do not apply.

Route implementation deliberately: server behavior to `build-backends`, browser UI to
`build-frontends`, native Android Kotlin/Java behavior to `build-mobile-apps`, database-primary work
to `database-engineering`, and changed trust boundaries to `secure-boundaries`. For uni-app,
Flutter, React Native, or mini programs, follow that project's platform workflow rather than
forcing a browser/native-Android skill. A design-only request ends after the contract and handoff
are complete.

## Completion Criteria

Design completion requires an explicit contract delta, understood consumer impact, consistent
error/evolution semantics, representative examples, and a verification plan. Implementation also
requires synchronized contract artifacts and relevant boundary-test evidence, or a disclosed
verification limitation. Match the detail to the changed boundary.
