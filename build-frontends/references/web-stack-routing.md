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

For a concrete performance decision, read [React performance](react-performance.md). For a
shared/compound component or controlled-state API, read [React composition](react-composition.md).
Do not load either for an unrelated copy or spacing edit.

## Next.js

Identify the router before editing.

For version-dependent APIs, use [Next.js version-matched guidance](nextjs-versioned-guidance.md)
to locate relevant installed documentation before relying on remembered caching/RSC defaults.

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

For a reactive ownership, computed/watch, or async cleanup issue, read
[Vue reactivity](vue-reactivity.md). Check the installed version before using compiler-dependent
props destructuring or cleanup APIs.

## Framework-agnostic rule

For a TypeScript boundary, state variant, or generic relationship that affects correctness, read
[TypeScript boundaries](typescript-boundaries.md). Do not load it for plain JavaScript tasks or
change compiler flags merely to match a newer example.

For an existing shadcn/ui project, use [shadcn integration](shadcn-integration.md) only when the
component/configuration decision needs it. Its presence is not a reason to install shadcn/ui.

When a pattern is version-sensitive or uncertain, inspect the installed package version and current official
framework documentation before changing architecture. The existence of this reference never authorizes a framework
upgrade or migration.
