# Observability and Recovery

Useful authoritative references:

- OpenTelemetry: https://opentelemetry.io/docs/
- Prometheus instrumentation practices: https://prometheus.io/docs/practices/instrumentation/

## Release observability

A release should be identifiable in logs/metrics/traces. For affected paths, prefer signals that explain user/system outcomes:

```text
request/job volume
success/error categories
latency distribution
resource saturation
retry/dead-letter behavior
queue depth/age
migration/backfill progress
```

Keep metric label cardinality bounded; do not put user IDs, raw URLs, stack traces, tokens, or unbounded values into labels.

## Recovery

Recovery should identify the failed invariant and choose the smallest safe action:

- disable the feature;
- stop new intake while draining/requeuing work;
- roll back compatible code/config;
- roll forward a corrective artifact;
- reconcile/replay durable work;
- repair/restore data with database-specific controls.

Record what happened and what evidence shows recovery, rather than merely reporting that a restart or rollback command completed.
