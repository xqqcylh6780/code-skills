# Mobile Engineering

Use this reference for lifecycle, state, networking, permissions, and device-oriented behavior independent of a specific framework.

## State by lifetime

Separate state by how long it should survive:

- component/view transient state;
- page/navigation state;
- authenticated app/session state;
- durable local preferences/cache;
- server-owned durable domain state.

Do not turn local storage into the authoritative copy of server-owned business state merely to make a screen convenient.

## Lifecycle

Assume pages and apps can be backgrounded, resumed, recreated, revisited, or interrupted. Make repeated lifecycle hooks idempotent where practical and avoid duplicate fetch/submission effects on resume.

## Networking

Every remote flow should define:

```text
loading:
timeout/cancellation behavior:
retryability:
offline/no-network state:
auth expiry:
duplicate submission behavior:
user-visible recovery:
```

Avoid infinite automatic retries and fixed sleeps. Preserve server idempotency for consequential writes.

## Permissions

Request only capabilities needed for the user action, preferably near the action with a recoverable denial path. Platform permission grants are not application authorization.

## Device UI

Check safe areas, status/navigation bars, keyboard/input overlap, text scaling, tap target size, orientation assumptions, and long/localized content where relevant. Treat “fits in one screenshot” as insufficient evidence of usability.
