---
name: deploy-and-operate
description: >-
  Build, release, deploy, verify, observe, roll back, or recover software in a target runtime.
  Trigger for Docker, CI/CD, configuration/secrets, migration rollout, health/readiness, smoke
  tests, release safety, rollback, incident recovery, or production operations. Do not use for
  ordinary feature implementation.
---

# Deploy and Operate

Treat delivery as a controlled transition between known states. Make artifact identity, configuration, data compatibility, health evidence, observability, and recovery explicit before changing a live environment.

## Activation Threshold

Use this skill when the requested deliverable is a release artifact, deployment configuration,
rollout, target-runtime operation, rollback, recovery, or a plan for that transition. Do not activate
it solely because a feature task runs a local build, focused test, or already-authorized runtime
check; those checks remain with the owning implementation skill unless they expose a delivery issue
that is itself in scope.

Do not deploy merely because code is ready. Use `diagnose-bugs` first for an incident whose cause is unknown. Use `database-engineering` for database-specific design/migration mechanics and `secure-boundaries` for secrets, privileges, or sensitive deployment boundaries.

## Route Adjacent Work

- Feature implementation → `build-frontends`, `build-mobile-apps`, or `build-backends`.
- Public compatibility decisions → `design-interfaces`.
- Database migration design, lock risk, backfill, restore → `database-engineering`.
- Unknown production failure → `diagnose-bugs`.
- Secrets, service identities, privileged deploy actions → `secure-boundaries`.
- Pre-merge risk review → `review-changes`.

## Workflow

### 1. Recover the delivery model

Inspect deployment docs, container/build definitions, package scripts, CI/CD workflows, infrastructure configuration, environment variables, migrations, health endpoints, monitoring, and previous release conventions.

Record:

```text
Target environment:
Artifact/build identity:
Deployment unit:
Configuration/secrets source:
Database/schema dependency:
Traffic/rollout model:
Health/readiness evidence:
Observability signals:
Rollback/roll-forward path:
Authorized actions:
```

Do not replace an established deployment system with Docker, Kubernetes, a cloud service, or another CI provider merely because a reference uses it.

### 2. Establish release invariants

Before rollout, make explicit what must remain true:

- artifact is reproducible/identified and corresponds to the reviewed source;
- required configuration exists without exposing secrets;
- new code is compatible with the database and external contracts during overlap;
- startup/readiness does not accept traffic before required dependencies are usable;
- rollback remains possible or a forward recovery path is defined;
- logs/metrics/traces can distinguish the new release and surface terminal failure.

Read [references/release-and-rollout.md](references/release-and-rollout.md) for sequencing and migration compatibility.

### 3. Build and configure deliberately

Use the repository's existing build path. Separate build-time inputs from runtime configuration and keep secrets out of images, source, logs, and command history where possible.

For containerized systems, read [references/containers-and-config.md](references/containers-and-config.md). Do not treat a successful image build as evidence that the service can start, become ready, reach dependencies, or handle a real request.

### 4. Verify pre-release gates

Run only the checks required by repository policy and changed risk:

1. focused tests/static checks;
2. build/package artifact checks;
3. migration compatibility or schema checks;
4. configuration completeness checks without printing secrets;
5. staging/sandbox verification when the production wiring cannot be proven from source.

If a step has side effects, verify user authorization before execution.

### 5. Roll out in observable stages

Prefer a rollout that lets failures be detected before full exposure. Depending on the existing platform this may be a single-instance replace, rolling update, canary, blue/green, or staged manual release.

For each stage define:

```text
what changes:
who/what receives traffic:
health gate:
error/latency/saturation signals:
observation window or evidence:
stop condition:
rollback/forward action:
```

Do not invent arbitrary time windows; use project policy or evidence appropriate to the failure mode.

### 6. Verify runtime behavior

Check more than process liveness:

- startup and readiness;
- representative smoke path;
- dependency connectivity and configuration;
- error rate and latency for affected paths;
- queue/job health where relevant;
- migration/backfill progress;
- logs/metrics/traces for new terminal failures or saturation.

Read [references/observability-and-recovery.md](references/observability-and-recovery.md).

### 7. Roll back or recover based on compatibility

Before rollback, verify that data/schema changes still permit the previous version to run. A code rollback can be unsafe after an irreversible schema or data transition.

Choose one explicitly:

```text
rollback code/config
roll forward with a corrective release
restore/reconcile data
pause traffic/workers
feature-disable the affected path
```

Coordinate database recovery with `database-engineering` and security-sensitive recovery with `secure-boundaries`.

### 8. Keep CI/CD minimal and auditable

When creating or changing pipeline automation, read [references/ci-cd.md](references/ci-cd.md). Prefer repository-owned scripts and immutable/pinned dependencies where practical. Keep build/test evidence separate from deployment authorization, and protect production environments with the controls the hosting platform supports.

## Handoff

Report the artifact/release identity, target, rollout state, checks actually run, runtime evidence, migrations/configuration that matter, and the remaining rollback or recovery path. Never present a prepared command as an executed deployment.

## Completion Criteria

Delivery is complete only when the requested target state is reached or a concrete deployment plan is delivered, the relevant health and behavior are verified with actual evidence, configuration/data compatibility is understood, and rollback or recovery remains explicit. Stop immediately on an unexplained material failure and route to `diagnose-bugs` rather than stacking deployment guesses.
