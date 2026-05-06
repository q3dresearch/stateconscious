#!/usr/bin/env python3
"""
Load ``parsed/*.json`` (parliament_my index extractions) for inspection.

Examples:
  python scripts/view_parsed.py path/to/file.json
  python scripts/view_parsed.py data/snapshots/parliament_my/parsed/ --format md
  python scripts/view_parsed.py path/to/file.json --format pandas   # needs pandas
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path


def load_parsed(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def links_rows(data: dict) -> list[dict]:
    links = data.get("links") or []
    rows: list[dict] = []
    for item in links:
        if not isinstance(item, dict):
            continue
        rows.append(
            {
                "source_id": data.get("source_id"),
                "index_url": data.get("index_url"),
                "url": item.get("url"),
                "text": item.get("text"),
            }
        )
    return rows


def print_csv_stdlib(rows: list[dict]) -> None:
    if not rows:
        print("(no links)")
        return
    buf = io.StringIO()
    fieldnames = list(rows[0].keys())
    w = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
    print(buf.getvalue().rstrip())


def print_md_stdlib(rows: list[dict]) -> None:
    if not rows:
        print("(no links)")
        return
    cols = list(rows[0].keys())

    def cell(v: object) -> str:
        s = "" if v is None else str(v)
        return s.replace("|", "\\|")

    print("| " + " | ".join(cell(c) for c in cols) + " |")
    print("| " + " | ".join("---" for _ in cols) + " |")
    for r in rows:
        print("| " + " | ".join(cell(r.get(c)) for c in cols) + " |")


def print_table_stdlib(rows: list[dict]) -> None:
    """Fixed-width columns without pandas."""
    if not rows:
        print("(no links)")
        return
    cols = list(rows[0].keys())
    widths = {c: len(c) for c in cols}
    for r in rows:
        for c in cols:
            widths[c] = max(widths[c], len("" if r.get(c) is None else str(r.get(c))))
    header = "  ".join(c.ljust(widths[c]) for c in cols)
    print(header)
    print("  ".join("-" * widths[c] for c in cols))
    for r in rows:
        print("  ".join(str(r.get(c) or "").ljust(widths[c]) for c in cols))


def print_pandas(rows: list[dict]) -> None:
    import pandas as pd

    df = pd.DataFrame(rows)
    if df.empty:
        print("(no links)")
        return
    pd.set_option("display.max_rows", 200)
    pd.set_option("display.max_colwidth", 80)
    print(df.to_string(index=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="View parsed index JSON as table / Markdown / CSV.")
    parser.add_argument(
        "path",
        type=Path,
        help="Parsed .json file or a directory of parsed JSON files",
    )
    parser.add_argument(
        "--format",
        choices=("table", "pandas", "md", "csv", "json"),
        default="table",
        help="table = UTF-8 columns (no extra deps); md/csv = stdlib; pandas = needs pandas",
    )
    args = parser.parse_args()

    paths: list[Path]
    if args.path.is_dir():
        paths = sorted(args.path.glob("*.json"))
        if not paths:
            print(f"No JSON files in {args.path}", file=sys.stderr)
            sys.exit(1)
    else:
        paths = [args.path]

    for p in paths:
        data = load_parsed(p)
        print(f"\n=== {p.name} ===", file=sys.stderr)
        if args.format == "json":
            print(json.dumps(data, ensure_ascii=False, indent=2))
            continue

        rows = links_rows(data)
        extras = {
            "link_count": data.get("link_count"),
            "detected_dr_labels": data.get("detected_dr_labels"),
        }
        print(json.dumps(extras, ensure_ascii=False), file=sys.stderr)

        if args.format == "pandas":
            try:
                print_pandas(rows)
            except ImportError:
                print("pandas not installed; use --format table or pip install pandas", file=sys.stderr)
                print_table_stdlib(rows)
        elif args.format == "md":
            print_md_stdlib(rows)
        elif args.format == "csv":
            print_csv_stdlib(rows)
        else:
            print_table_stdlib(rows)


if __name__ == "__main__":
    main()
