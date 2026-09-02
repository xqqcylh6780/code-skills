---
name: review-changes
description: >-
  Use when reviewing local changes, staged files, commits, branches, pull requests, completed
  implementation, or a proposed patch for correctness, regressions, requirement alignment,
  security, compatibility, maintainability, and test coverage. Covers evidence-backed, read-only
  code review and pre-merge risk assessment. Do not use to implement fixes unless the user also
  requests changes, or to diagnose a reported failure whose causal chain is still unknown.
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
- Report only actionable findings introduced or exposed by the reviewed change. Mention a
  pre-existing issue only when it directly blocks the change or makes its claimed behavior false.
- Distinguish verified defects, unresolved questions, and untested risks. Do not convert uncertainty
  into a confident finding.

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
problem, not merely where the symptom appears. Combine duplicate symptoms with one root finding.

After findings, state:

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
actual impact, requirement coverage and relevant boundaries were checked, and verification limits
are visible.
