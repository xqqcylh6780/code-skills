# PostgreSQL Access and Isolation Patterns

Read for PostgreSQL connection pressure, tenant-policy questions, or a concrete access-path
decision. Verify engine/provider versions and the actual schema. SQL below is an illustrative
read query, not an instruction to execute against a live database. Keep the workspace's database
policy in force for plans, tests, and configuration changes.

## Connection lifecycle

Identify direct versus pooled connections, application instance/worker counts, per-instance pool
limits, and the provider's connection budget. Multiplying a reasonable pool by many application
instances can exhaust the database. Do not cure saturation by blindly increasing every limit.

Session and transaction pooling have different lifetimes. Audit session settings, temporary
objects, locks, and driver prepared-statement support against the selected provider/mode.
Do not copy a connection URL or prepared-statement setting from an unrelated deployment. Keep
connection strings out of logs and handoff artifacts. Configuration edits are distinct from
changing a live database or provider service.

## Row-level security

Inspect whether RLS is enabled, applicable roles/policies, ownership, and bypass privileges.
With RLS enabled and no applicable policy, ordinary access is denied; table owners and privileged
roles can behave differently. A successful administrator query does not demonstrate tenant
isolation for the application role.

Distinguish row visibility (`USING`) from checks on new/changed rows (`WITH CHECK`). Trace where
tenant identity comes from rather than trusting a caller-supplied tenant ID. Combine with
`secure-boundaries` when designing or evaluating this trust boundary. Propose positive and
negative role/tenant cases; under read-only rules, do not create roles/policies or seed records
to run those cases.

## Stable pagination and indexes

For a descending feed with non-null timestamp and unique ID, an illustrative continuation query is:

```sql
SELECT id, updated_at, title
FROM boards
WHERE tenant_id = $1
  AND (updated_at, id) < ($2, $3)
ORDER BY updated_at DESC, id DESC
LIMIT $4;
```

The initial page omits the continuation predicate. Validate bounds and tie/null semantics at the
API boundary. An index beginning with the equality scope and matching the ordering is a candidate,
not a recommendation to create one without workload/plan evidence. Changing timestamps can move
rows between pages; define the feed's consistency contract instead of promising snapshot paging.

## Read the plan as evidence

Compare estimated/actual row counts where available, repeated loops, sorts/spills, filters, and
buffers. Planner cost is not elapsed milliseconds, and an index scan alone does not prove a win.
Record representative parameters and data volume when comparing plans. `EXPLAIN ANALYZE` executes
the statement; use permitted non-executing or captured evidence when execution would violate
database policy. Supply any index/policy/migration DDL for the user rather than applying it.

Sources: [Connection options](https://supabase.com/docs/guides/database/connecting-to-postgres),
[Row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html),
[Indexes and ordering](https://www.postgresql.org/docs/current/indexes-ordering.html),
[Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html).
