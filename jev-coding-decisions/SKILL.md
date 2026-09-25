---
name: jev-coding-decisions
description: Use TypeSafe Jev for repeated semantic judgments during coding work, such as ranking files, classifying CI failures, or triaging diffs, or when building Jev-backed decisions into an app. Jev does not generate code or replace the coding model.
---

# Jev for coding decisions

Use Jev as an optional decision step inside a normal coding workflow. It accepts a `state` and typed `questions`, then returns a Choice, Score, or Noul answer. The coding agent still reads code, edits files, runs checks, and owns the final conclusion. Do not switch the selected coding model or provider to Jev.

## Where it helps

- **Find likely files:** When literal search and code structure leave many plausible files, ask one relevance question per source-linked candidate and rank the answers. Read the selected files and their dependencies before editing. Do not send an entire repository just to avoid using `rg`.
- **Triage repeated items:** Classify issues, CI failures, log groups, or test failures against specific criteria. Give each item a stable ID so an answer can be checked against its original evidence.
- **Triage a diff:** Ask narrow questions about review depth, possible data loss, missing coverage, or the need for a specialist review. Treat answers as leads for inspection, never as proof that a change is safe or unsafe.
- **Build a Jev-backed feature:** Design the small judgments the application needs, then use the project's stack and TypeSafe's current SDK or HTTP API. The helper below is for exploratory calls during development; application code should call the API or SDK directly.

Use deterministic evidence first: filenames, imports, tests, type checks, and explicit rules. Reach for Jev when the remaining judgment is semantic and a closed answer is useful, especially across many items. For a single obvious item, inspect it directly. Jev does not count, compute, generate text, or know facts missing from the supplied state; keep those jobs in code or the coding agent.

## Call Jev

1. Confirm that this task authorizes sending the selected content to TypeSafe's external API. Remove credentials, personal data, and unrelated private code from `state`. If authorization is unclear, ask before sending content.
2. Frame each question as one small decision. Use `choice` for a fixed option set, `score` for an ordered rubric, and `noul` for the probability of a yes/no claim. Include an `other` or `needs_review` option when the offered choices may not cover the evidence. Give the model the relevant original snippets with file paths or item IDs; a conclusion you wrote about those snippets is not a substitute for evidence. Question IDs are for your code, so put the full meaning in each question's instructions.
3. Put the request JSON in the current task's scratch area. Use `python <skill-dir>/scripts/ask_jev.py --check <request.json>` to validate its shape without a network call. With `TYPESAFE_API_KEY` in the environment, omit `--check` to call Jev. On Windows the helper can also read this variable from the current user's environment registry when Codex was started before the variable was set. Pass `-` instead of a path to read JSON from standard input. The helper uses Python's standard library and prints the response JSON; it does not install packages or write results.
4. Batch independent questions that share a state in one call. Combine their answers with explicit code or direct reasoning; Jev questions do not see one another's answers. `confidence` exists for Choice and Score, but not Noul. A Noul value is the probability of “yes,” not a separate confidence score.
5. Check the returned answers against the original code, representative labeled cases, and relevant deterministic checks. Set any action threshold from task-specific validation; do not assume one global cutoff is safe. If the API fails, evidence is missing, or the answer is ambiguous, continue with direct inspection or surface the uncertainty. Never turn an error or a low score into an automatic approval.

Example request for a *review suggestion* (replace the state with a scoped summary or excerpt from the actual diff):

```json
{
  "state": {
    "path": "src/accounts/delete.py",
    "diff": "Include the relevant original diff excerpt here."
  },
  "model": "jev-latest",
  "questions": {
    "review_depth": {
      "type": "choice",
      "instructions": "What review depth does this change warrant based on the supplied evidence?",
      "criteria": {
        "standard": "Ordinary code review is sufficient",
        "deep": "Trace affected behavior and tests in detail",
        "needs_review": "The supplied evidence is insufficient to decide"
      }
    },
    "possible_data_loss": {
      "type": "noul",
      "instructions": "Could this change cause previously saved user data to be lost or silently discarded?"
    }
  }
}
```

The answer is advisory. Inspect the implicated paths and run the relevant deterministic checks before reporting a finding or completing the change. For recurring gates, evaluate examples from the target repository and pin a tested model version instead of assuming `jev-latest` will remain stable. When reporting a Jev-assisted result, identify what Jev suggested and what you independently verified.

Read current official documentation before implementing a Jev integration: [Jev with coding agents](https://docs.typesafe.ai/introduction/coding-agents), [API reference](https://docs.typesafe.ai/api), [confidence](https://docs.typesafe.ai/confidence), and [TypeSafe's agent skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md). Community design references: [Building with Jev](https://github.com/dbreunig/building-with-jev-skill) and [Jev Skills](https://github.com/wuyoscar/jev-skill).
