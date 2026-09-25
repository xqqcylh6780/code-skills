# Icon types, sets, and states

Read the relevant sections when creating a themed icon, coherent set, complete button, or interactive state variants.

## Function and metaphor

Select one dominant symbol that communicates the function at the intended display size. Navigation icons need unambiguous direction and minimal decoration. Feature icons (shop, inventory, quest, map, mail) can have more personality while retaining one clear metaphor. Resource icons (coins, gems, health, energy) need distinct shapes and colors when shown together, especially beside numbers. Skill icons may use one central effect with restrained supporting particles. Item and equipment icons should isolate the item without a holding character or scenery unless requested.

## A coherent set

Match outline width/color, perspective, corner language, lighting, depth, saturation, padding, visual weight, and occupied area. Inspect the set as a family at native UI size, not only each image enlarged. Keep enough space for extraction if a sheet is requested; otherwise deliver separate icons when practical.

When prompting a new symbol, use existing icons as style and sizing references while specifying the new function and metaphor explicitly; do not copy an unrelated reference symbol. Compare the finished set without labels at its intended size to catch icons that look consistent but communicate the wrong function or direction.

## Button and state variants

Generate a complete button only when requested; otherwise provide the bare icon. For a button family, keep corner radius, padding, symbol alignment, and depth consistent.

For normal, hover, pressed, disabled, selected, or locked states, reuse the same base geometry. Convey state through brightness, saturation, shadow, highlight, glow, or a small overlay as appropriate. Use an identity-preserving edit or reference workflow rather than separately redesigning each state. Check that the underlying symbol stays in the same position and remains legible in every state.

Keep the original normal icon as the reference for each state. In each prompt, state the one intended visual change and which geometry, padding, and symbol details must remain fixed. Review the states side by side at UI size; repair a state that shifts the symbol or loses its meaning before treating the set as complete.
