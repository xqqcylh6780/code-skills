# Native Android Engineering

Use for Android lifecycle, state, networking, permissions, and device behavior. Follow the project's existing architecture and supported API levels. Check current [Android Developers guidance](https://developer.android.com/) for version-sensitive platform APIs.

## State and lifecycle

Distinguish transient UI state, navigation state, state that must survive configuration change or process recreation, durable local data, and server-owned data. Use the project's ViewModel, saved state, repository, and persistence conventions where appropriate. Do not use local storage as the authoritative copy of server-owned data merely for screen convenience.

Treat activity/fragment/composable lifecycle as a source of repeated entry. Avoid duplicate fetches, submissions, observers, and stale callbacks after navigation or background/resume. Keep long-running work cancellable and bound to the intended owner.

## Networking and offline behavior

For a remote user flow, handle relevant loading, cancellation/timeout, no-network, retry, auth expiry, and duplicate-submit states. Preserve the project's existing client and error mapping. Avoid infinite retries; use server idempotency for consequential writes.

## Permissions and device APIs

Declare only capabilities needed by the feature. Request runtime permissions close to the user action and offer a usable denial path. Account for Android version differences, revocation, and the system returning no result when the app is interrupted. A platform permission grant is not application authorization.

## Device UI

Check system bar and display cutout insets, gesture navigation, keyboard overlap, back behavior, text scaling, orientation, and long content when they affect the request. Use the app's existing Compose or Views patterns for these behaviors.
