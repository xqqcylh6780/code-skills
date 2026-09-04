# JUnit and Testcontainers for Java

Use this reference when Java backend behavior needs automated tests and the repository already uses JUnit or
container-backed integration testing.

Official sources:

- JUnit: https://junit.org/
- Testcontainers for Java: https://java.testcontainers.org/

This reference supplements `test-behavior-first`; it does not require TDD for every Java change.

## JUnit

Follow the repository's current JUnit generation and conventions. Do not upgrade JUnit as an incidental feature change.

- Test observable behavior through stable seams.
- Use parameterized/dynamic tests when they improve clarity for one invariant, not merely to reduce line count.
- Keep time, locale, timezone, randomness, concurrency, and external services controlled.
- Avoid asserting Spring/Hibernate private call order unless interaction is itself the contract.

## Spring tests

Use the smallest faithful seam:

- plain unit test for pure rules;
- focused MVC/WebFlux/data slice where appropriate;
- full application context only when wiring across those boundaries is the risk.

## Testcontainers

Use a real containerized dependency when compatibility with PostgreSQL/MySQL/Redis/etc. is the risk and the
environment authorizes Docker/container use.

- Prefer known deterministic images and repository-owned lifecycle helpers.
- Do not start containers for tests that can faithfully run without them.
- Keep database state isolated between tests.
- Wait on service readiness or observable conditions instead of fixed sleeps.
- Do not present a mocked database test as proof of dialect or constraint behavior.

When strict test-first is requested or protects a material invariant, route through `test-behavior-first`.
