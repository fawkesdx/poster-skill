#!/usr/bin/env python3
"""Export poster.svg to a vector PDF and a PNG.

The PNG long edge is 900 px, so a draft is small enough to judge by eye.
Pass --ppi 150 (or 300) for a print-resolution PNG. Needs rsvg-convert or Inkscape.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from check_poster import page_size_mm


def raster_width(svg: Path, ppi: float | None, long_edge: int) -> int:
    root = ET.fromstring(svg.read_text(encoding="utf-8"))
    width, height, _ = page_size_mm(root)
    if not width or not height:
        return long_edge
    if ppi:
        return max(1, round(width / 25.4 * ppi))
    return max(1, round(width / max(width, height) * long_edge))


def run(cmd: list[str]) -> bool:
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return True


def export(svg: Path, ppi: float | None, long_edge: int) -> tuple[bool, bool, str]:
    pdf = svg.with_suffix(".pdf")
    png_name = svg.stem + ("-proof.png" if ppi else "-preview.png")
    png = svg.with_name(png_name)
    width = str(raster_width(svg, ppi, long_edge))
    tools = []
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        tools.append(
            (
                "rsvg-convert",
                [rsvg, "-f", "pdf", "-o", str(pdf), str(svg)],
                [rsvg, "-f", "png", "-o", str(png), "-w", width, str(svg)],
            )
        )
    ink = shutil.which("inkscape")
    if ink:
        tools.append(
            (
                "inkscape",
                [ink, str(svg), "--export-type=pdf", f"--export-filename={pdf}"],
                [ink, str(svg), "--export-type=png", f"--export-filename={png}", "-w", width],
            )
        )
    for name, pdf_cmd, png_cmd in tools:
        got_pdf = run(pdf_cmd)
        got_png = run(png_cmd)
        if got_pdf or got_png:
            return got_pdf, got_png, name
    return False, False, ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export a poster SVG to PDF and a PNG.")
    parser.add_argument("svg")
    parser.add_argument("--ppi", type=float, default=None, help="print PNG resolution; omit for a 900 px preview")
    parser.add_argument("--long-edge", type=int, default=900)
    args = parser.parse_args(argv)
    svg = Path(args.svg)
    if not svg.is_file():
        print(f"no such file: {svg}", file=sys.stderr)
        return 1
    got_pdf, got_png, tool = export(svg, args.ppi, args.long_edge)
    if not got_pdf and not got_png:
        print("no converter found. Install librsvg (rsvg-convert) or Inkscape.", file=sys.stderr)
        print("the SVG is still the source file.", file=sys.stderr)
        return 2
    print(f"exported with {tool}")
    if got_pdf:
        print(svg.with_suffix(".pdf"))
    if got_png:
        name = svg.stem + ("-proof.png" if args.ppi else "-preview.png")
        print(svg.with_name(name))
    if not got_png:
        print("PDF only; the PNG export failed.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
