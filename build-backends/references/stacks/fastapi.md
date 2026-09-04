# FastAPI

Authoritative source: https://fastapi.tiangolo.com/

Use this reference only when the inspected project actually uses FastAPI or the user requests it.

- Keep route handlers thin: parse/validate transport input, establish dependencies/identity, call an application capability, and translate outcomes.
- Reuse the project's dependency injection conventions for sessions, auth context, configuration, and adapters.
- Keep domain/service logic independent of `Request`, `Response`, ORM sessions, and HTTP exceptions where practical.
- Use response/request models to make transport shape explicit; do not return ORM objects accidentally just because serialization currently works.
- Map stable domain/application errors at one HTTP boundary rather than raising framework exceptions throughout the domain.
- Preserve async/sync boundaries deliberately; do not mark blocking database/vendor work async unless the underlying path is non-blocking or isolated appropriately.
- Use the repository's actual test client/ASGI test setup instead of inventing a second harness.

For a maintained production-oriented example, see FastAPI's Full Stack Template documentation:
https://fastapi.tiangolo.com/project-generation/
