---
name: resolve-git-conflicts
description: >-
  Diagnose or resolve Git merge, rebase, and cherry-pick conflicts while preserving both change
  intents and unrelated work. Use for unmerged paths and conflict markers; not ordinary review
  or an unsolicited history rewrite.
---

# Resolve Git Conflicts

Resolve the requested conflict against its actual base and both change intents. Removing markers
is insufficient if the result loses behavior. Keep unrelated work outside the resolution.

## Select the authorized outcome

- **Explain/review only:** inspect operation state, stages, history, and relevant callers/tests;
  report the cause and proposed resolution without editing or changing Git state.
- **Resolve:** edit the requested conflicted paths and verify their combined behavior. Preserve
  unrelated staged, unstaged, and untracked content.
- **Finish the operation:** only when the user requests completion or existing session authority
  clearly includes it, stage the resolved paths and continue/commit the established operation.
  Otherwise hand off the resolved working tree and state what remains. Skill selection does not
  itself authorize a new merge/rebase, commit, push, reset, or stash.

## Establish the state before edits

Confirm the target repository and worktree; inspect `git status`, the unmerged path list
(`git diff --name-only --diff-filter=U`), and `git ls-files --unmerged`. Identify the active merge, rebase, or cherry-pick
from Git's reported state and per-worktree metadata, resolved with `git rev-parse --git-path`
where needed. Do not assume `.git` is a directory or infer the operation only from branch names.
When parsing filenames programmatically, use Git's NUL-delimited output instead of splitting on
whitespace or treating quoted display paths as raw filenames.

Record the operation, target/base revisions, conflicted paths, and unrelated local changes.
Inspect the actual relevant commits and their intent. An existing unrelated staged change must
not silently become part of a merge commit; pause completion if it cannot be excluded safely
without changing the user's index. Do not reset or stash it as a convenience.

## Compare the real sides

For a normal content conflict, inspect the index entries and relevant base/side blobs:

```text
git ls-files --unmerged -- <path>
git show :1:<path>
git show :2:<path>
git show :3:<path>
```

Use argument arrays or proper target-shell quoting for real paths, and inspect renames through
the actual index entries. Stage 1 is the common base when present, stage 2 is ours, and stage 3
is theirs. During a rebase, ours is the upstream plus already replayed work, and theirs is the
commit currently being replayed. Do not map those labels to the user's branch by intuition.
Add/add and modify/delete conflicts may lack one or more stages; missing stages are evidence,
not a reason to manufacture an empty file.

## Resolve the smallest coherent behavior

Read the owning code, direct consumers, and relevant tests before choosing a result. Preserve
compatible changes from both sides. If the intents are incompatible and the requested goal does
not settle the choice, explain the concrete alternatives and ask for that decision.

Do not blanket-select ours/theirs or concatenate both hunks without checking their semantics.
For renamed/deleted paths, verify the remaining callers. For lockfiles/generated files, follow
the repository's authoritative source and approved generation path; inspect generators and hooks
before executing them and do not install dependencies merely to regenerate a file. For binary
or submodule conflicts, identify the actual versions/commits and obtain any unresolved choice
instead of guessing a text merge.

## Verify and finish proportionately

Inspect the resolution diff and run the relevant existing checks after their side effects are
understood. Check the affected behavior and remaining unmerged entries, not only marker text.
Searching for markers can surface legitimate examples or strings; review matches in context.

When completion is authorized, use explicit paths such as `git add -- <resolved-path>`; never
stage everything. Recheck the staged diff against the initial unrelated-change record. Inspect
relevant hooks before a commit or continuation; a continuation can run hooks or apply more commits.
Do not bypass hooks/signing requirements to force success. Reinspect the state after each step;
stop on an unexpected failure or newly ambiguous intent rather than blindly looping.

Do not use abort, skip, reset, clean, force checkout, or stash to make conflict indicators vanish.
If cancellation is explicitly requested, assess preservation of local work and explain the scoped
action under the active destructive-action rules. Never push or rewrite unrelated history as a
side effect of conflict resolution.

## Handoff

Report the operation and resolved paths, how both intents were handled, verification actually run,
unresolved choices, and whether the index/operation was completed or left for the user. Do not
claim a merge/rebase is finished while unmerged entries or continuation steps remain.

Sources: [Git merge](https://git-scm.com/docs/git-merge),
[Git rebase](https://git-scm.com/docs/git-rebase),
[Index stages](https://git-scm.com/docs/git-ls-files),
[Ours/theirs semantics](https://git-scm.com/docs/git-checkout).
