# Application Performance

## Backend

Check repeated remote/database calls, serialization volume, unnecessary copies, blocking work on async/event-loop paths, connection-pool saturation, retry amplification, queue depth, and lock scope before introducing new infrastructure.

Caching is an optimization only when key scope, freshness, invalidation, miss/outage behavior, and memory/cardinality limits are explicit.

## Web/mobile

Measure the target runtime. Common constraints include network waterfalls, oversized payloads/assets, excessive render work, unbounded lists, layout/media shifts, synchronous main-thread work, and duplicate fetching.

Do not use a browser-only measurement to claim native mobile performance parity, or a development build to claim production bundle/runtime performance.

## Database

Use `database-engineering` for SQL/index/plan changes. PostgreSQL plan guidance lives in the official documentation: https://www.postgresql.org/docs/current/using-explain.html
