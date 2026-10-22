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

## Specialist references added 2026-10-18

The following files are original local summaries and illustrative examples, informed by the
listed official documentation. No upstream skill package, script, or code file was imported.
skills.sh was used for discovery; live upstream sources were checked before authoring.

- `build-frontends/references/react-performance.md`: [React Server Components](https://react.dev/reference/rsc/server-components), [cache](https://react.dev/reference/react/cache), [lazy](https://react.dev/reference/react/lazy), [memo](https://react.dev/reference/react/memo).
- `build-frontends/references/react-composition.md`: [React state structure](https://react.dev/learn/choosing-the-state-structure), [context](https://react.dev/learn/passing-data-deeply-with-context).
- `build-frontends/references/nextjs-versioned-guidance.md`: [Next.js AI agents](https://nextjs.org/docs/app/guides/ai-agents), [next-skills retirement/migration](https://github.com/vercel-labs/next-skills). Local availability and the installed version remain authoritative; no codemod or framework upgrade is implied.
- `build-frontends/references/shadcn-integration.md`: [components.json](https://ui.shadcn.com/docs/components-json), [theming](https://ui.shadcn.com/docs/theming).
- `playwright/references/advanced-testing.md`: [auth](https://playwright.dev/docs/auth), [fixtures](https://playwright.dev/docs/test-fixtures), [network mocks](https://playwright.dev/docs/mock), [visual comparisons](https://playwright.dev/docs/test-snapshots), [traces](https://playwright.dev/docs/trace-viewer).
- `database-engineering/references/postgresql-patterns.md`: [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [index ordering](https://www.postgresql.org/docs/current/indexes-ordering.html), [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), [Supabase connection options](https://supabase.com/docs/guides/database/connecting-to-postgres).
- `resolve-git-conflicts/SKILL.md`: [Git merge](https://git-scm.com/docs/git-merge), [rebase](https://git-scm.com/docs/git-rebase), [index stages](https://git-scm.com/docs/git-ls-files), [ours/theirs](https://git-scm.com/docs/git-checkout). The skill is locally authored; it does not adopt the discovery candidate's blanket staging/commit or never-abort rules.

## Additional coverage pass, 2026-10-18

These are original local guidance and examples; no third-party skill package or source file was imported.

- `build-frontends/references/vue-reactivity.md`: [Vue reactivity fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html), [computed](https://vuejs.org/guide/essentials/computed.html), [watchers](https://vuejs.org/guide/essentials/watchers.html).
- `build-frontends/references/typescript-boundaries.md`: [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html).
- `upgrade-dependencies/`: [npm clean install](https://docs.npmjs.com/cli/commands/npm-ci), [pip install](https://pip.pypa.io/en/stable/cli/pip_install/), [Maven dependency mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html), [Gradle dependency locking](https://docs.gradle.org/current/userguide/dependency_locking.html). Package-specific release and migration evidence must still be checked for each requested upgrade.

## Domain-language and decision guidance, 2026-10-20

The additions to `shape-project` and `manage-spec-changes` are locally authored workflow guidance
informed by Matt Pocock's [domain-modeling skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)
and [grill-with-docs documentation](https://github.com/mattpocock/skills/blob/main/docs/engineering/grill-with-docs.md).
No upstream package, script, template, or skill text was imported. The adaptation preserves bounded
clarification, advice-only behavior, existing project conventions, and explicit documentation scope.
It also keeps accepted behavioral obligations in specifications even when no ADR qualifies.

## Refresh policy

Framework references should prefer stable principles over volatile version-specific claims. Before making a recommendation that depends on a current API, security default, deprecation, platform capability, or provider behavior, verify the current official source rather than treating this repository as the final authority.
