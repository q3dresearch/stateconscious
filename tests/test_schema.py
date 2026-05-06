from __future__ import annotations

import sqlite3

from lib.db.schema import init_schema
from lib.paths import repo_root


def test_migration_file_on_disk() -> None:
    p = repo_root() / "sql" / "migrations" / "001_init.sql"
    assert p.is_file(), f"Missing {p}"


def test_init_schema_creates_tables() -> None:
    conn = sqlite3.connect(":memory:")
    init_schema(conn)
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name",
    ).fetchall()
    names = {r[0] for r in rows}
    assert "source_library" in names
    assert "crawl_history" in names
    conn.close()
