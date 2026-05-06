-- StateConscious initial schema (SQLite).
-- Apply via lib.db.schema.init_schema

-- Canonical URLs we may crawl (indexes, feeds, document pages).
CREATE TABLE IF NOT EXISTS source_library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL UNIQUE,
    adapter_id TEXT NOT NULL,
    label TEXT,
    resource_kind TEXT NOT NULL DEFAULT 'index',
    poll_interval_s INTEGER,
    is_active INTEGER NOT NULL DEFAULT 1,
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- One row per fetch/parse attempt (cron-friendly audit trail).
CREATE TABLE IF NOT EXISTS crawl_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_library_id INTEGER,
    adapter_id TEXT NOT NULL,
    url TEXT NOT NULL,
    fetched_at TEXT NOT NULL,
    content_hash TEXT,
    http_status INTEGER,
    outcome TEXT NOT NULL,
    error_message TEXT,
    raw_html_relpath TEXT,
    parsed_json_relpath TEXT,
    parse_succeeded INTEGER,
    parse_error TEXT,
    meta_json TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (source_library_id) REFERENCES source_library(id)
);

CREATE INDEX IF NOT EXISTS idx_crawl_history_url ON crawl_history(url);
CREATE INDEX IF NOT EXISTS idx_crawl_history_fetched ON crawl_history(fetched_at);
CREATE INDEX IF NOT EXISTS idx_crawl_history_adapter ON crawl_history(adapter_id);
