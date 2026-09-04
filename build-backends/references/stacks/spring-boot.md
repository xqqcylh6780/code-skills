# Spring Boot

Use this reference when the repository already uses Spring Boot or the user explicitly chooses it.
Verify version-sensitive APIs and configuration against the current Spring Boot reference before changing them.

Official source: https://docs.spring.io/spring-boot/reference/

## Preserve the application's existing Spring shape

Inspect before editing:

- Spring Boot version and Java baseline.
- Maven or Gradle build.
- Web stack: Spring MVC, WebFlux, messaging, batch, scheduled jobs, or a mix.
- Configuration properties and active profiles.
- Existing controller/service/repository/module boundaries.
- Actuator, observability, security, persistence, and test setup.
- Repository conventions for exceptions and response mapping.

Do not introduce WebFlux into MVC, or MVC into a reactive service, simply because one API looks convenient.

## Configuration

- Prefer typed configuration-properties patterns already used by the project.
- Keep environment-specific values outside source.
- Fail clearly for required security or connectivity configuration.
- Avoid profile sprawl and duplicated configuration trees.
- Treat configuration keys as an observable compatibility surface when operators or deployments depend on them.

## Web and application boundaries

- Validate and normalize request data at the edge.
- Map domain/application errors at one transport boundary.
- Do not put durable business invariants only in controllers.
- Keep transactions narrow and outside remote calls.
- Preserve thread/reactive context assumptions of the chosen web stack.
- For large uploads/downloads or streaming, understand buffering and size limits before changing defaults.

## Actuator and operations

Use the project's existing Actuator setup when present. Distinguish:

- liveness: process can make progress;
- readiness: instance can safely receive traffic;
- dependency detail: useful diagnostics that should not expose credentials or sensitive topology.

Do not expose every Actuator endpoint publicly by default.

## Testing

Prefer the narrowest Spring test slice or ordinary unit/integration seam that proves the behavior.
Do not default every test to a full application context if a smaller seam is faithful.
Use Testcontainers only when a real dependency boundary is the risk and the repository already supports or
authorizes container-backed tests.
