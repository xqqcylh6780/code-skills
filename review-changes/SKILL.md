---
name: review-changes
description: >-
  Review diffs, commits, branches, PRs, or completed changes for concrete correctness and risk
  issues. Trigger for code review, regression review, pre-merge review, or review-and-fix when
  explicitly requested. Default to read-only findings; do not replace implementation or
  unknown-cause debugging.
---

# Review Changes

Review the change that was requested, not an imagined ideal codebase. Find concrete defects before
they reach users or become dependencies for later work, and report them with enough evidence that
an implementer can act without repeating the investigation.

## Core Principles

- Treat review as read-only unless the user explicitly asks to fix findings.
- Establish the requirements, comparison base, and change range before judging the patch.
- Prioritize correctness, data integrity, security, compatibility, and observable behavior over
  style preferences.
- Inspect enough unchanged context to understand the changed behavior, but do not turn a scoped
  review into a repository-wide audit.
- Validate each candidate finding against the actual code path, existing guards, tests, and
  supported environments before reporting it.
- Use deterministic bookkeeping for broad reviews so every changed file is routed, reviewed,
  intentionally skipped, or reported as blocked.
- Report only actionable findings introduced or exposed by the reviewed change. Mention a
  pre-existing issue only when it directly blocks the change or makes its claimed behavior false.
- Distinguish verified defects, unresolved questions, and untested risks. Do not convert uncertainty
  into a confident finding.

### Focused review fast path

For a small, clearly scoped diff with an established requirement and no public, data, security,
concurrency, migration, or deployment boundary, inspect the exact diff plus only the nearest
consumer/test context. Report actionable findings or `No actionable findings.` and stop. Do not
expand a tiny review into a repository-wide architecture audit.

## Workflow

### 1. Establish the Review Contract

Identify:

```text
Review target: working tree, staged diff, commit range, branch, PR, or supplied patch
Comparison base: exact revision or established baseline
Requirements: request, ticket, specification, plan, acceptance criteria, or contract
Review mode: report-only or review-and-fix
Risk focus: correctness, security, compatibility, data, performance, UX, or general
Verification available: tests, builds, static checks, runtime evidence, or none
```

Infer obvious local details from repository state. Ask only when different bases or requirements
would materially change the verdict. If the user asks only for a review, remain report-only.

### 2. Capture the Exact Change Set

Inspect the narrowest authoritative diff and its commit list or file status. Preserve the working
tree, index, HEAD, and branch state during review.

Check for:

- Untracked or staged files that the selected range omits.
- Generated, vendored, migration, lock, or configuration files that change runtime behavior.
- Multiple commits whose full range cannot be represented by only the last commit.
- Requirements implemented outside the visible diff through configuration or generated artifacts.

Record the files, observable behaviors, public boundaries, stored state, privileged effects, and
direct consumers touched by the change.

For a multi-file, multi-component, high-risk, or explicitly comprehensive review, read
[references/deterministic-review-pipeline.md](references/deterministic-review-pipeline.md). Use its
read-only manifest helper when Git is the authoritative source, then correct its heuristic review
units and lenses using actual behavioral coupling. Maintain a coverage ledger and disclose skipped
or blocked units. Do not force this pipeline onto the focused fast path.

### 3. Review in Risk-Ordered Passes

Review the highest-consequence paths first:

1. **Requirement alignment:** confirm every required behavior is present and no explicit non-goal
   was implemented accidentally.
2. **Correctness and state:** trace inputs, branches, state transitions, side effects, cleanup,
   failure paths, and concurrency-sensitive behavior.
3. **Boundaries:** inspect validation, authorization, sensitive data, persistence, external calls,
   serialization, compatibility, migrations, and rollback where relevant.
4. **Tests and evidence:** determine whether tests exercise the changed behavior through a stable
   seam and whether material failure paths remain unproved.
5. **Maintainability:** flag design or readability problems only when they create a concrete defect,
   regression risk, or unreasonable future change cost in the reviewed surface.

Read [references/review-checklist.md](references/review-checklist.md) when the change crosses public,
data, security, concurrency, deployment, or multi-component boundaries, or when a comprehensive
pre-merge review is requested.

For broad reviews, work review unit by review unit. Route each unit by behavior and file
characteristics, keep coupled implementation/tests/configuration/generated outputs together, and
mark its coverage state before moving on. Treat generated, vendored, binary, and lock files as
explicit review decisions rather than silently ignoring them.

