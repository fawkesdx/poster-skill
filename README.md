# Poster skill

A generic agent skill for making a poster, or for turning a paper into one.

The sheet carries one claim a person can read while walking. The speaker carries the explanation. The skill does not assume a field, a dataset, a tool, or an institution. It does not include any logo, seal, or wordmark. You bring the content. If you want a mark on the sheet, you supply the file.

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
python scripts/check_poster.py --self-test
```

The blank template fails the check until the scaffold text is replaced. That is intentional. Export uses `rsvg-convert` or Inkscape when one of them is installed, and otherwise a headless Chrome PDF.

## What is in here

| Path | Role |
|---|---|
| `SKILL.md` | Steps the agent follows |
| `references/from-paper.md` | How a paper becomes a poster |
| `references/sheet.md` | Sizes, type floors, skeletons |
| `references/example.md` | A layout shape with no real content |
| `templates/` | Brief, spec, facts, notes, blank sheet |
| `scripts/` | New poster, check, export |

## License

MIT. See [LICENSE](LICENSE).
