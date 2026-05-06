# Crawler agent — Act 1 brief

**Who may edit what:** [`docs/PROJECT_USE.md`](../docs/PROJECT_USE.md).

You maintain **scheduled, respectful ingestion** for StateConscious: discover legal artifacts from configured sites, store **immutable snapshots**, log outcomes, and emit **normalized text** (`.txt` / `.md`) only when extraction is warranted — without assuming every publication is a PDF.

---

## Authority & cross-references (read in this order)

1. **Adapter `seed_urls.txt`** under **`src/lib/sources/<region>/<adapter>/`** — **poll URLs** (one per line; optional tab label). **`config.py`** in that folder — **`SOURCE_ID`**, **`CRAWL_NOTES`**, **`RESOURCE_KIND`**, etc.
2. **`mds/agents/sitesCrawl.md`** — Registry conventions (adapter files → **`stateconscious.db`**).
3. **SQLite `source_library`** — Operational list for cron (`url`, `adapter_id`, …). Reconcile from adapter seeds via **`scripts/init_db.py`** (`lib.sources.discovery`); if seeds and DB disagree, **flag for human**; default operational truth is the **DB** for “what runs today.”
4. **Per-site code** — `src/lib/sources/<region>/<adapter_id>/` (e.g. `my/parliament_my/`): `config.py`, `fetch.py`, `parse.py`, and any future `discover.py` / `normalize.py`. **Site-specific rules live next to the adapter**, not in this file.
5. **`crawl_history`** — Every fetch attempt (success, error, hash, paths, parse flags). Use it for audits, budgets, and “what did we already see.”
6. **Project blueprint / game rules** — `blueprint/00-game-rules.md`, PRD: no scope creep mid-milestone; document discoveries in save files first when the harness is active.

---

## Non-negotiables: format-agnostic artifacts

- **Do not assume PDF.** Treat each URL as an **opaque resource** until the response (or file on disk) is classified:
  - Use **`Content-Type`**, URL path, and (if needed) **magic bytes** of the body.
  - Supported *categories* over time may include: `text/html`, `application/pdf`, `application/msword`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `application/zip`, `text/plain`, `application/octet-stream` (unknown), etc.
- **Store raw bytes first** (immutable snapshot path + **SHA-256**). Derive `.txt` / `.md` in a **separate pass** with an appropriate extractor per MIME/category; if extraction is not implemented, store metadata + `extract_status: pending` and move on.
- **Change detection = hash of raw bytes** (for that URL at that moment). Skip re-download when hash unchanged if policy allows; still optionally re-run extract if extractors improved (version that in `meta` or a dedicated column later).

---

## Mission shape (cron)

1. **Discovery pass (cheap):** For each active `source_library` row of kind `index` / `listing` / `feed`, fetch HTML or feed bytes, parse links / entries, enqueue **document** candidates in a frontier (table or `crawl_history`-derived — implement as code evolves). Apply **per-site rules** from the adapter to avoid collecting only nav/chrome.
2. **Fetch pass (budgeted):** Pull **N** frontier items per run (`crawl_budget` config or env). Prefer **newly seen** URLs and **recent** hints (dates in URL/text) over deep backlog when budget is tight.
3. **Extract pass:** For new/changed raw artifacts, run the right text pipeline; write `.txt` / `.md` under `data/derived/<adapter_id>/` (see `docs/ARCHITECTURE.md`) and log outcome.

Cold start: discovery can populate a large frontier; **do not** fetch all heavy documents on day one — respect budget, drain backlog over days, always prioritize **fresh** items when the listing changes.

---

## Operating rules

- **Rate limit and backoff** per host; honor `robots.txt` and site terms where applicable; prefer identifiable `User-Agent` and minimal concurrent requests.
- **TLS / 403:** Log in `crawl_history`; suggest browser-captured sample or `--insecure` only as dev escape hatch, documented in adapter notes.
- **Idempotency:** Same URL + same hash = no duplicate “new document” events for downstream; optional re-extract is a separate decision.
- **Never drop failures silently** — `outcome` / `error_message` / `parse_error` must explain what happened.

---

## Deliverables this agent cares about


| Output                            | Purpose                                             |
| --------------------------------- | --------------------------------------------------- |
| Raw snapshots on disk             | Evidence, diffing, re-parse after better extractors |
| `crawl_history` rows              | Audit trail                                         |
| Frontier queue (when implemented) | Budgeted backlog with prioritization                |
| `.txt` / `.md`                    | Downstream semantic / diff pipeline                 |


---

## When editing code

- Extend **`src/lib/sources/...`** for site quirks; keep this file **policy-only**. System layout: **`docs/ARCHITECTURE.md`**.
- Update the adapter’s **`seed_urls.txt`** and **`config.py`** (`CRAWL_NOTES`, etc.) when poll targets or notes change; follow **`mds/agents/sitesCrawl.md`**.
- Keep **`source_library`** in sync with seeds (`init_db.py`) for anything that should run on cron.

