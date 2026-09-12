# Lifecycle and Reconciliation

Read this reference when starting, resuming, fast-forwarding, implementing, or changing the accepted
direction of a durable change.

## Lifecycle States

| State | Meaning | Entry gate | Permitted next states |
|---|---|---|---|
| `PROPOSED` | Intent and candidate scope are reviewable | Problem, outcome, scope, assumptions, and material questions are visible | `READY`, `ABANDONED`, `SUPERSEDED` |
| `READY` | Implementation can start safely | Requirements accepted; blocking decisions resolved; verification strategy credible | `ACTIVE`, `PROPOSED`, `ABANDONED`, `SUPERSEDED` |
| `ACTIVE` | Authorized implementation or implementation preparation is underway | User authorized the work; executable next slice exists | `VERIFYING`, `READY`, `PROPOSED`, `ABANDONED`, `SUPERSEDED` |
| `VERIFYING` | Claimed implementation scope is frozen enough to assess | Implementation scope and revision/working-tree identity are known | `ACTIVE`, `READY`, `PROPOSED`, `COMPLETED`, `COMPLETED WITH ACCEPTED GAPS`, `ABANDONED`, `SUPERSEDED` |
| `COMPLETED` | All accepted obligations passed the completion gate | Complete, correct, coherent evidence with no unaccepted gap | archival only |
| `COMPLETED WITH ACCEPTED GAPS` | User accepted explicit residual gaps | Each gap and impact is documented and accepted | archival or reopened `ACTIVE` |
| `SUPERSEDED` | Another named change replaces this direction | Replacement identity and relationship are recorded | archival only |
| `ABANDONED` | Work intentionally stopped without claiming delivery | Reason, partial effects, and cleanup status are recorded | archival or explicit reopen |

State is not inferred from elapsed time, task checkmarks, or a confident summary. Update the change
manifest only after its entry gate is satisfied, and append every actual transition to
`stateHistory`. Keep narrative outcome and rationale in proposal/evidence without duplicating the
machine-status field.

## New Change Procedure

1. **Establish identity.** Confirm repository root, search active and archived changes for matching
   intent, choose a stable outcome-oriented ID, and create `change.json`.
2. **Calibrate depth.** Decide between compact and full artifacts using uncertainty, blast radius,
   coordination duration, and verification burden.
3. **Inspect evidence.** Read the smallest sufficient repository sources, current instructions,
   relevant task/project memory, existing contracts, and prior decisions.
4. **Draft proposal.** Separate confirmed facts, assumptions, accepted decisions, open questions, and
   excluded scope.
5. **Specify behavior.** Read the relevant canonical specs and express accepted changes as delta
   operations with stable IDs. Resolve contradictions before `READY`.
6. **Design conditionally.** Capture only consequential choices and their relationship to requirements.
7. **Plan executable slices.** Identify dependencies, exit conditions, rollback or recovery, and
   focused verification.
8. **Run the readiness gate.** Populate touched boundaries, check active-change overlaps, run the
   validator, and set `READY` only when the first authorized slice can begin without an unanswered
   material decision.

If the user requested implementation rather than a planning deliverable, do not stop after producing
documents. Continue once the readiness gate passes and authority is clear.

## Readiness Gate

A change is `READY` when all applicable answers are concrete:

- What observed problem or desired capability motivates it?
- Which adopted project principles or governance rules constrain it, and is any exception required?
- Which behavior is required, optional, and explicitly excluded?
- Which assumptions remain, and are they safe for the next slice?
- What current repository evidence supports the proposed boundaries?
- Which public contract, data, security, migration, operational, and compatibility obligations apply?
- Which approach was chosen, and why does it fit better than meaningful alternatives?
- What is the first observable slice, its dependency set, exit condition, and recovery posture?
- How will each material requirement be verified?
- Which outcome-level success criteria add information beyond the acceptance scenarios, and how can
  they be assessed without assuming a particular implementation?
- Which canonical capabilities and active changes overlap this work, and how is the overlap resolved?
- Which decisions are deferred, who or what will resolve them, and why do they not block the next
  action?

Use `READY WITH DECISIONS` in `tasks.md` only when unaffected slices can safely proceed. Keep the
proposal `PROPOSED` if the unresolved decision changes the overall accepted contract.

## Resume Procedure

Resume from state rather than replaying all artifacts:

1. Confirm the intended repository and active change ID.
2. Read `.agents/TASK_STATE.md` when applicable and treat it as navigation, not evidence.
3. Read `proposal.md`, then the artifact named by the exact next action.
4. Inspect current version-control status and the affected files before assuming prior work remains
   unchanged. Preserve unrelated user changes.
5. Recheck volatile external facts only when they matter to the next action.
6. Compare recorded state with actual artifacts and implementation. If they conflict, reconcile
   before continuing.
7. Run structural validation when manifest state, IDs, mappings, or canonical synchronization may no
   longer be trustworthy.
8. Announce the current outcome, blocker, and next action without repeating the entire history.

Do not reopen settled discovery or re-run unchanged checks without a concrete reason.

## Fast-forward Procedure

Fast-forward is appropriate when the intent is clear and the user wants implementation-ready
artifacts without separate approval pauses.

