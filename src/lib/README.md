# lib/ — Library Roadmap

All shared code for the StateConscious pipeline lives here.
**Rule:** nothing goes at `lib/` root unless it is infrastructure used by every category (`paths.py`, `artifacts.py`).

## Structure

```
src/lib/
  paths.py          shared: repo_root() — single source of truth for all path math
  artifacts.py      shared: content-addressed path helpers

  db/               database layer
  sources/          crawlers — one adapter per legal source
  parser/           shared parsers used by multiple adapters
  pipeline/         processing pipeline: download → extract → analyze
  llm/              LLM client and prompt utilities  (planned)
```

## Categories

### `db/`
SQLite connection, schema, and repository (CRUD helpers).
All DB access goes through here — no raw `sqlite3` calls scattered elsewhere.

| File | Role |
|------|------|
| `connection.py` | Open / close DB; apply migrations |
| `schema.py` | Table definitions and `init_schema()` |
| `repository.py` | `insert_crawl_history`, `get_source_library`, etc. |

### `sources/`
One adapter per legal source, organised by region → adapter ID.
Adapters fetch and parse a specific site. No pipeline logic here.

```
sources/
  discovery.py              seed_urls.txt → source_library (DB seeding)
  my/parliament_my/         parlimen.gov.my bill index + PDF crawl
  sg/...                    (future)
```

Each adapter contains: `fetch.py`, `parse.py`, `crawl.py`, `config.py`, `seed_urls.txt`.

### `parser/`
Shared parsing utilities used by multiple adapters (e.g. `seed_txt.py` — reads `seed_urls.txt`).
Not site-specific.

### `pipeline/`
Processing stages that run after a source has been crawled.
Each stage is a self-contained module, callable as `python -m lib.pipeline.<stage>`.

| File | Stage | Status |
|------|-------|--------|
| `download.py` | Fetch PDFs from bill URLs → `data/raw/` | planned |
| `extract.py` | PDF → Markdown (`pymupdf4llm`) → `data/derived/.../extracted/` | ✅ |
| `analyze.py` | Markdown + metadata → LLM → `analysis.json` | planned |

### `llm/` *(planned)*
Provider-agnostic LLM client, prompt builders, response parsers.
No direct LLM API calls anywhere outside this category.

| File | Role |
|------|------|
| `client.py` | HTTP wrapper; reads `OPENROUTER_API_KEY` from `.env` |
| `prompts.py` | Prompt templates for each pipeline stage |

## Import rules

Cross-category imports flow in one direction only:

```
pipeline  →  db, llm, paths, artifacts
sources   →  db, parser, paths
llm       →  paths
```

Never import `pipeline` from `sources`. Never import `sources` from `pipeline`.

## Size limit

Each category folder should stay under 10 `.py` files. If it grows past that, split by responsibility before adding more.
