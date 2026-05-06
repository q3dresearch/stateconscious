#!/usr/bin/env python3
"""Create ``stateconscious.db`` and seed ``source_library`` from adapter ``seed_urls.txt`` files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from lib.sources.discovery import iter_source_library_seeds  # noqa: E402
from lib.db.connection import DEFAULT_DB_PATH, connect  # noqa: E402
from lib.db.repository import upsert_source_library  # noqa: E402
from lib.db.schema import init_schema  # noqa: E402


def main() -> None:
    conn = connect()
    init_schema(conn)
    for row in iter_source_library_seeds():
        upsert_source_library(conn, **row)
    conn.close()
    print(f"OK: schema ready and sources seeded at {DEFAULT_DB_PATH}")


if __name__ == "__main__":
    main()
