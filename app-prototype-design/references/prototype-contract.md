# Prototype Contract

Use this checklist to prevent a polished but incomplete prototype.

## Source-of-truth inventory

Record only facts supported by code, supplied artifacts, or the user's words:

```text
Target: Android / iOS / cross-platform / unspecified
Primary navigation: label -> destination, in exact order
Subpages: parent -> child -> return destination
Contextual actions: screen -> action -> result
Sheets or dialogs: trigger -> content -> dismiss/confirm behavior
Assets: path -> semantic name -> screens using it
Core happy path: entry -> actions -> success state
Explicit exclusions or placeholders:
Output directory:
```

If code and a mock disagree, surface the discrepancy and follow the user's latest explicit correction. Do not silently merge incompatible navigation models.

## Screen completeness

For each promised screen, identify:

- purpose and primary action;
- entry and exit routes;
- content sections backed by real product behavior;
- interactive controls and visible resulting state;
- empty, loading, error, disabled, or success state when material;
- asset and terminology dependencies.

Prominent UI that does nothing is a defect unless visibly labeled as a non-interactive placeholder.

## Existing codebase extraction

Inspect navigation declarations first, then the screens reachable from them. Search for user-facing labels, callbacks, route enums, screen composables/controllers, and menu items. Read detail and form screens linked by callbacks before declaring the prototype complete.

Do not infer the product hierarchy from filenames alone. Confirm it from actual route wiring and callbacks.

## Default deliverable layout

For a portable prototype folder:

```text
prototype-name/
|-- index.html or a clearly named primary HTML file
|-- prototype-contract.json when using the deterministic verifier
|-- assets/
|   `-- supplied local images and icons
`-- screenshots/
    `-- only the representative verification captures the user benefits from
```

If the user supplied an exact existing directory, preserve it instead of inventing another output location.

The optional machine-readable contract uses this shape:

```json
{
  "platform": "android",
  "screens": ["home", "detail", "entry"],
  "primaryNavigation": [{ "id": "home", "label": "首页" }],
  "subpages": [{ "id": "detail", "backTo": "home" }],
  "modals": ["filter"],
  "coreFlow": ["home", "detail", "entry"]
}
```

Keep ids stable and labels exact. `coreFlow` names the screens reached in order by visible `data-route-to` controls; it does not describe invisible test-only shortcuts.
