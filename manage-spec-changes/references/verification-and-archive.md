# Verification and Archive

Read this reference before claiming lifecycle completion, accepting residual gaps, or archiving a
change.

## Verification Inputs

Establish the exact subject before testing:

- Change ID, manifest status/history, and accepted proposal scope.
- Current specification and stable requirement/scenario IDs.
- Relevant canonical baseline, delta operations, and overlapping active manifests.
- Implementation identity: commit/range when immutable, otherwise precise working-tree scope and
  relevant current diff.
- Environment, configuration class, feature flags, test data assumptions, and external dependencies
  that affect behavior.
- Applicable repository instructions and known limitations of the available verification tools.

If implementation changes after a check, determine which evidence is stale before reusing it.

## Three Verification Axes

### 1. Completeness

Prove every accepted obligation has a disposition:

- Each `R-###` and `SC-###` maps to one or more tasks and evidence entries.
- Every in-scope task is complete, explicitly deferred, removed by an accepted requirement change, or
  blocked with impact stated.
- Conditional obligations—migration, compatibility window, rollout, rollback, cleanup, docs,
  observability, accessibility, security review, and manual validation—are accounted for when
  applicable.
- No accepted scenario depends on an unimplemented placeholder, unverified mock, or follow-up hidden
  outside the change record.
- Explicit non-goals remain excluded and were not accidentally introduced.

Completeness is a coverage property. It does not prove that the implementation is right.

### 2. Correctness

For each requirement, choose evidence proportional to its failure risk:

- Focused automated tests for primary and negative behavior.
- Type checking, compilation, linting, or static analysis when they test a relevant invariant.
- Integration or contract tests for real boundaries and serialization semantics.
- Migration dry-run, compatibility checks, query-plan evidence, or rollback rehearsal when authorized
  and safely available.
- Browser/device/manual observation for interaction, accessibility, visual, platform, or operational
  behavior that lower-level tests cannot establish.
- Security-specific validation for authorization, tenant isolation, secrets, untrusted input, and
  privileged effects.
- Performance measurements against an explicit workload and threshold, not intuition.

Inspect script and command entry points for side effects before execution. Do not run migrations,
deployments, database writes, or other unauthorized effects under the label of verification.

For each check record expected and observed behavior. Treat these as insufficient on their own:

- A checkmark without evidence.
- Code review without exercising a behavior that needs runtime proof.
- “All tests pass” without identifying whether the accepted scenarios are covered.
- A mocked test when correctness depends on the real boundary being mocked.
- A screenshot without the state and interaction needed to interpret it.
- A manual claim without reproducible steps or an identified observer/environment.

### 3. Coherence

Read across artifacts and implementation to find contradictions:

- Proposal scope versus detailed requirements.
- Requirement wording versus scenarios and failure behavior.
- Design decisions versus implemented ownership, flow, interfaces, and state transitions.
- Task mappings versus actual changed files and behavior.
- Tests versus specified outcomes rather than internal implementation details alone.
- Rollout, compatibility, migration, rollback, and cleanup claims versus actual configuration and
  operational artifacts.
- User documentation or UI behavior versus the accepted contract.
- Accepted delta specs versus the resulting canonical current specification.

Resolve contradictions at their authoritative source, then invalidate or rerun downstream evidence.
Do not simply edit the evidence table to match whatever the code currently does.

## Traceability Review

Build or audit the matrix in `evidence.md`:

| Requirement / scenario | Planned task | Implementation | Evidence | Result |
|---|---|---|---|---|
| R-001 / SC-001-A | T-001 | symbol/path/contract | V-001 | Pass |
| R-001 / SC-001-B | T-002 | denial path | V-002 | Pass |

Review both directions:

- **Forward:** every accepted requirement reaches implementation and credible evidence.
- **Backward:** every material implementation change maps to accepted scope, enabling work, or an
  explicitly approved adjustment.

Backward tracing catches scope creep, undocumented compatibility changes, and unrelated refactors
that forward-only coverage misses.

## Verification Result Semantics

Use one result:

- `PASS`: all applicable completion gates pass, with no unaccepted material gap.
- `PASS WITH ACCEPTED GAPS`: remaining gaps are explicit, impact-assessed, and accepted by the user or
  designated authority.
