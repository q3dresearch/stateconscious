#!/usr/bin/env python3
"""Print ``source_library`` and recent ``crawl_history`` rows — smoke-test the audit trail."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from lib.db.connection import DEFAULT_DB_PATH, connect  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(description="Inspect SQLite crawl audit tables.")
    p.add_argument(
        "--database",
        type=Path,
        default=None,
        help=f"SQLite path (default: {DEFAULT_DB_PATH})",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Max crawl_history rows to show (latest first).",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of plain text.",
    )
    args = p.parse_args()

    conn = connect(args.database)
    init_row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='crawl_history'",
    ).fetchone()
    if not init_row:
        print("No crawl_history table — run scripts/init_db.py first.", file=sys.stderr)
        sys.exit(1)

    sources = conn.execute(
        """
        SELECT id, adapter_id, resource_kind, substr(url, 1, 80) AS url_short, label
        FROM source_library
        ORDER BY id
        """
    ).fetchall()

    lim = int(max(1, min(args.limit, 500)))
    hist = conn.execute(
        """
        SELECT id, source_library_id, adapter_id, fetched_at, outcome, http_status,
               substr(content_hash, 1, 16) AS hash16,
               raw_html_relpath, parsed_json_relpath, parse_succeeded, substr(error_message, 1, 60) AS err
        FROM crawl_history
        ORDER BY id DESC
        LIMIT ?
        """,
        (lim,),
    ).fetchall()
    conn.close()

    if args.json:
        out = {
            "source_library": [dict(s) for s in sources],
            "crawl_history": [dict(h) for h in hist],
        }
        print(json.dumps(out, indent=2, default=str))
        return

    print("=== source_library ===")
    if not sources:
        print("(empty)")
    for s in sources:
        print(
            f"  id={s['id']} adapter={s['adapter_id']} kind={s['resource_kind']}\n"
            f"    url={s['url_short']}\n"
            f"    label={s['label']}",
        )

    print("\n=== crawl_history (latest first) ===")
    if not hist:
        print("(empty — did you run fetch with --db?)\n")
        print(
            "  Example: PYTHONPATH=src python -m lib.sources.my.parliament_my.crawl "
            "--db --insecure -v",
        )
        return
    for h in hist:
        ps = h["parse_succeeded"]
        ps_s = "?" if ps is None else ("1" if ps else "0")
        print(
            f"  id={h['id']} src_lib_id={h['source_library_id']} at={h['fetched_at']}\n"
            f"    outcome={h['outcome']} http={h['http_status']} hash16={h['hash16']} parse_ok={ps_s}\n"
            f"    raw={h['raw_html_relpath']}\n"
            f"    parsed={h['parsed_json_relpath']}\n"
            f"    err={h['err']}",
        )


if __name__ == "__main__":
    main()
