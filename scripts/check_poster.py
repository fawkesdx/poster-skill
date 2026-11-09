#!/usr/bin/env python3
"""Check a poster SVG for size, type floors, and leftover scaffold text.

The sheet uses millimetres: width="841mm" and a viewBox in the same numbers.
Every font-size must use pt. Raster images should carry data-pxw and data-pxh
so placement can be checked at 150 pixels per inch.
"""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET

XLINK = "http://www.w3.org/1999/xlink"


def local(tag: str) -> str:
    return tag.split("}")[-1] if isinstance(tag, str) else ""


def classes(el: ET.Element) -> set[str]:
    return set((el.get("class") or "").split())


def parse_length(value: str | None) -> tuple[float | None, str | None]:
    if not value:
        return None, None
    text = value.strip().lower()
    for unit in ("mm", "px", "pt", "cm", "in"):
        if text.endswith(unit):
            return float(text[: -len(unit)]), unit
    return float(text), None


def to_mm(value: float, unit: str | None) -> float | None:
    if unit in (None, "mm"):
        return value
    if unit == "cm":
        return value * 10
    if unit == "in":
        return value * 25.4
    if unit == "pt":
        return value * 25.4 / 72
    if unit == "px":
        return value * 25.4 / 96
    return None


def parse_font(value: str | None) -> tuple[float | None, str | None]:
    if not value:
        return None, None
    text = value.strip().lower()
    number, unit = parse_length(text)
    if number is None:
        return None, None
    if unit == "pt" or unit is None:
        return number, unit or "bare"
    if unit == "px":
        return number, "px"
    if unit == "mm":
        return number * 72 / 25.4, "mm"
    if unit == "in":
        return number * 72, "in"
    return None, unit


def style_map(style: str | None) -> dict[str, str]:
    out: dict[str, str] = {}
    if not style:
        return out
    for part in style.split(";"):
        if ":" not in part:
            continue
        key, val = part.split(":", 1)
        out[key.strip().lower()] = val.strip()
    return out


def page_size_mm(root: ET.Element) -> tuple[float | None, float | None, list[str]]:
    notes: list[str] = []
    width, w_unit = parse_length(root.get("width"))
    height, h_unit = parse_length(root.get("height"))
    box = (root.get("viewBox") or "").split()
    if width is None or height is None:
        if len(box) == 4:
            return float(box[2]), float(box[3]), ["page size taken from viewBox; set width and height in mm"]
        return None, None, ["SVG has no width and height"]
    w_mm = to_mm(width, w_unit)
    h_mm = to_mm(height, h_unit)
    if w_unit is None or h_unit is None:
        notes.append("width and height should use mm")
    return w_mm, h_mm, notes


def href_of(el: ET.Element) -> str:
    return el.get("href") or el.get(f"{{{XLINK}}}href") or ""


def direct_text(el: ET.Element) -> str:
    return el.text or ""


