# Domain Language and Decision Records

Read for recurring business vocabulary or consequential trade-offs that need a durable record.
Apply only the parts needed by the requested task; this reference does not start an interview,
authorize file writes, or require a specification lifecycle.

## Resolve meaning before recording it

Find the existing glossary or equivalent vocabulary section. Follow a context map when present;
the same word may legitimately differ between bounded contexts. Check relevant code and accepted
requirements, distinguish today's behavior from the proposed change, and use a concrete example
to expose a material ambiguity. Ask only about the unresolved choice, with a reasoned recommendation.
Do not re-ask settled questions or search every context for a local definition.

## Keep each document responsible for one thing

- **Vocabulary:** agreed business meanings, relevant context, and distinctions between easily
  confused terms. Reuse the established location; create a glossary only when persistent shared
  language is useful and documentation is in scope. A small change can define its term in its brief.
- **Behavior:** accepted defaults, ordering guarantees, exclusions, edge cases, and acceptance
  criteria belong in the owning requirement/specification. Link the term rather than copying its
  definition. A decision failing the ADR test can still impose a required behavior.
- **Rationale:** a durable decision record explains a chosen trade-off; it does not replace the
  behavioral contract, task list, or current task state.

During authorized writing, update a definition once it is settled, rather than waiting for a final
interview dump. Keep proposals and disputed meanings visibly unresolved. Do not overwrite another
context's definition or silently convert a proposed semantic change into accepted behavior.
For analysis-only requests, return suggested edits; create no files.

## Decide whether an ADR adds value

Follow an explicit repository decision-record policy first. Otherwise create an ADR only when
all three questions have a supported yes:

1. Would reversing the choice impose a substantial migration, compatibility, or operational cost?
2. Would a future maintainer need missing context to understand the choice?
3. Were viable alternatives rejected for concrete reasons?

If a condition is absent, retain any necessary behavior or implementation explanation in its
owning artifact. Do not generate an ADR per question, per file, or per reversible UI preference.
Record a material rejection reason only when it helps the user evaluate a disputed decision.

Use the existing ADR path, numbering, and template; create a location only for a qualifying record.
Capture the decision's status, drivers, real alternatives, chosen approach, consequences, and links
to requirements. Keep a proposal visibly proposed until accepted. When an accepted choice changes,
preserve its rationale and link its successor using the repository's supersession convention.
Do not fabricate alternatives or rewrite the old choice to make the new history look inevitable.

## Finish without losing obligations

Report changed definitions/records and the owning location of accepted behavior. Flag unresolved
terms that block the next slice. Stop when the scoped language/decision work is usable; no ADR or
new glossary can be a valid result. Do not require a second approval for already-authorized edits.

Sources informing this locally authored guidance:
[domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md),
[grill-with-docs workflow](https://github.com/mattpocock/skills/blob/main/docs/engineering/grill-with-docs.md).
