# React Performance Decisions

Read for a React request waterfall, duplicate server work, heavy client bundle, or measured render
problem. Start with the installed React/framework version and existing data layer. A small style
edit does not need this reference. Examples use illustrative project loader names.

## Start independent work together

Before (unnecessary dependency):

```ts
const board = await loadBoard(boardId);
const people = await loadPeople(teamId);
```

After, only when neither request depends on the other:

```ts
const [board, people] = await Promise.all([
  loadBoard(boardId),
  loadPeople(teamId),
]);
```

Preserve authorization and real dependencies: tenant membership must be established before a
protected fetch. Decide whether one failure should reject both results; optional regions can
have their own error/loading boundaries instead. Check request timing rather than assuming
parallel syntax improved the actual critical path.

## Deduplicate within the right lifetime

For a supported Server Component environment, a shared module can export one React `cache`
wrapper around an existing loader. Consumers must reuse that wrapper; creating it inside each
component defeats sharing. Prefer primitive arguments with stable values and include the relevant
actor/tenant scope where the loader requires it.

React `cache` is server-render request memoization, not a durable application cache or a client
query store. It also memoizes errors. Keep existing authorization checks and the project's cache
invalidation contract; do not add process-global maps for private user responses.

## Keep optional work off the initial path

Inspect the actual imports and bundle evidence before changing them. A client-side editor used
only after an explicit action can use the project's code-splitting pattern; React `lazy` belongs
at module scope with an appropriate Suspense fallback. Preserve server rendering requirements,
keyboard focus, and error recovery. Do not replace every import with a dynamic import.

At a server/client boundary, pass only fields the interactive child needs. Browser-only behavior
does not require moving the full page, data loader, and heavy server dependencies to the client.

## Optimize renders from evidence

Locate the expensive interaction with the existing profiler or render evidence. First remove
duplicate state, unnecessary effects, and broad subscriptions. Add `memo`, `useMemo`, or
`useCallback` only when their cost model and prop identities support a benefit; account for an
existing React Compiler configuration instead of mechanically layering memoization.

Verify the affected interaction and request/bundle/render evidence under comparable conditions.
Keep speculative micro-optimization outside ordinary feature work.

Sources: [Server Components](https://react.dev/reference/rsc/server-components),
[cache](https://react.dev/reference/react/cache), [lazy](https://react.dev/reference/react/lazy),
[memo](https://react.dev/reference/react/memo).
