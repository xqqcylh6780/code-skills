# Planning Checklist

Apply only the sections relevant to the shaped work. Use this checklist to expose omissions, not to require every project to produce every artifact.

## Contents

- [Product and Scope](#product-and-scope)
- [Current System Evidence](#current-system-evidence)
- [Architecture and Ownership](#architecture-and-ownership)
- [Data and State](#data-and-state)
- [Interfaces and Compatibility](#interfaces-and-compatibility)
- [Security and Privacy](#security-and-privacy)
- [User Experience and Accessibility](#user-experience-and-accessibility)
- [Reliability and Performance](#reliability-and-performance)
- [Testing and Acceptance](#testing-and-acceptance)
- [Delivery and Operations](#delivery-and-operations)
- [Plan Review Questions](#plan-review-questions)

## Product and Scope

- Name the user or system actor, triggering situation, and desired outcome.
- Separate required behavior from a preferred implementation.
- Define the first coherent release and why it is useful.
- List explicit non-goals and deferred capabilities.
- Identify affected existing behavior and user expectations.
- Record success evidence and how it will be observed.
- Confirm that scope expansion or reduction has a stated reason.

## Current System Evidence

- Identify relevant files, components, services, jobs, schemas, and documentation.
- Verify current behavior instead of relying only on issue text.
- Record established framework, dependency, test, deployment, and design-system conventions.
- Identify active migrations, feature flags, compatibility layers, and deprecated paths.
- Distinguish repository facts from assumptions about production configuration.
- Note pre-existing failures or constraints that can affect verification.

## Architecture and Ownership

- Identify the boundary that owns each invariant and side effect.
- Define entry points, orchestration, domain logic, persistence, and external adapters.
- Trace the primary data or event flow end to end.
- State synchronous and asynchronous boundaries.
- Define lifecycle, resource cleanup, cancellation, and concurrency where relevant.
- Reuse existing capabilities before proposing a new service, queue, framework, or abstraction.
- Check whether a new dependency spends complexity on a demonstrated requirement.
- Identify the operational owner after release.

Use a compact diagram when three or more components exchange state or control:

```text
actor -> entry point -> domain capability -> persistence/integration
                         |                 -> event/job
                         -> policy/error   -> observable result
```

## Data and State

- Define identifiers, ownership, tenant scope, and lifecycle.
- Distinguish create/update input, stored representation, and returned representation.
- Specify optional, omitted, empty, and null semantics.
- Define valid state transitions and invalid transition behavior.
- Address uniqueness, ordering, consistency, concurrency, and idempotency.
- Plan schema migration, backfill, dual-read/write, cutover, and cleanup when applicable.
- Define retention, deletion, export, recovery, and audit requirements for sensitive data.
- Identify cache invalidation and stale-read behavior.

## Interfaces and Compatibility

- Identify public and shared contracts: HTTP, GraphQL, events, CLI, configuration, module API, component props, files, and schemas.
- Define inputs, outputs, errors, side effects, limits, ordering, retries, and cancellation.
- Classify each contract change as additive, conditionally compatible, or breaking.
- Plan consumer migration, telemetry, deprecation, rollback, and removal.
- Validate third-party responses and version assumptions.
- Use `design-interfaces` for detailed contract work.

## Security and Privacy

- Mark trust boundaries and privileged effects.
- Identify authentication, authorization, tenancy, and ownership checks.
- Validate untrusted input and encode output for its destination context.
- Protect secrets, credentials, personal data, logs, exports, caches, and model context.
- Bound size, time, rate, retries, memory, archive expansion, and outbound destinations.
- Consider replay, enumeration, injection, confused deputy, cross-tenant access, and business-logic abuse.
- Define negative tests, detection, revocation, rollback, and incident response.
- Use `secure-boundaries` when any of these controls are material.

## User Experience and Accessibility

- Trace the primary user task from entry to completion.
- Define loading, empty, populated, error, offline, denied, pending, and success states as relevant.
- Preserve information hierarchy and action priority across narrow and wide layouts.
- Include keyboard access, focus behavior, labels, errors, announcements, contrast, reduced motion, and touch targets.
- Use real or approved content; identify missing copy and localization pressure.
- Confirm every visible control has working behavior.
- Use `build-frontends` for detailed design, implementation, and browser verification.

## Reliability and Performance

- Identify expected workload, latency, throughput, payload, and availability constraints when evidence exists.
- Define timeout, retry, backoff, duplicate, partial failure, and degraded-mode behavior.
- Avoid retries on non-idempotent effects without duplicate protection.
- Plan observability for the user journey and important boundaries.
- Define alerts, dashboards, audit evidence, and ownership only where operationally justified.
- Identify likely request waterfalls, unbounded work, large assets, expensive queries, and contention.
- Establish a baseline before claiming a performance improvement.

## Testing and Acceptance

- Map each acceptance criterion to a practical verification seam.
- Cover primary success, boundary input, denial, failure, recovery, and compatibility risks.
- Prefer stable public behavior over internal call structure.
- Define fixtures, test data, services, browser runtime, and environment needs.
- Identify manual or sandbox verification where automation cannot establish the outcome.
- Separate test-harness work from product behavior.
- Use `test-behavior-first` when implementation can proceed through a reliable red-green cycle.

## Delivery and Operations

- Order work by dependencies, uncertainty, risk, and independently useful outcomes.
- Define rollout, flags, data migration, compatibility window, and old-path removal.
- Include rollback or disablement for material changes.
- Identify documentation, support, training, or operational runbook changes required by the release.
- State deployment environment and configuration assumptions.
- Verify production or staging health through observable signals when the request includes delivery.
- Avoid calendar estimates without team capacity and repository evidence.

## Plan Review Questions

Before approval, ask:

1. Which claim in this plan is least supported by evidence?
2. Which decision would be most expensive to reverse?
3. Which failure would harm users while still passing the happy-path tests?
4. Which existing consumer or workflow could break silently?
5. Which slice first proves end-to-end value or retires the largest uncertainty?
6. Which proposed component or dependency can be removed without weakening the outcome?
7. Are the non-goals strong enough to prevent scope drift?
8. Can another implementer begin the first slice without rediscovering a material decision?
9. Can every acceptance criterion be observed or measured?
10. Is there a safe recovery path if rollout fails halfway?

Return unresolved answers to the requirements ledger as decisions, risks, or discovery tasks. Do not hide them in prose.
