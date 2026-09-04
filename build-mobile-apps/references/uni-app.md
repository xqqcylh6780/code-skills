# uni-app / Vue 3

Authoritative sources:

- https://uniapp.dcloud.net.cn/
- https://github.com/dcloudio/uni-app

Verify current platform support and API details against official documentation when the behavior may have changed.

## Recover project conventions first

Inspect:

- `pages.json` and route/subpackage organization;
- `manifest.json` and App permissions/capabilities;
- Vue 3 component style and composition conventions;
- `uni.*` network/storage/navigation APIs in existing code;
- conditional compilation blocks;
- HBuilderX versus CLI/package-manager workflow;
- existing component library and theme;
- target App/H5/mini-program platforms.

## Routing and lifecycle

Use the project's configured page routes and established navigation APIs. Keep page initialization, show/resume refresh, and unload/cleanup behavior distinct when the feature depends on them.

Do not assume browser globals or DOM APIs exist on every target. Isolate H5-specific code behind an explicit target boundary.

## Conditional compilation

Use conditional compilation when a platform genuinely requires a different implementation or capability. Keep the shared path dominant and small; excessive target branches usually indicate an abstraction or product-support decision is missing.

## Network and storage

Use established wrappers around `uni.request`/upload/download/storage when the repository has them. Centralize authentication, common error mapping, base URL, timeout, and request correlation rather than duplicating them across pages.

## Configuration safety

Treat `manifest.json`, signing, App permissions, SDK keys, universal/deep links, and platform capability declarations as release-affecting configuration. Do not add permissions or credentials casually to satisfy a local code path.
