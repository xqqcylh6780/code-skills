# Prototype Verification

Use the narrowest browser-backed flow that proves the promised prototype.

## Required checks

1. Load the local artifact and wait for the first meaningful screen.
2. Assert the document title and exact primary navigation labels/count.
3. Click each primary destination and assert its visible active state.
4. Complete one core path through a detail or form screen and back.
5. Exercise one sheet/dialog, one tab/filter, one toggle, and validation when present.
6. Assert every image is complete and has `naturalWidth > 0`.
7. Capture the desktop overview and representative phone screens.
8. Repeat the entry screen at a realistic mobile viewport such as 390×844.
9. Fail on browser `pageerror` or console errors.

## Deterministic helper

For portable HTML using the data hooks documented in [starter-kit.md](starter-kit.md), first run:

```powershell
python scripts/verify_prototype.py path\to\index.html
```

This catches contract drift, broken route targets, navigation label changes, missing back controls, incomplete modal wiring, broken core-flow edges, and missing local images. It does not prove JavaScript interaction or rendering.

If Python Playwright and its browser are already installed, run the browser mode:

```powershell
python scripts/verify_prototype.py path\to\index.html --browser --screenshot-dir path\to\screenshots
```

Browser mode clicks every primary navigation item, exercises declared subpage back paths and modal controls, checks rendered images and browser errors, and checks horizontal overflow at 390×844. Do not install missing Playwright dependencies without authorization. When the prototype uses another structure, perform the equivalent checks with the available Playwright skill or the repository's own tests rather than forcing the starter hooks into it.

## Visual inspection

Open at least the overview, the core detail screen, the densest data screen, and the narrow phone capture. Look for:

- content hidden behind fixed navigation or actions;
- clipped text, sideways scrolling, or unusable touch targets;
- inconsistent names, currencies, dates, or project images;
- active states that are too subtle;
- theme colors not applied to charts, shadows, dialogs, or dark mode;
- desktop-only presentation elements leaking into the phone viewport.

## Evidence language

Report “HTML prototype verified in browser” when that is what ran. Do not claim the native Android/iOS app was validated unless an emulator or device build actually ran.
