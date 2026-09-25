# Routing Examples

## Should trigger

- “Build this Kotlin Jetpack Compose profile screen in my Android app.”
- “Fix the keyboard covering the submit button in this Android XML form.”
- “Add an Android permission flow for selecting a photo.”
- “Implement back navigation and restored state for this native Android screen.”
- “Update the Android manifest and verify the affected build variant.”

## Should not trigger

- “Build a Next.js dashboard.” → `build-frontends`.
- “Build this uni-app page for H5 and WeChat mini program.” → outside this skill.
- “Implement this Flutter or React Native screen.” → outside this skill.
- “Implement the Python endpoint consumed by the Android app.” → `build-backends`.
- “Why does the Android build crash? We do not know the cause.” → `diagnose-bugs` first.
- “Review the Android PR without changing it.” → `review-changes`.

## Focused workflow scenarios

- **Copy-only edit:** Change a button label in an existing Android screen. Inspect the owner and strings resources; do not require a device run by habit.
- **Small patch with device risk:** Fix Android keyboard overlap caused by one layout declaration. Check insets and keyboard behavior on an appropriate Android target when available; do not classify risk by line count.
- **Legacy Views project:** Add a screen in an XML/Java or Kotlin project. Continue the existing Views stack; do not introduce Compose without a project reason.
