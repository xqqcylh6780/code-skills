# WebSocket Services

Use this reference when the existing server exposes persistent WebSocket connections.

Define:

```text
connection authentication:
authorization / channel scope:
message schema/version:
heartbeat / idle timeout:
server/client reconnect policy:
backpressure / queue bound:
duplicate/order semantics:
shutdown behavior:
```

- Revalidate authorization when subscription/resource scope changes; connection authentication alone does not authorize every message.
- Bound per-connection memory and outbound queues; decide what happens to slow consumers.
- Make reconnect/resubscribe idempotent and distinguish at-most-once connection delivery from durable application guarantees.
- Avoid broadcasting sensitive cross-tenant data through shared channel keys.
- Emit connection/message error metrics with bounded labels and correlation context where useful.
- For public message contracts, route schema/evolution decisions through `design-interfaces`.
