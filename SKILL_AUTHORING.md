# Skill Authoring Guide

Use this guide to keep `code-skills` small, routable, evidence-driven, and maintainable.

## 1. Decide whether a new skill is justified

A new skill should satisfy all of these conditions:

1. It represents a recurring **work goal**, not merely a technology.
2. It has an activation threshold that differs from existing skills.
3. It has a workflow that materially differs from existing skills.
4. A user can reasonably ask for that work without also asking for another skill's primary job.
5. Keeping it separate reduces ambiguity or context rather than increasing routing complexity.

Decision tree:

```text
independent work goal?
   ├─ no  → reference / script / example
   └─ yes
        ↓
independent activation threshold?
   ├─ no  → extend an existing skill
   └─ yes
        ↓
meaningfully different workflow?
   ├─ no  → reference
   └─ yes → candidate skill
```

Frameworks such as FastAPI, SQLAlchemy, PostgreSQL, Redis, Docker, Wot Design Uni, and GitHub Actions normally belong in references.

## 2. Standard directory shape

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── topic.md
├── scripts/          # optional
└── evals/            # recommended
    └── routing.md
```

Do not create empty directories for symmetry.

## 3. `SKILL.md` responsibilities

Keep `SKILL.md` focused on decisions and execution, not encyclopedic framework documentation.

A strong skill answers:

```text
WHEN   → when should this skill activate?
WHAT   → what outcome does it own?
HOW    → what is the safest efficient workflow?
PROVE  → what evidence is required?
STOP   → when is the task complete?
ROUTE  → which adjacent skill owns nearby work?
```

Recommended sections:

```md
---
name: skill-name
description: >-
  What it does, when to use it, and an important non-trigger.
---

# Title

Mission statement.

## Activation Threshold
## Route Adjacent Work
## Workflow
## References
## Guardrails
## Handoff
## Completion Criteria
```

The exact headings may vary when the workflow reads better another way.

## 4. Activation thresholds

Descriptions and activation sections should distinguish similar intents.

Good:

```text
Use database-engineering when schema, index, query-plan, migration, integrity, backup, or database-level operational behavior is itself the task. Do not activate for a normal application feature merely because it persists data.
```

Weak:

```text
Use for database work.
```

Write at least a few non-trigger examples for routing-heavy skills.

## 5. Metadata budget and trigger quality

Codex initially sees Skill names, descriptions, and paths before it decides which full `SKILL.md` to load.
Treat description text as scarce routing metadata, not a mini-SKILL.

- Front-load the concrete job and user-language trigger terms.
- Include one important boundary or non-trigger.
- Put framework names in the description only when they materially improve routing.
- Keep details, workflow steps, and long exclusions in the body or references.
- This repository keeps each description at or below 420 characters and the combined description budget at or below 6000 characters, leaving headroom for names and paths.

Example:

```text
Build or modify browser-based frontend UI in React, Vue, Next.js, Vite, HTML/CSS, or similar web apps. Trigger for pages/components, screenshot implementation, CSS/layout/responsive fixes, accessibility, redesign, visual polish, or browser verification. Do not use for uni-app/native mobile.
```

Test description changes against `evals/routing.md`; do not compensate for weak metadata by making the Skill body larger.

## 6. Progressive disclosure

Keep stable workflow rules in `SKILL.md`. Move detail into references when it is:

- framework-specific;
- database/vendor-specific;
- only relevant to one branch of the workflow;
- detailed enough that loading it every time wastes context;
- likely to change more frequently than the core workflow.

A skill should say **when** to read a reference, not force every reference into every task.

## 7. Preserve repository architecture

Every implementation skill should prefer the current project's:

- language and runtime;
- package manager;
- framework;
- module boundaries;
- data access conventions;
- build/test commands;
- deployment model;
- supported platforms.

Do not use a preferred reference as permission to migrate a project.

## 8. Verification rules

Verification should widen only when the changed risk crosses another boundary:

```text
focused check
  ↓
affected integration / contract
  ↓
build / static checks
  ↓
runtime or end-to-end only when needed
```

Do not run a full suite by habit. Do not claim a command proved behavior it did not execute.

## 9. Safety and authorization

Skills must distinguish inspection from consequential action. Do not silently:

- install dependencies;
- run production migrations;
- write or repair production data;
- deploy or publish;
- rotate secrets;
- submit external forms;
- broaden permissions;
- delete data or artifacts.

When state-changing work is not authorized, produce the plan, patch, command, or SQL for review instead of implying execution occurred.

## 10. Routing evals

For a new lifecycle skill, add `evals/routing.md` with at least:

- five prompts that should trigger it;
- five prompts that should not;
- three conflict/routing prompts when adjacent skills overlap.

These examples are not a benchmark framework; they are a durable contract for future edits.

## 11. Reference freshness

Technology references should include authoritative source links and avoid hard-coding volatile information unless necessary.

Prefer:

1. official specification or documentation;
2. official maintained repository/template;
3. mature project source;
4. reputable engineering material.

For frequently changing facts such as provider pricing, current defaults, quotas, or security advisories, instruct the agent to verify current official documentation at task time.

## 12. Definition of done for a new skill

- [ ] Independent work goal and activation threshold.
- [ ] Clear non-goals and adjacent routing.
- [ ] Small coherent workflow.
- [ ] Risk-matched verification.
- [ ] Completion/stop condition.
- [ ] `agents/openai.yaml` uses the correct `$skill-name`.
- [ ] References are loaded only when relevant.
- [ ] Routing examples cover trigger and non-trigger cases.
- [ ] `python scripts/validate_skills.py` passes.
- [ ] `README.md` skill map is updated.
- [ ] New upstream sources are recorded in `SOURCES.md`.
