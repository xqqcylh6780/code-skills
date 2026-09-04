# Alembic

Authoritative source: https://alembic.sqlalchemy.org/en/latest/

Use Alembic when the inspected SQLAlchemy project already uses it or the user requests it.

- Treat `--autogenerate` output as a migration candidate that requires human/agent review.
- Verify renames, destructive changes, server defaults, constraints, indexes, enum/type changes, and data conversions explicitly.
- Keep migration order and downgrade policy consistent with repository conventions.
- Separate long data backfills from schema DDL when operational risk or restartability requires it.
- Avoid importing application runtime paths that make historical migrations depend on today's mutable domain code.
- For deployed systems, coordinate expand/migrate/contract sequencing with `database-engineering` and `deploy-and-operate`.

Official Alembic autogenerate documentation explicitly expects generated candidate migrations to be reviewed and adjusted manually.
