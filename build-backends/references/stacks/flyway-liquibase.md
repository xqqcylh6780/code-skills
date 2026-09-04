# Flyway and Liquibase

Use this reference when a Java/JVM repository already manages schema changes with Flyway or Liquibase.

Official sources:

- Flyway: https://documentation.red-gate.com/fd
- Liquibase: https://docs.liquibase.com/

## Preserve the repository's migration system

Do not introduce both tools into one project casually. Use the migration framework already present.

## Migration rules

- Treat applied migration history as immutable unless the repository has an explicit repair policy.
- Prefer forward-compatible staged migrations for zero/low-downtime deployments.
- Separate schema expansion, backfill, application switch, constraint tightening, and cleanup when old/new
  application versions can overlap.
- Keep destructive operations explicit and authorized.
- Bound large backfills and make progress/retry observable.
- Verify indexes and constraints for production-sized tables before assuming an `ALTER` is harmless.

## Flyway

- Keep versioned/repeatable migration semantics intentional.
- Do not edit already-applied versioned migrations simply to make local validation pass.
- Use Java migrations only when SQL is insufficient and the project has a clear reason.

## Liquibase

- Keep changelog ordering and change-set identity stable.
- Use preconditions/rollback metadata according to repository policy rather than as a substitute for rollout design.
- Avoid environment-specific drift hidden inside ad-hoc conditional change sets.

For migration architecture, rollback compatibility, index/query effects, or data repair, combine with
`database-engineering` and `deploy-and-operate`.
