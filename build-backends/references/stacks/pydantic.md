# Pydantic

Authoritative source: https://docs.pydantic.dev/

Use Pydantic at external/configuration boundaries according to the project's current major version and conventions.

- Distinguish create/update input models from durable/output representations when semantics differ.
- Normalize once at the boundary; avoid repeatedly reparsing trusted internal data.
- Make omitted versus `null` semantics explicit for partial updates.
- Keep validation deterministic and side-effect free; database/network authorization belongs outside model validators.
- Use settings models or the project's configuration layer without logging secrets.
- Review serialization aliases, defaults, extra-field handling, and strictness when they are part of a public contract.

Verify current official documentation before using version-sensitive validator or settings APIs.
