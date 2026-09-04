# Java Backend

Use this reference only when the repository is already Java/JVM or the user explicitly chooses Java.
Do not replace an established Python or other backend with Java merely because this reference exists.

## Detect the local Java stack first

Inspect:

- `pom.xml`, `mvnw`, `.mvn/` for Maven.
- `build.gradle`, `build.gradle.kts`, `gradlew`, `gradle/` for Gradle.
- Java version and toolchain configuration.
- Spring Boot, Jakarta EE, Quarkus, Micronaut, Vert.x, plain Servlet/JAX-RS, or another framework.
- Persistence: Spring Data JPA, Hibernate/Jakarta Persistence, MyBatis, jOOQ, JDBC, or another adapter.
- Database migration tooling: Flyway, Liquibase, or repository-specific scripts.
- Test tooling: JUnit, Mockito, AssertJ, Testcontainers, Spring test support, or repository-specific harnesses.

Preserve the repository's existing framework, build tool, Java baseline, module layout, and persistence style.

## Layering

Typical Spring-style code may use controller -> application/service -> domain -> repository/adapter, but do not
force that shape onto an established codebase. Keep these concerns explicit:

- Transport/controller: request parsing, validation, authentication context, response/error mapping.
- Application/service: use-case orchestration and transaction ownership where the existing architecture places it.
- Domain: business invariants and state transitions without servlet/JPA leakage where practical.
- Persistence/integration: JPA/MyBatis/JDBC/client-specific details behind the repository's established boundary.

Avoid letting entities, persistence sessions, HTTP request objects, or third-party SDK payloads become the
universal domain model by convenience.

## Runtime and concurrency

- Understand whether the application is thread-per-request, virtual-thread based, reactive, message-driven, or mixed.
- Do not introduce Reactor, virtual threads, or async executors as an incidental optimization.
- Bound executor queues and remote fan-out.
- Propagate cancellation/timeouts where the chosen stack supports them.
- Do not keep database transactions open across remote calls.
- Treat scheduled jobs and message handlers as replayable unless stronger delivery guarantees are proven.

## Load narrower references only when relevant

- Spring Boot: [spring-boot.md](spring-boot.md)
- Spring Security: [spring-security.md](spring-security.md)
- Jakarta Persistence / Hibernate / Spring Data JPA: [jpa-hibernate.md](jpa-hibernate.md)
- MyBatis: [mybatis.md](mybatis.md)
- Flyway / Liquibase: [flyway-liquibase.md](flyway-liquibase.md)
- Maven / Gradle: [maven-gradle.md](maven-gradle.md)
- JUnit / Testcontainers: [junit-testcontainers.md](junit-testcontainers.md)

Do not load all Java references for every Java task. Follow the actual repository.
