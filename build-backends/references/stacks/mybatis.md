# MyBatis

Use this reference when the repository already uses MyBatis or MyBatis-Spring.

Official source: https://mybatis.org/mybatis-3/

## Keep SQL explicit and bounded

- Keep statement purpose and result mapping obvious.
- Parameterize values; do not build executable SQL from untrusted strings.
- Whitelist dynamic identifiers or clauses when they truly must vary.
- Keep pagination, ordering, filters, and null semantics explicit.
- Avoid `SELECT *` where result shape or schema evolution matters.
- Treat generated keys, affected-row counts, and optimistic concurrency as contractual behavior when relied upon.

## Mapper boundaries

- Keep mapper methods aligned to application/domain operations rather than exposing arbitrary table primitives everywhere.
- Avoid huge generic mapper utilities that hide SQL behavior.
- Keep XML/annotation style consistent with the repository.
- Verify nested mappings and collection joins for duplicate rows, memory growth, and N+1 queries.

## Transactions

Use the transaction owner already established by Spring or the application. Do not mix manual commit/rollback
with framework-managed transactions casually.

## Verification

For material query changes:

- inspect the executed SQL;
- verify representative result mapping;
- test empty/null/boundary inputs;
- use `database-engineering` for query plans, indexes, locking, or migration concerns.
