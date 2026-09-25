---
name: build-mobile-apps
description: >-
  Build or modify native Android apps using the project's Kotlin or Java, Jetpack Compose
  or Views stack. Use for Android screens, navigation, lifecycle, permissions, device APIs,
  Gradle packaging, and device behavior. Excludes browser, uni-app, Flutter, and React Native work.
---

# Build Native Android Apps

Implement the requested Android user path in the repository's existing stack. Preserve its UI system, architecture, build variants, and supported Android versions. Do not introduce Compose, Views, new libraries, or architecture layers solely because this skill mentions them.

## Scope and routing

- Use for native Android projects: Kotlin or Java with Android SDK, Jetpack Compose, or Android Views/XML.
- Use `build-frontends` for browser pages. This skill does not route uni-app, Flutter, React Native, or mini-program work.
- Use `design-interfaces` for shared API contracts and `build-backends` for server changes.
- Use `secure-boundaries` when authentication, tokens, privileged deep links, sensitive local data, or untrusted files cross a trust boundary. Handle ordinary Android permission prompts and denial recovery here.
- Use `diagnose-bugs` first when the cause of a build, crash, or device failure is unknown.

## Work size

For a copy, color, spacing, or icon edit with no platform behavior, inspect the owning UI and make a focused change. A small diff involving insets, keyboard, back navigation, lifecycle, or permissions still needs platform-specific checking.

For a new screen or flow, or a material behavior change, follow the workflow below. Read [references/android-native.md](references/android-native.md) for Android project and UI decisions. Read [references/mobile-engineering.md](references/mobile-engineering.md) when state, networking, permissions, or lifecycle behavior changes.

## Workflow

1. **Recover the project contract.** Inspect the app module, Gradle settings and version catalog, manifest, min/target SDK, build variants, nearby screens, navigation, theme/resources, state and data patterns, and relevant test entry points. Inspect script entry points and hooks before running them.
2. **Define the affected Android behavior.** Identify supported API levels and form factors relevant to the request. Check whether configuration change, process recreation, app background/resume, system bars, keyboard, back navigation, or a denied permission can interrupt the flow.
3. **Implement the complete requested path.** Follow the existing Compose or Views approach and reuse components. Keep UI state and business effects in the project's established layers. Cover applicable loading, empty, error, pending, and success states; handle one-time effects and cancellation where they matter.
4. **Verify at the appropriate level.** Use [references/app-verification.md](references/app-verification.md). Run safe, scoped source/build/test checks where available. Compare an actual Android render with supplied design references when visual fidelity matters. Use an already available emulator/device or an explicitly authorized device run for behavior that compilation cannot prove. State what was actually verified.

## External effects

Do not install SDKs or dependencies, create signing credentials, publish to a store, or add unrelated permissions as a shortcut. Preserve signing and release configuration unless the task explicitly requires a change. Follow the active workspace's execution and approval rules before launching Android Studio, an emulator, or a background process.

## Handoff

Report the implemented user path, Android stack and variants affected, checks run, and any remaining device, signing, or release verification. Do not claim device behavior was tested from source inspection or a successful build alone.
