#!/usr/bin/env python3
"""Export slides defined in YAML front matter to CSV."""

from __future__ import annotations

import argparse
import csv
import os
import re
from pathlib import Path
from typing import Any


def extract_front_matter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1].strip()


def try_import_yaml() -> Any:
    try:
        import yaml

        return yaml
    except ImportError:
        return None


def parse_yaml_fallback(yaml_text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    lines = yaml_text.splitlines()
    current_key: str | None = None
    current_list_item: dict[str, Any] | None = None
    in_slides = False
    base_indent = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if re.match(r"^[^\s].*:$", line):
            current_key = stripped[:-1]
            if current_key == "slides":
                data["slides"] = []
                in_slides = True
                base_indent = None
            else:
                data[current_key] = None
                in_slides = False
            current_list_item = None
            continue

        if in_slides and re.match(r"^\s*-\s+.*", line):
            if base_indent is None:
                base_indent = len(line) - len(line.lstrip())
            if current_list_item is not None:
                data["slides"].append(current_list_item)
            current_list_item = {}
            item_line = line.strip()[1:].strip()
            if item_line:
                if ":" in item_line:
                    key, value = item_line.split(":", 1)
                    current_list_item[key.strip()] = _parse_scalar(value.strip())
            continue

        if in_slides and current_list_item is not None:
            line_indent = len(line) - len(line.lstrip())
            if base_indent is not None and line_indent > base_indent:
                if ":" in stripped:
                    key, value = stripped.split(":", 1)
                    current_list_item[key.strip()] = _parse_scalar(value.strip())
                continue

        if current_key and not in_slides and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key.strip() == current_key:
                data[current_key] = _parse_scalar(value.strip())

    if in_slides and current_list_item is not None:
        data["slides"].append(current_list_item)

    return data


def _parse_scalar(value: str) -> str:
    if value.startswith("'") and value.endswith("'") or value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value


def parse_front_matter(yaml_text: str) -> dict[str, Any]:
    yaml_module = try_import_yaml()
    if yaml_module is not None:
        return yaml_module.safe_load(yaml_text) or {}
    return parse_yaml_fallback(yaml_text)


def find_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    files: list[Path] = []
    for extension in ["*.html", "*.md", "*.markdown"]:
        files.extend(path.rglob(extension))
    return sorted(files)


def load_page_data(file_path: Path) -> dict[str, Any] | None:
    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = file_path.read_text(encoding="latin-1")

    front_matter = extract_front_matter(text)
    if not front_matter:
        return None

    data = parse_front_matter(front_matter)
    if not isinstance(data, dict):
        return None
    return data


def collect_slides(files: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for file_path in files:
        page_data = load_page_data(file_path)
        if not page_data:
            continue
        slides = page_data.get("slides")
        if not slides or not isinstance(slides, list):
            continue
        page_title = page_data.get("title", "") or ""
        for slide in slides:
            if not isinstance(slide, dict):
                continue
            rows.append(
                {
                    "page": str(file_path).replace("\\", "/"),
                    "title": page_title,
                    "src": str(slide.get("src", "") or ""),
                    "alt": str(slide.get("alt", "") or ""),
                    "caption": str(slide.get("caption", "") or ""),
                    "link": str(slide.get("link", "") or ""),
                }
            )
    return rows


def write_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["page", "title", "src", "alt", "caption", "link"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export gallery page slides from YAML front matter into CSV.")
    parser.add_argument("input", nargs="?", default=".", help="Input file or directory to scan (default: current directory).")
    parser.add_argument("-o", "--output", default="slides.csv", help="Output CSV file path (default: slides.csv).")
    parser.add_argument("--no-title", action="store_true", help="Exclude page title column from output.")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Error: input path does not exist: {input_path}")

    files = find_files(input_path)
    rows = collect_slides(files)
    if not rows:
        raise SystemExit("No slides found in the provided input.")

    output_path = Path(args.output)
    write_csv(rows, output_path)

    print(f"Exported {len(rows)} slides from {len(files)} file(s) to {output_path}.")
    if args.no_title:
        print("Note: title column was excluded from the output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
