---
name: app-prototype-design
description: Create or refine high-fidelity clickable mobile app prototypes from an app idea, existing Android/iOS/cross-platform codebase, screenshots, or supplied assets. Use for app prototype, mobile mockup, interaction demo, screen-flow design, or HTML phone prototype requests. Do not use for implementing the production native app itself.
---

# App Prototype Design

Create a prototype that communicates the real product structure and lets the user experience its important flows. Treat HTML as the delivery medium, not the product architecture.

## Establish the product contract

Use the strongest available source of truth in this order:

1. Existing application code, navigation configuration, route declarations, and screen callbacks.
2. User-provided screenshots, design system, assets, copy, and explicit corrections.
3. Product brief and conversation context.
4. Clearly labeled prototype assumptions.

For an existing repository, inspect the smallest relevant set of files needed to recover:

- target platform and device conventions;
- exact primary navigation count, order, labels, and destinations;
- screen inventory and the main end-to-end user paths;
- contextual actions, forms, sheets, empty/error/loading states, and back behavior;
- existing theme tokens, icons, logos, project images, and terminology.

Do not modify production source code unless the user separately asks for implementation. Preserve dirty worktree changes.

Write a compact internal screen-and-flow inventory before designing. Use [references/prototype-contract.md](references/prototype-contract.md) when the app has more than four screens, is based on an existing codebase, or has ambiguous navigation.

## Choose a visual direction

If the user has already selected a direction, supplied a clear reference, or is iterating an existing prototype, continue that direction without reopening selection.

If a new prototype has no visual direction, create two or three genuinely different, rendered direction samples using the same product facts and assets. A direction sample must be visible UI, not only palette names or prose. Keep it to one representative screen per direction, show the user, and wait for selection before expanding the full prototype.

Never treat a user correction such as “less warm,” “remove blue,” or a renamed project as a request to restart the design direction. Apply it consistently across tokens, charts, states, and dark mode.

Read [references/visual-quality.md](references/visual-quality.md) when inventing a visual language, evaluating a direction, or changing theme colors.

## Use assets deliberately

Inventory the supplied asset directory before layout work and visually inspect images whose meaning is not obvious. Preserve the user's mapping between filename and product name. Reuse the same asset consistently across home, ranking, social, detail, and compose screens.

Prefer real supplied content. Do not invent branded logos, product art, or authoritative metrics. Use clearly identified placeholders only when missing content blocks completion. Keep asset references relative to the prototype when the user wants a portable folder; inline assets only when a truly single-file deliverable is required.

## Build the interaction prototype

Default to a portable HTML prototype with local CSS and JavaScript plus an `assets/` folder. Use a platform-appropriate Android or iOS device frame; do not show iOS chrome for an Android product. The same artifact should remain usable at a phone-sized viewport without the desktop presentation frame.

For a new portable Android prototype, or when an existing prototype lacks a coherent multi-screen shell, read [references/starter-kit.md](references/starter-kit.md). Adapt the dependency-free files in `assets/android-prototype-starter/` instead of rebuilding device chrome, independent screen state, and audit hooks from scratch. Treat its labels, content, screen count, and palette as replaceable examples; the recovered product contract remains authoritative.

When the request is for a broad prototype rather than one isolated screen, present four to six representative phone views together when that accurately covers the main product. Each phone must remain independently interactive. Use the actual screen count when the source product needs fewer or more views; do not pad or drop screens to hit a template number.

Required behavior:

- Match primary navigation exactly. Do not add a center plus button or extra tab unless the product contract contains it.
- Keep contextual actions on their owning screen, such as “记一笔” inside a project detail screen.
- Make every prominent control either change visible state, open a sheet, navigate, or provide explicit prototype feedback.
- Implement one complete happy path end to end, including back navigation and success feedback.
- Forms must demonstrate meaningful state changes: tab selection, amount updates, toggles, validation, save/publish results.
- Hide global navigation on subpages when that matches the app; restore it through the real back path.
- Make modals and sheets dismissible through their visible controls and, when appropriate, the backdrop.
- Keep labels, project names, dates, currencies, and terminology consistent across all screens.

Use a small route/state model instead of disconnected static panels. Avoid dependencies when plain HTML/CSS/JavaScript is sufficient. Do not install packages merely to display the prototype.

## Verify before delivery

Read [references/verification.md](references/verification.md) before signing off a multi-screen or interactive prototype.

When Playwright is available, verify through normal user actions:

- exact primary navigation labels and count;
- every promised screen is reachable;
- at least one core flow completes;
- key tabs, filters, toggles, sheets, and validation respond;
- supplied images load with nonzero dimensions;
- desktop presentation and a realistic phone viewport render without material overflow;
- browser `pageerror` and console error counts are zero.

Visually inspect representative screenshots after automated checks. Browser verification proves the HTML prototype, not native Android/iOS runtime behavior.

For portable HTML following the starter data contract, run `scripts/verify_prototype.py` for deterministic route, navigation, back-path, modal, and local-asset checks. Add `--browser` only when Python Playwright and its browser are already available; the helper must not install them. Static checks complement rather than replace the real browser flow and visual inspection.

## Handoff

Lead with the finished artifact and its exact location. State:

- screens and flows included;
- primary navigation contract;
- assets used and any placeholders remaining;
- viewports and interactions actually verified;
- whether production app code was changed;
- any native behavior still requiring implementation or device validation.
