# Discovery Questions

Use these questions selectively to turn an idea or ambiguous request into concrete product evidence. Do not conduct a fixed questionnaire. Choose the smallest set that can change the plan.

## Contents

- [Stage Routing](#stage-routing)
- [Question Families](#question-families)
- [Follow-Up Discipline](#follow-up-discipline)
- [Discovery Exit Criteria](#discovery-exit-criteria)
- [Anti-Patterns](#anti-patterns)

## Stage Routing

Select questions according to the current stage:

| Stage | Primary questions |
|---|---|
| Idea only | Problem, user, current alternative, desired outcome |
| Requirements known | Contradictions, constraints, success evidence, non-goals |
| Existing users | Observed behavior, failure points, adoption friction, retention |
| Internal tooling | Current workflow, frequency, cost of error, operational ownership |
| Infrastructure | Current limitation, workload evidence, reliability target, migration |
| Plan review | Unsupported assumptions, unresolved decisions, omitted failure paths |

Skip questions already answered by repository evidence or supplied artifacts. When the user explicitly says a premise is fixed, record it as a constraint and challenge only consequences that remain material.

## Question Families

### 1. Problem Reality

Ask for the concrete situation that creates the need:

- What happened the last time this problem occurred?
- Who experienced it, and what were they trying to complete?
- What observable cost did it create: lost time, failed task, risk, money, confusion, or manual work?
- How often does the situation occur, and under what trigger?
- Which part is verified and which part is currently a belief?

Push category labels such as “admins,” “developers,” or “customers” toward a real role, workflow, and context. Accept “unknown” when evidence is unavailable; turn it into a validation task.

### 2. Current Alternative

Understand the status quo before designing a replacement:

- How is the task completed today?
- Why is the current workflow tolerated despite its problems?
- Which existing behavior must remain available during migration?
- What would make users refuse to switch?
- Is the proposed feature replacing work, adding a new capability, or moving responsibility?

The current alternative includes spreadsheets, messages, manual review, memory, external products, scripts, and simply not doing the task.

### 3. Desired Outcome

Separate outcome from requested implementation:

- What should become easier, faster, safer, clearer, or newly possible?
- What would the user observe when the change succeeds?
- Which behavior matters more than the proposed UI, API, or technology choice?
- What negative outcome must not be introduced?
- How will the team know the result is useful after release?

Avoid success measures that count only shipped artifacts, such as number of endpoints or screens, unless the artifact itself is the contractual deliverable.

### 4. Narrowest Coherent Wedge

Find the first complete capability rather than the smallest amount of code:

- What single user journey proves the core outcome?
- Which states and failure paths are required for that journey to be trustworthy?
- What can be deferred without forcing a rewrite or misleading users?
- Which dependency or unknown should be tested before broad implementation?
- Can one vertical slice cross UI, contract, logic, and persistence with a narrow scope?

A coherent wedge may still require authentication, empty states, denial behavior, observability, or migration. Do not cut requirements that make the result unusable or unsafe.

### 5. Constraints and One-Way Doors

Identify limits that shape the solution:

- Which platform, framework, provider, data location, compatibility promise, or deadline is fixed?
- Which choices are reversible and which create migration or lock-in?
- Are there regulatory, privacy, accessibility, localization, performance, or availability requirements?
- Who owns the system after release?
- Which destructive or externally visible actions need explicit approval?

Ask for evidence behind unusual constraints when it can reveal a better option. Do not treat preferences as hard constraints unless the user confirms them.

### 6. Future Fit

Test whether the first slice supports the credible next step:

- If this works, what is the most likely next capability?
- Which extension pressure is already known from real users or system limits?
- What should remain intentionally unsupported?
- Which identifier, state, ownership, or boundary decision would be costly to reverse?
- Is the proposed abstraction solving a present need or speculating about an imagined future?

Design for known evolution seams, not every possible future.

## Follow-Up Discipline

When an answer is vague, follow up with one of:

- “Can you give the most recent concrete example?”
- “What would the user see or do differently?”
- “Which source establishes that requirement?”
- “What happens if we do not build this?”
- “Is that fixed, preferred, inferred, or still open?”
- “Which of these two outcomes matters more?”

Stop pushing when the answer is specific enough to influence scope or acceptance, or when the uncertainty has been honestly recorded with a resolution plan.

For consequential alternatives, state the issue, stakes, options, recommendation, and trade-off before asking. Do not ask the user to choose between unlabeled technical mechanisms they have no reason to understand.

## Discovery Exit Criteria

Exit discovery when:

- A concrete user or system actor and triggering situation are known.
- The current behavior or alternative is understood.
- The desired observable outcome is distinct from the requested mechanism.
- The first coherent wedge and explicit non-goals can be stated.
- Material constraints and one-way decisions are visible.
- Unknowns have owners or validation steps.

Discovery does not require certainty about every implementation detail. It requires enough product truth to make engineering decisions responsibly.

## Anti-Patterns

- Asking all questions regardless of project stage.
- Treating confidence, enthusiasm, or a waitlist as equivalent to observed need.
- Interrogating the user about facts already present in the repository.
- Repeatedly arguing for less scope after the user has made an informed scope choice.
- Forcing product-market language onto internal, compliance, migration, or infrastructure work.
- Turning every unknown into a blocker instead of identifying a reversible assumption or discovery task.
- Accepting “make it scalable,” “modern,” or “user-friendly” without an observable meaning.
