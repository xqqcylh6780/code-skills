# App Verification

Choose verification based on what can fail only on a target runtime.

## Source/build checks

Useful for:

- syntax/types;
- route/config references;
- imports;
- platform compilation;
- unit/module behavior.

They do not prove native permissions, safe-area layout, lifecycle, packaging, WebView behavior, or store/runtime configuration.

## H5

Use browser/H5 for shared layout and network flows when applicable. It can provide fast feedback and Playwright automation, but label the evidence as H5/browser evidence.

## Mini programs

Use the target platform devtool/simulator for platform component/API restrictions, package/subpackage behavior, permissions, and navigation differences.

## Native App

Use an emulator/device or the project's HBuilderX/native run path when the change depends on:

- App lifecycle/background/resume;
- native permissions;
- keyboard/safe area/status bar;
- camera/location/files/notifications;
- native plugins/SDKs;
- signing/build/package behavior.

Record the target OS/runtime and do not generalize one platform result to all targets without reason.
