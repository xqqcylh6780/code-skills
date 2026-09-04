# Refactoring Loop

Reference catalog: https://refactoring.com/catalog/

Refactoring is a sequence of small behavior-preserving transformations, not a rewrite labeled cleanup.

## Loop

```text
select one structural problem
↓
establish a protection seam
↓
make one small transformation
↓
run focused verification
↓
inspect behavior/diff
↓
repeat only if the target still requires it
```

## Good protection seams

Prefer stable observable boundaries:

- public/module function behavior;
- service/domain outcomes;
- HTTP/event contract;
- persistence state/invariants;
- rendered interaction for UI;
- characterization test for legacy behavior.

Avoid tests that freeze private call order or the very structure being changed.

## Common transformations

Use the smallest suitable transformation: rename, extract function/value/class, move function, encapsulate variable/state, introduce adapter, simplify conditional, replace duplicated policy, or remove proven dead code.

The catalog is a vocabulary, not a mandatory sequence. Preserve project conventions and choose transformations that reduce the actual change cost.
