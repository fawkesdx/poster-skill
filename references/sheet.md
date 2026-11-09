# The sheet

Sizes are millimetres. Type is points. The drawing file uses a viewBox of 1 unit = 1 mm, and every `font-size` carries a `pt` unit.

## Size

Use the venue's size and orientation. If the venue says nothing, assume A0 portrait, 841 × 1189 mm, and say so.

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

The checker defaults match A0/A1. For a smaller sheet:

```
python scripts/check_poster.py poster.svg --expect 420x594 --min-pt 18 --warn-pt 20 --title-min-pt 36
```

## Ink

Light paper. A full-bleed dark ground wastes ink and fails in some halls. One colour for type. One accent, used in a few places, for the claim. Colours that already live inside a source image stay there. Do not draw a second legend for them. Ignore any brand palette unless the user gives one.

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

Drawn parts are vector, so the type stays editable. A photograph, plot, or other raster is at least 150 pixels per inch at the size you place it, 300 if the venue asks. Record the pixel size on the image as `data-pxw` and `data-pxh`.

```xml
<image href="art/result.png" x="16" y="640" width="400" height="260" data-pxw="2400" data-pxh="1560"/>
```

Links: only URLs the user gave. Prefer a short address in type that meets the floor. Add a QR image only if a local tool can make it from that URL (`qrencode` if it is installed). Do not invent a link, and do not fetch a badge.

## Header and footer

Header: title, names, affiliations, as text. No mark slot. If the user supplies mark files and asks, place those files and keep the title as text.

Footer: one line. A limit the reader must not miss, or a short link. Not a bibliography. Not a seal.

## Thumbnail

Render the proof, then look at it with the long edge about 360 px. You should see where to start and what the claim is. If you cannot, the layout is wrong. Detail will not fix it.
