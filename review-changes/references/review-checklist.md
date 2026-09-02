# Review Checklist

Use this reference for comprehensive or high-risk reviews. Apply only sections relevant to the
change; a checklist item is an investigation prompt, not automatic evidence of a defect.

## Contents

- [Requirements and scope](#requirements-and-scope)
- [Control flow, data, and state](#control-flow-data-and-state)
- [Errors and reliability](#errors-and-reliability)
- [Contracts and compatibility](#contracts-and-compatibility)
- [Security and privacy](#security-and-privacy)
- [Concurrency and performance](#concurrency-and-performance)
- [Tests and verification](#tests-and-verification)
- [Delivery and operations](#delivery-and-operations)
- [Finding validation](#finding-validation)

## Requirements and scope

- Map each acceptance criterion to implementation and evidence.
- Identify omitted required behavior and accidental scope expansion.
- Check defaults, limits, copy, identifiers, formats, and other exact values.
- Confirm error and denial behavior, not only successful behavior.
- Separate plan defects from implementation defects.
- Confirm feature flags and configuration expose the intended behavior.

## Control flow, data, and state

- Trace changed inputs through validation, transformation, persistence, and output.
- Check null, empty, boundary, malformed, duplicate, stale, and oversized inputs.
- Check every new branch for a defined result and cleanup behavior.
- Verify state transitions cannot skip required invariants.
- Confirm partial failures do not leave contradictory or unrecoverable state.
- Check ownership, lifetime, cleanup, cancellation, and retry interactions.
- Check serialization and deserialization preserve meaning and precision.
- Verify UI state connects producers, listeners, loading, error, empty, and success paths.

## Errors and reliability

- Confirm exceptions or rejected results are mapped at the correct boundary.
- Check retry safety, idempotency, timeout behavior, and duplicate delivery.
- Ensure fallbacks do not hide corruption, authorization failures, or permanent errors.
- Check resources are released on success, failure, cancellation, and timeout.
- Verify logs and diagnostics preserve useful context without exposing secrets.
- Check recovery, rollback, cache invalidation, and in-flight work when relevant.

## Contracts and compatibility

- Compare changed public signatures, schemas, commands, events, and configuration.
- Check existing consumers, version floors, defaults, optionality, and error semantics.
- Confirm additions do not change behavior for omitted fields or old clients unexpectedly.
- Review migrations for ordering, reversibility, mixed-version operation, and stored data.
- Check renamed or removed values have a deliberate compatibility or deprecation path.
- Confirm generated clients, schemas, documentation, and fixtures remain consistent.

## Security and privacy

- Identify untrusted inputs, privileged effects, tenant boundaries, and sensitive assets.
- Check authentication and authorization at the effect-producing boundary.
- Verify object ownership and tenant scope cannot be selected by an attacker.
- Check injection, traversal, unsafe deserialization, browser output, SSRF, and upload handling.
- Ensure secrets and sensitive data are not logged, cached, returned, or committed.
- Check dependency or build changes for new execution paths and supply-chain exposure.
- Verify limits for size, count, recursion, decompression, rate, and resource consumption.
- Treat model, tool, webhook, and external-service output as untrusted input.

## Concurrency and performance

- Identify shared mutable state, ordering assumptions, and non-atomic read-modify-write sequences.
- Check cancellation, retry, duplicate processing, lost updates, and stale reads.
- Confirm locks, transactions, and queues protect the intended invariant without deadlock.
- Look for request waterfalls, repeated queries, unbounded loops, fan-out, and large allocations.
- Distinguish plausible workload regressions from speculative optimization opportunities.
- Require representative measurement before claiming a performance defect when static evidence is
  insufficient.

## Tests and verification

- Confirm tests reach the changed public seam and assert observable results.
- Check the expected result is independent of the implementation algorithm.
- Verify failure, denial, boundary, recovery, and compatibility paths proportional to risk.
- Check mocks do not make the test pass while the real integration remains broken.
- Inspect skips, retries, warnings, snapshots, broad matchers, and false-positive assertions.
- Confirm regression tests would fail against the defective behavior.
- Distinguish tests present in the diff from tests actually executed and observed.
- Identify runtime, browser, integration, migration, or load checks that static tests cannot replace.

## Delivery and operations

- Check rollout order, feature flags, configuration defaults, and safe disable paths.
- Confirm observability can distinguish success, expected denial, transient failure, and corruption.
- Review background jobs, schedules, webhooks, and migrations for duplicate or partial execution.
- Check deployment assumptions, supported platforms, locale, timezone, filesystem, and permissions.
- Confirm documentation is updated when users or operators depend on changed behavior.
- Identify cleanup of old paths only when the new path is proven and rollout permits removal.

## Finding validation

Before reporting a finding, answer:

1. Which changed line introduced or exposed the behavior?
2. What concrete input, state, sequence, or environment triggers it?
3. Which requirement, invariant, contract, or supported behavior does it violate?
4. Is there an existing guard, caller constraint, feature flag, fallback, or test that prevents it?
5. What is the real impact and therefore the lowest accurate severity?
6. Can the implementer understand and verify the issue without repeating the entire review?

If any answer is missing, investigate further or report the matter as an open question or residual
risk rather than a confirmed finding.
