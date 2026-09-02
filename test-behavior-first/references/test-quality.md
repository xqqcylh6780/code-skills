# Test Quality Reference

Read only the sections relevant to the current test decision.

## Table of contents

- Choose the seam and size
- Build independent expectations
- Structure readable tests
- Select test doubles
- Control nondeterminism and flakiness
- Test databases, APIs, events, CLIs, and browsers
- Use table, property, snapshot, and approval tests
- Test errors, recovery, and concurrency
- Diagnose a failing test
- Review suite quality

## Choose the seam and size

| Seam | Prefer when | Main risk | Avoid when |
|---|---|---|---|
| Pure unit | Deterministic logic is the public contract | Logic defects and edge cases | It tests a private detail |
| Module/service | Collaborators form one stable capability | State transitions and orchestration | Setup reproduces the whole application |
| Database/repository | Queries, constraints, transactions, or migrations matter | Persistence semantics | An in-memory fake hides database behavior |
| API/command/event | Request, response, exit code, file, or message defines behavior | Boundary contract and integration | Infrastructure cost obscures a smaller logic failure |
| Component/browser | Rendering, focus, interaction, browser APIs, or accessibility matter | User-observable UI | A lower seam proves the same behavior reliably |
| End-to-end | Cross-system wiring and deployment are the changed risk | Critical user flow | It is the only coverage for internal rules |

Classify resource cost as well:

- **Small:** one process, no real network or database; milliseconds.
- **Medium:** localhost services, test database, multiple processes; seconds.
- **Large:** browser plus backend, external sandbox, staging; slower and fewer.

Prefer many small tests, enough medium contract tests to validate boundaries, and a small number of critical end-to-end flows. Do not enforce fixed percentages; architecture and failure history should determine the mix.

## Build independent expectations

Good sources of expected values:

- Product specification or acceptance criterion.
- Manually worked example.
- Known-good literal or golden artifact reviewed independently.
- External standard or official protocol example.
- Invariant that must hold for all valid inputs.

Avoid calculating the expectation with the same helper, mapping, query, or algorithm used by production. That creates a tautology.

For complex transformations, use several complementary oracles: a small hand-worked example, round-trip property, conservation invariant, and comparison with a separately trusted implementation.

## Structure readable tests

Use Arrange–Act–Assert or Given–When–Then. Make setup reveal only the facts relevant to the outcome.

Prefer names such as:

```text
rejects an update when the caller does not own the resource
preserves omitted fields during a partial update
retries a transient delivery without duplicating the side effect
```

One assertion per concept does not require one assertion statement. Group assertions that together prove one behavior. Split tests when failures would have different causes or remediation.

Favor DAMP—descriptive and meaningful phrases—over aggressive DRY in tests. Extract builders and helpers for irrelevant boilerplate, but keep behavior-defining values visible at the call site.

## Select test doubles

Preference order:

1. Real implementation when fast, deterministic, and safe.
2. Fake with meaningful behavior, such as an in-memory store.
3. Stub returning a narrow canned result.
4. Spy or interaction mock when the interaction itself is contractual.

Mock at external or uncontrollable boundaries: network providers, clocks, randomness, email, payments, destructive tools, and expensive infrastructure.

Do not mock every internal collaborator. Over-mocking can prove that code calls itself as designed while the real system fails.

When a mock models a third-party contract, add a contract test or periodic sandbox check if drift would be costly. Match error, timeout, retry, schema, and idempotency behavior—not only happy-path fields.

## Control nondeterminism and flakiness

Control:

- Time and timezone through an injected clock or framework time control.
- Randomness with explicit seeds and recorded failing cases.
- IDs through deterministic factories when their values matter.
- Locale, encoding, sorting, and environment variables.
- Network with bounded local fakes or explicit sandboxes.
- Mutable state with per-test setup and teardown.
- Concurrency with barriers, latches, fake schedulers, or observable state.

Avoid fixed sleeps. Poll or wait for the result that defines completion, with a bounded timeout and useful failure message.

When a test is flaky, record run count, failure count, seed, order, duration, and environment. Retries may gather evidence but should not normalize an unexplained failure.

## Test databases, APIs, events, CLIs, and browsers

### Database

- Exercise the real database engine when query, collation, constraint, transaction, locking, or migration semantics matter.
- Isolate state per test through transaction rollback, schema/database isolation, or deterministic cleanup.
- Assert externally meaningful results and constraints, not incidental SQL text.
- Test migration forward behavior, representative existing data, and rollback only when rollback is supported.

### API

- Assert status, structured body, headers, side effects, authentication, authorization, and error mapping.
- Cover omitted, null, empty, invalid, unknown, oversized, and boundary inputs as relevant.
- Verify idempotency and retry semantics for writes that clients may repeat.
- Treat exact human error text as non-contractual unless the interface promises it.

### Events and jobs

- Test duplicate delivery, out-of-order events, retry, poison messages, timeout, cancellation, and idempotency.
- Assert durable state or published contract, not only handler call counts.
- Control scheduler and clock behavior.

### CLI

- Assert exit code, stdout, stderr, filesystem effects, and signal/cancellation behavior.
- Keep machine-readable output stable and separate from human diagnostics.
- Test paths and quoting using the target platforms when portability matters.

### Browser/UI

- Query by roles, labels, and user-visible names when possible.
- Test user interactions and observable rendering, not component internals.
- Verify keyboard, focus, validation, loading, empty, and error states.
- Use real browser checks for layout, browser APIs, accessibility tree, network wiring, and visual regressions.

## Use table, property, snapshot, and approval tests

Use table-driven tests when many named inputs share one rule. Keep each case readable and ensure a failure identifies the case.

Use property-based tests when the domain has strong invariants across a large input space, such as round trips, ordering, idempotency, conservation, or parser robustness. Preserve the minimized failing example as a named regression test when useful.

Use snapshots for small stable structures whose full shape is the contract. Avoid large snapshots, volatile values, or updates accepted without review.

Use golden or approval artifacts for complex rendered output only when changes are intentionally reviewed and the artifact diff is understandable. Pair them with targeted semantic assertions for critical rules.

## Test errors, recovery, and concurrency

For error paths, assert:

- The correct public error category or status.
- No partial or forbidden side effects.
- Sensitive internals are not exposed.
- Retryability and user recovery are clear.
- Cleanup, rollback, and resource release occur.

For concurrency, define the invariant first: exactly-once effect, at-most-once publication, monotonic version, no lost update, stable order, or bounded duplication. Construct a schedule that would violate the invariant without the control. A loop that merely hopes to trigger a race is weaker evidence.

## Diagnose a failing test

Classify before editing:

- Product behavior is wrong.
- Test expectation is wrong or obsolete.
- Test does not reach the intended seam.
- Fixture, generated artifact, or environment is broken.
- State leaks across tests.
- Timing or order makes it flaky.
- Dependency contract changed.

Change the test only when the desired public behavior changed or the test never represented that behavior correctly. Preserve a previously valid regression guard when refactoring implementation.

## Review suite quality

Look for:

- Tests whose names do not identify behavior.
- Assertions coupled to private functions or call order.
- Extensive mocks without contract checks.
- Duplicate coverage at expensive seams.
- Important branches covered only by snapshots.
- Hidden skips, retries, quarantines, or conditional execution.
- Shared mutable fixtures and order dependence.
- Slow setup repeated where a safe reusable fixture would help.
- Coverage metrics increasing while meaningful behavior remains untested.

Coverage is a map, not proof. Use it to find unexamined code, then decide whether that code represents a meaningful risk or contract.
