# Android App Verification

Choose checks for the changed behavior and the repository's existing test setup. Inspect Gradle tasks and hooks for side effects before running them.

## Source and build

Compile the relevant module and variant when practical. Run focused unit tests or lint for changed code where they add evidence. A successful build catches types, resources, manifest merging, and packaging errors; it does not prove lifecycle, permissions, layout, or device API behavior.

## UI and design

For a supplied screenshot or design, compare an actual Android render at the intended screen size and text scale. Check system bars, display cutouts, scrolling, keyboard overlap, long or localized text, and touch targets when relevant. Note whether the render came from Compose Preview, an emulator, or a physical device; previews do not establish runtime behavior.

## Emulator or device

Use a suitable already running emulator/device, or start one when the active task authorizes it, for changes involving permission grants and denial, back navigation, process recreation, background/resume, camera/location/files/notifications, system insets, keyboard, native SDKs, or hardware behavior. Exercise the specific path and inspect relevant logs when diagnosing failures. Record API level, device type, build variant, and observed result.

## Release and packaging

When the task changes manifest, permissions, min/target SDK, build variants, shrinking, signing, or packaging, check the affected variant and merged outputs where practical. A debug build does not establish that a release build or store submission works. Do not create signing credentials or publish as part of verification without authorization.
