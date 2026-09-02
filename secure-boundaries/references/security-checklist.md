# Security Boundary Checklist

Read only the sections that match the current attack surface. Verify framework-, provider-, and version-specific settings against current official documentation.

## Table of contents

- Input, parsing, and injection
- Authentication and account lifecycle
- Sessions, tokens, and cookies
- Authorization and multi-tenancy
- Browser output, CORS, CSRF, and headers
- Files, archives, and media
- Server-side URL fetching
- External services, webhooks, payments, and queues
- Secrets, cryptography, and sensitive data
- Dependencies, builds, CI, and artifacts
- Availability and abuse resistance
- Logging, audit, privacy, and incident response
- AI, retrieval, agents, plugins, and tools
- Verification evidence

## Input, parsing, and injection

- Validate type, shape, length, encoding, range, allowed values, collection size, nesting, and total processing cost at entry.
- Normalize once and validate the canonical form; watch for Unicode, percent-encoding, path, hostname, and case-normalization discrepancies.
- Parameterize database queries; allowlist dynamic identifiers that cannot be parameters.
- Use structured process execution with a fixed executable and separate arguments. Avoid invoking a shell for untrusted values.
- Avoid `eval`, unsafe deserialization, dynamic templates, and expression engines on untrusted input.
- Encode output for the exact destination context: HTML text, attribute, URL, JavaScript, CSS, log, CSV, or command output.
- Reject duplicate or ambiguous parameters when libraries disagree about which value wins.
- Cap decompressed size and parser work to prevent bombs and pathological inputs.
- Keep error messages useful without exposing schemas, queries, paths, stack traces, or secrets.

## Authentication and account lifecycle

- Use established identity providers and maintained authentication libraries.
- Verify passwords with modern adaptive password hashing; do not encrypt passwords reversibly.
- Protect login, recovery, enrollment, verification, and token endpoints from brute force and enumeration.
- Make recovery no weaker than primary authentication; expire and single-use recovery artifacts.
- Define multi-factor enrollment, challenge, fallback, reset, and recovery behavior.
- Reauthenticate for sensitive changes when risk warrants it.
- Define account disablement, deletion, credential rotation, and compromised-account response.
- Avoid revealing whether an account exists through status, wording, timing, or side effects when enumeration matters.

## Sessions, tokens, and cookies

- Generate identifiers with cryptographically secure randomness.
- Rotate session identifiers after authentication, privilege change, and recovery.
- Set cookie `Secure`, `HttpOnly`, `SameSite`, path, domain, and lifetime deliberately.
- Define idle and absolute expiry, refresh, revocation, logout, and concurrent-session behavior.
- Bind tokens to the correct issuer, audience, client, redirect URI, nonce/state, and supported algorithm.
- Do not accept algorithm or key confusion from untrusted token metadata.
- Store browser credentials using the safest mechanism supported by the architecture; minimize exposure to script.
- Protect refresh and access tokens in logs, analytics, URLs, crash reports, and support tooling.

## Authorization and multi-tenancy

- Enforce permission at every protected resource and action, including bulk, export, search, admin, background, and indirect paths.
- Derive user, tenant, owner, price, entitlement, and role from trusted state rather than request fields.
- Deny by default when policy data is missing, stale, or ambiguous.
- Test horizontal and vertical escalation, tenant crossing, object enumeration, and alternate identifiers.
- Apply scope to database queries, caches, indexes, object storage, events, and analytics—not only controller code.
- Protect privileged workflows from confused-deputy behavior and untrusted delegated parameters.
- Recheck permission for long-running jobs and time-of-check/time-of-use-sensitive actions when appropriate.
- Audit privileged changes with actor, target, action, decision, and outcome.

## Browser output, CORS, CSRF, and headers

- Rely on framework auto-escaping and avoid raw HTML paths; sanitize only with maintained context-appropriate tools when raw markup is required.
- Avoid inserting untrusted strings into JavaScript, CSS, URL, or HTML attribute contexts.
- Restrict CORS to intended origins, methods, headers, and credentials behavior. Do not reflect arbitrary origins.
- Protect cookie-authenticated state changes from CSRF using appropriate SameSite, tokens, and origin checks.
- Configure content security, transport security, MIME sniffing, framing, referrer, and permissions policies appropriate to deployment.
- Avoid open redirects and validate navigation targets.
- Keep secrets out of browser bundles, source maps, DOM, client logs, local storage, and analytics.
- Test authorization independently of hidden controls or disabled buttons.
- Protect sensitive responses from shared caches and browser history where needed.

## Files, archives, and media

- Allowlist intended file types using verified content and parsing, not only name or client MIME type.
- Generate server-side names and store uploads outside executable and public paths by default.
- Enforce per-file, total, count, decompressed-size, dimension, page, duration, and processing-time limits.
- Prevent traversal, absolute paths, alternate separators, device names, symlink/hardlink escape, and archive bombs.
- Re-encode or sanitize complex formats when active content or metadata is risky.
- Process untrusted media or documents in a least-privilege isolated worker when impact warrants it.
- Scan or quarantine before downstream use according to risk.
- Serve downloads with safe content type, disposition, caching, and authorization.
- Delete temporary and rejected files reliably without leaking cross-tenant artifacts.

## Server-side URL fetching

