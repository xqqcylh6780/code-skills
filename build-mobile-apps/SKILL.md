---
name: build-mobile-apps
description: >-
  Build or modify uni-app, mobile, mini-program, or cross-platform app UI and flows. Trigger
  when lifecycle, device APIs, permissions, safe areas, native packaging, HBuilderX, or
  App/mini-program behavior matters. Use build-frontends for browser-only Web UI.
---

# Build Mobile Apps

Build the requested user path for the actual target platforms, preserving the repository's stack and component system. Treat platform lifecycle, navigation, network state, permissions, safe areas, packaging, and runtime verification as product behavior rather than browser details.

## Activation Threshold

Use this skill when the requested surface targets a mobile/cross-platform application runtime or depends on platform APIs/packaging. For browser-only UI use `build-frontends`.

This skill is framework-neutral at the workflow level. The bundled stack references initially focus on uni-app/Vue 3 and Wot Design Uni because they are common repository targets; they are not a mandate to migrate other mobile stacks.

## Route Adjacent Work

- Browser-only web interface → `build-frontends`.
- Public/shared API or event contract → `design-interfaces`.
- Server behavior → `build-backends`.
- Authentication, permissions, tokens, uploads, deep links with privileged effects, or sensitive local data → `secure-boundaries`.
- Unknown runtime/build/device failure → `diagnose-bugs`.
- Browser/H5 flow automation → `playwright` where it faithfully covers the target; do not claim H5 proves native App behavior.

## Workflow

### 1. Recover the app contract

Inspect the smallest set of repository files that establishes:

- framework/runtime and version conventions;
- page/navigation configuration;
- component/design system;
- state/network/storage patterns;
- target platforms;
- conditional compilation;
- app/page lifecycle use;
- manifest/permission configuration;
- package/build/test entry points;
- nearby pages and user flow.

For uni-app, read [references/uni-app.md](references/uni-app.md) when the task crosses routing, lifecycle, `uni.*` APIs, conditional compilation, App packaging, or mini-program behavior. Read [references/wot-design-uni.md](references/wot-design-uni.md) when that component library is already used or requested.

### 2. Define platform scope before editing

State the requested/verified targets. Do not silently claim parity across:

```text
H5
App Android
App iOS
WeChat mini program
other mini programs
```

Identify platform-specific constraints such as safe areas, keyboard behavior, permission prompts, native navigation, file paths, upload APIs, WebView differences, and app lifecycle transitions.

### 3. Implement one complete mobile slice

Build the primary user path end to end:

- use repository-native navigation and component patterns;
- separate remote data, persistent local state, app/session state, and transient presentation state;
- represent loading, empty, error, disabled/pending, and success states;
- handle back navigation and interrupted/re-entered flows where material;
- account for safe-area and keyboard overlap on device-oriented screens;
- use platform APIs behind a narrow adapter when behavior differs by target;
- prefer conditional compilation only for real platform differences, not as a substitute for reusable design.

Read [references/mobile-engineering.md](references/mobile-engineering.md) for state, networking, permissions, offline/retry, and lifecycle guidance.

### 4. Preserve the component system

Reuse the project's existing mobile UI library and theme before inventing custom components. Do not import browser-only component libraries into a uni-app/native target without verified support.

For Wot Design Uni, prefer its established components and theme variables where they match the requested UI, while keeping application state and domain behavior outside presentation components.

### 5. Verify on the strongest available target

Use [references/app-verification.md](references/app-verification.md).

Verification can widen as needed:

1. source/type/lint/build checks;
2. H5/browser check for shared layout/network behavior;
3. mini-program simulator/devtool when that is the target;
4. Android/iOS emulator/device or HBuilderX runtime when native APIs, permissions, packaging, safe area, keyboard, or lifecycle are material.

Do not say “App verified” because only H5 rendered successfully.

### 6. Respect packaging and external effects

Do not install platform SDKs, create signing credentials, publish an app, request store submission, or change consequential platform permissions without user authorization. Inspect and prepare configuration first.

## Handoff

Lead with the implemented mobile user path, supported/verified targets, component and navigation approach, platform-specific behavior, checks actually run, and anything that still requires a real device, native build, signing, or store environment.

## Completion Criteria

Mobile work is complete when the requested user path works in source and is verified on the strongest practical target for the changed behavior, relevant lifecycle/platform states are handled, and platform support claims match actual evidence rather than assumed cross-platform parity.
