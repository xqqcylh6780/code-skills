# Canonical and Delta Specifications

Read this reference when establishing current project specifications, proposing a behavioral change,
reconciling accepted behavior, synchronizing completion, or resolving conflicts between changes.

## Two Sources With Different Questions

| Source | Question answered | Lifecycle |
|---|---|---|
| Canonical specification | What behavior is effective now? | Long-lived and updated after accepted implementation |
| Change delta specification | What must be added, modified, removed, or renamed by this change? | Lives with one active/archived change |

Canonical specs are not a backlog. Delta specs are not current truth before successful
implementation and synchronization.

Default layout:

```text
.agents/
├── specs/
│   ├── export-permissions.md
│   └── account-lifecycle.md
└── changes/
    └── enforce-export-permissions/
        └── specs/
            └── export-permissions.md
```

If the repository already has OpenSpec or an equivalent current-spec store, use its schema and
location rather than creating `.agents/specs`.

## Canonical Specification Contract

Organize canonical files by stable capability, not implementation directory. Each requirement keeps
the same `R-###` identity used by active and archived changes.

```markdown
# Export permissions

## Context and Boundary

Current actors, entry points, owned state, and relevant trust boundaries.

## Requirements

### R-001: Export creation permission

The system SHALL require `export:create` before creating an export job.

#### SC-001-A: Authorized request

- Given ...
- When ...
- Then ...

#### SC-001-B: Unauthorized request

- Given ...
- When ...
- Then ...
- And no export job is created

## Compatibility and Operational Semantics

Only currently effective compatibility, migration, rollout, or operational rules.
```

Do not retain obsolete behavior in the normative requirements merely for history. History belongs in
archived changes and version control; the canonical spec may link to the relevant change when the
rationale remains useful.

## Delta Operations

A delta file uses one or more operation sections.

### `ADDED`

Introduce a new requirement with a new stable ID and all necessary scenarios. Confirm that the ID is
not already used in canonical or active specifications.

### `MODIFIED`

Restate the complete intended requirement and affected scenarios, not only the changed sentence.
Preserve the requirement ID. Explain the semantic difference and compatibility impact in the change
proposal or design.

### `REMOVED`

Name the existing requirement ID, state what behavior disappears, and document compatibility,
migration, cleanup, and consumer impact. Do not silently delete the canonical requirement before the
change is successfully delivered.

### `RENAMED`

Use only when identity and semantics remain the same but the capability or requirement name changes.
State old and new names. If behavior changes too, use `MODIFIED` as well.

Example:

```markdown
# Export permissions delta

## MODIFIED

### R-001: Export creation permission

The system SHALL require `export:create` before creating an export job.

#### SC-001-B: Unauthorized request

- Given an authenticated account without `export:create`
- When it requests an export
- Then the established authorization error is returned
- And no export job or audit-success event is created

## ADDED

### R-004: Denial audit event

The system SHALL emit the established denial audit event without sensitive request data.
```

## Baseline and Identity

Before writing a delta:

1. Read the relevant canonical capability.
2. Inspect active change manifests that touch the same capability, contract, data, or security
   boundary.
3. Record the implementation/canonical baseline in the proposal or manifest when concurrent work or
   later verification could otherwise make the comparison ambiguous.
4. Reuse existing requirement IDs for modifications/removals; allocate new IDs only for new
   obligations.

If no canonical spec exists for an already implemented capability, first capture only the verified
current behavior needed to define the delta. Do not attempt to document the entire project as an
unrequested prerequisite.

## Synchronization Procedure

Synchronize only after implementation and behavioral verification support the accepted delta:

1. Freeze the implementation state being verified.
2. Re-read the current canonical spec; detect changes since the delta baseline.
3. Apply each operation semantically:
   - add new requirements and scenarios;
   - replace modified requirements with their complete accepted form;
   - remove requirements only after compatibility and cleanup obligations pass;
   - rename without changing stable identity.
4. Resolve overlap with other active or recently completed changes. Never use last-writer-wins for
   conflicting behavior.
5. Review the resulting canonical file as a coherent current contract, not a concatenation of deltas.
6. Run focused behavioral/coherence verification if the merge reveals an interaction.
7. Set `canonicalSync.status` to `applied` and list the actual canonical files.
8. Run the validator before archival.

If synchronization cannot be completed safely, keep the change in `VERIFYING` or return it to
`ACTIVE`. Do not archive a successful terminal change with `canonicalSync.status: pending`.

## Conflict Resolution

An overlap in `touches` requires one of these explicit dispositions:

- **Order:** one change completes and synchronizes before the other rebases its delta.
- **Unify:** combine the changes when they represent one inseparable behavioral decision.
- **Partition:** establish non-overlapping requirement or boundary ownership and update manifests.
- **Coordinate:** keep both active but define a shared contract and integration verification.
- **Supersede:** one change replaces the other's intent; record the relationship before archival.

Filesystem separation alone is not a valid disposition.

## Deletion and Historical Integrity

- Never delete an accepted canonical requirement merely because an active delta proposes removal.
- Never rewrite archived delta specs to match later canonical behavior.
- Correct factual errors in an archive transparently or create a linked correction change.
- When a canonical spec is removed because the capability no longer exists, retain the terminal
  removal change and its evidence in the archive.

