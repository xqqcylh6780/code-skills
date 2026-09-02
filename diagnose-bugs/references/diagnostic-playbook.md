# Diagnostic Playbook

Use only the sections matching the failure class. This file supplements the core workflow; it does not replace reproduction and causal evidence.

## Table of contents

- Deterministic logic and data-flow failures
- State, cache, and data failures
- Environment and build failures
- Intermittent, timing, and concurrency failures
- Integration and distributed-system failures
- Performance and resource regressions
- Production-safe instrumentation
- Recovery and rollback decisions
- Diagnostic anti-patterns

## Deterministic logic and data-flow failures

Compare actual values with the contract at successive boundaries. Look for:

- Incorrect normalization, parsing, units, rounding, encoding, locale, or timezone handling.
- Missing branch coverage, invalid default, inverted condition, or stale derived value.
- Mutation, aliasing, object reuse, or incorrect lifecycle ownership.
- Off-by-one boundaries, empty input, duplicate values, overflow, and invalid sentinel values.
- Serialization differences between in-memory types and wire or storage formats.

Prefer a minimal input that changes only one relevant property. If two nearby implementations disagree, derive the expected result from a specification or worked example rather than assuming either is correct.

## State, cache, and data failures

Determine whether the bad result is produced on write, stored incorrectly, or read/interpreted incorrectly.

Check:

- Clean state versus existing state.
- First request versus subsequent request.
- Cache hit versus miss and invalidation timing.
- Transaction boundaries, isolation, retries, and partial commits.
- Schema and migration version versus application version.
- Soft-delete, tenancy, ownership, and filtering predicates.
- Event duplication, omission, reordering, and replay.

Inspect representative records without exposing sensitive data. Make recovery idempotent and auditable. Back up or snapshot material data before any mutation when authorized.

## Environment and build failures

Build an explicit difference table between working and failing environments:

| Dimension | Working | Failing |
|---|---|---|
| Source revision | | |
| Runtime/compiler | | |
| Dependency/lockfile | | |
| OS/architecture | | |
| Locale/timezone | | |
| Environment/config | | |
| Permissions/network | | |
| Generated/cache state | | |

For build failures, classify before changing dependencies:

- Syntax/type/compiler error.
- Missing or mismatched import/export.
- Generated artifact out of date.
- Configuration schema or toolchain mismatch.
- Lockfile/install inconsistency.
- Platform-specific path, case, line-ending, or native module issue.
- CI permission, secret, network, or resource constraint.

Prefer checked-in wrappers and immutable installs. Do not delete caches broadly until their role is tested; compare a clean build with the existing state and preserve the failing evidence.

## Intermittent, timing, and concurrency failures

Measure rather than label a test "flaky." Record total runs, failures, seeds, duration, and execution order.

Probe one dimension at a time:

- Fix or vary random seeds.
- Freeze or control time.
- Run alone versus with the suite.
- Run serially versus concurrently.
- Increase contention or insert diagnostic barriers at suspected race points.
- Repeat with cold and warm caches.
- Simulate cancellation, timeout, retry, duplicate delivery, and out-of-order completion.

Look for shared mutable state, missing awaits, unjoined workers, leaked resources, non-atomic check-then-act sequences, inconsistent lock ordering, and reliance on wall-clock sleeps.

Replace fixed sleeps with waits on observable conditions. A retry may help quantify frequency, but must not become the permanent solution unless transient failure is explicitly part of the contract.

## Integration and distributed-system failures

Capture both sides of the boundary when possible:

- Request method, URL class, headers, schema, correlation ID, and timestamp.
- Response status, schema, retry metadata, and latency.
- Contract or version used by each side.
- Authentication, authorization, clock skew, expiry, and rate-limit state.
- Whether the operation is idempotent and whether duplicates are possible.

Validate external payloads before trusting them. Distinguish transport failure, protocol failure, semantic rejection, dependency degradation, and local interpretation error.

For queues and events, inspect publish, persistence, delivery, acknowledgement, retry, dead-letter, and consumer state separately. For eventual consistency, define the expected convergence window before treating stale reads as defects.

## Performance and resource regressions

Define the metric and workload before optimizing:

```text
Metric: latency/throughput/CPU/memory/I/O/contention
Workload: input size, concurrency, data shape, warm-up
Baseline: median and tail values with variance
Regression threshold: explicit comparison
```

Use profiles, traces, query plans, allocation data, and counters to find where time or memory is spent. Separate cold-start, steady-state, and tail behavior. Confirm the bottleneck moves or disappears after the change without shifting cost to another constrained resource.

Avoid conclusions from one run, debug builds, unequal inputs, or a benchmark that omits the real boundary.

## Production-safe instrumentation

Add the least invasive signal that distinguishes hypotheses:

- Structured event with timestamp, operation, outcome, duration, and correlation ID.
- Counter or histogram for rates and latency.
- Trace span around the suspected boundary.
- Invariant assertion that fails safely.
- Sampling for high-volume paths.

Never log secrets, credentials, raw tokens, full sensitive payloads, or cross-tenant data. Bound cardinality. Mark temporary diagnostics and remove them after the investigation unless they provide lasting operational value.

## Recovery and rollback decisions

Separate code repair from operational recovery:

- **Rollback** when the new version is the likely cause and reversal is compatible with stored state.
- **Roll forward** when rollback would violate a migration or contract.
- **Feature disablement** when a safe switch isolates the failure.
- **Data repair** only with a verified predicate, dry run, backup or recovery path, idempotency, and audit trail.
- **Replay** only when consumers are idempotent or duplicates are handled explicitly.

Verify rollback and recovery plans against schema, queue, cache, and client compatibility. A code rollback does not automatically undo external side effects.

## Diagnostic anti-patterns

- Editing before capturing the original failure.
- Treating the final stack frame as the root cause.
- Changing several variables and accepting a green result.
- Deleting caches, lockfiles, or data without proving relevance.
- Updating dependencies merely because an error mentions one.
- Weakening a test to match current output before confirming desired behavior.
- Adding null checks, retries, deduplication, or catch-all handling at the presentation layer when upstream invariants are broken.
- Keeping verbose temporary logging that leaks data or degrades performance.
- Reporting "works on my machine" as verification of an environment-dependent issue.
