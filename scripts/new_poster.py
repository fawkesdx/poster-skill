#!/usr/bin/env python3
"""Copy the blank poster templates into a new folder."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = {
    "brief.md": Path("docs") / "brief.md",
    "spec.md": Path("docs") / "spec.md",
    "facts.md": Path("docs") / "facts.md",
    "notes.md": Path("docs") / "notes.md",
    "handoff.md": Path("docs") / "handoff.md",
    "poster.svg": Path("poster.svg"),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Start a poster folder from the generic templates.")
    parser.add_argument("dest", help="new folder; it must not already exist")
    args = parser.parse_args(argv)
    dest = Path(args.dest)
    if dest.exists():
        print(f"{dest} already exists", file=sys.stderr)
        return 1
    dest.mkdir(parents=True)
    (dest / "art").mkdir()
    (dest / "docs").mkdir()
    for name, rel in TEMPLATES.items():
        source = ROOT / "templates" / name
        target = dest / rel
        shutil.copyfile(source, target)
        print(target)
    print("next: fill docs/brief.md, then draw poster.svg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
