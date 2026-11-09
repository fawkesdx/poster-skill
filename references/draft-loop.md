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

Another chat or tool may draw an illustration. You write the handoff. You do not pretend to be that tool.

One picture per handoff. State:

- where it will sit on the sheet
- the direction inside the picture (this can differ from the band's direction on the sheet)
- what must be visible
- what must not appear
- the file name to save into `art/`

If they paste into a chat that already has the style, write only the change. Do not repeat the standing style.

When the file arrives, open that file. The newest save wins. If they say it is blurry, use the file they just saved, not an earlier copy.

Copy candidates into `art/` and name which file is under discussion before it is placed.

## Crop and place

Crop the object, not a neighbourhood of it. No leftover corner, no chopped head, no caption from the source. If you need an arrow, crop the arrow as its own object.

Place labels in the drawing, at poster size. If the source picture already has writing that fights those labels, use a clean version of the picture and put the words back yourself.

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

Take the palette from the pictures they brought. Push the ground toward white so the print does not flood ink. Darken the type until it stays readable on that ground.

## Locks

In `docs/notes.md`, under Locks, write anything they said to leave alone, and which block is current.

## Board size

Draft on the size they gave. If they later give the real board, refit. A tall draft may have to become square. Say what lost height.
