# code-skills

Agent-oriented software engineering skills for Codex and compatible coding agents.

This repository is not a prompt collection. Each skill represents a distinct engineering job with an activation threshold, a bounded workflow, evidence requirements, adjacent-skill routing, and a clear stopping condition. Detailed framework or vendor knowledge lives in references so an agent can load only the context needed for the current task.

## Design goals

- **Route before acting.** Pick the smallest skill that matches the actual work.
- **Preserve project conventions.** Do not migrate frameworks or add infrastructure without a concrete requirement.
- **Use progressive disclosure.** Keep `SKILL.md` focused; load references only when the task crosses that topic.
- **Prefer vertical slices.** Prove one observable outcome end to end before multiplying abstractions.
- **Match verification to risk.** Run the narrowest evidence-producing check that proves the changed boundary.
- **Stop when the requested outcome is proven.** Do not turn small changes into repository-wide cleanups.

## Install for Codex discovery

The skill folders at this repository's root are **source folders**. Codex local discovery scans `.agents/skills`
locations, so cloning this repository alone does not make the root folders globally available as Skills.

Install all skills for the current user:

```bash
python scripts/install_codex_skills.py --scope user
```

On Windows this installs to:

```text
C:\Users\<you>\.agents\skills\
```

Install only the skills you actually want available everywhere (recommended when keeping the initial Skill list
small):

```bash
python scripts/install_codex_skills.py --scope user --skills build-frontends build-mobile-apps build-backends diagnose-bugs review-changes
```

Install into one project instead of globally:

```bash
python scripts/install_codex_skills.py --scope project --project "D:\path\to\project"
```

Use `--force` to replace an older installed copy after reviewing local modifications. After installation, run
`/skills` in Codex CLI/IDE or type `$` and confirm `build-frontends` is listed. If an update is not visible, restart
Codex.

For routing:

```text
React / Vue / Next.js / Vite / HTML-CSS browser UI -> build-frontends
uni-app / HBuilderX / App / mini program / device APIs -> build-mobile-apps
```

## Skill map

### Planning and contracts

| Skill | Use it for |
| --- | --- |
| [`shape-project`](shape-project/SKILL.md) | Turn ambiguous ideas or large changes into an execution-ready brief and first vertical slice. |
| [`design-interfaces`](design-interfaces/SKILL.md) | Design or evolve public/shared HTTP, GraphQL, event, job, module, configuration, or adapter contracts. |

### Implementation

| Skill | Use it for |
| --- | --- |
| [`build-frontends`](build-frontends/SKILL.md) | Build, fix, polish, and proportionately verify React/Vue/Next/Vite and other browser-based web interfaces. |
| [`build-mobile-apps`](build-mobile-apps/SKILL.md) | Build cross-platform/mobile application surfaces, initially focused on uni-app/Vue 3. |
| [`build-backends`](build-backends/SKILL.md) | Implement server-side product behavior, services, jobs, integrations, persistence, retries, caching, and observability. |
| [`database-engineering`](database-engineering/SKILL.md) | Design, change, diagnose, or operate relational database structures and query behavior when the database itself is the task. |

### Safety and verification

| Skill | Use it for |
| --- | --- |
| [`secure-boundaries`](secure-boundaries/SKILL.md) | Threat-model and harden authentication, authorization, secrets, sensitive data, uploads, payments, webhooks, and other trust boundaries. |
| [`test-behavior-first`](test-behavior-first/SKILL.md) | Use a witnessed red-green-refactor loop for high-value behavior or requested TDD. |
| [`playwright`](playwright/SKILL.md) | Automate and verify real browser workflows with Playwright. |

### Investigation and maintenance

| Skill | Use it for |
| --- | --- |
| [`diagnose-bugs`](diagnose-bugs/SKILL.md) | Reproduce, isolate, explain, and repair failures with an unknown or disputed causal chain. |
| [`refactor-code`](refactor-code/SKILL.md) | Improve internal structure while preserving observable behavior. |
| [`performance-engineering`](performance-engineering/SKILL.md) | Measure, profile, benchmark, optimize, and capacity-test performance. |
| [`review-changes`](review-changes/SKILL.md) | Review diffs, commits, branches, or PRs for concrete correctness and risk issues. |