def check_svg(
    text: str,
    expect: str | None = None,
    min_pt: float = 20,
    warn_pt: float = 24,
    title_min_pt: float = 60,
    min_ppi: float = 150,
) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return [("FAIL", f"SVG did not parse: {exc}")]
    if local(root.tag) != "svg":
        findings.append(("FAIL", "root element is not svg"))

    width, height, notes = page_size_mm(root)
    for note in notes:
        findings.append(("WARN", note))
    if width is None or height is None:
        findings.append(("FAIL", "could not read the page size in mm"))
    else:
        findings.append(("OK", f"page {width:.0f} × {height:.0f} mm"))
        if expect:
            ew, eh = (float(part) for part in expect.lower().split("x"))
            if abs(width - ew) > 1 or abs(height - eh) > 1:
                findings.append(("FAIL", f"page is {width:.0f}×{height:.0f} mm, expected {ew:.0f}×{eh:.0f} mm"))

    parent: dict[ET.Element, ET.Element | None] = {root: None}
    for el in root.iter():
        for child in list(el):
            parent[child] = el

    def inherited_font(el: ET.Element) -> tuple[float | None, str | None]:
        seen = el
        while seen is not None:
            size, unit = parse_font(seen.get("font-size"))
            if size is None:
                size, unit = parse_font(style_map(seen.get("style")).get("font-size"))
            if size is not None:
                return size, unit
            seen = parent.get(seen)
        return None, None

    def inherited_classes(el: ET.Element) -> set[str]:
        found: set[str] = set()
        seen = el
        while seen is not None:
            found |= classes(seen)
            seen = parent.get(seen)
        return found

    saw_title = False
    for el in root.iter():
        kind = local(el.tag)
        if kind == "script":
            findings.append(("FAIL", "script element is not allowed"))
        if "guide" in classes(el):
            findings.append(("WARN", "guide geometry is still on the sheet"))
        if kind == "image":
            findings.extend(_image(el, min_ppi))
        if kind not in ("text", "tspan"):
            continue
        shown = direct_text(el).strip()
        if kind == "tspan" or not shown:
            if shown:
                findings.extend(
                    _type(shown, *inherited_font(el), inherited_classes(el), min_pt, warn_pt, title_min_pt, words=False)
                )
            continue
        full = " ".join(el.itertext()).strip()
        size, unit = inherited_font(el)
        role = inherited_classes(el)
        if "title" in role:
            saw_title = True
        findings.extend(_type(full, size, unit, role, min_pt, warn_pt, title_min_pt, words=True))

    if not saw_title:
        findings.append(("WARN", "no text with class title"))
    return findings


def _type(
    shown: str,
    size: float | None,
    unit: str | None,
    role: set[str],
    min_pt: float,
    warn_pt: float,
    title_min_pt: float,
    words: bool,
) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    label = shown if len(shown) <= 48 else shown[:45] + "..."
    if "PLACEHOLDER" in shown:
        findings.append(("FAIL", f"replace scaffold text: {label}"))
    if size is None:
        findings.append(("FAIL", f"text has no font-size: {label}"))
    else:
        if unit == "bare":
            findings.append(("FAIL", f"font-size needs a pt unit: {label}"))
        elif unit == "px":
            findings.append(("WARN", f"font-size uses px; use pt: {label}"))
        if "title" in role and size < title_min_pt:
            findings.append(("FAIL", f"title is {size:.0f} pt, floor is {title_min_pt:.0f} pt"))
        elif size < min_pt:
            findings.append(("FAIL", f"text is {size:.0f} pt, floor is {min_pt:.0f} pt: {label}"))
        elif "title" not in role and size < warn_pt:
            findings.append(("WARN", f"text is {size:.0f} pt, aim for {warn_pt:.0f} pt: {label}"))
    if words and "url" not in role:
        count = len(shown.split())
        limit = 30 if "title" in role else 12
        hard = 40 if "title" in role else 40
        if count > hard and "title" not in role:
            findings.append(("FAIL", f"text is a paragraph ({count} words); move it to notes"))
        elif count > limit:
            findings.append(("WARN", f"text is long ({count} words); a label should name the thing"))
    return findings


def _image(el: ET.Element, min_ppi: float) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    href = href_of(el)
    if not href:
        findings.append(("FAIL", "image has no href"))
        return findings
    if href.startswith(("http://", "https://")):
        findings.append(("FAIL", "image href is remote; use a local file"))
    width, unit = parse_length(el.get("width"))
    pxw = el.get("data-pxw")
    if width is None:
        findings.append(("WARN", f"image has no width: {href}"))
        return findings
    width_mm = to_mm(width, unit)
    if not pxw or not el.get("data-pxh"):
        findings.append(("WARN", f"set data-pxw and data-pxh on {href}"))
        return findings
    if width_mm is None or width_mm <= 0:
        findings.append(("WARN", f"could not read image width in mm: {href}"))
        return findings
    ppi = float(pxw) / (width_mm / 25.4)
    if ppi < min_ppi:
        findings.append(("FAIL", f"{href} is {ppi:.0f} ppi at the placed size; need {min_ppi:.0f}"))
    return findings


def _print(findings: list[tuple[str, str]]) -> int:
    fails = 0
    for level, message in findings:
        print(f"{level}: {message}")
        if level == "FAIL":
            fails += 1
    if fails:
        print(f"{fails} fail")
        return 1
    print("no fail")
    return 0


