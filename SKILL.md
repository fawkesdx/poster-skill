---
name: poster-skill
description: >-
  Use when making a conference, meeting, or hallway poster; turning a paper,
  preprint, or abstract into a poster; or revising poster layout, type size,
  and claims. Any field. No institution, logo, or topic is assumed. Triggers
  include poster, scientific poster, research poster, paper-to-poster, poster
  draft, and poster layout.
---

# Poster

A poster is one claim a person can get while walking. Build it in front of the user, one block at a time. They agree by looking at a proof, not by reading a description.

Start from this poster's brief. Do not reuse the layout, colours, or wording of a previous poster.

The drawing source is the file you edit (`poster.svg`, or the project's drawing file). An exported PDF or PNG is a proof. Say that once, early. Edits made only on the PDF will not come back into the next pass.

## Ask first

Ask these before any drawing, in one message, then wait. Do not fill a blank yourself. On a revise, ask only what is still blank.

1. **Size.** What sheet or board, and portrait or landscape? Do not assume A0. If they do not know, offer A0 portrait (841 × 1189 mm) and wait for a yes.
2. **Title.** The exact words.
3. **Authors.** Names, in the order they should read.
4. **Who belongs where.** For each author, which institution or institutions. One person can have more than one. Ask the link. Do not guess it by lining the two lists up.
5. **Logos.** Search for an official logo of each institution that an author is linked to. Save the files into `art/`. Show what you found. Do not redraw a mark.
6. **Logo order.** Ask which institution is primary, and the order of the marks (left to right, or top to bottom). Do not place a mark before they answer.
7. **What goes on the sheet.** Ask which they are bringing: a layout, the content in their own words, or a paper, preprint, or abstract to turn into the poster. A paper follows [references/from-paper.md](references/from-paper.md).

Write the answers into `docs/brief.md`.

## Paths

- **Notes.** The user talks the story. Write what to draw, where, and which words. Then draw the block they are on.
- **Paper.** Read [references/from-paper.md](references/from-paper.md) first, then the same draft loop.
- **Revise.** Change only what they asked. Record it in `docs/notes.md`.

If they lock a title or a sentence ("leave it"), do not change it until they ask.

## Draft loop

Details, the picture handoff, crops, and locks are in [references/draft-loop.md](references/draft-loop.md). Sizes are in [references/sheet.md](references/sheet.md).

Copy this list and keep it:

```
Poster progress:
- [ ] Asked: size, title, authors, which author belongs to which institution, logo order, and source
- [ ] Logos searched and shown
- [ ] Story: what is drawn, where, which words
- [ ] Takeaway, must-not list, facts ledger
- [ ] Missing pictures named; handoff written if needed
- [ ] Current block rendered as a small proof
- [ ] User looked and said this block can stand
- [ ] Next block, same way
- [ ] User agreed the whole sheet
- [ ] Print board confirmed
- [ ] One print-resolution export, vector PDF included
```

1. **Listen, then write the placement.** Before pixels, write the story into `docs/brief.md` and `docs/spec.md`: regions, order, and the words on each region. Use their words when they dictate a label. A shape, not content to copy, is in [references/example.md](references/example.md).

2. **Claims.** One takeaway sentence. A must-not list. `docs/facts.md`: every number on the sheet has a source location. No source, no ink.

3. **Name what is missing.** If a picture or a result is not in the folder, say so. Write one handoff from [templates/handoff.md](templates/handoff.md). Do not invent the missing result. Do not draw past it.

4. **One block.** Header, then whichever region they name. Header is about an eighth of the sheet and is shown on its own until they accept it. Title, names, and affiliations are text. Marks sit in the order from step 6 of Ask first.

5. **Proof, then stop.** `python scripts/export_poster.py poster.svg` writes a preview whose long edge is 900 px. Show that image. Do not start the next block in the same turn unless they already told you to continue. Do not pass `--ppi` until they agree the whole sheet, or they ask for the print file.

6. **Their fix list is the whole task.** Do those items, re-render the crop, stop. A label they do not understand gets rewritten with them. Empty space is filled by enlarging or splitting the art, not by a paragraph.

7. **Print.** After they agree, or when they ask for the file to print: confirm the board size (it may differ from the draft), run the checker, then `python scripts/export_poster.py poster.svg --ppi 150`. Give the vector PDF, the proof PNG, and the drawing source.

## Report

Which block you just showed, what you left locked, what is still missing, and the proof file. On the print pass, add the board size and the export paths.

## Red flags

- Drawing before size, title, authors, the author-to-institution link, logo order, and source are answered
- Assuming a sheet size
- Skipping the logo search after an institution is named
- Placing marks before they set the order
- Drawing the whole poster before they have seen a block
- Asking them to approve a layout from measurements alone
- A print-resolution render before they agree
- A paragraph on the sheet
- A number with no facts row
- A chopped subject, a leftover corner in a crop, or a blurred file they just resaved
- An empty region left "for later"
- Changing a locked title
- Editing from the PDF instead of the drawing source