### Delivery and operations

| Skill | Use it for |
| --- | --- |
| [`deploy-and-operate`](deploy-and-operate/SKILL.md) | Prepare, release, verify, observe, roll back, and recover software safely. |

### Tools and domain skills

| Skill | Use it for |
| --- | --- |
| [`github-repository-search`](github-repository-search/SKILL.md) | Find and compare GitHub repositories using current evidence. |
| [`pixel-art-maker`](pixel-art-maker/SKILL.md) | Create and verify pixel-art game assets and Aseprite-oriented workflows. |

## Typical routing

```text
ambiguous requirement
        ↓
  shape-project
        ↓
public/shared contract changes?
        ├─ yes → design-interfaces
        ↓
implementation boundary
        ├─ web UI      → build-frontends
        ├─ mobile/app  → build-mobile-apps
        ├─ server      → build-backends
        └─ database    → database-engineering
        ↓
trust boundary? → secure-boundaries
        ↓
high-value test seam? → test-behavior-first
        ↓
unknown failure? → diagnose-bugs
        ↓
behavior-preserving cleanup? → refactor-code
        ↓
performance goal? → performance-engineering
        ↓
review-changes
        ↓
deploy-and-operate
```

Routing is not a mandatory ceremony. A small CSS fix may use only `build-frontends`; an unexplained production failure may begin directly with `diagnose-bugs`. Load only what materially changes the work.

## Skill vs reference

Create a **new skill** when the capability is a recurring, independent work type with its own activation threshold and workflow.

Add a **reference** when the capability is a framework, provider, library, platform, or implementation variant inside an existing work type.

Examples:

```text
Database engineering        → skill
Deployment and operations   → skill
Refactoring                 → skill

FastAPI                     → build-backends reference
SQLAlchemy                  → build-backends / database reference
PostgreSQL                  → database reference
Wot Design Uni              → build-mobile-apps reference
Docker                      → deploy-and-operate reference
```

Avoid creating fragmented skills such as `fastapi-skill`, `jwt-skill`, `redis-skill`, or `docker-skill` unless they later become genuinely independent work types.

## Repository structure

A normal skill looks like:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── ...
└── evals/                  # recommended for routing-heavy skills
    └── routing.md
```

Scripts belong in a skill only when repeated automation is materially safer or more reliable than instructions alone.

## Authoring and contributing

- Read [`SKILL_AUTHORING.md`](SKILL_AUTHORING.md) before adding or splitting a skill.
- Record upstream material and licenses in [`SOURCES.md`](SOURCES.md).
- Follow [`CONTRIBUTING.md`](CONTRIBUTING.md) for validation and routing expectations.
- See [`CHANGELOG.md`](CHANGELOG.md) for repository-level changes.

## Validate the repository

The validator uses only the Python standard library:

```bash
python scripts/validate_skills.py
```

It checks skill frontmatter, directory/name alignment, `agents/openai.yaml`, local Markdown references, and README registration.

GitHub Actions runs the same validation on pushes and pull requests.

## Source and license notes

This repository contains locally authored skills plus explicitly attributed third-party material. Third-party components retain their own license and notice files. See [`SOURCES.md`](SOURCES.md) for provenance. The repository as a whole does not declare a new license here; add one only after the repository owner chooses the intended licensing policy.

## Primary Backend Stacks

`build-backends` remains framework-independent, but the first-class backend references are optimized for
the stacks currently used by this repository's owner:

```text
Python
├── FastAPI
├── Pydantic
├── SQLAlchemy
└── Alembic

Java
├── Spring Boot
├── Spring Security
├── Jakarta Persistence / Hibernate / Spring Data JPA
├── MyBatis
├── Flyway / Liquibase
├── Maven / Gradle
└── JUnit / Testcontainers
```

Rule: **detect first, preserve the existing stack, then load only relevant references**.
Do not drift Python into Java or Java into Python unless the user explicitly requests a migration.
