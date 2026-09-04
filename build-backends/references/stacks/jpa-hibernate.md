# Jakarta Persistence, Hibernate, and Spring Data JPA

Use this reference when the Java repository uses Jakarta Persistence/JPA, Hibernate ORM, or Spring Data JPA.

Official sources:

- Jakarta Persistence: https://jakarta.ee/specifications/persistence/
- Hibernate ORM: https://hibernate.org/orm/
- Spring Data JPA: https://docs.spring.io/spring-data/jpa/reference/

## Entity and domain boundaries

- Do not expose persistence entities directly as public API models by default.
- Keep ownership, nullability, uniqueness, and lifecycle invariants explicit in both code and the database.
- Treat `equals`/`hashCode`, identifiers, mutable collections, and proxy/lazy behavior carefully.
- Avoid entity graphs that accidentally serialize an entire object graph.

## Fetching

- Identify N+1 behavior with evidence; do not make every association eager.
- Use repository/query/entity-graph/fetch-join mechanisms deliberately for a known use case.
- Pagination plus collection fetch joins can have surprising behavior; verify SQL and result semantics.
- Keep batch size and second-level cache changes measurement-driven.

## Transactions

- Place transactions around the invariant, not around an entire web request by habit.
- Understand propagation and isolation already configured by the repository.
- Do not hold a database transaction open across remote network calls.
- Handle optimistic/pessimistic locking only when the concurrency invariant requires it.
- Treat lazy loading outside transaction/session boundaries as an architecture signal, not something to hide globally.

## Spring Data repositories

- Use derived queries only while their intent stays obvious.
- Prefer explicit queries/specifications when filtering becomes hard to reason about.
- Avoid broad `save()`-everywhere patterns when aggregate ownership and update intent matter.
- Verify bulk updates/deletes against persistence-context synchronization semantics.

## Schema ownership

ORM mapping does not replace database design. Use `database-engineering` for schema/index/query-plan work and
`flyway-liquibase.md` when migration tooling is involved.
