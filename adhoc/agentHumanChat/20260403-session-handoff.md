---
topic: pdf-ingestion-from-bills-csv
status: open
---

## agent — session wrap-up & next session brief

### Where things stand (2026-04-03)

- **Parliament MY arkib:** `lang=en` landing + shared `requests.Session` for dhtmlx XHR and PDF resolve cookies; BI-only billindex surface (BM paths rewritten / avoided); parallel `--arkib-resolve-pdfs`; `list_*_arkib_dhtmlx_sweep` return **`(data, cookies)`**.
- **CSV output:** `crawl --list-arkib-bills --arkib-csv-dir …` → `bills_{year}.csv` under chosen dir (e.g. `src/out/bills_csv/`). Columns include `pdf_url`, `dr_label`, `year`, `seed_url`, `pdf_resolve_status`, etc. (`parse.ARKIB_BILL_CSV_FIELDS`).
- **Ops:** `docs/OPERATIONS.md`, adapter under `src/lib/sources/my/parliament_my/`.

### Next session — planned work

1. **Read PDFs from returned CSV**  
   - Ingest rows (per year file or merged): use `pdf_url` (+ `Referer` / `seed_url` as today’s fetch layer expects). Handle failures, retries, and TLS/`--insecure` parity if needed.

2. **Store PDFs under `data/` and wire DB**  
   - Align with existing content-addressed layout: `lib/paths.py`, `lib/artifacts.py` (`raw_pdf_snapshot_path` pattern already used elsewhere).  
   - Extend SQLite schema / migrations: store **content hash**, **canonical URL**, **local relpath**, **source row id / bill key** (e.g. year + `dr_label` or stable id), **ingested_at**, optional **csv provenance** (file + row).  
   - Reuse or extend `crawl_history` vs new `bill_pdf_artifacts` table — decide in design (avoid duplicating audit semantics).

3. **Pandas layer**  
   - DataFrame from CSV + join to DB export (or SQL → pandas) for: querying, **change detection** (hash or mtime per URL), bill metadata columns.  
   - Keep logic in `lib/`; thin script optional under `scripts/`.

4. **Embeddings / semantic search (decision)**  
   - **Decide** whether bill PDFs need **chunking + embeddings** and **semantic search** (user mentioned “gbrain” infra).  
   - If yes: scope storage (vector DB vs sqlite+json), chunking strategy for RUU PDFs, Malay/English, cost/latency; if no: document “keyword + metadata only” and close the spike.

### Files / entrypoints to re-read first

- `src/lib/artifacts.py`, `src/lib/db/schema.py`, `sql/migrations/`
- `src/lib/sources/my/parliament_my/fetch.py` (`probe_pdf_magic`, `fetch_url`)
- `tests/test_schema.py`, live test `tests/test_parliament_live_year_csv_pdf.py` (optional network)

### Open questions for human (optional)

- **DB:** single table for “bill PDF object” vs separate link table for URL history?  
- **gbrain:** required for MVP or phase 2?

## human

https://github.com/EveryInc/compound-engineering-plugin

_(answers / decisions for the next session)_
