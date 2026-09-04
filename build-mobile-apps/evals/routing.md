# Routing Examples

## Should trigger

- “Build this uni-app Vue 3 seller list page with Wot Design Uni.”
- “Fix the Android safe-area and keyboard overlap in this uni-app form.”
- “Add an App permission flow for selecting and uploading a photo.”
- “Implement this page for H5 and WeChat mini program with a platform-specific file API.”
- “Verify this uni-app route and lifecycle behavior on App.”

## Should not trigger

- “Build a Next.js dashboard.” → `build-frontends`.
- “Implement the Python endpoint consumed by the mobile app.” → `build-backends`.
- “Design the JSON response contract shared by several clients.” → `design-interfaces`.
- “Why does the Android build crash? We do not know the cause.” → `diagnose-bugs` first.
- “Review the mobile PR without changing it.” → `review-changes`.

## Conflict cases

- “Add login to a uni-app client and the backend.” → `design-interfaces` if the contract changes, `secure-boundaries`, `build-mobile-apps`, and `build-backends` for their owned surfaces.
- “A Wot form works in H5 but fails in the mini program for an unknown reason.” → `diagnose-bugs` first; return to `build-mobile-apps` after the failing boundary is localized.
- “Refactor several uni-app pages into shared composables without changing behavior.” → `refactor-code`, with `build-mobile-apps` references as needed for platform semantics.