- `FAIL`: evidence contradicts one or more accepted requirements or reveals a material regression.
- `BLOCKED`: required evidence cannot currently be obtained; state the missing capability, why
  alternatives are insufficient, and the exact next action.

Do not convert `BLOCKED` into `PASS WITH ACCEPTED GAPS` without explicit acceptance of the uncertainty
and its impact.

## Completion Gate

Before setting the proposal to a completion state, confirm:

### Contract

- Final delivered scope, excluded scope, and deferred work are explicit.
- Requirement and scenario IDs are stable and have dispositions.
- Accepted changes discovered during implementation were reconciled upstream.

### Implementation

- The intended implementation state is identifiable.
- No known required placeholder, temporary bypass, unsafe fallback, or incomplete cleanup remains
  undisclosed.
- Public contract, data, security, migration, operational, and compatibility changes match the
  accepted design where applicable.

### Evidence

- Completeness, correctness, and coherence reviews were all performed.
- Relevant automated and manual checks include actual observations.
- Failures and unrelated pre-existing failures are distinguished.
- Stale evidence was rerun or explicitly excluded.
- The machine validator passes for the verified manifest and artifact set.

### Residual state

- Risks and gaps have impact, disposition, and follow-up ownership.
- Repository task state contains no stale “next action” for completed work.
- External actions not performed by Codex are not represented as completed.
- Delta specifications have been semantically synchronized into canonical current specs, or the
  manifest credibly records that synchronization is not required.

If a gate fails, return to `ACTIVE`, remain `VERIFYING`, or record a terminal non-completion status.

## Accepted Gaps

A gap may be accepted only when the record says:

```text
Gap:
Affected requirement/scenario:
Why it remains:
User/system impact:
Risk and likelihood:
Available mitigation:
Follow-up owner or condition:
Acceptance source:
```

Lack of time, unavailable environment, flaky infrastructure, or a pre-existing failure explains a
gap but does not automatically make it acceptable.

## Archive Procedure

Follow an established repository archive convention when one exists. Otherwise:

1. Freeze the verification subject and finish `evidence.md`.
2. For successful changes, apply each accepted delta to canonical specs, review the resulting current
   contract, and record `canonicalSync.status` and files in `change.json`.
3. Run the bundled change validator. Resolve structural, traceability, canonical-sync, and applicable
   active-conflict errors before claiming completion.
4. Append the valid terminal transition to `change.json`; record the narrative final outcome and any
   accepted gaps in proposal/evidence without introducing a second machine-status field.
5. Confirm task state no longer claims unfinished work for the change, or update it to the next
   unrelated objective according to repository memory rules.
6. Move the entire directory to `.agents/changes/archive/YYYY-MM-DD-<change-id>/`, preserving artifact
   names, IDs, and history. Resolve name collisions explicitly; do not overwrite an archive.
7. Re-run the validator against the archived location so archive naming and canonical-root resolution
   remain valid.
8. Recheck links from active documentation or task state and update only links broken by the move.
9. Report the terminal outcome, delivered scope, verification result, accepted gaps, and archive
   location.

Archival is a material filesystem change. Perform it only when the user's requested workflow includes
completion/archival or the user explicitly asks for it. Otherwise report that the change is ready to
archive and leave it in place.

## Reopening an Archived Change

Prefer a new change ID linked to the archived record when new requirements or implementation work are
substantial. Reopen the same change only to correct its record or finish explicitly deferred work
whose original identity remains accurate.

When reopening:

- Preserve the prior terminal outcome and verification evidence.
- Record why reopening is necessary and what earlier evidence becomes stale.
- Move or copy according to established repository convention without overwriting another active
  change.
- Return to the earliest lifecycle state required by the new decision, not automatically `ACTIVE`.

## Final Report

Lead with the actual outcome:

```text
Change: <id>
Status: COMPLETED | COMPLETED WITH ACCEPTED GAPS | FAIL | BLOCKED | SUPERSEDED | ABANDONED
Delivered: <observable scope>
Verification: <key checks and results>
Traceability: <coverage summary>
Accepted gaps / residual risks: <none or explicit list>
Artifacts: <active or archive location>
```

Mention commands only to the level needed for reproducibility. Do not bury a failed requirement or
blocked check beneath a general statement that most tests passed.
