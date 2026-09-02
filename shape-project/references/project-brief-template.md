# Project Brief Template

Use this template selectively. Omit irrelevant sections, but never omit a material uncertainty merely to make the brief look complete.

## Contents

- [Header](#header)
- [Problem and Outcome](#problem-and-outcome)
- [Evidence and Current State](#evidence-and-current-state)
- [Requirements and Scope](#requirements-and-scope)
- [Decisions and Approach](#decisions-and-approach)
- [Solution Boundary](#solution-boundary)
- [Acceptance and Verification](#acceptance-and-verification)
- [Implementation Slices](#implementation-slices)
- [Delivery and Handoff](#delivery-and-handoff)

## Header

```markdown
# <Project or Feature Name>

Status: READY | READY WITH DECISIONS | NEEDS CONTEXT | NOT READY
Mode: Discover | Kickoff | Review | Reframe
Project state: Greenfield | Existing product | Migration | Replacement
Prepared from: <user request, repository paths, issue, design, docs, research>
```

## Problem and Outcome

```markdown
## Problem

<Concrete user or system situation, current pain, and why it matters.>

## Target Users and Primary Workflow

- Actor:
- Trigger:
- Current workflow:
- Desired workflow:

## Desired Outcome

<Observable change in behavior or system capability, distinct from implementation.>

## Success Evidence

- <Metric, observed behavior, support reduction, completion result, or validation method>
```

Do not claim demand, frequency, scale, or impact without a source. Use “Unknown — validate by …” when needed.

## Evidence and Current State

```markdown
## Verified Current State

| Finding | Evidence | Planning consequence |
|---|---|---|
| <current behavior or structure> | <file, test, command, artifact, source> | <constraint or opportunity> |

## Requirements Ledger

### Confirmed
- ...

### Assumed
- ...

### Decided
- ...

### Open
- ...

### Rejected
- ...
```

Keep evidence specific enough that another implementer can verify it without repeating the whole investigation.

## Requirements and Scope

```markdown
## Required Behavior

1. ...
2. ...

## Quality Attributes

- Accessibility:
- Security/privacy:
- Performance/scale:
- Reliability/recovery:
- Compatibility:
- Operability:

## Constraints

- ...

## In Scope

- ...

## Out of Scope

- ...

## Deferred but Preserved

- <credible next capability and the seam preserved for it>
```

Separate “deferred” from “rejected.” Deferred work remains directionally compatible; rejected work should not influence the current architecture.

## Decisions and Approach

```markdown
## Alternatives Considered

| Approach | Optimizes | Benefits | Costs/risks | Reversibility |
|---|---|---|---|---|
| A | ... | ... | ... | ... |
| B | ... | ... | ... | ... |

## Recommended Approach

<Recommendation tied to confirmed requirements and verified project evidence.>

## Decision Record

| Decision | Choice | Reason | Status/owner |
|---|---|---|---|
| ... | ... | ... | accepted / open — owner |
```

Do not include fake alternatives. When project conventions already establish the choice, cite the convention and record the decision briefly.

## Solution Boundary

```markdown
## Affected Components and Ownership

| Component/boundary | Responsibility | Change | Owner/invariant |
|---|---|---|---|
| ... | ... | ... | ... |

## Primary Flow

actor -> entry point -> domain capability -> persistence/integration -> result

## Data and State

- Identifiers and ownership:
- State transitions:
- Persistence and lifecycle:
- Consistency/concurrency:
- Migration/backfill:

## Contracts and Integrations

- Public/shared interface:
- Compatibility strategy:
- External dependency assumptions:

## Failure and Recovery

- Expected failure modes:
- Retry/idempotency:
- User-visible error behavior:
- Rollback/disablement:

## Security and Operational Boundaries

- Trust and privilege changes:
- Sensitive data:
- Observability:
- Deployment/configuration:
```

Use diagrams only when they clarify multiple components, branches, states, or event ordering better than prose.

## Acceptance and Verification

```markdown
## Acceptance Criteria

1. <Specific pass/fail outcome>
2. <Specific pass/fail outcome>
3. <Important denial, failure, or compatibility outcome>

## Verification Plan

| Criterion/risk | Verification seam | Command or scenario | Required environment |
|---|---|---|---|
| ... | unit / API / browser / integration / manual | ... | ... |
```

The acceptance criteria define product completion. The verification plan explains how to establish it.

## Implementation Slices

```markdown
## Slice 1 — <Observable outcome>

- Included behavior:
- Affected boundaries:
- Dependencies:
- Verification:
- Rollback/recovery:
- Exit condition:

## Slice 2 — <Observable outcome>

...
```

End with:

```markdown
## Recommended First Action

<Exact decision, research step, contract task, prototype, or implementation slice to begin now.>

## Decisions Required Before It

- None, or list only decisions that block the first action.
```

## Delivery and Handoff

```markdown
## Risks and Mitigations

| Risk | Evidence/likelihood | Impact | Mitigation or owner |
|---|---|---|---|
| ... | ... | ... | ... |

## Rollout and Cleanup

- Rollout:
- Compatibility window:
- Monitoring:
- Rollback:
- Old-path removal:

## Downstream Skills

- `design-interfaces`: <why or not needed>
- `build-frontends`: <why or not needed>
- `secure-boundaries`: <why or not needed>
- `test-behavior-first`: <why or not needed>
- `diagnose-bugs`: <why or not needed>

## Residual Risks

- ...
```

Recommend only applicable skills. A handoff is complete when the next action and its required evidence are explicit.
