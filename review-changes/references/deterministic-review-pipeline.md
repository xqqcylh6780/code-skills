# Deterministic Review Pipeline

Use this pipeline when a review spans several files, crosses components or risk boundaries, or
claims comprehensive coverage. It turns repository facts into an auditable review plan while
leaving defect judgment to the reviewer.

## 1. Build the manifest

Run the bundled read-only helper from the skill directory:

```text
python scripts/build_review_manifest.py --repo <repository> --mode worktree
python scripts/build_review_manifest.py --repo <repository> --mode staged
python scripts/build_review_manifest.py --repo <repository> --mode range --base <base> [--head <head>]
python scripts/build_review_manifest.py --repo <repository> --mode commit --commit <revision>
```

The helper calls read-only Git commands and writes JSON only to stdout. It records exact paths,
Git status, rename sources, changed line ranges, suggested review lenses, review units, and a
pending coverage seed. The lens and unit suggestions are routing hints, not conclusions.

Do not use the helper when the review target is a supplied patch with no repository, a provider
diff already gives a more authoritative file list, or the focused fast path is sufficient.

## 2. Correct and group the review units

Keep coupled changes together even when paths differ:

- implementation with its tests, fixtures, snapshots, schemas, and generated outputs;
- API producer with callers and consumers;
- migration with model, query, rollback, and mixed-version behavior;
- configuration with loaders, defaults, deployment templates, and documentation;
- UI state producer with screens, navigation, assets, and accessibility behavior.

Split a large manifest into review units that can each be traced end to end. Override the helper's
path-based grouping when behavioral coupling provides a better boundary.

## 3. Route each unit to relevant checks

Use file characteristics and behavior to select review lenses:

| Signal | Emphasis |
| --- | --- |
| Tests or fixtures | Assertion strength, failure paths, false positives, stable seams |
| Configuration or lockfiles | Defaults, compatibility, rollout, supply-chain effects |
| Generated or vendored output | Source-of-truth consistency; do not skip automatically |
| Migration or persistence | Ordering, partial failure, mixed versions, integrity, rollback |
| Auth, permission, token, session | Trust boundaries, ownership, leakage, privilege effects |
| API, route, handler | Validation, error semantics, consumers, compatibility |
| UI, view, screen | State wiring, navigation, loading/error/empty states, accessibility |

Apply only relevant sections of [review-checklist.md](review-checklist.md). A routed check is an
investigation prompt, never automatic evidence of a defect.

## 4. Maintain a coverage ledger

For a comprehensive review, track every manifest path or review unit as:

```text
reviewed — diff and necessary context inspected
skipped — intentionally omitted with a reason
blocked — unavailable, truncated, binary, generated from an unavailable source, or otherwise unreadable
```

Record the reason for every skipped or blocked item. Do not claim complete coverage while any item
is pending or blocked. A reviewed file can still have a verification gap; coverage is not proof of
correctness.

## 5. Reflect on candidate findings

Before promoting a candidate to a finding:

1. Re-open the final diff and current surrounding code.
2. Reproduce or trace the concrete trigger and observable consequence.
3. Search for caller constraints, guards, fallbacks, feature flags, migrations, and tests.
4. Decide whether the issue is introduced or newly exposed by the reviewed range.
5. Merge duplicate symptoms under the earliest actionable root cause.
6. Reject the candidate or downgrade it to an open question/residual risk when evidence is incomplete.

This reflection pass is specifically for reducing plausible-sounding false positives.

## 6. Calibrate locations against the final artifact

Re-check each cited path and line after all inspection and any authorized fixes. Prefer the changed
line that causes the defect. For renamed files, cite the new path; for pure deletions, cite the
nearest changed line that makes the omission actionable and explain the deleted behavior. Never
reuse stale line numbers from an earlier diff.

## 7. Close the review

Before reporting completion, reconcile:

- manifest files versus reviewed, skipped, and blocked units;
- requirements versus implementation and evidence;
- reported findings versus the final diff and line locations;
- checks inspected versus checks actually executed;
- unresolved uncertainty versus open questions and residual risks.

Summarize material coverage gaps in the final review. Keep the internal manifest and rejected
candidates out of the report unless they explain a limitation or the user asks for the audit trail.
