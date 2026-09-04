# Relational Databases

Use this reference for normal application persistence in PostgreSQL/MySQL-style relational databases. For database design, index/query-plan analysis, large migrations, backup/restore, or database administration, route to `database-engineering`.

- Keep transactions around the smallest invariant that must change atomically.
- Prefer parameterized queries and repository/query APIs over string-built SQL.
- Enforce durable uniqueness/referential integrity in the database where applicable.
- Make isolation, lock/retry behavior, and stale-read tolerance explicit for concurrency-sensitive paths.
- Avoid remote network calls while holding database transactions unless the workflow explicitly tolerates the lock duration and partial failures.
- Bound list queries and use stable pagination/order semantics for public collections.

Engine sources:

- PostgreSQL: https://www.postgresql.org/docs/current/
- MySQL: https://dev.mysql.com/doc/refman/en/
