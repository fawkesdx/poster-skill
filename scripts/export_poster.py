#!/usr/bin/env python3
"""Export poster.svg to a PDF and a 150 ppi proof PNG.

Tries rsvg-convert, then Inkscape, then a headless Chrome PDF.
Does not install anything. The SVG remains the editable source.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from check_poster import check_svg


def proof_px(svg: Path, ppi: float) -> int:
    text = svg.read_text(encoding="utf-8")
    findings = check_svg(text)
    for level, message in findings:
        if level == "OK" and message.startswith("page "):
            width = float(message.split()[1])
            return max(1, round(width / 25.4 * ppi))
    return 4960


def chrome() -> str | None:
    found = [
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for path in found:
        if path and Path(path).exists():
            return path
    return None


def run(cmd: list[str]) -> bool:
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return True


def export(svg: Path, ppi: float) -> tuple[bool, bool, str]:
    pdf = svg.with_suffix(".pdf")
    png = svg.with_name(svg.stem + "-proof.png")
    width = str(proof_px(svg, ppi))
    rsvg = shutil.which("rsvg-convert")
    if rsvg and run([rsvg, "-f", "pdf", "-o", str(pdf), str(svg)]) and run(
        [rsvg, "-f", "png", "-o", str(png), "-w", width, str(svg)]
    ):
        return True, True, "rsvg-convert"
    ink = shutil.which("inkscape")
    if ink and run([ink, str(svg), "--export-type=pdf", f"--export-filename={pdf}"]) and run(
        [ink, str(svg), "--export-type=png", f"--export-filename={png}", "-w", width]
    ):
        return True, True, "inkscape"
    browser = chrome()
    if browser and run(
        [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf}",
            svg.resolve().as_uri(),
        ]
    ):
        return True, False, "chrome"
    return False, False, ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export a poster SVG to PDF and a proof PNG.")
    parser.add_argument("svg")
    parser.add_argument("--ppi", type=float, default=150)
    args = parser.parse_args(argv)
    svg = Path(args.svg)
    if not svg.is_file():
        print(f"no such file: {svg}", file=sys.stderr)
        return 1
    got_pdf, got_png, tool = export(svg, args.ppi)
    if not got_pdf and not got_png:
        print("no converter found. Install librsvg (rsvg-convert) or Inkscape.", file=sys.stderr)
        print("the SVG is still the source file.", file=sys.stderr)
        return 2
    print(f"exported with {tool}")
    if got_pdf:
        print(svg.with_suffix(".pdf"))
    if got_png:
        print(svg.with_name(svg.stem + "-proof.png"))
    if not got_png:
        print("PDF only; PNG needs rsvg-convert or Inkscape.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
