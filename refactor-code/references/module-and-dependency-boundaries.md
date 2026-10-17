# Module and Dependency Boundaries

Use this reference when the refactor changes module ownership or dependency direction.

## Ownership

A module should own behavior and state that change for the same reason. Prefer moving policy toward the module that owns the invariant rather than creating a generic `utils` layer.

Judge a proposed module by what its callers gain from its interface. Imagine removing it: if
policy or orchestration would spread across callers, the module is carrying useful complexity;
if only a forwarding call disappears, prefer the simpler structure. Keep the interface small
enough that callers can use the capability without learning its internal steps.

## Dependencies

Map the current direction before moving code:

```text
caller → public capability → internal collaborators
```

Watch for:

- cycles;
- domain code importing transport/framework types;
- services importing concrete vendor clients everywhere;
- shared mutable globals;
- duplicated interfaces whose owners disagree;
- “common” modules that depend back on feature modules.

Introduce an adapter/interface only when it creates a real seam for ownership, testing, platform/vendor isolation, or migration. Do not abstract a one-line dependency merely to satisfy a diagram.

## Moves

Move one cohesive responsibility with its tests/callers in a controlled sequence. When many callers exist, a temporary forwarding adapter can reduce blast radius; remove it after migration rather than making it permanent accidentally.
