---
name: shape-project
description: >-
  Turn a materially ambiguous product, project, or feature into an execution-ready brief.
  Trigger for vague scope, competing approaches, unclear requirements, acceptance criteria,
  staged delivery, or work that needs a first vertical slice. Do not invoke for small,
  already-specific implementation tasks.
---

# Shape Project

Shape the work before building it. Convert what the user knows into a shared, verifiable contract for what to build, why it matters, how to approach it, and what should happen first.

## Operating Principles

- Match the depth of planning to the uncertainty and blast radius. Do not turn a small, obvious change into a product workshop.
- Separate user-stated facts, repository evidence, external evidence, assumptions, recommendations, and unresolved decisions.
- Inspect available sources before asking questions the repository, documentation, or supplied artifacts can answer.
- Ask only when the answer could change scope, behavior, architecture, safety, cost, or delivery order. Ask one material decision at a time; group only short independent factual gaps.
- Challenge the requested solution without dismissing the underlying need. Preserve explicit user constraints unless changing them is necessary and authorized.
- Compare alternatives for consequential decisions. Do not manufacture options when one approach clearly follows from established project conventions.
- Prefer the smallest coherent scope that proves the desired outcome. Do not confuse a thin but unusable demo with a useful first slice.
- Make acceptance criteria observable and pass/fail. Avoid “works correctly,” “looks good,” and other subjective completion claims.
- Treat planning as the current deliverable when the user requests a plan, specification, or
  approach. When the user requests implementation, use only enough shaping to resolve material
  blockers, then continue into the authorized work unless a user decision is genuinely required.

### Focused shaping fast path

For a small or already well-specified change, do not run the full discovery workflow. Inspect the
nearest repository evidence, confirm the observable outcome, material constraint, and verification
path, then stop shaping as soon as the next safe vertical slice is unambiguous. Do not create a
requirements ledger, alternatives analysis, readiness report, or standalone brief when those
artifacts would not change the implementation decision.

Use the full workflow only when uncertainty, blast radius, migration, security, architecture, or
sequencing makes those steps decision-relevant.

## Workflow

### 1. Classify the Starting Point

Choose one primary mode internally:

- **Discover:** the user has an idea, pain point, or desired outcome but the product and scope are still fluid.
- **Kickoff:** the user asks for an effective way to begin or for an implementation-ready plan.
- **Review:** a brief, specification, ticket, or implementation plan already exists and needs pressure-testing.
- **Reframe:** evidence suggests the proposed solution does not address the stated problem or creates disproportionate cost or risk.

Also identify whether the work is greenfield, an addition to an existing product, a migration, or replacement of existing behavior. Change modes if new evidence warrants it; do not force every project through the same interview. If no mode applies because the request is already execution-ready, stop shaping and proceed with the relevant implementation skill.

### 2. Inspect the Available Context

For an existing repository, inspect the smallest set of sources that establishes:

- Product purpose, user-facing behavior, and nearby features.
- Frameworks, runtime, package manager, build and test entry points.
- Architecture, modules, public boundaries, persistence, integrations, and deployment shape.
- Existing conventions, design system, security controls, observability, and operational constraints.
- Current implementation or prior attempts related to the request.
- Repository instructions, active plans, issues, decision records, and relevant history.

Use structural code tools for definitions, dependencies, and impact. Use literal search for requirements, comments, configuration, error text, and documentation. Inspect current official sources when an external API, library, regulation, price, or platform behavior may have changed.

For greenfield work, inspect supplied notes, examples, research, reference products, and target environment. Do not invent an existing codebase or operational constraint.

### 3. Build a Requirements Ledger

Maintain these categories while working:

| Category | Meaning |
|---|---|
| Confirmed | Explicit user requirement or verified source fact |
| Assumed | Working assumption that is safe and reversible |
| Decided | Material choice accepted by the user or established by project policy |
| Open | Missing answer that can change the plan |
| Rejected | Considered option or scope deliberately excluded |

Normalize the request into:

