# Redis

Authoritative source: https://redis.io/docs/latest/

Use Redis only when the project already depends on it or a concrete requirement justifies another stateful dependency.

For each use define:

```text
key namespace and tenant scope:
value/schema version:
TTL/retention:
source of truth:
invalidation owner:
behavior when Redis is unavailable:
```

- Do not use cache presence as authorization or durable business truth.
- Bound key/value size, cardinality, and TTL growth.
- Make serialization compatibility explicit across deployments.
- Use atomic Redis primitives only with a clear failure/recovery model; “single threaded” is not a substitute for reasoning about multi-command races.
- For queues/streams/locks, define delivery, acknowledgement, duplicate, lease/expiry, and recovery semantics rather than assuming a library's defaults imply exactly-once behavior.
