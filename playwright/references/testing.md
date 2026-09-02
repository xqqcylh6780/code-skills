# Playwright Test Authoring

Read this reference only when the user requests Playwright test files or an authorized implementation requires browser tests.

## Inspect the repository first

Identify:

- `playwright.config.*` and existing test directories
- the package manager and lockfile
- existing scripts such as `test:e2e`
- fixtures, authentication setup, base URL, projects, reporters, and artifact policy
- naming and locator conventions in nearby tests

Do not create a second configuration or install `@playwright/test` when the repository already has a standard path.

## Write behavior-focused tests

- Name tests after observable user behavior.
- Arrange only the state required by the scenario.
- Interact through roles, labels, placeholders, visible text, or established test IDs.
- Assert the final user-visible result with Playwright's web-first `expect` assertions.
- Keep each test independent and safe to retry.
- Avoid coupling to DOM structure, generated class names, array positions, or incidental copy.
- Avoid `waitForTimeout`; wait for a locator, URL, response, or explicit application state.

Example:

```ts
import { test, expect } from '@playwright/test';

test('shows the saved profile name', async ({ page }) => {
  await page.goto('/profile');
  await page.getByLabel('Display name').fill('Ada');
  await page.getByRole('button', { name: 'Save' }).click();
  await expect(page.getByText('Profile saved')).toBeVisible();
  await expect(page.getByLabel('Display name')).toHaveValue('Ada');
});
```

Use project fixtures instead of hard-coded credentials or production data. Never commit storage state, cookies, tokens, or screenshots containing secrets.

## Verification

Run the narrowest existing command that covers the changed test. Do not start the application or alter test data unless the user has authorized that operation.

Report:

- test file and scenario covered
- command selected from the repository
- pass, fail, or not run
- captured trace, screenshot, or console evidence when relevant
- remaining environment or data prerequisites

