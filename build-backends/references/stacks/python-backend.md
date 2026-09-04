# Python Backend

Use this reference only when the repository is already Python or the user explicitly chooses Python.
Do not migrate a Java or other established backend to Python merely because this reference exists.

## Detect the local Python stack first

Inspect the repository before choosing framework-specific guidance:

- `pyproject.toml`, `requirements*.txt`, `Pipfile`, `poetry.lock`, `uv.lock`, or equivalent.
- Framework imports and entrypoints such as FastAPI, Flask, Django, Starlette, or custom ASGI/WSGI.
- Persistence such as SQLAlchemy, SQLModel, Django ORM, raw drivers, or another repository abstraction.
- Migration tooling such as Alembic or framework-native migrations.
- Test tooling and repository scripts; prefer checked-in wrappers over guessed commands.
- Runtime version and deployment constraints.

Preserve the existing package manager, framework, ORM, project layout, and supported Python version unless
the user explicitly requests a migration.

## Implementation posture

- Keep request parsing and framework objects at the transport boundary.
- Use typed validation where the project already does so; do not introduce Pydantic into unrelated code solely for style.
- Keep database sessions and transactions scoped to the business invariant they protect.
- Avoid blocking I/O inside an async path unless the repository already isolates it safely.
- Do not mix sync and async database or HTTP clients without understanding lifecycle and cancellation behavior.
- Treat process workers, thread pools, asyncio tasks, and external job systems as different concurrency models.
- Make timeouts, cancellation, retries, and shutdown behavior explicit around remote work.
- Use the project's real logging and configuration conventions instead of inventing global singletons.

## Load narrower references only when relevant

- FastAPI: [fastapi.md](fastapi.md)
- Pydantic: [pydantic.md](pydantic.md)
- SQLAlchemy: [sqlalchemy.md](sqlalchemy.md)
- Alembic: [alembic.md](alembic.md)

For Flask or Django, follow the repository's established conventions and verify current official documentation
when framework-specific behavior materially affects the change. Add a dedicated reference only when repeated
work justifies it.