```text
Problem or opportunity:
Target users and triggering situation:
Desired observable outcome:
Required behaviors:
Quality attributes:
Constraints:
Non-goals:
Success evidence:
```

Do not silently promote an inference into a confirmed requirement.

### 4. Resolve Product and Requirement Uncertainty

In **Discover** or **Reframe** mode, read [references/discovery-questions.md](references/discovery-questions.md). Select only the questions appropriate to the project stage and push vague answers toward concrete examples, observed behavior, or an explicit “unknown.”

In **Kickoff** mode, assume the user’s requirements are useful input. Check completeness and contradictions without restarting discovery from zero. Concentrate on decisions required to begin safely.

In **Review** mode, preserve the plan’s intent while testing its premises, omissions, dependencies, and evidence. Do not rewrite the plan merely to impose a different style.

### 5. Challenge the Framing and Scope

Test the relationship between the problem and requested solution:

- Does the proposed behavior directly improve the desired outcome?
- Is the request solving a root problem, a symptom, or an implementation preference?
- Which user journey or system capability is the essential wedge?
- What must be present for the first release to be coherent and usable?
- What can be deferred without creating a dead end, false promise, or unsafe foundation?
- What existing behavior, migration, or operational burden would the change introduce?

Choose a scope posture:

- **Expand:** include an adjacent capability only when it materially improves the outcome or prevents rework.
- **Hold:** preserve the requested scope and raise its rigor.
- **Reduce:** remove work that does not support the outcome or makes the first slice unnecessarily risky.
- **Stage:** retain the full direction but sequence it into independently valuable increments.

Do not default to reduction. Recommend the posture that best balances completeness, evidence, reversibility, and delivery risk.

### 6. Compare Meaningful Approaches

For a material solution choice, present two or three viable approaches with:

```text
Approach:
What it optimizes:
How it fits the current system:
Benefits:
Costs and risks:
Reversibility:
When to choose it:
```

Recommend one approach and connect the reasoning to confirmed requirements and project evidence. Ask for a decision when alternatives change user behavior, public contracts, data ownership, dependencies, long-term architecture, security posture, or irreversible work.

Do not block on routine implementation choices that established project conventions already answer.

### 7. Shape the Solution Boundary

Define only the architecture needed to make the plan executable:

- User or system entry points and primary flows.
- Components, modules, services, jobs, and ownership boundaries affected.
- Data model, state transitions, persistence, and lifecycle.
- Public contracts, compatibility, migrations, and external integrations.
- Authentication, authorization, tenancy, sensitive data, and untrusted input.
- Failure behavior, retries, idempotency, recovery, and rollback.
- Performance, scale, accessibility, observability, and operational needs.
- Dependencies, rollout order, feature flags, and cleanup of old paths.

Read [references/planning-checklist.md](references/planning-checklist.md) and apply only the sections relevant to the change. Do not add infrastructure or abstraction merely to make the plan look comprehensive.

### 8. Write Testable Acceptance Criteria

Express acceptance criteria as numbered, observable outcomes. Cover the primary flow and the distinct risks identified during shaping.

Good criteria identify the actor or starting state, action, result, and important invariant:

```text
1. Given an account without export permission, when it requests an export, the server returns the established authorization error and creates no export job.
2. Given a valid export request, when processing completes, the user can download the file until the configured expiry time.
```

Include measurable quality thresholds only when the project has a credible way to measure them. Mark unknown targets as decisions or measurement tasks rather than inventing numbers.

### 9. Plan Vertical Slices

Break the work into increments that produce observable behavior or retire a concrete risk. For each slice state:

```text
Outcome:
Included behavior:
Affected boundaries:
Dependencies:
Verification:
Rollback or recovery:
Exit condition:
```

Order slices by prerequisite structure, uncertainty, user value, and risk—not by arbitrary file layers. Prefer an end-to-end first slice over “build all models, then all APIs, then all UI” when a vertical seam is practical.

Identify the first slice precisely enough that an implementer can begin without rediscovering the plan. Avoid calendar estimates unless the user requests them and sufficient repository evidence exists.

