from __future__ import annotations

import sqlite3
from pathlib import Path

from lib.paths import repo_root

REPO_ROOT = repo_root()
# Operational SQLite for cron queries (some docs say db.sqlite3 — same role; default filename is below).
DEFAULT_DB_PATH = REPO_ROOT / "stateconscious.db"


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    path = db_path or DEFAULT_DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
