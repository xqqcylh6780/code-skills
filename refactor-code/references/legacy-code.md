# Legacy Code Refactoring

Legacy code often lacks reliable tests, clear boundaries, or reproducible environments. Reduce uncertainty before large movement.

## Characterize before changing

Capture behavior at the highest stable seam practical. A characterization test records what supported behavior currently does; it is not an endorsement of every oddity.

Separate:

```text
supported behavior to preserve
known defect to fix separately
accidental behavior with unknown consumers
dead/unsupported behavior proven removable
```

## Create seams incrementally

Useful first moves include:

- wrap a global/vendor dependency behind one local adapter;
- extract pure decision logic from I/O;
- isolate parsing/serialization from domain state changes;
- make time/randomness/configuration injectable at a narrow boundary;
- introduce a façade around a large legacy module before splitting internals.

Avoid full rewrites unless incremental preservation is demonstrably more risky/costly and the replacement has an explicit compatibility and migration plan.
