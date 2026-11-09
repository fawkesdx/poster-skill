# The sheet

Sizes are millimetres. Type is points. The drawing file uses a viewBox of 1 unit = 1 mm, and every `font-size` carries a `pt` unit.

Draft proofs stay small. See [draft-loop.md](draft-loop.md). Print resolution is a separate, later export.

## Reading distance

The reader is about a metre away and should not squint. On A0 that means labels around 24–36 pt, and nothing under 20 pt. Section labels are larger than the labels inside the section. The title is the largest text. If they say a word is small, make it larger and show the proof. Do not answer with a smaller size.

## Size

Ask the size and orientation before drawing. Use the answer. A0 portrait, 841 × 1189 mm, is an offer when they do not know, and only after they say yes.

| Name | mm |
|---|---|
| A0 | 841 × 1189 |
| A1 | 594 × 841 |
| A2 | 420 × 594 |
| A3 | 297 × 420 |

Portrait or landscape follows the venue. Swap the numbers for landscape.

Outer margin 12–16 mm. Gaps between panels are even. No empty band across the sheet. If a region larger than about a fifth of a panel is empty, enlarge the art, merge the panel, or shorten the sheet. Do not save the hole for later.

## Type floors

Readable at a walk, not at a desk.

| Sheet | Anything on the sheet | Labels | Title |
|---|---|---|---|
| A0, A1 | at least 20 pt; aim at least 24 pt | 24–36 pt | aim 72–100 pt; do not go under 60 pt |
| A2 and smaller | at least 18 pt | 20–28 pt | aim 48–72 pt; do not go under 36 pt |

A long title gets words cut. It does not get crushed through the floor. Two lines maximum. Section headings are noun phrases. Lines on drawn art are about 2–5 pt on A0, thinner in proportion on a smaller sheet.

The checker picks those floors from the page size. A short side of 420 mm or less uses the smaller row. Pass `--min-pt`, `--warn-pt`, or `--title-min-pt` only to override.

## Ink

Search for the home institution's official poster template. Use its colours, header, and grid only after they say yes. If they decline, or none exists, those stay off the sheet: light paper, one colour for type, one accent for the claim. A full-bleed dark ground wastes ink unless that ground is the accepted template. Colours that already live inside a source image stay there. Do not draw a second legend for them. A confirmed logo file can still be placed in the order they set.

## Skeletons

Pick one.

| Skeleton | Use when | Shape |
|---|---|---|
| Bands | The story opens with an idea and ends with evidence | Horizontal bands, top to bottom |
| Columns | Two things must be compared | Equal columns, same scale if they are the same kind of measurement |
| Pipeline | The claim is a sequence | Left to right, result at the end |
| Zoom | The claim is one part of a larger system | System, then the part |

Time and reading order run left to right, then top to bottom. Panel letters only if you would say them aloud.

## Art

Drawn parts are vector, so the type stays editable. A photograph, plot, or other raster is at least 150 pixels per inch at the size you place it, 300 if the venue asks. The checker opens the file and uses its real pixel size. `data-pxw` and `data-pxh` are a fallback when the file is not there yet, and a warning when they disagree with the file.

```xml
<image href="art/result.png" x="16" y="640" width="400" height="260" data-pxw="2400" data-pxh="1560"/>
```

Links: only URLs the user gave. Prefer a short address in type that meets the floor. Add a QR image only if a local tool can make it from that URL (`qrencode` if it is installed). Do not invent a link, and do not fetch a badge.

## Header and footer

Header: title, then names, then affiliations, as text. Each name is tied to the institution the user gave for that person. Search for a logo only for those linked institutions, show the files, and place them only in the order they set.

Footer: one line. A limit the reader must not miss, or a short link. Not a bibliography. Not a seal.

## Thumbnail

Render the preview (`export_poster.py`, long edge 900 px), then look at it. You should see where to start and what the claim is. If you cannot, the layout is wrong. Detail will not fix it.
