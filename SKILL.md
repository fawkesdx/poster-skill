---
name: poster-skill
description: >-
  Use when making a conference, meeting, or hallway poster; turning a paper,
  preprint, or abstract into a poster; or revising poster layout, type size,
  and claims. Any field. No institution, logo, or topic is assumed. Triggers
  include poster, scientific poster, research poster, paper-to-poster, and
  poster layout.
---

# Poster

A poster is one claim a person can get while walking. The sheet shows the claim. The speaker explains it.

Start from this poster's brief. Do not reuse the layout, colours, or wording of a previous poster.

## Paths

- **Notes.** The user has a story and no paper. Write the brief from what they said.
- **Paper.** The user gives a paper, preprint, or abstract. Read [references/from-paper.md](references/from-paper.md) before the brief.
- **Revise.** An existing poster plus a change request. Change only what was asked. Record the request in `docs/notes.md`.

If the user locked a title or a sentence, leave it until they ask for a change.

## Steps

Copy this list and keep it:

```
Poster progress:
- [ ] 1. Sheet size locked
- [ ] 2. Takeaway written in one sentence
- [ ] 3. Must-not list written
- [ ] 4. Facts line for every number and named claim
- [ ] 5. Two layouts scored, one kept
- [ ] 6. Panels specified
- [ ] 7. Sheet drawn, labels short
- [ ] 8. Checker clean
- [ ] 9. Thumbnail read cold
- [ ] 10. PDF and proof PNG exported
```

1. **Lock the sheet.** Use the size and orientation the venue states. If the venue is silent, use A0 portrait (841 × 1189 mm) and say that you assumed it. Sizes, type floors, and skeletons are in [references/sheet.md](references/sheet.md).

2. **Write the takeaway** in `docs/brief.md` (copy [templates/brief.md](templates/brief.md)). One sentence a passer-by can repeat. Then 3–6 key ideas, a must-not list, and what stays off the sheet.

3. **Write the must-not list** from the source's limits. If the source does not show it, the poster must not imply it: no extra count, score, mechanism, or comparison.

4. **Ledger.** `docs/facts.md` (copy [templates/facts.md](templates/facts.md)). Every number, count, name, and citation that will appear on the sheet gets a row with its source location. If a row has no source, it does not go on the sheet. Unknown stays off, or you ask.

5. **Two layouts, then one.** In `docs/spec.md`, sketch two different skeletons in a few lines each. Score both: takeaway visible on a thumbnail; true to the source; one story; type floors still hold. Keep one. State why in one line. Skeletons are in [references/sheet.md](references/sheet.md). A filled shape, not content to copy, is in [references/example.md](references/example.md).

6. **Spec the kept layout.** For each panel: its job in one line, the words on it, and where the art comes from (`draw`, a file the user supplied, or `omit`).

7. **Draw.** Start from [templates/poster.svg](templates/poster.svg), or run `python scripts/new_poster.py <folder>`. Header is title, names, and affiliations as text. Cut title words before you shrink type. Two lines maximum. Place a mark only when the user supplies the file and asks for it. Do not search for, download, or redraw a seal, crest, wordmark, or brand colour. Build one panel at a time. Crop a source image to the claim. Do not paste a multi-panel figure whole. Labels name things, about 2–4 words. A sentence means the panel is unclear: redraw it, or move the sentence to `docs/notes.md`.

8. **Check.** `python scripts/check_poster.py poster.svg --expect <w>x<h>`. Fix every FAIL. A WARN stays only with a reason written in `docs/notes.md`.

9. **Cold read.** Render a thumbnail whose long edge is about 360 px. Before you reread the brief, write what the sheet claims. If a key idea is missing, change the picture. Do not add a paragraph.

10. **Export.** `python scripts/export_poster.py poster.svg`. Deliver the SVG, the PDF, a proof PNG, and `docs/brief.md`, `docs/spec.md`, `docs/facts.md`, `docs/notes.md`.

## Report

State the sheet size and whether you assumed it, the skeleton you kept and why, the takeaway sentence, the files, and any number you left off because it had no source.

## Red flags

Stop and go back to the step in parentheses.

- Drawing before the takeaway sentence (2)
- A paragraph on the sheet (7)
- A count, score, or citation with no facts row (4)
- A mark you fetched because a poster "should" have one (7)
- Every figure from the paper, shrunk to fit (5)
- Type under the floor (8)
- An empty band left for later (5)
- A result the source does not state (3)
