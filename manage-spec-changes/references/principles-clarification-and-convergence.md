# Principles, Clarification, and Convergence

Read this reference when starting or substantially revising a durable change, when ambiguity could
make planning unsafe, or after implementation needs to be assessed against accepted artifacts.

These practices strengthen the existing lifecycle without introducing a second command system,
policy file, or artifact tree.

## 1. Establish Governing Sources

Before accepting a proposal, identify the sources that can constrain it. Use the repository's real
authority order and include only sources relevant to the change:

1. Active system, developer, user, and applicable repository instructions.
2. Adopted governance or policy documents such as a project constitution, `SECURITY.md`, approved
   RFCs, compatibility policy, or data-handling rules.
3. Stable project context and canonical specifications.
4. Verified architectural and testing conventions in the existing codebase.

Do not create a new constitution by default. When principles already live in `AGENTS.md`, project
context, policies, or established specifications, reference those locations from the proposal or
design only where they materially affect a decision. Copying them creates competing truth.

Before `READY`, check:

- Does any accepted requirement conflict with a binding principle?
- Does the design require an exception, new dependency, new trust boundary, or governance change?
- Are compliance obligations represented in tasks and verification rather than mentioned only in
  prose?
- If a principle itself must change, is that change separately authorized and propagated to every
  dependent artifact?

A binding conflict is a blocking decision. Resolve it by changing the proposal/design, obtaining an
explicit exception, or updating the governing source with proper authority. Do not weaken the
principle inside one feature spec.

## 2. Run a Focused Clarification Audit

Use repository evidence and reasonable defaults first. Audit the dimensions whose answers could
change observable behavior or delivery risk:

- actors, primary flows, and user-visible outcomes;
- included and excluded scope;
- data shape, ownership, retention, and source of truth;
- authentication, authorization, privacy, and cross-user behavior;
- invalid input, denial, partial failure, retry, concurrency, and recovery;
- compatibility, migration, rollout, rollback, and cleanup;
- accessibility, performance, availability, and operational acceptance where material;
- assumptions that distinguish a product requirement from an implementation preference.

Ask the user only when several reasonable interpretations remain, the choice materially changes the
accepted result or risk, and no safe default follows from project evidence. Group no more than three
highest-impact questions in one clarification round so decisions stay reviewable; continue another
round only when the answers reveal new material ambiguity.

Record each consequential answer at the earliest authoritative location:

- behavior and boundaries in the delta specification;
- rationale or scope in the proposal;
- architecture in the design;
- work and verification in tasks.

Use decision IDs for unresolved material choices. `READY` artifacts must not contain unresolved
placeholder markers or hidden assumptions that an implementer must guess. Non-blocking deferred
decisions need an owner or resolution condition and a reason they do not block the next slice.

## 3. Define Useful Success Criteria

Acceptance scenarios prove specific behavior. Add proposal-level success criteria only when they
express a broader outcome that scenarios alone do not make obvious.

A useful criterion is:

- observable by a user, operator, or interoperating system;
- independent of a preferred framework, class, database, or test command;
- assessable with a credible method;
- bounded by a real product or operational expectation.

Do not invent percentages, latency limits, volumes, or satisfaction targets. When no defensible
measurement exists, use a qualitative but observable acceptance statement or rely on scenarios.
Implementation checks belong in the delivery and verification strategy.

## 4. Analyze Before Implementation

Before the first implementation slice, perform a cross-artifact check:

- governing constraints versus proposal and design;
- desired outcome and scope versus requirements;
- requirements versus acceptance scenarios and negative behavior;
- design decisions versus affected contracts, data, security, and operations;
- tasks versus every accepted requirement/scenario and dependency;
- planned checks versus the invariants they claim to prove.

Fix contradictions at their source and regenerate only affected downstream content. Structural
validator success is required where available, but it cannot establish that requirements are correct
or that tasks are sufficient.

## 5. Converge After Implementation

Run convergence only after implementation has been attempted against the current `tasks.md`. It is a
present-state assessment, not a diff review and not a substitute for tests.

### Inputs

Read the minimum authoritative material needed:

- governing sources relevant to the change;
- proposal scope, exclusions, and decisions;
- accepted requirements and scenarios;
- material design decisions;
- tasks and their claimed completion state;
- current implementation, tests, migrations, configuration, and recorded evidence.

### Assessment

Check each accepted obligation in both directions:

- Forward: does every requirement/scenario reach implementation and credible verification?
- Reverse: does each material implementation behavior belong to accepted scope and design?
- Constraint: does the result comply with governing principles and explicit exceptions?
- History: are completed tasks and retained evidence still truthful for the current implementation
  identity?

Classify findings by consequence:

- **Critical:** violates a binding principle, security/data boundary, or creates an unsafe release.
- **High:** an accepted requirement or important negative scenario is absent or contradicted.
- **Medium:** a material design, compatibility, operational, or verification obligation is incomplete.
- **Low:** a bounded traceability or documentation gap that does not hide incorrect behavior.

### Disposition

Choose exactly one outcome:

- **CONVERGED:** no accepted implementation obligation is missing. Leave `tasks.md` byte-for-byte
  unchanged; proceed to independent verification.
- **GAPS FOUND:** append a new `## Slice ...: Convergence` section containing new `T-###` tasks for
  each actionable implementation gap, mapped to affected requirement/scenario IDs. Return the change
  to `ACTIVE` and implement those tasks before converging again.
- **RECONCILIATION REQUIRED:** the artifact is wrong, ambiguous, or no longer reflects accepted
  intent. Update the earliest authoritative artifact, invalidate dependent evidence, rebuild affected
  tasks, and resume from the earliest incomplete lifecycle gate.
- **DECISION REQUIRED:** the gap cannot be resolved within accepted authority. Record the blocking
  decision and ask the user rather than choosing a new product behavior.

Within a convergence pass, never rewrite, renumber, delete, or silently check off completed task
history merely to produce a clean result. Append implementation-gap tasks. This append-only rule does
not prevent normal reconciliation from correcting authoritative proposal, spec, or design errors.

If no gaps exist, do not append an empty convergence section. Report the clean outcome and record the
assessment method in `evidence.md` when it materially supports verification.

## 6. Completion Relationship

Convergence answers “is anything accepted still missing?” It does not by itself prove runtime
correctness, migration safety, usability, or deployed behavior. The ordinary verification gate still
requires evidence proportional to risk, traceability, contradiction review, canonical
synchronization, and a valid terminal transition.
