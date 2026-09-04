# Web Stack Routing

Read this reference when framework-specific behavior affects a browser frontend task. Detect the existing stack
first and preserve it. Do not migrate frameworks, routers, state libraries, styling systems, or component libraries
as an incidental implementation choice.

## Detect the repository

Inspect `package.json` plus the nearest config/entry files before choosing patterns:

- React: React packages, JSX/TSX, router/state conventions, component library.
- Next.js: `next` dependency and whether the repository uses App Router, Pages Router, or both.
- Vue: Vue version, SFCs, Composition vs Options API, Vue Router, Pinia/Vuex, component library.
- Vite: treat Vite as build tooling; identify the actual UI framework instead of calling the project “a Vite app”.
- Styling: preserve Tailwind, CSS Modules, scoped CSS, Sass, CSS-in-JS, utility classes, or design-token conventions
  already used by the project.
- Testing: preserve Vitest/Jest, Testing Library, Cypress/Playwright, Storybook, or repository-specific harnesses.

Use checked-in package-manager files and scripts (`pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`, Bun lockfiles,
workspace config) rather than silently switching package managers.

## React

- Preserve the repository's component and hook conventions.
- Keep state at the narrowest owner; do not add global state for local coordination.
- Do not add memoization, effects, or abstraction layers by habit.
- Keep server/cache state in the project's established data-fetching layer when one exists.
- Use stable identity keys for reorderable data and clean up subscriptions/timers/listeners.

## Next.js

Identify the router before editing.

- Do not convert Pages Router to App Router or the reverse for an ordinary feature.
- Respect existing server/client component boundaries; do not add `use client` broadly just to access one browser API.
- Keep data fetching, caching, revalidation, route handlers, metadata, and navigation consistent with the installed
  Next.js version and the repository's current patterns.
- Verify direct-route loads and production/preview behavior when routing, assets, SSR, or hydration changes.

## Vue

- Preserve Composition API vs Options API conventions already used nearby.
- Reuse existing composables, stores, router patterns, and component library.
- Keep props/events and two-way binding explicit; avoid duplicating derived state across refs/stores.
- Respect scoped styling and existing design-token/theme mechanisms.

## Framework-agnostic rule

When a pattern is version-sensitive or uncertain, inspect the installed package version and current official
framework documentation before changing architecture. The existence of this reference never authorizes a framework
upgrade or migration.
