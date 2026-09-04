# Schema and Integrity

Use this reference when the task is primarily relational modeling or integrity design.

## Model invariants before tables

Start with entities, ownership, lifecycle, identity, and state transitions. Then choose tables and keys that make invalid durable state difficult to represent.

- Use stable primary keys that match the project's existing identity policy.
- Express mandatory relationships with `NOT NULL` and foreign keys when the database owns the relationship.
- Use `UNIQUE` constraints for durable uniqueness, including composite uniqueness when the business key spans columns.
- Use `CHECK` constraints for local value/state invariants the engine can enforce predictably.
- Distinguish missing, unknown, not-applicable, empty, and zero rather than using one sentinel accidentally.
- Avoid storing the same source-of-truth fact in several columns/tables unless synchronization is itself designed and verified.

## Relationship decisions

For each relationship define:

```text
owner:
cardinality:
required or optional:
delete behavior:
update behavior:
history/audit requirement:
tenant scope:
```

Choose cascade actions deliberately. A convenient ORM cascade is not a substitute for understanding database delete/update behavior.

## Denormalization

Denormalize only when a measured read/write tradeoff justifies the synchronization burden. Record which copy is authoritative and how stale or conflicting copies are repaired.

## Schema review questions

- Can the database represent a state the domain says is impossible?
- Can a concurrent writer bypass an application-only uniqueness check?
- Can deletion create orphaned or accidentally cascading data?
- Is tenancy/ownership represented consistently?
- Is every required query possible without reconstructing business state from ambiguous fields?
