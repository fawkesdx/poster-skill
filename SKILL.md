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

Ask 1–4, 6, and 8 in one message, then wait. Do not fill a blank yourself. On a revise, ask only what is still blank. After they answer, do 5 and 7, show what you found, and wait again before any drawing.

1. **Size.** What sheet or board, and portrait or landscape? Do not assume A0. If they do not know, offer A0 portrait (841 × 1189 mm) and wait for a yes.
2. **Title.** The exact words.
3. **Authors.** Names, in the order they should read.
4. **Who belongs where.** For each author, which institution or institutions. One person can have more than one. Ask the link. Do not guess it by lining the two lists up.
5. **Logos.** Search for an official logo of each institution that an author is linked to. Use a mark from that institution's own public page, save it into `art/`, and show the file and the page it came from. Place it only after they say that file is the right mark. Do not redraw a mark. Do not take a person's photo, email, phone, or postal address from the search. This skill ships with no mark.
6. **Logo order.** Ask which institution is home, which mark is primary, and the order of the marks (left to right, or top to bottom). Do not place a mark before they answer.
7. **Home-institution template.** After they name the home institution, search for its official poster template on that institution's own public page. If you find one, show it and ask whether to use it. Wait. Yes: follow that template's size, colours, header, and grid, and record the choice and the page it came from in `docs/brief.md`. Do not copy sample names, sample results, or sample text off the template. No, or none found: say so, and continue with the design steps in this skill. Do not apply a template they did not accept. Do not use a file that sits behind a login.
8. **What goes on the sheet.** Ask which they are bringing: a layout, the content in their own words, or a paper, preprint, or abstract to turn into the poster. A paper follows [references/from-paper.md](references/from-paper.md).

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
- [ ] Home-institution poster template searched; user chose it or declined
- [ ] Story: what is drawn, where, which words
- [ ] Takeaway, must-not list, facts ledger
- [ ] Existing panels and objects named
- [ ] Missing panels asked as a pictorial idea; handoff sent to the figure subagent, or the handoff file left for the user when no figure mode is available
- [ ] Returned figures split into blank objects; type added only on the sheet
- [ ] Current block rendered as a small proof
- [ ] User looked and said this block can stand
- [ ] Next block, same way
- [ ] User agreed the whole sheet
- [ ] Print board confirmed
- [ ] One print-resolution export, vector PDF included
```

1. **Listen, then write the placement.** Before pixels, write the story into `docs/brief.md` and `docs/spec.md`: regions, order, and the words on each region. Use their words when they dictate a label. A shape, not content to copy, is in [references/example.md](references/example.md).

2. **Claims.** One takeaway sentence. A must-not list. `docs/facts.md`: every number on the sheet has a source location. No source, no ink.

3. **Start from objects.** Prefer panels and objects the user already has. Place those files, rearrange them, and add only the new layer on top: title, names, short labels, bands, arrows. If a panel is not in the folder, do not draw the science yourself and do not invent the result. Ask the user for the pictorial idea: what the picture must show, the direction inside it, and what must not appear. Write that as one handoff from [templates/handoff.md](templates/handoff.md). Do not draw past the missing file.

If this session has a subagent or a mode that draws figures, send that handoff to it. If it does not, leave the handoff file and tell the user to pass that file to their figure agent. Do not draw the figure in either case.

When a figure comes back, split it into separate objects before you place it. Each object is its own piece, so a later pass can move one without redrawing the panel. Leave those objects blank of type: no title, caption, axis words, or label inside the file. Fonts go on only in the poster drawing, at poster size, so the type stays sharp at print resolution.

The handoff is the pictorial idea only. It does not include the paper, a local file path, an email or phone, notes marked off the sheet, or a number the picture does not need. A picture of a person, a medical image, or a result they have not said can be shown stays off the sheet and out of the handoff until they clear that item.

4. **One block.** Header, then whichever region they name. Header is about an eighth of the sheet and is shown on its own until they accept it. Title, names, and affiliations are text. Marks sit in the order from step 6 of Ask first.

5. **Proof, then stop.** `python scripts/export_poster.py poster.svg` writes a preview whose long edge is 900 px. Show that image. Do not start the next block in the same turn unless they already told you to continue. Do not pass `--ppi` until they agree the whole sheet, or they ask for the print file.

6. **Their fix list is the whole task.** Do those items, re-render the crop, stop. A label they do not understand gets rewritten with them. Empty space is filled by enlarging or splitting the art, not by a paragraph.

7. **Print.** After they agree, or when they ask for the file to print: confirm the board size (it may differ from the draft), run the checker, then `python scripts/export_poster.py poster.svg --ppi 150`. Give the vector PDF, the proof PNG, and the drawing source.

## Report

Which block you just showed, what you left locked, what is still missing, and the proof file. On the print pass, add the board size and the export paths.

## Private

The poster project belongs to the user. Do not copy their poster, paper, logos, template, or notes into this skill.

Do not add an email, a phone, a postal address, or a photo of a person unless they asked for that exact item. A link on the sheet is one they gave. If it contains a token or a private-share key, ask before it is printed or turned into a QR code.

## Red flags

- Drawing before size, title, authors, the author-to-institution link, logo order, the template choice, and source are answered
- Assuming a sheet size
- Skipping the logo search after an institution is named
- Placing marks before they set the order
- Skipping the home-institution template search
- Applying an institution poster template before they say yes
- Drawing the whole poster before they have seen a block
- Asking them to approve a layout from measurements alone
- A print-resolution render before they agree
- A paragraph on the sheet
- A number with no facts row
- Holding the handoff when a figure subagent is available, instead of sending it
- Drawing the figure yourself when no figure mode is available, instead of leaving the handoff file for the user
- Sending a handoff that contains the paper, a local path, a contact, or an uncleared picture
- Placing a picture of a person, a medical image, or an uncleared result before they say it can be shown
- Adding an email, phone, postal address, or photo of a person they did not ask for
- Printing a link that contains a token or a private-share key
- Copying sample names or sample results off an institution template
- Using a logo or a template from behind a login, or from a page that is not the institution's own
- Copying the user's poster, paper, or notes into this skill
- Drawing a missing panel instead of asking for the pictorial idea
- Placing a multi-object figure as one locked panel
- Type, captions, or axis words baked into a figure file
- A chopped subject, a leftover corner in a crop, or a blurred file they just resaved
- An empty region left "for later"
- Changing a locked title
- Editing from the PDF instead of the drawing source
