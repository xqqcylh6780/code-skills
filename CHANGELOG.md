# Changelog

## Unreleased

### Added

- Added first-class Java backend references for Spring Boot, Spring Security, JPA/Hibernate/Spring Data JPA, MyBatis, Flyway/Liquibase, Maven/Gradle, and JUnit/Testcontainers.
- Added explicit Python/Java stack-detection and preservation rules so Codex does not silently migrate one backend language to the other.

- `database-engineering` for relational schema, integrity, index, query-plan, migration, and recovery work.
- `deploy-and-operate` for release preparation, rollout, runtime verification, rollback, and recovery.
- `build-mobile-apps` for mobile and cross-platform application work, initially focused on uni-app/Vue 3.
- `refactor-code` for behavior-preserving structural change.
- `performance-engineering` for measured profiling, optimization, load, and capacity work.
- Backend stack references for FastAPI, Pydantic, SQLAlchemy, Alembic, relational databases, Redis, and WebSockets.
- Repository authoring, contribution, provenance, validation, and GitHub Actions files.
- Routing eval examples for the new lifecycle skills.

### Changed

- Optimized all Skill descriptions for Codex's bounded initial Skill-list budget and front-loaded trigger matching.
- Reworked `build-frontends` into a lean router/execution loop with focused-change, product, redesign, and audit paths.
- Added Web stack routing for React, Vue, Next.js, Vite, package managers, and styling/test conventions.
- Added a cross-platform installer that copies selected Skills into Codex `.agents/skills` discovery locations.
- Explicitly enabled implicit invocation for Web and mobile frontend Skills and strengthened Web/mobile conflict evals.

- Expanded the root README into a skill map and routing guide.
- Updated existing skill routing so mobile, pure database, refactoring, and deployment work can reach the new owners deliberately.
