# Sources and Provenance

This file records external material used as reference or incorporated into the repository. Most skill text is locally authored and summarizes general engineering practice; source links are provided so framework-specific guidance can be refreshed against authoritative documentation.

## Existing incorporated material

### build-frontends design-intelligence

- Upstream: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Integrated revision: `abb7f2fd5a083fa1ff55c326a963ff0d95c33f99`
- License: MIT
- Local files: `build-frontends/scripts/design-intelligence/`
- Required notices are retained in that directory's `LICENSE` and `NOTICE` files.

### Playwright skill assets and notices

- Local license and attribution files are retained in `playwright/LICENSE.txt` and `playwright/NOTICE.txt`.

## Authoritative references for new engineering guidance

### Backend and data

- FastAPI documentation: https://fastapi.tiangolo.com/
- FastAPI Full Stack Template: https://fastapi.tiangolo.com/project-generation/
- SQLAlchemy 2.0 documentation: https://docs.sqlalchemy.org/en/20/
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/
- PostgreSQL documentation: https://www.postgresql.org/docs/current/
- MySQL reference manual: https://dev.mysql.com/doc/refman/en/
- Redis documentation: https://redis.io/docs/latest/

### Java backend

- Spring Boot reference: https://docs.spring.io/spring-boot/reference/
- Spring Security reference: https://docs.spring.io/spring-security/reference/
- Spring Data JPA reference: https://docs.spring.io/spring-data/jpa/reference/
- Jakarta Persistence specification: https://jakarta.ee/specifications/persistence/
- Hibernate ORM: https://hibernate.org/orm/
- MyBatis 3: https://mybatis.org/mybatis-3/
- Flyway documentation: https://documentation.red-gate.com/fd
- Liquibase documentation: https://docs.liquibase.com/
- Apache Maven guides: https://maven.apache.org/guides/
- Gradle User Manual: https://docs.gradle.org/current/userguide/
- JUnit: https://junit.org/
- Testcontainers for Java: https://java.testcontainers.org/

### Web frontend

- OpenAI Codex Skills guidance: https://developers.openai.com/codex/skills
- OpenAI frontend prompting guidance: https://developers.openai.com/api/docs/guides/frontend-prompt
- React documentation: https://react.dev/
- Vue documentation: https://vuejs.org/guide/
- Next.js documentation: https://nextjs.org/docs
- Vite documentation: https://vite.dev/guide/

### Mobile / uni-app

- uni-app documentation: https://uniapp.dcloud.net.cn/
- uni-app repository: https://github.com/dcloudio/uni-app
- Wot Design Uni repository: https://github.com/Moonofweisheng/wot-design-uni

### Delivery and operations

- Docker documentation: https://docs.docker.com/
- Docker Compose production guidance: https://docs.docker.com/compose/how-tos/production/
- GitHub Actions documentation: https://docs.github.com/en/actions
- OpenTelemetry documentation: https://opentelemetry.io/docs/
- Prometheus instrumentation guidance: https://prometheus.io/docs/practices/instrumentation/

### Refactoring

- Martin Fowler, Refactoring: https://refactoring.com/
- Refactoring catalog: https://refactoring.com/catalog/

### Agent/skill organization reference

- InsForge skills: https://github.com/InsForge/insforge-skills

The InsForge source is used as an organizational reference for progressive disclosure and skill/reference separation, not as a platform dependency of this repository.

## Refresh policy

Framework references should prefer stable principles over volatile version-specific claims. Before making a recommendation that depends on a current API, security default, deprecation, platform capability, or provider behavior, verify the current official source rather than treating this repository as the final authority.
