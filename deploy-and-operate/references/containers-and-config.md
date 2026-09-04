# Containers and Configuration

Authoritative Docker source: https://docs.docker.com/

## Image/build

- Keep the build reproducible from checked-in inputs and the repository's package lock strategy.
- Minimize unnecessary build context and runtime packages.
- Do not bake runtime secrets into layers or source-controlled build arguments.
- Run the process with the least privileges compatible with the application and platform.
- Give the runtime an explicit signal/termination path and allow graceful shutdown where the service owns in-flight work.

## Runtime configuration

Separate defaults, environment-specific configuration, and secrets. Validate required values at startup without echoing secret contents.

For Docker Compose production guidance, verify current official documentation at:
https://docs.docker.com/compose/how-tos/production/

A development Compose file may need production overrides for code mounts, ports, log settings, restart policy, external services, resource settings, and image sources. Preserve the project's actual hosting model rather than assuming Compose is the production platform.

## Health

Distinguish:

- **liveness:** should the platform restart this process?
- **readiness:** should this instance receive work/traffic now?
- **dependency/diagnostic status:** useful operator evidence that should not necessarily kill liveness.
