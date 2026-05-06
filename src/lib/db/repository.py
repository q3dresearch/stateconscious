from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any


def upsert_source_library(
    conn: sqlite3.Connection,
    *,
    url: str,
    adapter_id: str,
    label: str | None = None,
    resource_kind: str = "index",
    notes: str | None = None,
) -> int:
    conn.execute(
        """
        INSERT INTO source_library (url, adapter_id, label, resource_kind, notes)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            adapter_id = excluded.adapter_id,
            label = COALESCE(excluded.label, source_library.label),
            resource_kind = excluded.resource_kind,
            notes = COALESCE(excluded.notes, source_library.notes),
            updated_at = datetime('now')
        """,
        (url, adapter_id, label, resource_kind, notes),
    )
    conn.commit()
    row = conn.execute(
        "SELECT id FROM source_library WHERE url = ?",
        (url,),
    ).fetchone()
    assert row is not None
    return int(row["id"])


def source_id_for_url(conn: sqlite3.Connection, url: str) -> int | None:
    row = conn.execute(
        "SELECT id FROM source_library WHERE url = ?",
        (url,),
    ).fetchone()
    return int(row["id"]) if row else None


def insert_crawl_history(
    conn: sqlite3.Connection,
    *,
    source_library_id: int | None,
    adapter_id: str,
    url: str,
    fetched_at: str,
    content_hash: str | None,
    http_status: int | None,
    outcome: str,
    error_message: str | None = None,
    raw_html_relpath: str | None = None,
    parsed_json_relpath: str | None = None,
    parse_succeeded: bool | None = None,
    parse_error: str | None = None,
    meta: dict[str, Any] | None = None,
) -> int:
    meta_json = json.dumps(meta) if meta else None
    parse_int = None if parse_succeeded is None else (1 if parse_succeeded else 0)
    cur = conn.execute(
        """
        INSERT INTO crawl_history (
            source_library_id, adapter_id, url, fetched_at, content_hash,
            http_status, outcome, error_message, raw_html_relpath,
            parsed_json_relpath, parse_succeeded, parse_error, meta_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            source_library_id,
            adapter_id,
            url,
            fetched_at,
            content_hash,
            http_status,
            outcome,
            error_message,
            raw_html_relpath,
            parsed_json_relpath,
            parse_int,
            parse_error,
            meta_json,
        ),
    )
    conn.commit()
    return int(cur.lastrowid)


def relpath_from_repo(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()
