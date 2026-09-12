# Manifest and Validation

Read this reference before creating or changing `change.json`, entering `READY` or a later lifecycle
state, diagnosing validator output, or integrating the validator with another tool.

## Why JSON

`change.json` stores machine-relevant identity, state, artifact indexes, touched boundaries, and gate
results. Markdown remains authoritative for human-readable requirements, decisions, tasks, and
evidence.

JSON is used instead of YAML so the bundled validator can run with the Python standard library and no
project dependency installation. Do not duplicate complete requirement text in the manifest.

## Manifest Contract

```json
{
  "schemaVersion": 1,
  "changeId": "enforce-export-permissions",
  "status": "ACTIVE",
  "stateHistory": ["PROPOSED", "READY", "ACTIVE"],
  "kind": "full",
  "artifacts": {
    "proposal": "proposal.md",
    "specs": ["specs/export-permissions.md"],
    "design": "design.md",
    "tasks": "tasks.md",
    "evidence": "evidence.md"
  },
  "touches": {
    "specs": ["export-permissions"],
    "contracts": ["POST /exports"],
    "data": ["export_jobs"],
    "security": ["export:create"]
  },
  "blockingDecisions": [],
  "acceptedGaps": [],
  "verification": {
    "implementationState": "commit:abc123"
  },
  "canonicalSync": {
    "status": "pending",
    "root": "specs",
    "files": []
  }
}
```

### Required fields

| Field | Contract |
|---|---|
| `schemaVersion` | Integer `1`; change only with a documented format migration |
| `changeId` | Lowercase hyphen-case; matches the active directory name |
| `status` | One lifecycle state defined by the skill |
| `stateHistory` | Ordered states beginning at `PROPOSED` and ending at the current `status` |
| `kind` | `compact` or `full` |
| `artifacts.proposal` | Relative path within the change directory |
| `artifacts.specs` | Array of relative delta-spec paths; may be empty for compact changes |
| `touches` | Object with `specs`, `contracts`, `data`, and `security` string arrays |
| `blockingDecisions` | IDs of decisions that prevent accepted progression |
| `acceptedGaps` | Gap IDs whose impact and acceptance are documented in evidence |

`design`, `tasks`, and `evidence` are present only when those artifacts exist. Do not declare future
placeholder files.

### Conditional fields

- `verification.implementationState` is required from `VERIFYING` through successful completion. Use
  a commit identity for immutable review or a precise working-tree description when commits are not
  available.
- `canonicalSync` is required for successful terminal changes that contain delta specs.
- `canonicalSync.status` is `pending`, `applied`, or `not-required`. A successful terminal change with
  deltas must be `applied`.
- `canonicalSync.root` defaults to `specs`, resolved from the workspace containing `changes/`.
- `canonicalSync.files` lists canonical paths actually reconciled.
- `supersededBy` is required for `SUPERSEDED`.
- `terminalReason` is required for `ABANDONED`.

Archived directories may be named `YYYY-MM-DD-<change-id>` while preserving the original
`changeId` in the manifest.

Append to `stateHistory` only when the lifecycle state actually changes. The validator rejects
illegal jumps and a history whose final state disagrees with `status`. Git remains the source for
timestamps and authorship; do not add noisy repeated state entries merely because another manifest
field changed.

## Touched-Boundary Vocabulary

Choose stable identifiers rather than source filenames:

- `specs`: canonical capability names, such as `export-permissions`.
- `contracts`: method plus API path, event name, CLI surface, configuration key family, or library
  contract.
- `data`: logical table, collection, durable record, ownership boundary, or migration domain.
- `security`: permission, trust boundary, tenant boundary, secret class, or privileged effect.

Normalize spelling within a repository. Two active manifests touching the same normalized identifier
produce a conflict warning; `--strict-conflicts` turns it into an error. An overlap does not prove the
changes are incompatible, but it must be explicitly coordinated before unsafe parallel execution.

## Validator Usage

The validator is located in the skill directory:

```text
python <skill-dir>/scripts/validate_change.py <change-directory>
python <skill-dir>/scripts/validate_change.py <change-directory> --strict-conflicts
python <skill-dir>/scripts/validate_change.py <change-directory> --json
```

On Windows, use UTF-8 mode when the active Python defaults to a legacy locale:

```text
py -3 -X utf8 <skill-dir>/scripts/validate_change.py <change-directory>
```

The script is read-only. It reads the selected change, declared artifacts, canonical files named by
the manifest, and sibling manifests for conflict detection. It does not create, synchronize, move,
or archive files.

Exit codes:

- `0`: no errors; warnings may remain.
- `1`: one or more validation errors.
- `2`: command-line usage error produced by the argument parser.

Structured JSON contains `valid`, error/warning counts, and issue objects with `severity`, `code`, and
`message`.

## Enforced Invariants

The validator checks:

- Manifest encoding, JSON shape, schema version, change ID, kind, and lifecycle status.
- Lifecycle history begins at `PROPOSED`, ends at the current state, and contains only allowed
  transitions.
- Artifact paths stay within the change directory and declared files exist as UTF-8.
- Full changes contain delta specs and delta-operation headings.
- Requirement, scenario, task, and evidence declaration IDs are unique.
- Scenario IDs have a matching parent requirement.
- READY-or-later full changes contain tasks and task coverage mappings.
- Task mappings do not reference undeclared requirements or scenarios.
- Successful terminal changes contain no incomplete task.
- VERIFYING-or-later changes declare an implementation state and evidence artifact.
- Evidence status agrees with the terminal lifecycle state.
- Every accepted requirement and scenario appears in the traceability section.
- Every completed task appears in terminal traceability and every terminal trace row reports `Pass`.
- Traceability does not cite undeclared task or evidence IDs.
- Successful changes with deltas record applied canonical synchronization and existing canonical
  files.
- Other active manifests with overlapping touched boundaries are reported.

The validator cannot prove whether requirement wording is correct, tests exercised the real boundary,
the implementation matches the specification, or a canonical merge preserved semantic intent. Those
remain behavioral and coherence-review obligations.

## When to Run It

Run after a relevant manifest or artifact change and specifically:

1. Before changing `PROPOSED` to `READY`.
2. After task/spec reconciliation that affects IDs or mappings.
3. Before accepting a `VERIFYING` result as successful.
4. After canonical specs are synchronized.
5. After archival, to confirm archive naming and canonical paths still validate.

Do not rerun it when neither inputs nor environment changed merely to obtain another identical log.

## Error Handling

Resolve errors at their authoritative source:

- Manifest/path error: fix `change.json` or the declared layout.
- Duplicate or missing ID: fix the requirement/task/evidence declaration, preserving accepted IDs.
- Coverage error: add a real execution/evidence path or explicitly change accepted scope.
- Evidence-state error: perform or correct verification; do not edit the status just to pass.
- Canonical-sync error: reconcile the delta, verify semantics, then record the applied files.
- Active conflict: coordinate changes and record ordering/ownership; use strict mode when unresolved
  overlap must prevent progression.

Never suppress a validator error by deleting an accepted requirement, marking an unfinished task
complete, or recording evidence that was not observed.