- Prefer allowlisted services, schemes, ports, and destinations.
- Parse URLs with a maintained library; reject embedded credentials and ambiguous forms.
- Resolve and block loopback, private, link-local, multicast, unspecified, metadata, and other reserved addresses for both IPv4 and IPv6.
- Validate every redirect target or disable redirects.
- Protect against DNS rebinding and resolution/connect time-of-check/time-of-use gaps; enforce egress policy at the network layer for high-risk services.
- Bound connect/read timeouts, response size, redirects, decompression, and supported content types.
- Do not forward user credentials or internal headers to arbitrary destinations.
- Revalidate URLs supplied indirectly through feeds, manifests, model output, or third-party responses.

## External services, webhooks, payments, and queues

- Validate external responses before using them in decisions, storage, or rendering.
- Set explicit timeouts and bounded retries with jitter only for safe/retryable operations.
- Verify webhook authenticity according to the protocol, often against the raw payload.
- Reject stale or replayed events using timestamp, nonce, or event identifiers when available.
- Make handlers idempotent and safe for duplicate and out-of-order delivery.
- Scope service credentials to minimum resources and actions.
- For payments and other high-impact effects, bind amount, currency, recipient, order, and caller authorization to trusted server state.
- Separate acknowledgement from completion for long work; use durable queues and terminal failure handling.
- Treat sandbox and production credentials, endpoints, and data as distinct.
- Define behavior under partial failure so retries do not duplicate side effects.

## Secrets, cryptography, and sensitive data

- Keep real secrets out of repositories, prompts, fixtures, logs, screenshots, URLs, error messages, and command arguments.
- Use secret managers or platform stores and short-lived credentials where possible.
- Rotate exposed secrets immediately and assess downstream use; deletion alone is insufficient.
- Use maintained cryptographic libraries, secure random generation, authenticated encryption, and documented protocols.
- Separate keys by purpose and environment; define storage, access, rotation, revocation, backup, and destruction.
- Avoid custom cryptography, hard-coded keys, predictable nonces, weak password hashing, and encryption without integrity.
- Minimize collected and returned personal or regulated data.
- Define retention, deletion, export, backup, and recovery behavior.
- Redact or tokenize sensitive fields consistently across application, infrastructure, analytics, and support logs.

## Dependencies, builds, CI, and artifacts

- Keep one authoritative lockfile per installation boundary and use frozen/immutable installs in CI.
- Review new dependencies for necessity, ownership, provenance, maintenance, release history, transitive graph, native code, and install scripts.
- Block or explicitly approve dependency install scripts when the ecosystem supports it.
- Triage advisories by affected version, reachability, exploitability, exposure, compensating controls, and upgrade risk.
- Do not apply blind broad upgrades solely to reduce an audit count.
- Pin external actions, images, toolchains, and build inputs where integrity and reproducibility matter.
- Protect CI tokens, secrets, forks, untrusted pull requests, caches, and artifact upload/download paths.
- Generate provenance, signatures, or software bills of materials when the delivery risk justifies them.
- Separate build and release authority; make artifacts immutable after approval.

## Availability and abuse resistance

- Bound request bodies, collection sizes, pagination, query complexity, file processing, recursion, fan-out, and job duration.
- Set timeouts, concurrency limits, queue caps, circuit breakers, and backpressure at expensive boundaries.
- Rate-limit by a dimension attackers cannot trivially rotate when possible; protect authentication and recovery endpoints specifically.
- Prevent high-cardinality logs, metrics, cache keys, and unbounded error detail.
- Define behavior during dependency degradation; avoid retry storms and synchronized retries.
- Test cancellation and cleanup so abandoned work does not continue consuming resources.
- Separate quotas and resources across tenants where noisy-neighbor impact matters.

## Logging, audit, privacy, and incident response

- Log security-relevant decisions with timestamp, actor, target, action, outcome, and correlation identifier.
- Do not log raw credentials, tokens, sensitive payloads, or unnecessary personal data.
- Protect audit integrity, access, retention, and tenant separation.
- Distinguish operational logs from security audit records and analytics.
- Alert on actionable signals such as repeated denied access, credential abuse, policy failures, anomalous privileged actions, and verification failures.
- Define ownership, investigation steps, containment, credential rotation, data repair, and notification paths.
- Test that logging and failure reporting still work under degraded conditions without leaking internals.

## AI, retrieval, agents, plugins, and tools

- Treat prompts, retrieved content, webpages, documents, model output, tool output, plugin metadata, and logs as untrusted.
- Keep secrets, hidden instructions, and cross-tenant data out of model context unless strictly required and authorized.
- Parse model output into a narrow schema; validate types, ranges, identifiers, destinations, and action allowlists.
- Enforce authorization and tenancy in code. Prompts and model policies are not authorization controls.
- Separate planning from execution and require confirmation for destructive, financial, externally visible, or privilege-changing actions.
- Scope tools, network, files, credentials, and plugins to least privilege.
- Cap tokens, iterations, tool calls, recursion, requests, execution time, and output size.
- Defend against indirect prompt injection in retrieved content and tool results; never follow embedded instructions merely because they appear in data.
- Do not pass model output directly to SQL, shell, `eval`, raw HTML, file paths, network destinations, or privileged tools.
- Record safe action audit events and preserve the human or system authorization chain.

## Verification evidence

- Positive tests prove intended authorized behavior.
- Negative tests prove malformed, unauthorized, cross-tenant, replayed, oversized, and injected cases are rejected.
- Runtime inspection confirms headers, cookies, CORS, cache, redirects, authorization, rate limits, and outbound destinations.
- Error responses and logs omit internals and sensitive values.
- Dependency findings have explicit dispositions; installs and artifacts are reproducible where required.
- Security configuration fails closed when missing or invalid.
- Recovery, rotation, rollback, and feature-disable paths are documented or exercised proportionately to risk.
- Residual risks, assumptions, and unverified environment controls are written down.
