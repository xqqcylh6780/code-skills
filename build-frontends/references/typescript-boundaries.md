# TypeScript at Product Boundaries

Read when props/events, API data, nullable state, or reusable types affect a frontend change.
Preserve compiler strictness and nearby conventions. Do not enable repository-wide compiler flags
or introduce advanced type machinery for an isolated fix.

## Validate external values

A type assertion does not validate a network response. Use the existing runtime parser/schema
or narrow an `unknown` value before treating it as trusted. Do not replace an error with `any`,
a non-null assertion, or a double cast just to make type checking pass.

This illustrative parser deliberately checks only its two required public fields:

```ts
type Card = { id: string; title: string };

function isCard(value: unknown): value is Card {
  if (typeof value !== 'object' || value === null) return false;
  return 'id' in value && typeof value.id === 'string'
    && 'title' in value && typeof value.title === 'string';
}
```

Adapt validation to the actual contract, including nested values and allowed variants. This
predicate permits extra properties; do not mistake it for exact-schema validation. Type guards
themselves need correct runtime logic: their return annotation is not proof of the claim.

## Represent real alternatives

Use a discriminant when states carry different data, such as pending, failed(message), and
ready(items). Narrow on that discriminant before accessing variant fields. Avoid optional fields
that permit impossible combinations, but do not merge truly independent states into one union.

Preserve omitted/null/empty semantics and handle the missing case at the boundary. Make exhaustive
handling intentional for a closed union; if the external protocol can add variants, define its
unknown-variant behavior rather than asserting those values can never occur.

## Keep generic APIs understandable

Use a type parameter when it preserves a real relation between input and output. Prefer concrete
domain types when callers gain no such relation. Constrain keys and values only as far as the
operation requires; avoid broad assertions inside a generic function that make it appear sound.

Use the repository's existing type-check/test command, with the installed compiler, for the
changed boundary. Keep shared-contract compatibility in `design-interfaces` and teaching requests
in `programming-language-deep-learning`.

Sources: [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html),
[Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html).
