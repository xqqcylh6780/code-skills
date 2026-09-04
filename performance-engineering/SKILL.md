---
name: performance-engineering
description: >-
  Measure and improve software performance against an explicit workload or target. Trigger for
  profiling, benchmarking, latency/throughput, memory/CPU, database or cache performance,
  load/capacity testing, frontend performance, or regression comparison. Do not optimize
  speculatively without evidence.
---

# Performance Engineering

Optimize measured constraints, not code that merely looks expensive. Establish a representative baseline, localize the dominant cost, change the smallest responsible boundary, and compare equivalent measurements after the change.

## Activation Threshold

Use this skill when the user asks to measure or improve performance, establish a performance budget, run a benchmark/load test, profile resource use, or plan capacity.

Use `diagnose-bugs` first when a production slowdown/regression is an unexplained failure and the causal chain is disputed. Use `database-engineering` when the primary task is a database query plan/index/schema decision. Use a build skill when performance work requires product behavior changes outside the accepted optimization scope.

## Route Adjacent Work

- Unknown/intermittent performance regression or incident → `diagnose-bugs` first.
- SQL plan/index/database-engine performance → `database-engineering` for the data boundary.
- Web/mobile implementation changes → `build-frontends` or `build-mobile-apps`.
- Backend implementation changes → `build-backends`.
- Production rollout of an optimization → `deploy-and-operate`.
- Review-only performance findings → `review-changes`.

## Workflow

### 1. Define the performance contract

State what is being optimized and under what workload:

```text
User/system operation:
Environment/runtime:
Input/data size:
Concurrency/load:
Metric(s):
Current baseline:
Target/budget:
Correctness guardrails:
Resource/cost guardrails:
```

Do not invent latency or capacity targets. If no target exists, establish a baseline and compare alternatives rather than claiming “fast enough.”

### 2. Make measurement reproducible

Control the variables that materially affect the result: build mode, dataset, cache state, warmup, concurrency, hardware/runtime class, network boundary, random seed, and background load.

Use repeated measurements and report distribution/variance where it matters; one favorable run is not evidence.

Read [references/measurement-and-profiling.md](references/measurement-and-profiling.md).

### 3. Localize the dominant cost

Profile before changing architecture. Determine whether the constraint is CPU, allocation/memory, I/O, database, network, lock/contention, queueing, rendering, serialization, or external dependency time.

Prefer traces/profilers/query plans and direct counters over guessing from source shape. Stop expanding the search when one boundary explains enough of the target cost to test an optimization.

### 4. Choose the smallest optimization that can move the metric

Examples include:

- remove repeated work or N+1 access;
- reduce data transferred/serialized/rendered;
- change an algorithm/data structure where input scale justifies it;
- batch or stream bounded work;
- improve an access path/index through `database-engineering`;
- cache only when freshness/invalidation/failure semantics are explicit;
- reduce lock scope or contention while preserving correctness;
- move expensive work off a latency-critical path when product semantics allow it.

Do not trade away correctness, authorization, consistency, accessibility, or recovery behavior for a benchmark unless the user explicitly accepts that product tradeoff.

### 5. Compare equivalent before/after evidence

Run the same representative workload and compare:

```text
metric baseline:
metric after:
variance:
resource/cost change:
correctness checks:
new bottleneck or saturation point:
```

Reject an optimization whose apparent gain comes from a changed dataset, disabled validation, stale cache, skipped work, weaker consistency, or a different environment unless that change is the intended design decision.

### 6. Load/capacity test only with safe bounds

Read [references/load-and-capacity.md](references/load-and-capacity.md) for concurrent/load testing. Never direct unbounded load at a production or third-party system without explicit authorization and an understood safety envelope.

### 7. Roll out with observability

For production-sensitive optimizations, coordinate `deploy-and-operate`: identify release/version, compare the same service-level signals, watch saturation and error behavior, and retain a rollback/feature-disable path.

## Handoff

Report the workload, baseline, localized bottleneck, optimization, equivalent after-measurement, correctness/resource tradeoffs, and remaining capacity limit. Distinguish measured facts from modeled estimates.

## Completion Criteria

Performance work is complete when a representative measurable target has been established, the dominant cost is supported by evidence, the optimization preserves required behavior, and before/after measurements under equivalent conditions show the actual effect without hiding new resource or reliability costs.