def self_test() -> int:
    page = 'xmlns="http://www.w3.org/2000/svg" width="841mm" height="1189mm" viewBox="0 0 841 1189"'

    def run(body: str, **kwargs: object) -> list[tuple[str, str]]:
        return check_svg(f"<svg {page}>{body}</svg>", **kwargs)  # type: ignore[arg-type]

    def levels(findings: list[tuple[str, str]]) -> set[str]:
        return {level for level, _ in findings}

    def messages(findings: list[tuple[str, str]]) -> str:
        return "\n".join(message for _, message in findings)

    clean = run(
        '<text class="title" font-size="72pt">Short title</text>'
        '<text class="label" font-size="28pt">A label</text>'
    )
    assert "FAIL" not in levels(clean), messages(clean)

    small = run('<text class="title" font-size="72pt">Title</text><text font-size="18pt">Tiny</text>')
    assert any("floor" in msg for _, msg in small if _ == "FAIL"), messages(small)

    warn = run('<text class="title" font-size="72pt">Title</text><text font-size="22pt">Close</text>')
    assert "FAIL" not in levels(warn) and "WARN" in levels(warn), messages(warn)

    title = run('<text class="title" font-size="40pt">Title</text>')
    assert any("title" in msg for _, msg in title if _ == "FAIL"), messages(title)

    hold = run('<text class="title" font-size="72pt">PLACEHOLDER title</text>')
    assert any("scaffold" in msg for _, msg in hold if _ == "FAIL"), messages(hold)

    paragraph = " ".join(["word"] * 41)
    prose = run(f'<text class="title" font-size="72pt">Title</text><text font-size="28pt">{paragraph}</text>')
    assert any("paragraph" in msg for _, msg in prose if _ == "FAIL"), messages(prose)

    bare = run('<text class="title" font-size="72">Title</text>')
    assert any("pt unit" in msg for _, msg in bare if _ == "FAIL"), messages(bare)

    guide = run(
        '<text class="title" font-size="72pt">Title</text>'
        '<rect class="guide" x="0" y="0" width="10" height="10"/>'
    )
    assert any("guide" in msg for _, msg in guide if _ == "WARN"), messages(guide)

    soft = run(
        '<text class="title" font-size="72pt">Title</text>'
        '<image href="art/a.png" x="0" y="0" width="100" height="80" data-pxw="100" data-pxh="80"/>'
    )
    assert any("ppi" in msg for _, msg in soft if _ == "FAIL"), messages(soft)

    sharp = run(
        '<text class="title" font-size="72pt">Title</text>'
        '<image href="art/a.png" x="0" y="0" width="100" height="80" data-pxw="800" data-pxh="640"/>'
    )
    assert "FAIL" not in levels(sharp), messages(sharp)

    size = run('<text class="title" font-size="72pt">Title</text>', expect="420x594")
    assert any("expected" in msg for _, msg in size if _ == "FAIL"), messages(size)

    remote = run(
        '<text class="title" font-size="72pt">Title</text>'
        '<image href="https://example.com/a.png" width="100" data-pxw="800" data-pxh="800"/>'
    )
    assert any("remote" in msg for _, msg in remote if _ == "FAIL"), messages(remote)

    print("self-test ok")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a poster SVG against poster-skill floors.")
    parser.add_argument("svg", nargs="?", help="path to the poster SVG")
    parser.add_argument("--expect", help="page size in mm, such as 841x1189")
    parser.add_argument("--min-pt", type=float, default=20)
    parser.add_argument("--warn-pt", type=float, default=24)
    parser.add_argument("--title-min-pt", type=float, default=60)
    parser.add_argument("--min-ppi", type=float, default=150)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.svg:
        parser.error("give an SVG path, or --self-test")
    with open(args.svg, encoding="utf-8") as handle:
        text = handle.read()
    return _print(
        check_svg(
            text,
            expect=args.expect,
            min_pt=args.min_pt,
            warn_pt=args.warn_pt,
            title_min_pt=args.title_min_pt,
            min_ppi=args.min_ppi,
        )
    )


if __name__ == "__main__":
    sys.exit(main())
