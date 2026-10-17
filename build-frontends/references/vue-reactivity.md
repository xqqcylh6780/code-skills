# Vue Reactivity and Ownership

Read for Vue state updates, computed/watch behavior, async races, or component data flow. Detect
the installed Vue/compiler version and preserve Options API, Composition API, and existing
composables/stores; this reference does not mandate a migration to script setup or TypeScript.

## Preserve reactive sources

Keep reactive reads connected to their owner. Copying a primitive property from a reactive object
into a local variable does not create a live binding. For a watched property, an explicit getter
such as `watch(() => props.itemId, ...)` identifies the source; passing its current scalar value
does not. Props-destructuring compiler behavior varies by Vue version, so inspect the actual
supported transform before rewriting it.

Mutate state through the reactive owner and understand whether an assignment replaces a ref's
value or abandons an existing object reference. Avoid maintaining a second local copy of a prop
unless it is deliberately an editable draft with reset/commit semantics.

## Derivation versus effects

Use a computed value for derived display/filtering data. Keep its getter free of requests and
mutations. A watch belongs to an effect such as loading a resource or synchronizing an external
API; do not build chains of watches to keep several redundant values equal.

Read the exact reactive dependencies inside the computed/getter. Keep heavy transformations out
of repeated template expressions when the same derived value can be shared. Do not introduce a
global store for coordination between two nearby components.

## Async cleanup

For an existing watcher-based request, register cleanup before awaiting. Cancel old work where
the transport supports it and guard stale results when cancellation cannot prevent completion.
Handle rejected requests and pending/error states; an aborted old request should not overwrite
the newest request's status.

Vue's cleanup APIs have version and timing requirements. Reuse the supported callback pattern or
existing project helper instead of copying a newer API blindly. Watchers created asynchronously
can have different ownership/cleanup behavior from those created during setup; inspect lifetime
before adding one. Verify rapid input changes and unmount when those trigger the reported defect.

Sources: [Reactivity fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html),
[Computed properties](https://vuejs.org/guide/essentials/computed.html),
[Watchers](https://vuejs.org/guide/essentials/watchers.html).
