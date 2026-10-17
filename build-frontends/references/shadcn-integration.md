# Existing shadcn/ui Projects

Read only when the project already uses shadcn/ui or the user explicitly requests it. This
reference does not select a component library for an unrelated frontend task.

Inspect `components.json`, the package manifest/lockfile, aliases, local component source, global
CSS, theme variables, and nearby usages. Determine the actual primitive packages from imports;
do not assume every shadcn-derived project uses identical internals or current defaults.

Reuse and modify the local component source carefully: it may contain product-specific behavior
that differs from today's upstream example. Follow existing variants, class merging, sizes, and
semantic color tokens. Preserve light/dark semantic pairs and verify both themes when affected;
avoid overriding a primitive globally just to fix one caller.

For a dialog, menu, popover, or form wrapper, preserve its accessible name, focus management,
keyboard controls, disabled state, and ref/event forwarding expected by existing consumers.
Inspect actual markup and behavior after composition; a styled element is not proof of a working
accessible interaction.

Use current official component documentation when an API is uncertain. Do not automatically run
`npx ...@latest`, initialize a library, overwrite local components, or add dependencies to inspect
a project. Any authorized CLI action still needs its effects and package runner checked first.

Sources: [components.json](https://ui.shadcn.com/docs/components-json),
[Theming](https://ui.shadcn.com/docs/theming).
