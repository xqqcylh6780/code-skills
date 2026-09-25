# Native Android Project Decisions

Use this reference for native Kotlin/Java Android work. Google's [Android skills](https://github.com/android/skills) and [Android Developers](https://developer.android.com/) provide focused, current guidance for platform-specific tasks; consult the relevant topic when an API or policy may have changed.

## Establish the implementation surface

- Find the owning app/feature module, source sets, build variants, min/target SDK, Gradle plugins, and version catalog before adding code or dependencies.
- Identify whether the screen uses Compose, Views/XML, or existing interop. Continue its current approach unless the user requests a migration.
- Check the project's navigation, dependency injection, data, theme, localization, and test conventions in nearby features. Do not impose a template architecture on a small change.
- Inspect the manifest and merged manifest when components, intent filters, exported flags, permissions, or device capabilities are involved.

## UI behavior

- For Compose, follow existing state hoisting, lifecycle-aware state collection, side-effect, navigation, and Material/theme conventions. For Views, follow existing lifecycle owner, view binding, fragment/activity, and resource conventions.
- Keep UI strings and accessibility labels in the project's resource system. Check semantics or content descriptions, touch targets, and text scaling when modifying interactive UI.
- Handle system insets, keyboard, and predictive/back navigation according to the project's supported Android versions and current platform guidance.

## Build and release boundaries

- Prefer the repository's Gradle wrapper and existing tasks. Inspect task definitions, plugins, and hooks before execution.
- Treat manifest permissions, build variants, application ID, signing, min/target SDK, shrinker rules, and native libraries as release-affecting configuration. Change only what the requested feature needs.
- Verify the affected build variant; do not infer release behavior from a debug build.
