# Routing Examples

## Should trigger

- “Split this 2,000-line service into cohesive modules without changing behavior.”
- “Remove this dependency cycle while keeping the API unchanged.”
- “Extract the duplicated authorization policy into one owner without changing outcomes.”
- “Modernize this legacy module incrementally; existing behavior must stay compatible.”
- “Remove proven dead code and simplify the internal control flow.”

## Should not trigger

- “Add a new export feature.” → relevant build skill.
- “This service returns the wrong result and we do not know why.” → `diagnose-bugs`.
- “Change the public API response shape while cleaning the code.” → `design-interfaces` plus implementation.
- “Review whether this class is too large.” → `review-changes` if review-only.
- “Reformat and sort imports.” → normal focused edit; a full refactoring workflow is unnecessary.

## Conflict cases

- “Fix a known bug and then clean the implementation.” → prove/fix through `diagnose-bugs` or `test-behavior-first`, then use `refactor-code` under green behavior.
- “Split a backend module and change one API field.” → `design-interfaces` owns the contract change; `refactor-code` owns only behavior-preserving structural movement.
- “Move data access to a new repository abstraction while preserving SQL behavior.” → `refactor-code`; consult `database-engineering` only if schema/query semantics themselves change.
