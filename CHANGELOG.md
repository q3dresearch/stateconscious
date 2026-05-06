# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Docs and agent briefs now describe **per-adapter `seed_urls.txt`**, **`python -m lib.sources…`**, and optional **`src/config/`** (no central `sites.yaml` / `fetch_parliament_indices.py`).
- Agent briefs live under **`mds/agents/`** (was `src/agents/`). Added **`mds/skills/`** (npx skills) and documented **`mds/human/`** as human-only.
- **`src/config/sites.md`** → **`sites.yaml`** + central **`seed_urls.txt`** (historical). **Current:** poll URLs and crawl notes live per adapter under **`src/lib/sources/.../`** (`seed_urls.txt`, `config.py`); `init_db.py` uses **`lib.sources.discovery`** (no PyYAML registry).

### Added

- **`src/lib/sources/my/parliament_my/README.md`** — per-adapter runbook (no sitemap, URL hints); **`sitesCrawl.md`** documents README vs config vs future sitemap crawl.
- **`docs/PROJECT_USE.md`** — single playbook: human vs agent, `adhoc/todo`, `adhoc/agentHumanChat`, cron failure and maintenance direction. Other agent docs trimmed to point here.
- **`adhoc/agentHumanChat/`** (+ **`resolved/`**) for agent-to-human threads.
- **`adhoc/todo/README.md`** (inbox instructions; not a work item), **`adhoc/done/`**, **`cron/lib/adhoc.py`** — `list_todo_markdown()` skips `README.md` / `_*.md`; no auto-archive. Seeds may set **`seed_role`** / **`from_adhoc`**; notes propagate to SQLite.
- Parliament **`--discover-pdfs`**: bounded PDF download after indices (`data/raw/.../pdf/<hash>/`), optional HTML follow (`--follow-html`), `runs.jsonl` + `crawl_history` meta `resource_kind=pdf`.
- `scripts/inspect_crawl.py` — dump `source_library` + recent `crawl_history`.
- Fetch **`--verbose` / `-v`** — stderr trace for DB path, inserts, row counts.
- `docs/ARCHITECTURE.md`, `docs/OPERATIONS.md` — system map and operator playbook.
- `sql/migrations/001_init.sql` — SQLite schema; `lib.db.schema.init_schema` applies it.
- `src/lib/` package — `sources/` (incl. **`parser/`**, **`discovery`**), `db/`, `artifacts` with hash-scoped `data/raw` / `data/derived` paths.
- `tests/fixtures/html/` + pytest for parliament index parser.
- GitHub Actions workflow — pytest on push/PR.
