## StateConscious

**StateConscious** is a lens on how legal reality evolves — an intelligence layer that tracks, interprets, and explains changes in governance.

**What “StateConscious” signals**

- **state**: the underlying legal and institutional reality  
- **consciousness**: the tracking, awareness, and interpretation of that reality

Together, this frames StateConscious as:

- **a lens / intelligence layer**, not just a tool
- **a diff engine for public policy**
- **version control for legislation**

### Taglines / positioning

- **StateConscious** — Tracking how reality under law evolves  
- **StateConscious** — A diff engine for public policy  
- **StateConscious** — What changed. Who it affects. Why it matters.  
- **StateConscious** — Version control for legislation

### Repository layout

See **`docs/PROJECT_USE.md`** (human vs agent, adhoc), **`docs/ARCHITECTURE.md`** (layout), **`docs/OPERATIONS.md`** (how to run). Library code: **`src/lib/`**; poll URLs: each adapter’s **`seed_urls.txt`** under **`src/lib/sources/<region>/<adapter>/`** (see **`mds/agents/sitesCrawl.md`**); optional **`src/config/`** for secrets only; DB: **`stateconscious.db`** (`source_library`) for cron; agent briefs: **`mds/agents/`**; human-only notes: **`mds/human/`**; npx skills: **`mds/skills/`**. Repo folder **`stateconscious/`** is the product root. **`scripts/`** are general inspect/DB tools; site crawls use **`python -m lib.sources…`**; **`sql/migrations/`** holds SQLite DDL.

## Installation

Requires **Python 3.12+**.

```bash
cd stateconscious

python -m venv .venv
```

Activate the venv:

- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **macOS / Linux:** `source .venv/bin/activate`

```bash
pip install -r requirements.txt
```

Put **`src`** on `PYTHONPATH` (pytest uses `pytest.ini` automatically):

- **Git Bash / macOS / Linux:** `export PYTHONPATH="$PWD/src"`
- **PowerShell:** `$env:PYTHONPATH = "$PWD\src"`

Quick check:

```bash
PYTHONPATH=src python -c "from lib.sources.my.parliament_my import config; print(config.BILL_INDEX_URLS)"
```

### Dev tests (optional)

```bash
pip install -r requirements-dev.txt
pytest
```

## Parliament CLI (PDF paths)

Dewan Rakyat arkib: structured bill rows and PDF URLs (stdout JSON; optional CSV dir):

```bash
PYTHONPATH=src python -m lib.sources.my.parliament_my.crawl --list-arkib-bills
# optional: --arkib-csv-dir ./out --arkib-resolve-pdfs --insecure
```

List PDFs from seeds (`--list-pdfs`) or parse a saved HTML file (`--parse-html FILE`). See **`python -m lib.sources.my.parliament_my.crawl --help`**.

SQLite (repo root `stateconscious.db`, gitignored) — seed **`source_library`** and inspect history:

```bash
python scripts/init_db.py
python scripts/inspect_crawl.py
```

**Note:** The parliament **`crawl`** module no longer runs a default index fetch or **`--db`** audit trail; use **`docs/OPERATIONS.md`** for DB-oriented workflows.

Inspect parsed JSON if you have **`data/derived/.../parsed/`** snapshots from other tooling:

```bash
python scripts/view_parsed.py data/derived/parliament_my/parsed/<64-char-sha256>/ --format md
```

Crawler policy: **`mds/agents/crawlerAgent.md`**.

Optional: copy `.env.example` to `.env` when you add LLM calls.