- Draft proposal first so later artifacts share the same identity and scope.
- Write requirements and scenarios before decomposing tasks.
- Decide whether design is necessary based on actual boundaries and tradeoffs.
- Build task slices from accepted scenarios and design dependencies.
- Cross-check IDs and readiness after all artifacts exist.
- Do not invent decisions to preserve momentum. Pause only on a decision that materially changes the
  accepted result, risk, cost, or irreversibility.

Fast-forward does not imply authorization to apply the change.

## Apply Procedure

During authorized implementation:

1. Select the next unblocked vertical slice.
2. Confirm its covered requirements, current design constraints, and expected verification.
3. Use relevant specialist skills and inspect exact runtime/test entry points before executing them.
4. Implement the smallest coherent slice while preserving unrelated work.
5. Run focused verification and capture the observed result.
6. Reconcile any discovered change before declaring the task complete.
7. Update task status and current repository task state.

A checked task means its described output exists and its verification has a recorded disposition. It
does not mean every mapped requirement is complete unless the traceability evidence proves that.

After the current task set has been implemented, use the convergence procedure in
[`principles-clarification-and-convergence.md`](principles-clarification-and-convergence.md). Genuine
implementation gaps become new traceable tasks; contradictions in intent are reconciled upstream.
Repeat apply and convergence until no accepted obligation is missing, then enter final verification.

## Reconciliation Triggers

Reconcile when any of these changes:

- Observable success, error, denial, retry, recovery, or side-effect behavior.
- Public/shared API, schema, event, CLI, configuration, or compatibility semantics.
- Data ownership, persistence, transaction, migration, retention, or cleanup behavior.
- Authentication, authorization, tenancy, secret handling, trust boundary, or untrusted-input flow.
- Required performance, accessibility, availability, observability, rollout, or rollback behavior.
- Accepted scope, non-goals, dependency ordering, or task exit condition.
- Verification method proves infeasible or fails to test the claimed invariant.

Ordinary private refactoring, renamed locals, or implementation detail changes do not require a spec
change unless they invalidate a recorded design decision or evidence pointer.

## Reconciliation Procedure

1. **Capture evidence.** State what the repository, test, integration, or constraint revealed.
2. **Classify impact.** Clarification, design adjustment, requirement change, or scope discovery.
3. **Find the earliest affected artifact.** Change the source decision rather than patching only its
   downstream symptoms.
4. **Assess blast radius.** Identify affected requirement/scenario IDs, design elements, tasks,
   implementation, tests, compatibility, migration, rollout, and evidence.
5. **Resolve authority.** Apply accepted clarifications and in-scope design corrections directly;
   request direction for material behavior/scope/risk changes outside accepted intent.
6. **Update downstream artifacts.** Preserve IDs where obligations remain the same, add new IDs for new
   obligations, and explicitly supersede removed behavior.
7. **Invalidate stale evidence.** Mark checks stale when the tested behavior or implementation identity
   changed.
8. **Update the manifest.** Refresh touched boundaries, blockers, artifacts, and verification identity;
   run validation when mappings or state changed.
9. **Resume from the earliest incomplete gate.** Do not pretend the change remained `READY` or
   `VERIFYING` if a new blocking decision exists.

Record consequential decisions in the proposal or design with the evidence and reason. Avoid a
chronological diary of trivial edits.

## Staleness Rules

An artifact is stale when a changed upstream decision could alter its conclusions:

| Change | Usually stale |
|---|---|
| Scope or desired outcome | Specs, design, tasks, evidence |
| Requirement/scenario semantics | Mapped design, tasks, implementation claims, evidence |
| Design boundary or contract | Dependent tasks and evidence; specs only if behavior changed |
| Task decomposition | Task mapping and execution state; requirements remain authoritative |
| Implementation after verification | Evidence touching the changed behavior |
| Test-only improvement with unchanged behavior | Evidence record, not necessarily design/tasks |

Do not erase stale evidence. Mark it superseded or rerun it against a newly identified implementation
state so the audit trail does not imply verification that never occurred.

## Concurrent Work and Handoffs

- Divide responsibility by artifact, slice, module, or verification surface with non-overlapping
  ownership when possible.
- One accepted requirement statement must have one authoritative location even if several tasks
  implement it.
- Contributors may propose changes, but material requirement and boundary decisions must be
  reconciled centrally before dependent work proceeds.
- Compare `touches` in sibling active manifests. Resolve overlap through explicit ordering, unification,
  partition, coordination, or supersession rather than assuming directory isolation.
- On handoff, state the active change ID, lifecycle status, completed slices, changed files, checks and
  results, unresolved decisions, and exact next action.
- Never overwrite another contributor's unreviewed artifact or code merely to restore a planned
  shape. Integrate current state deliberately.

## Failure, Supersession, and Abandonment

When work stops before completion:

- Record what was implemented or externally changed and what remains.
- Record whether partial effects need cleanup, rollback, migration, or operator action.
- For `SUPERSEDED`, link the replacement change and explain which requirements moved, changed, or
  disappeared.
- For `ABANDONED`, state why, what evidence was learned, and whether reopening is safe.
- Do not check unfinished tasks merely to close the record.
- Archive only with the terminal status visible so readers cannot mistake the record for a completed
  implementation.
