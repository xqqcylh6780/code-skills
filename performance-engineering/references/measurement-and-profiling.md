# Measurement and Profiling

Choose tools that observe the suspected boundary without changing the workload more than necessary.

## Baseline quality

Record environment, revision, build mode, dataset, cache/warm state, concurrency, and exact command/scenario. Warm up runtimes when compilation/JIT/cache startup is not part of the user-facing target; include startup when it is.

Prefer percentiles/distributions for latency and repeated samples for benchmarks. Report both improvement and absolute values when possible.

## Profiling

Localize time/resources before optimizing:

- CPU/profile stacks for compute-bound paths;
- allocation/heap evidence for memory pressure;
- tracing for cross-service/dependency latency;
- query plans and database metrics for SQL/storage;
- browser/runtime performance tooling for render/network/main-thread work;
- queue/lock/concurrency metrics for contention.

Python's standard profiler documentation: https://docs.python.org/3/library/profile.html

Profilers add overhead; use them to identify dominant cost, then confirm the final result with lower-overhead representative measurements.
