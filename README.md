# Poster skill

A generic agent skill for making a poster, or for turning a paper into one.

The speaker presents the explanation. Before any drawing, the agent asks the sheet size, the title, the authors, which author belongs to which institution, the logo order, and whether the poster comes from a layout, from notes, or from a paper. It searches for each institution logo and places the marks in the order you set. It also searches for the home institution's official poster template and uses that template only if you say yes. Then it draws one block, shows a small proof, and waits. Print resolution comes after you agree the sheet.

## Install

Cursor, from a clone of this repo:

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/fawkesdx/poster-skill.git ~/.cursor/skills/poster-skill
```

The same folder works for other agents that load skills from a directory you choose. Put the clone on that path. The skill file is `SKILL.md`.

## Start a poster

```bash
python ~/.cursor/skills/poster-skill/scripts/new_poster.py ./my-poster
```

That creates `docs/brief.md`, `docs/spec.md`, `docs/facts.md`, `docs/notes.md`, an empty `art/` folder, and a blank `poster.svg`. Then ask the agent to use this skill. Give it notes, or a paper.

From a paper, the agent reads the abstract, the figure captions, and the last section, then keeps one claim. Methods become a short flow. Extra figures stay off the sheet. Numbers on the sheet have to appear in the paper.

## Check and export

```bash
python scripts/check_poster.py poster.svg --expect 841x1189
python scripts/export_poster.py poster.svg
python scripts/export_poster.py poster.svg --ppi 150
python scripts/check_poster.py --self-test
```

The blank template fails the check until the scaffold text is replaced. That is intentional. The checker picks type floors from the page size, and it reads each photo's real pixel size. Export writes a 900 px preview unless you pass `--ppi`. It uses `rsvg-convert` or Inkscape. The SVG stays the source file when neither is installed.

## What is in here

| Path | Role |
|---|---|
| `SKILL.md` | Steps the agent follows |
| `references/draft-loop.md` | One block, a proof, then wait |
| `references/from-paper.md` | How a paper becomes a poster |
| `references/sheet.md` | Sizes, type floors, skeletons |
| `references/example.md` | A layout shape with no real content |
| `templates/` | Brief, spec, facts, notes, handoff, blank sheet |
| `scripts/` | New poster, check, export |

## License

MIT. See [LICENSE](LICENSE).
