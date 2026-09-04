# SQLAlchemy 2.x

Authoritative source: https://docs.sqlalchemy.org/en/20/

Use the project's existing SQLAlchemy sync/async pattern and session ownership.

- Keep Session lifetime explicit and bounded to the application/request/job unit of work.
- Put commit/rollback ownership at a clear orchestration boundary; avoid hidden commits in low-level repositories unless that is an established project contract.
- Use `Session.begin()` / transaction contexts where they make the invariant and rollback behavior clearer.
- Avoid leaking ORM-mapped objects across layers when their lazy-loading/session lifetime creates hidden I/O or ownership ambiguity.
- Load relationships intentionally and check for N+1 behavior on material collection paths.
- Use database constraints for durable uniqueness/integrity even when application checks improve error messages.
- For async SQLAlchemy, prevent accidental implicit I/O and keep one session scoped to one concurrent task/unit of work.

Database-specific schema/index/query-plan work belongs to `database-engineering`.
