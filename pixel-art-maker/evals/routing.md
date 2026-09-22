# Routing Examples

## Should trigger

- "Create a 32x32 farmland tile, outline only."
- "Draw a character in Aseprite and save the layered source file."
- "Create a 4-direction walking sprite sheet."
- "Check whether this set of pixel tiles can tile seamlessly."
- "Explain how to draw pixel art grass tufts without generating an image."
- "Make a 16x16 potion bottle icon in retro pixel style."

## Should not trigger

- "Write player movement code in GDScript." → game implementation workflow, not pixel art.
- "Create a high-resolution concept art illustration." → general image creation (`game-art-maker` or general image tools).
- "Build a FastAPI backend endpoint." → `build-backends`.
- "Search for open-source Aseprite alternatives." → `github-repository-search`.
- "How do I setup tilemap collisions in Godot 4?" → game engine/code workflow.

## Conflict cases

- "Create a pixel character and integrate it into the game engine." → this skill produces the visual assets, sprite sheets, and import parameters; engine runtime logic is delegated to game development skills.
- "User only asks about Aseprite shortcuts or menu options." → explain the tool/operation only; do not generate an image or create canvas files.
- "I already have an outline, do the final coloring." → edit and build upon the existing confirmed outline; do not regenerate a completely unrelated design.
