#!/usr/bin/env python3
"""Extract page image records from HTML/Markdown files into a CSV file.

This script standardizes <img> tag records and optional slide/front-matter slide records
for the `webPage` import workflow.

Columns:
  page, page_title, record_type, item_index, src, alt, title, class, link, caption

Usage:
  python export_img_tags.py                # scan current folder and export imgs
  python export_img_tags.py file.html      # scan a single file
  python export_img_tags.py dir -o out.csv
  python export_img_tags.py --include-slides gallery/fungi
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Any

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None  # type: ignore

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # type: ignore


CSV_FIELDS = [
    "page",
    "page_title",
    "record_type",
    "item_index",
    "src",
    "alt",
    "title",
    "class",
    "link",
    "caption",
]


def extract_front_matter(text: str) -> str | None:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1]
    return None


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def parse_front_matter(text: str) -> dict[str, Any]:
    yaml_text = extract_front_matter(text)
    if not yaml_text:
        return {}
    if yaml is not None:
        try:
            data = yaml.safe_load(yaml_text)
            if isinstance(data, dict):
                return data
        except Exception:
            pass
    return parse_yaml_fallback(yaml_text)


def parse_yaml_fallback(yaml_text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    lines = yaml_text.splitlines()
    current_key: str | None = None
    current_item: dict[str, Any] | None = None
    in_list = False
    base_indent = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if re.match(r"^[^\s].*:$", line):
            current_key = stripped[:-1]
            if current_key == "slides":
                data["slides"] = []
                in_list = True
                base_indent = None
            else:
                data[current_key] = None
                in_list = False
            current_item = None
            continue

        if in_list and re.match(r"^\s*-\s+.*", line):
            if base_indent is None:
                base_indent = len(line) - len(line.lstrip())
            if current_item is not None:
                data["slides"].append(current_item)
            current_item = {}
            payload = line.strip()[1:].strip()
            if ":" in payload:
                key, value = payload.split(":", 1)
                current_item[key.strip()] = _parse_scalar(value.strip())
            continue

        if in_list and current_item is not None:
            indent = len(line) - len(line.lstrip())
            if base_indent is not None and indent > base_indent:
                if ":" in stripped:
                    key, value = stripped.split(":", 1)
                    current_item[key.strip()] = _parse_scalar(value.strip())
                continue

        if current_key and not in_list and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key.strip() == current_key:
                data[current_key] = _parse_scalar(value.strip())

    if in_list and current_item is not None:
        data["slides"].append(current_item)

    return data


def _parse_scalar(value: str) -> str:
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1]
    return value


def find_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    files: list[Path] = []
    for ext in ("*.html", "*.htm", "*.md", "*.markdown"):
        files.extend(path.rglob(ext))
    return sorted(files)


def extract_page_title(front_matter: dict[str, Any], soup: Any) -> str:
    title = front_matter.get("title") or ""
    if title:
        return str(title)
    if soup is not None and soup.title:
        return soup.title.string.strip() if soup.title.string else ""
    return ""


def find_caption_for_img(img: Any) -> str:
    candidates = []
    if img.parent is not None:
        for tag in img.parent.find_all(["p", "figcaption"], class_=("caption",), recursive=False):
            candidates.append(tag)
    sibling = img.find_next_sibling()
    if sibling and sibling.name in ("p", "figcaption") and "caption" in (sibling.get("class") or []):
        candidates.append(sibling)
    if sibling and sibling.name == "figcaption":
        candidates.append(sibling)
    if candidates:
        return candidates[0].get_text(separator=" ", strip=True)
    return ""


def normalize_path(path: Path) -> str:
    return path.as_posix()


def parse_img_rows(file_path: Path, text: str, include_imgs: bool) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if not include_imgs:
        return rows

    html = strip_front_matter(text)
    soup = None
    if BeautifulSoup is not None:
        soup = BeautifulSoup(html, "html.parser")
    if soup is None:
        return rows

    front_matter = parse_front_matter(text)
    page_title = extract_page_title(front_matter, soup)

    for index, img in enumerate(soup.find_all("img"), start=1):
        src = str(img.get("src", "") or "")
        alt = str(img.get("alt", "") or "")
        title = str(img.get("title", "") or "")
        cssclass = " ".join(img.get("class", [])) if img.get("class") else ""
        parent_a = img.find_parent("a")
        link = str(parent_a.get("href", "")) if parent_a else ""
        caption = find_caption_for_img(img)

        rows.append(
            {
                "page": normalize_path(file_path),
                "page_title": page_title,
                "record_type": "img",
                "item_index": str(index),
                "src": src,
                "alt": alt,
                "title": title,
                "class": cssclass,
                "link": link,
                "caption": caption,
            }
        )

    return rows


def parse_slide_rows(file_path: Path, text: str, include_slides: bool) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if not include_slides:
        return rows

    front_matter = parse_front_matter(text)
    slides = front_matter.get("slides")
    if not isinstance(slides, list):
        return rows

    page_title = str(front_matter.get("title", "") or "")
    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            continue
        rows.append(
            {
                "page": normalize_path(file_path),
                "page_title": page_title,
                "record_type": "slide",
                "item_index": str(index),
                "src": str(slide.get("src", "") or ""),
                "alt": str(slide.get("alt", "") or ""),
                "title": "",
                "class": "",
                "link": str(slide.get("link", "") or ""),
                "caption": str(slide.get("caption", "") or ""),
            }
        )
    return rows


def collect_rows(files: list[Path], include_imgs: bool, include_slides: bool) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = file_path.read_text(encoding="latin-1")
            except Exception:
                continue

        rows.extend(parse_img_rows(file_path, text, include_imgs))
        rows.extend(parse_slide_rows(file_path, text, include_slides))
    return rows


def write_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract web page image/slide records into CSV for database import.")
    parser.add_argument("input", nargs="?", default=".", help="Input file or directory to scan")
    parser.add_argument("-o", "--output", default="webpage_records.csv", help="Output CSV path")
    parser.add_argument("--include-imgs", dest="include_imgs", action="store_true", default=True, help="Include <img> tag records (default)")
    parser.add_argument("--no-imgs", dest="include_imgs", action="store_false", help="Do not extract <img> tag records")
    parser.add_argument("--include-slides", dest="include_slides", action="store_true", default=True, help="Include slide front-matter records (default)")
    parser.add_argument("--no-slides", dest="include_slides", action="store_false", help="Do not extract slide front-matter records")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Input path does not exist: {input_path}")

    files = find_files(input_path)
    if not files:
        raise SystemExit("No files found to scan.")

    rows = collect_rows(files, args.include_imgs, args.include_slides)
    if not rows:
        raise SystemExit("No records found in the scanned files.")

    write_csv(rows, Path(args.output))
    print(
        f"Exported {len(rows)} rows from {len(files)} file(s) to {args.output} "
        f"(imgs={args.include_imgs}, slides={args.include_slides})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
