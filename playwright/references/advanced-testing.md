# Focused Playwright Test Patterns

Read only the section needed for authorized test authoring or failure investigation. Reuse the
repository's runner/configuration and inspect setup hooks before execution. These examples are
illustrative; they do not authorize account creation, data seeding, or external submissions.

## Authentication and fixtures

Reuse the existing setup-project or fixture contract. Shared authenticated state is suitable
when tests cannot interfere through the same account's server state. Tests that mutate shared
account state may need distinct worker-scoped accounts or isolated contexts; first confirm those
accounts and operations are authorized. A fresh browser context does not isolate backend data.

Treat `storageState` files as credentials. Keep them out of source control and public artifacts.
Do not re-login in every test by habit, or add a global login routine when the project already
has a working one. Diagnose expiry, redirects, and role mismatch before overwriting state.

Use test-scoped fixtures for per-test resources. Use worker-scoped fixtures only when their
lifetime and isolation match the scenario. Cleanup belongs to the fixture that created the
resource; do not delete shared user data as teardown. Database-write restrictions also apply
to setup/teardown, including local test databases.

## Controlled network failures

Register a narrow route before the navigation/action that issues the request. Exercise loading,
empty, denied, or failed responses without depending on an uncontrolled external service:

```ts
await page.route(url => url.pathname === '/api/boards', route => route.fulfill({
  status: 503,
  contentType: 'application/json',
  body: JSON.stringify({ code: 'TEMPORARILY_UNAVAILABLE' }),
}));
await page.goto('/boards');
await expect(page.getByRole('button', { name: 'Retry' })).toBeVisible();
```

Adapt the URL and response to the real API. Avoid broad mocks that hide unrelated integration
failures. A mock passing proves UI behavior for the simulated response, not the real service
contract, authentication, or database correctness.

## Visual regressions

Use the existing snapshot workflow only when visual regression tests are requested or needed.
Keep viewport, browser/OS, fonts, locale, clock, and input data stable. Compare a focused locator
when only one component matters. Mask only truly volatile regions; do not mask the control or
content under review. Match animation handling to the scenario rather than hiding animation bugs.

Inspect the actual image and diff before accepting a new baseline. Do not increase thresholds or
update all snapshots just to make failures pass. A screenshot assertion complements user-visible
behavior assertions and keyboard checks.

## Trace-led flaky-test diagnosis

Inspect the failing action, locator resolution, navigation, network, and visible state in the
existing trace. Check shared accounts, order dependence, unfinished requests, and late route
registration. Replace a fixed sleep with the specific observable assertion. Retries are evidence
of instability, not a repair. Capture traces/screenshots only as permitted; they can contain
private UI content, credentials, and responses.

Run the affected scenario first, then an additional worker/retry configuration only when it
tests the suspected isolation or timing cause. Report whether evidence came from a mock, a real
authorized service, a visual comparison, or a source check.

Sources: [Authentication](https://playwright.dev/docs/auth),
[Fixtures](https://playwright.dev/docs/test-fixtures), [Mock APIs](https://playwright.dev/docs/mock),
[Visual comparisons](https://playwright.dev/docs/test-snapshots),
[Trace viewer](https://playwright.dev/docs/trace-viewer).
