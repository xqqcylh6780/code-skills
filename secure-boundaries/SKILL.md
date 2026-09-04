---
name: secure-boundaries
description: >-
  Design, implement, or review controls at a meaningful trust boundary. Trigger for
  authentication, authorization, tenancy, secrets, sensitive data, uploads, SSRF,
  webhooks/payments, crypto, privileged effects, or untrusted/model output. Do not run a full
  security workflow for ordinary low-risk code.
---

# Secure Boundaries

Secure the places where data, identity, privilege, and side effects cross trust boundaries. Start from assets and abuse cases, apply controls at the owning boundary, and prove both allowed and denied behavior.

## Select the Requested Outcome

- **Review/assessment:** inspect existing controls and available evidence without edits. Report
  supported findings, proposed controls, and unverified risks. Do not add tests, change permissions,
  rotate credentials, or repair configuration merely to complete a review.
- **Design:** deliver invariants, control placement, tradeoffs, and a verification plan; do not
  implement or mutate live state unless the user also requests it.
- **Implementation:** make the authorized control changes and verify allowed and denied behavior
  at the affected boundary. A security-related topic alone is not implementation authorization.

Apply the implementation and test-creation steps below only in Implementation mode. In Review or
Design mode, assess existing evidence or describe proposed checks instead. Runtime probes must
stay within the task's execution and side-effect permissions in every mode.

## Activation Threshold

Use this skill when the requested change creates, modifies, or evaluates a boundary where failure
could expose sensitive data, cross an identity or tenant boundary, grant privilege, execute
attacker-influenced content, move money, reach protected networks, or cause another consequential
effect.

Do not load the full security workflow for routine persistence, display-only browser work, ordinary
API consumption, dependency use, or internal refactoring with no changed trust boundary. Apply the
repository's normal secure coding conventions in those tasks without turning them into a threat
modeling exercise.

### Focused-boundary fast path

When the task changes one established control at one known boundary and introduces no new actor,
data class, privilege, execution capability, or external effect, keep the work narrow: state the
security invariant and inspect the existing control pattern. For implementation, make the smallest
change and prove the allowed case and relevant denied case; for review/design, assess the evidence
or propose the control without edits. Inspect runtime configuration only when it can alter that
control. Do not produce a full threat model or abuse-case inventory unless the change creates
a new trust relationship or materially broadens impact.

## Security Posture

- Treat all external input and output as untrusted until validated: requests, files, configuration, dependencies, third-party responses, webpages, logs, retrieved documents, model output, and tool output.
- Enforce authentication and authorization in code at the protected action.
- Deny by default when identity, policy, tenancy, validation, or security configuration is absent or ambiguous.
- Use established platform primitives for sessions, password hashing, encryption, signatures, and secret storage.
- Minimize privileges, sensitive data, exposed surface, execution time, and dependency count.
- Preserve usability and operability; controls that cannot be monitored, recovered, or used correctly will be bypassed.
- Do not claim security from a checklist alone. Require negative tests and runtime evidence.

## Workflow

### 1. Define Scope and Security Invariants

Identify the exact feature, entry points, affected components, deployment environments, and data categories. State invariants such as:

```text
Only the owner or an administrator can read this record.
No caller-controlled value becomes executable syntax.
The server never fetches private or metadata-network addresses.
One idempotency key can produce at most one payment effect.
Secrets and cross-tenant data never enter logs or model context.
```

Separate confidentiality, integrity, availability, authenticity, accountability, and privacy requirements. Note applicable organizational or regulatory constraints without inventing compliance claims.

### 2. Map Trust Boundaries, Assets, and Effects

Inventory:

- Entry points: HTTP, UI, CLI, files, messages, jobs, configuration, dependencies, plugins, and model/tool output.
- Actors: anonymous users, authenticated users, tenants, administrators, services, operators, and compromised dependencies.
- Assets: credentials, personal data, money, entitlements, intellectual property, infrastructure, audit records, and availability.
- Trust changes: browser to server, service to service, tenant to shared store, model to tool, worker to shell, application to third party.
- Outbound effects: queries, writes, file operations, shell execution, network calls, messages, email, payments, and privileged tools.

Draw a small data-flow map for multi-step or cross-system features. Mark where identity is established, data is validated, authorization is decided, and effects occur.

### 3. Enumerate Abuse Cases and Rank Risk

For each important flow ask how an attacker or compromised component could:

- Spoof identity.
- Tamper with input, state, or messages.
- Repudiate a privileged action.
- Disclose sensitive data.
- Exhaust resources or block service.
- Elevate privilege or cross tenant boundaries.

Also consider replay, enumeration, confused deputy, injection, unsafe deserialization, race conditions, supply-chain compromise, and business-logic abuse.

Rank by plausible impact, reachability, attacker capability, exposure, and existing controls. Focus implementation on realistic high-impact paths rather than generating a long unprioritized list.

### 4. Choose Layered Controls

Prefer this order:

1. Remove an unnecessary capability or data flow.
2. Reduce exposure and privilege.
3. Establish identity and per-action authorization.
4. Validate and normalize input into a narrow schema.
5. Use safe APIs and context-specific encoding.
6. Bound time, size, rate, memory, recursion, and retries.
7. Add integrity, replay, concurrency, and idempotency controls.
8. Record safe audit evidence and detect abuse.
9. Define recovery, revocation, rollback, and incident handling.

