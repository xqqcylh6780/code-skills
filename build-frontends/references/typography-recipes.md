# Typography Implementation Recipes

Use when implementing or refining heading wraps, reading rhythm, numeric alignment, or text that
breaks a layout. Keep the product's existing typography; these examples are not a new font system.
Values below are starting points to map to repository tokens, not universal limits.

## Choose the intervention

| Visible problem | First intervention | Avoid |
| --- | --- | --- |
| Awkward heading wrap | Check content width, then balanced wrapping | Hard-coded breaks that fail on mobile |
| Exhausting body lines | Constrain reading measure and tune leading | Shrinking all text to fit |
| Counters jump sideways | Tabular numerals and a stable data layout | Animating the whole card on every tick |
| Long names break a row | Allow the flex/grid text item to shrink and wrap | Hiding essential text by default |

## Heading and body rhythm

```css
.article-title {
  font-size: clamp(1.75rem, 1.2rem + 2vw, 3rem);
  line-height: 1.15;
  text-wrap: balance;
}

.article-copy {
  max-inline-size: 65ch;
  line-height: 1.6;
  text-wrap: pretty;
}
```

Use `balance` for short text and `pretty` selectively for reading surfaces. These enhance normal
wrapping; unsupported values should fall back to readable browser wrapping, not a polyfill or
mandatory JavaScript measurement. Browser limits differ; do not encode one browser's line-count
limit as a product rule. See [MDN text-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap).

The `ch` unit is based on the font's zero glyph, not the number of characters in every language.
Tune measure and leading with actual Chinese/CJK text and mixed-language labels. Do not carry
Latin negative tracking or forced capitalization into CJK copy. Preserve deliberate user-supplied
line breaks when they are part of an approved composition.

## Stable numbers and difficult content

```css
.metric-value {
  font-variant-numeric: tabular-nums;
}

.record-label {
  min-inline-size: 0;
  overflow-wrap: anywhere;
}
```

Tabular numerals help supported fonts align digits, but do not reserve space for a new digit or
currency suffix. Test changes such as `99` to `100` and localized numbers; reserve a suitable column
width only when the layout needs it. Keep essential numbers and units visible at narrow widths.

Apply aggressive wrapping to long identifiers, URLs, or names that need it, not indiscriminately to
every paragraph. For truncation, provide an accessible way to obtain the complete value.

## Verify the detail

- Inspect a short and long heading at narrow and wide widths, with real product copy.
- Check text zoom, fallback fonts, localized labels, and the longest supported identifier.
- Confirm numbers align without clipping or an oversized empty column.
- Preserve semantic heading order and labels; a visual size is not a heading level.
- Do not globally alter font smoothing just to make type thinner. It is not a substitute for a
  suitable weight, contrast, or inspection on the target platform.
