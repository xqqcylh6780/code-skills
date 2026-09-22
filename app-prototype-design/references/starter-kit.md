# Android Prototype Starter Kit

Use this starter for a new portable Android prototype or to repair an incomplete prototype shell. Do not copy it unchanged and present the sample ledger content as the user's product.

## Included resources

`assets/android-prototype-starter/` contains:

- `android-frame.js`: a dependency-free Android custom element with status and gesture areas;
- `index.html`: six side-by-side phone views backed by one reusable app shell;
- `styles.css`: desktop overview and 390-pixel phone presentation modes;
- `app.js`: independent state per phone, routes, back paths, dialog handling, tabs, a toggle, form validation, and success feedback;
- `prototype-contract.json`: the machine-readable navigation, screen, subpage, modal, and core-flow contract.

Copy the folder into the user's requested prototype location, then adapt it in this order:

1. Replace `prototype-contract.json` with the recovered product facts.
2. Make the HTML screen ids, navigation order and labels, subpage back targets, dialogs, and core-flow actions match the contract exactly.
3. Replace sample content and connect supplied assets using portable relative paths.
4. Replace the visual tokens and signature detail with the chosen product direction.
5. Remove unused example behavior and add the actual product's meaningful state transitions.

Preserve the six-view overview only when it represents the product well. Four to six phones is a useful default for broad presentations, not a product requirement. On a narrow viewport, the starter intentionally shows a single full-screen phone.

## Data hooks

The static and browser verifier recognizes these stable hooks:

| Hook | Meaning |
| --- | --- |
| `data-prototype-instance` | One independently interactive phone |
| `data-start-screen` | Initial screen for that phone |
| `data-screen="id"` | Declared screen |
| `data-route-to="id"` | Forward navigation control |
| `data-back-to="id"` | Back control and destination |
| `data-nav-item` | Primary navigation control |
| `data-nav-label="label"` | Visible label excluding decorative icons |
| `data-modal="id"` | Dialog or sheet |
| `data-modal-open="id"` | Dialog trigger |
| `data-modal-close="id"` | Dialog dismiss or confirm control |

These hooks are a verification interface, not a styling system. Keep them when changing layout or visual direction.

## Verification helper

Static verification has no third-party dependency:

```powershell
python scripts/verify_prototype.py path\to\prototype\index.html
```

When Python Playwright and its Chromium browser are already installed, add browser interaction and optional screenshots:

```powershell
python scripts/verify_prototype.py path\to\prototype\index.html --browser --screenshot-dir path\to\screenshots
```

Exit code `0` means the requested checks passed, `1` means the prototype failed a check, and `2` means `--browser` was requested but Playwright was unavailable. Never install Playwright or browser binaries implicitly to change exit code `2`.

