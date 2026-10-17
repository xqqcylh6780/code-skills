# React Component Composition

Read for a reusable component API, incompatible boolean props, duplicated ownership, or complex
controlled state. Preserve existing component conventions and supported React versions. Ordinary
private JSX does not require a component-library redesign.

## Replace impossible combinations

Before: `loading`, `failed`, and `empty` booleans can all be true. Model mutually exclusive states
where that matches the real behavior:

```ts
type ResultsState<T> =
  | { status: 'pending' }
  | { status: 'failed'; message: string }
  | { status: 'ready'; items: T[] };
```

An empty ready list is empty data, not another flag to synchronize. Keep genuinely independent
state independent; do not force unrelated selection and network states into one giant union.

## Choose the narrowest useful API

- Fixed product variants: use named variants with explicit meaning and defaults.
- Flexible content/layout: pass children or semantic slots instead of flags for every arrangement.
- Coordinated parts such as a picker trigger and options: compound components can share a small
  provider owned by that picker instance. Nested instances must not accidentally share selection.
- Several siblings coordinating the same value: lift that value to their nearest common owner.

Derive the selected object from its stable ID and source list rather than retaining a stale second
copy. Avoid duplicating derived values in effects.

## Controlled behavior and context

For a controlled input, the caller owns the current value and receives change events. For an
uncontrolled input, an initial/default value seeds internal state; document which model applies
and avoid switching between them during a component lifetime.

Before adding context, consider explicit props and composition. Use context for data that really
belongs to multiple descendants; keep its value small and give a clear error for a required part
rendered outside its owner. Preserve the actual library's focus, keyboard, label, disabled, and
form-submission semantics when adding wrappers.

A shared API change also uses `design-interfaces` for compatibility. Do not mechanically replace
`forwardRef`, context access, or provider syntax from an online example: check the installed React
version and existing library consumers first. Verify two independent instances, controlled value
updates, and the affected keyboard path when those are relevant.

Sources: [Choosing state structure](https://react.dev/learn/choosing-the-state-structure),
[Passing data with context](https://react.dev/learn/passing-data-deeply-with-context).
