# Indexes and Query Plans

Design indexes from access paths and verify them with the engine's planner.

## Query inventory

For a material query record:

```text
predicate columns:
join columns:
ordering/grouping:
expected selectivity:
rows returned:
frequency:
write pressure on the table:
latency sensitivity:
```

## Index principles

- Primary/unique indexes enforce invariants; performance indexes should justify their write/storage cost.
- Composite index column order should follow real equality/range/order access patterns, not alphabetical order.
- Avoid adding separate indexes for every predicate without checking whether an existing composite index already serves the query.
- Index foreign-key columns when their lookup/delete/update patterns justify it; do not assume every engine creates them automatically.
- Partial/filtered, covering/include, expression, or specialized indexes are engine-specific tools; use them only when the workload and engine support make the benefit clear.

## Plans and measurements

Use the engine's plan tooling (`EXPLAIN` or equivalent) and representative statistics. For plans that execute the query, verify safety before running writes or expensive scans.

Check:

- estimated versus actual row counts when available;
- scan type and rows filtered;
- join order/algorithm;
- sorts, temporary structures, spills, or repeated loops;
- index usage and selectivity;
- total latency and variance under comparable conditions.

Do not treat “uses an index” as automatically good or a sequential/table scan as automatically bad. Small tables and low-selectivity queries can make full scans correct.
