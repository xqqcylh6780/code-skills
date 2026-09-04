# Release and Rollout

Treat a release as a compatibility transition, not just a process restart.

## Release ledger

Track:

```text
source revision:
artifact/image version:
configuration revision:
database/schema version:
external contract assumptions:
feature flags:
rollback-compatible until:
```

## Expand before contract

When database, API, event, or config shapes change across independently deployed components, prefer additive compatibility first. Deploy consumers/producers that tolerate both states, switch authority, observe adoption, then remove old behavior after the rollback window closes.

## Rollout choices

Use the mechanism the platform already supports. The important property is bounded exposure and evidence between stages, not the marketing name of the strategy.

- Single-instance replacement: simple but may require a maintenance window or fast restart.
- Rolling: keep versions overlap-compatible.
- Canary: route limited representative traffic and compare health.
- Blue/green: keep a separately addressable prior/new environment and understand shared-database constraints.

## Stop conditions

Stop or reverse progression when a material invariant fails: readiness, error budget/policy, data integrity, authentication/authorization behavior, queue accumulation, terminal dependency errors, or migration safety.
