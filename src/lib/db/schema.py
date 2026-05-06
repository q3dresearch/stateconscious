from __future__ import annotations

import sqlite3

from lib.paths import repo_root

MIGRATIONS_DIR = repo_root() / "sql" / "migrations"


def init_schema(conn: sqlite3.Connection, *, migration_file: str = "001_init.sql") -> None:
    path = MIGRATIONS_DIR / migration_file
    if not path.is_file():
        raise FileNotFoundError(f"Migration not found: {path}")
    sql = path.read_text(encoding="utf-8")
    conn.executescript(sql)
    conn.commit()
