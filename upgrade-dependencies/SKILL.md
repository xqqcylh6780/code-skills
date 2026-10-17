---
name: upgrade-dependencies
description: >-
  Assess or upgrade existing project dependencies and lockfiles with compatibility and migration
  evidence. Use for version bumps, peer/transitive conflicts, or upgrade plans; not routine
  installs, new features, or deployment.
---

# Upgrade Dependencies

Own the version transition: why it is needed, which packages must move together, which consumers
change, and what evidence demonstrates compatibility. Newer alone is not a sufficient reason.

Use `review-changes` for a general diff/PR review; this skill supplies upgrade-specific
compatibility checks when that review needs them. An unexplained post-upgrade failure starts
with `diagnose-bugs` rather than another version change.

## Select the outcome

- **Assessment/plan:** inspect manifests, locks, relevant source and primary release/migration
  notes. Report current/resolved/target versions, blockers, and proposed checks without editing
  files, installing packages, or querying private registries without authority.
- **Implementation:** update only the requested existing packages and the smallest necessary
  compatibility cohort. Inspect package-manager lifecycle hooks, generators, test setup, and
  registry configuration before executing the authorized commands. Reuse clear existing
  authorization; a new package/source, unrelated major upgrade, or toolchain migration needs its
  own scope decision.

Preserve the package manager, registry, runtime support, and unrelated local work. Dependency
resolution can download packages and execute build/install code; a lockfile-only label does not
establish that a command is side-effect-free. Workspace restrictions, including read-only
database access, apply to lifecycle hooks and verification. Do not install missing tools merely
to complete an assessment.

## Establish the actual graph

Inspect the owning workspace and effective declarations, resolved lockfile, runtime pins, parent
or BOM/constraint management, peer/transitive requirements, and relevant CI targets. Distinguish
declared ranges from installed/resolved versions and direct dependencies from managed/transitive
ones. A project can use several manifests but one shared lock or inherited version authority.

For stack-specific decisions, read the relevant section of
[stack-checks.md](references/stack-checks.md). Do not load every ecosystem reference by default.

Record the user-selected target and reason. If the request says latest, verify the compatible
release against the runtime and actual registry; do not substitute a different named target.
Use official releases, migration guides, advisories, and source to establish changes across the
versions crossed. An audit result is a lead, not authority for forced remediation or an unrelated
upgrade batch. State unavailable evidence rather than guessing compatibility.

## Plan the smallest coherent change

Identify required peer/framework/driver cohorts, changed APIs, configuration/build changes,
runtime requirements, and the affected consumer behavior. For a major migration, choose stages
that leave a usable verification boundary; do not upgrade all tooling at once to make resolution
easier. Keep new product features and optional cleanup outside the transition.

Establish the existing baseline with permitted focused checks before edits. Separate pre-existing
failures from upgrade effects. If execution is blocked, provide the version/migration patch or
plan and label the unproven behavior; do not claim an installed or tested upgrade.

## Update and verify

Change the authoritative declaration and use the project's inspected resolution path for its
lockfile. Review the actual diff: unexpected package churn, source/URL changes, peer overrides,
runtime/toolchain changes, and generated files need explanations. Do not hand-edit lockfile
integrities or delete the lockfile to suppress a resolver conflict. Do not use force/legacy-peer
options or broad overrides as a substitute for understanding incompatibility.

Make the minimal consumer/API/config changes required by the target version. Keep the relevant
implementation skill responsible for product behavior; consult `design-interfaces` only when an
observable contract changes. Unknown post-upgrade failures use `diagnose-bugs` before more bumps.

Run the baseline's focused checks, relevant type/build/contract checks, and an affected runtime
path when permitted and material. Resolution success alone does not prove source/runtime
compatibility. Broaden testing only for a distinct affected boundary or repository requirement.
Keep manifest, lock, and consumer changes reviewable as one cohort; do not start deployment,
commit, push, or configure automatic updates merely because verification passed.

## Handoff and stopping point

Report versions and rationale, affected cohort/consumers, migration changes, resolver/lockfile
effects, checks actually run, remaining blockers, and the reviewed reversion/forward path. Revert
only task-owned changes when asked; do not reset a dirty repository to undo an upgrade.

Assessment ends with an actionable compatibility conclusion or a precise evidence gap.
Implementation ends when the requested cohort and consumers agree and permitted checks support
the result, or when a concrete unresolved compatibility/permission boundary blocks continuation.
Do not silently lower the target or expand the cohort to force a passing outcome.