### 4. Validate Every Candidate Finding

Before reporting a problem, establish:

```text
Trigger: the input, state, environment, or sequence that reaches the problem
Location: the smallest changed line range responsible for it
Behavior: what the code actually does
Expected: what the requirement, contract, invariant, or supported behavior requires
Impact: who or what fails and how severely
Evidence: code path, test, specification, or reproducible reasoning that distinguishes the defect
```

Search for an existing caller, guard, fallback, feature flag, migration, or test that may invalidate
the finding. If evidence remains incomplete, report it as an open question or residual risk instead
of a defect.

After the initial pass, reflect on all candidates together: re-open the final code and diff, reject
false positives, merge duplicate symptoms under the earliest actionable root cause, and confirm the
issue was introduced or newly exposed by the selected range.

### 5. Calibrate Severity

Use the lowest severity that accurately represents the consequence:

- **P0 — Critical:** immediate widespread outage, exploitable security failure, irreversible data
  loss, or a change that cannot safely ship or remain deployed.
- **P1 — High:** common-path breakage, authorization bypass, serious data corruption, broken public
  contract, or failure requiring prompt correction before merge.
- **P2 — Medium:** real defect under plausible conditions, incomplete required behavior, meaningful
  regression, or test gap that leaves a material changed risk unprotected.
- **P3 — Low:** localized correctness or maintainability issue with limited impact and a clear
  relationship to the change. Do not use P3 for personal style preferences.

Do not inflate severity to make a finding more visible. A small patch may have no findings.

### 6. Report Findings First

Order findings by severity and then by dependency or execution order. For each finding include:

```text
[P1] Short imperative title
Location: path/to/file.ext:line
Trigger and behavior:
Why it matters:
Suggested direction: include only when not obvious
```

Keep the cited line range tight and place the explanation on the changed line that causes the
problem, not merely where the symptom appears. Recalibrate paths and line numbers against the final
review artifact; do not reuse positions from a stale diff. Combine duplicate symptoms with one root
finding.

After findings, state:

- Coverage gaps for comprehensive reviews, including skipped or blocked units and reasons.
- Open questions or assumptions that materially affect the verdict.
- Verification inspected and material checks not run.
- Residual risks that are not proven defects.
- A concise overall assessment.

If no actionable findings exist, say so directly and still disclose meaningful verification gaps.
Do not pad the report with praise, generic recommendations, or invented minor issues.

### 7. Handle Review-and-Fix Requests

Only enter this mode when the user explicitly requests fixes. Confirm each finding against current
code before editing, implement one coherent repair at a time, and run focused verification after
each material fix. Use `diagnose-bugs` when a finding's cause is uncertain, `test-behavior-first`
for deterministic behavior changes, `secure-boundaries` for trust-boundary repairs, and
`design-interfaces` for observable contract changes.

Do not silently expand a review into refactoring, dependency upgrades, migrations, or interface
redesign.

## Review Guardrails

- Do not claim tests pass from old output, a reviewer report, or an exit code you did not inspect.
- Do not flag code outside the review range unless the change newly depends on it or makes it fail.
- Do not require a preferred pattern when the existing implementation is correct and maintainable.
- Do not treat missing comments, documentation, logging, or tests as defects without a relevant
  requirement or an unprotected material risk.
- Do not report speculative race conditions, performance problems, or security issues without a
  plausible execution path.
- Do not approve a change solely because tests pass; tests may omit requirements or assert the wrong
  behavior.
- Do not reject a change solely because verification cannot run; state the limitation and judge only
  what the available evidence supports.

## Output Format

Return:

```text
Findings:
- [P0-P3] title — file:line
  Trigger and behavior:
  Impact:
  Suggested direction:

Open questions or assumptions:
Coverage gaps:
Verification inspected:
Checks not run:
Residual risks:
Overall assessment:
```

Omit empty subsections inside an individual finding. When no findings exist, begin with
`No actionable findings.` and continue with verification gaps and residual risks.

## Completion Criteria

Complete the review only when the exact change range and requirements are known or explicitly
bounded, every reported finding has a plausible trigger and tight location, severity reflects
actual impact, requirement coverage and relevant boundaries were checked, broad-review coverage is
reconciled with the exact file set, and verification limits are visible.