When the user requests a file-level implementation plan, the work spans several coordinated
tasks, or another agent or session will execute it, read
[references/execution-plan.md](references/execution-plan.md). Add exact file responsibilities,
interfaces between tasks, focused verification commands and expected evidence, while preserving
vertical outcomes instead of decomposing the plan into arbitrary technical layers.

### 10. Run the Readiness Gate

Before declaring the project ready, confirm:

- The problem, users, desired outcome, and current state are understood.
- Required scope and explicit non-goals do not contradict each other.
- Material assumptions and unresolved decisions are visible.
- The recommended approach fits the verified project and constraints.
- Public, data, security, operational, and migration boundaries are covered where relevant.
- Acceptance criteria are observable and testable.
- The first vertical slice and its verification path are clear.
- Risks have owners, mitigations, discovery tasks, or explicit acceptance.

Use one status:

- **READY:** implementation can start with no material unanswered decision.
- **READY WITH DECISIONS:** useful work can start, but list decisions required before affected slices.
- **NEEDS CONTEXT:** a missing fact or choice prevents a reliable plan; state exactly what is needed.
- **NOT READY:** evidence shows the proposed work should not begin as framed; explain the issue and next validation step.

For an implementation request, this gate is a decision aid rather than a mandatory separate
deliverable. Continue immediately when the first slice is clear and no material decision remains.

### 11. Produce the Brief and Handoff

Read [references/project-brief-template.md](references/project-brief-template.md) and produce the sections appropriate to the project. Keep verified current-state evidence and decisions close to the claims they support.

Route downstream work deliberately:

| Need | Next skill |
|---|---|
| Public API, schema, command, event, configuration, or shared boundary | `design-interfaces` |
| Browser-only web page, component, workflow, responsiveness, or visual system | `build-frontends` |
| Mobile/uni-app page, app lifecycle, device API, or cross-platform application flow | `build-mobile-apps` |
| Server-side service, domain, job, persistence, or integration behavior | `build-backends` |
| Database schema, indexes, query plans, migration, integrity, or recovery as the primary task | `database-engineering` |
| Authentication, authorization, untrusted input, sensitive data, or privileged effects | `secure-boundaries` |
| Deterministic high-value behavior with a practical test seam | `test-behavior-first` |
| Existing failure whose causal chain is unknown | `diagnose-bugs` |
| Behavior-preserving structural improvement | `refactor-code` |
| Performance measurement, profiling, optimization, or capacity target | `performance-engineering` |
| Build artifact, release, rollout, runtime verification, rollback, or recovery | `deploy-and-operate` |

Recommend only the skills required by the shaped work. State whether the next action is a decision, research spike, contract design, first implementation slice, prototype, migration preparation, or defect investigation.

## Quality Gates

Do not hand off a plan that:

- Repeats the user’s request without adding verified context, decisions, boundaries, or sequencing.
- Invents users, demand, repository behavior, dependencies, metrics, or constraints.
- Leaves “TBD” on a decision required for the first slice without naming an owner or resolution path.
- Lists tasks by file or technical layer without explaining the behavior each slice delivers.
- Uses vague acceptance criteria or treats “tests pass” as the complete product outcome.
- Ignores migration, compatibility, denial behavior, failure recovery, or rollback when they are material.
- Adds speculative infrastructure, abstractions, dependencies, or scope without a demonstrated requirement.
- Starts implementation during a planning-only request.

## Output Format

Return the brief, then finish with:

```text
Status: READY | READY WITH DECISIONS | NEEDS CONTEXT | NOT READY
Recommended first action:
First vertical slice:
Decisions required before it:
Downstream skills:
Evidence inspected:
Residual risks:
```

## Completion Criteria

Complete a planning deliverable only when the user can see what is being built, why this approach
fits, what is explicitly excluded, which facts and assumptions support the plan, how completion
will be verified, and the exact first step. For implementation requests, shaping is complete as
soon as the next safe vertical slice is unambiguous. Do not equate document length with readiness.
