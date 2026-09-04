# Routing Examples

## Should trigger

- “Profile this API and reduce P95 latency under the provided benchmark.”
- “Measure how many concurrent jobs this worker can handle before saturation.”
- “This page is functionally correct; reduce render/network cost against a performance budget.”
- “Benchmark these two implementations with representative input sizes.”
- “Build a safe load test and capacity estimate for this service.”

## Should not trigger

- “Production suddenly became slow and we do not know why.” → `diagnose-bugs` first.
- “Add an index for this known query plan.” → `database-engineering`.
- “Implement pagination because the API contract is changing.” → `design-interfaces` plus the relevant build skill.
- “Review whether this PR hurts performance.” → `review-changes` if review-only.
- “Replace a loop because another syntax looks faster” with no measurable target → ordinary refactor/review; do not launch a performance workflow by habit.

## Conflict cases

- “An endpoint is slow because EXPLAIN shows a bad access path.” → `database-engineering` owns the query/index change; `performance-engineering` can own the end-to-end benchmark.
- “Optimize an API and deploy the result safely.” → `performance-engineering` proves the gain; `deploy-and-operate` owns rollout and production comparison.
- “Refactor a hot path for readability and speed.” → separate behavior-preserving structure (`refactor-code`) from measured optimization (`performance-engineering`) so each claim has its own evidence.