Controls should live at the boundary that owns the invariant. UI hiding, prompt instructions, client validation, network location, and obscurity are not authorization boundaries.

### 5. Implement Input and Execution Safety

Validate external data for type, shape, length, encoding, range, allowed values, nesting, and total processing cost. Reject or safely ignore unknown fields according to the contract.

- Parameterize database queries.
- Use structured process APIs with fixed executables and separate arguments; avoid shell composition.
- Resolve and constrain file paths beneath an approved root; defend against traversal, symlinks, device paths, and archive expansion.
- Encode output for its destination context: HTML, attribute, URL, JavaScript, CSS, log, or CSV.
- Avoid dynamic evaluation and unsafe deserialization.
- Validate third-party and model-generated output before it influences decisions or actions.

Do not rely on blacklist filtering when an allowlist or typed representation is available.

### 6. Implement Identity, Authorization, and Tenancy

Use established authentication flows. Define credential issuance, storage, expiry, refresh, rotation, revocation, logout, and compromised-session behavior.

At every protected action:

1. Establish the authenticated principal from a trusted mechanism.
2. Derive tenant and ownership scope from trusted identity or policy.
3. Check permission for the specific resource and action.
4. Revalidate after material state changes when time-of-check/time-of-use matters.
5. Audit privileged outcomes without recording secrets.

Test horizontal access, vertical privilege escalation, tenant crossing, object enumeration, and policy failure. Authentication alone does not grant authorization.

### 7. Protect Secrets and Sensitive Data

- Keep real secrets out of source, prompts, fixtures, screenshots, command lines, URLs, logs, and error responses.
- Use a secret manager or platform credential store and least-privilege identities.
- Redact tokens, session identifiers, authorization headers, and sensitive fields centrally.
- Collect, retain, return, and expose only required data.
- Separate tenant data and protect backups, exports, caches, analytics, and support tooling.
- Rotate or revoke exposed credentials; deleting the text is not remediation.
- Use established cryptographic libraries and protocols; do not invent algorithms, formats, or key management.

Document data deletion, retention, recovery, and audit requirements when the feature introduces a new sensitive-data category.

### 8. Harden Surface-Specific Boundaries

Read [references/security-checklist.md](references/security-checklist.md) and load only the relevant sections for:

- Web/browser and cross-origin behavior.
- Authentication, sessions, and recovery.
- Authorization and multi-tenancy.
- SQL, command, template, and log injection.
- Files, archives, and media processing.
- Server-side URL fetching and redirects.
- Webhooks, external services, payments, and queues.
- Dependencies, CI, artifacts, and supply chain.
- LLMs, retrieval, agents, plugins, and tool execution.
- Availability, rate limits, logging, and incident response.

Verify framework- and provider-specific settings against current official documentation when versions or security defaults may have changed.

### 9. Test Abuse Cases

For each security invariant, add at least one allowed case and relevant denied cases. Cover as applicable:

- Malformed, boundary, oversized, deeply nested, duplicate, and unexpected input.
- Missing, expired, forged, or wrong identity.
- Cross-user, cross-role, and cross-tenant access.
- Injection payloads at each executable or rendering context.
- Replay, double submission, race, cancellation, and partial failure.
- Unsafe URLs, redirects, file names, archive entries, and content types.
- Rate, timeout, memory, and workload limits.
- Error, log, cache, analytics, and response leakage.
- Dependency or external-service failure and compromised output.

Prove rejection at the server-side boundary. A test that only confirms a hidden button or client-side validation is insufficient.

### 10. Verify the Running System

Use runtime evidence where possible:

- Response headers, cookies, CORS, redirects, and cache behavior.
- Authorization outcomes using principals from different roles and tenants.
- Actual outbound destinations, DNS/redirect handling, and network egress restrictions.
- File storage path, permissions, serving behavior, and processing isolation.
- Audit events, redaction, rate limits, timeouts, and resource caps.
- Dependency audit disposition, immutable install, signatures or provenance when used.
- Failure responses under dependency outage or invalid security configuration.

Inspect source and runtime configuration together; secure code can be defeated by deployment settings.

### 11. Review Rollout and Recovery

Before shipping a security-relevant change, define:

- Backward-compatibility and migration impact.
- Credential or key rotation procedure.
- Feature disablement or rollback path.
- Detection signals and alert ownership.
- Data repair or notification obligations if the control fails.
- Residual risk and accepted assumptions.

Do not silently broaden permissions, data collection, network access, CORS, file handling, or destructive capability. Surface material scope changes for explicit approval.

## Output Format

Return:

```text
Scope and assets:
Trust boundaries and actors:
Security invariants:
Priority abuse cases:
Controls assessed, proposed, or implemented (label which):
Allowed/denied evidence and proposed or unrun checks:
Operational detection and recovery:
Residual risks and assumptions:
```

## Completion Criteria

Review is complete with evidence-backed findings, control assessment, and explicit verification
limits; design is complete with actionable invariants, control placement, and a verification plan.
Neither mode requires fixes or new tests. Implementation requires controls enforced at the owning
boundary, allowed and denied behavior tested where feasible, runtime configuration inspected where
relevant, and residual risk stated without overclaiming. Keep boundary and abuse-case detail
proportionate to the task. Route ordinary implementation back to the relevant build skill and release/runtime
hardening to `deploy-and-operate` rather than expanding this skill beyond the trust boundary.
