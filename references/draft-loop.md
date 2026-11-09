# Draft loop

The user steers. You draw the block they are looking at, show a proof, and wait.

## Before any pixels

Write a placement note:

- the regions, top to bottom or left to right
- what sits in each region
- the words on each region, in their wording when they gave it
- what is not on the sheet

If the title names two ends and a link, the sheet shows those regions. Band heights are provisional. They move when a later region needs room.

The questions in SKILL.md "Ask first" are already answered before this note. If one is blank, ask it and wait. Do not draw.

## One block

Work the header before the body if they are talking about the header. Otherwise work the region they named. Do not redesign a region they already accepted.

Header, until they accept it:

- about one seventh to one eighth of the sheet height
- title largest, names next, affiliations next
- marks in the order they set, primary mark included
- show the header crop alone

A title may stay wrong on purpose. Record the lock in `docs/notes.md`.

## Proof

Render a preview with `python scripts/export_poster.py poster.svg`. The PNG long edge is 900 px. Keep every source image at full resolution on disk. The preview is small. The art file is not.

Show the proof. Stop. They cannot approve a description or a table of millimetres.

When they send a numbered list, do that list on the current block, render again, stop.

Low resolution ends when they say the sheet is agreed, or they ask for the print file. Then `python scripts/export_poster.py poster.svg --ppi 150` (300 if the printer asks). The PDF is vector. Tell them the PDF is for a last nudge, and the drawing source is what the next pass reads.

## Pictures from somewhere else

Start from objects the user already has. Copy each one into `art/` and name which file is under discussion before it is placed. Your job on those files is to arrange them and add the poster layer on top.

If a panel does not exist, ask for the pictorial idea in their words and write the handoff. If this session has a subagent or a mode that draws figures, send the handoff to that subagent. If it does not, leave the handoff file and tell the user to pass that file to their figure agent. The handoff is the pictorial idea only: no paper, no local path, no email or phone, no notes marked off the sheet, and no picture of a person, medical image, or result they have not cleared. You do not draw the figure yourself, and you do not pretend to be that agent.

One picture per handoff. State:

- the pictorial idea, in their words
- the objects to return as separate files
- where it will sit on the sheet
- the direction inside the picture (this can differ from the band's direction on the sheet)
- what must be visible
- what must not appear, including any title, caption, axis words, or label
- the file name to save into `art/`
- the words that will be added later on the poster, not inside the picture

If they paste into a chat that already has the style, write only the change. Do not repeat the standing style.

When the file arrives, open that file. The newest save wins. If they say it is blurry, use the file they just saved, not an earlier copy.

## Blank objects

A generated figure is not ready to drop onto the sheet. Split every object inside that panel into its own piece: one curve, one map, one arrow, one module. Save each piece under its own name in `art/`. A later rearrange then moves one object and leaves the others.

Strip type out of those files. The object is the picture only. Titles, captions, tick labels, axis words, and callouts are added in `poster.svg` when the poster is arranged, at the poster point size. Type drawn inside the figure is raster or the wrong size, and it goes soft when the sheet is printed. If the file that came back already has writing, ask for a blank version of the same objects, or crop the writing off, and put the words back on the sheet.

## Crop and place

Crop the object, not a neighbourhood of it. No leftover corner, no chopped head, no caption from the source. If you need an arrow, crop the arrow as its own object.

Place labels in the drawing, at poster size.

Labels sit next to the thing they name. They do not touch it, cover it, or cross an arrow. The same role uses the same size and the same baseline. A shared legend is written once.

An arrow that was there before a rearrange is still there after it, and it still meets the two ends.

Reuse an object the user says is the same object. Do not draw a second copy that drifts.

Pictures sit on the sheet ground. No white card and no hard patch, unless they ask. A group of panels that are one idea can share a rounded region. The region has to meet the objects that belong to it, not merely the heads of figures in front of it.

Repeated people or repeated modules stay the same size, so the reader can compare them.

## Words

Use the words they dictated. If they cannot tell what a sentence means, replace it with words they accept. Do not keep a clever line.

Section labels are large and equal to each other, larger than the labels inside the section.

Do not print an explanation they said they will say aloud.

## Empty space

A sparse region is unfinished. Enlarge the art, split one picture into its objects, or give the height to a region that needs it. Do not fill the hole with a paragraph.

Two columns that they want matched are made the same height. Squeeze one, expand the other.

## Colour

If they accepted a home-institution poster template, use its colours, header, and grid, and leave that ground as the template drew it. Otherwise take the palette from the pictures they brought for this poster, push the ground toward white so the print does not flood ink, and darken the type until it stays readable. Do not reuse an older poster's colours or header unless they ask for that layout.

## Locks

In `docs/notes.md`, under Locks, write anything they said to leave alone, and which block is current.

## Board size

Draft on the size they gave. If they later give the real board, refit. A tall draft may have to become square. Say what lost height.
