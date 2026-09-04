# Wot Design Uni

Authoritative repository: https://github.com/Moonofweisheng/wot-design-uni

Use this reference when the existing uni-app project uses Wot Design Uni or the user explicitly requests it.

## Component strategy

- Prefer an existing Wot component for standard mobile controls, forms, overlays, navigation-adjacent UI, feedback, pickers, lists, and common states when it fits the product.
- Keep remote fetching, domain rules, auth policy, and cross-page state outside purely presentational components.
- Reuse theme variables/tokens instead of scattering local color/spacing overrides.
- Wrap a component only when the application needs a stable domain-level abstraction or repeated policy, not simply to rename every prop.
- Verify target-platform support for components that depend on platform behavior.

## Avoid

- importing web-only libraries to reproduce a component already supported by Wot/uni-app;
- copying a full component implementation only to change styling;
- mixing Wot and another design system without an intentional boundary;
- assuming documentation examples establish the project's routing, state, or API conventions.
