# Maven and Gradle

Use this reference when Java backend work changes dependencies, build configuration, packaging, test execution,
or multi-module boundaries.

Official sources:

- Maven: https://maven.apache.org/guides/
- Gradle: https://docs.gradle.org/current/userguide/

## First rule: use the checked-in wrapper

Prefer `./mvnw` / `mvnw.cmd` or `./gradlew` / `gradlew.bat` when present.
Do not rely on a globally installed build-tool version over the repository wrapper.

## Preserve the build system

Do not convert Maven to Gradle or Gradle to Maven for an ordinary feature.

## Dependencies

- Add a dependency only for a concrete requirement.
- Prefer dependency-management/BOM/version-catalog conventions already used by the project.
- Avoid forcing versions that conflict with framework-managed dependency sets without evidence.
- Inspect transitive effects for security-sensitive or runtime-critical changes.
- Keep test-only dependencies out of production configurations.

## Maven

Respect parent POMs, dependencyManagement, pluginManagement, profiles, and module structure.
Do not add a profile when ordinary configuration or deployment environment already owns the distinction.

## Gradle

Respect Groovy vs Kotlin DSL, version catalogs, convention plugins, included builds, and task wiring.
Do not add custom tasks or plugins when standard lifecycle tasks already express the need.

## Verification

Use the narrowest repository command that proves compile/test/package behavior.
Avoid `clean` by habit when it adds cost without changing the evidence needed.
