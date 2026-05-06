# Site crawling — instructions & strategy

**Roles (human vs agent):** [`docs/PROJECT_USE.md`](../docs/PROJECT_USE.md).

## Registry (adapter files → SQLite → cron)

1. **`src/lib/sources/<region>/<adapter>/seed_urls.txt`** — **URL list** for that adapter: one URL per line; `#` comments; optional **`URL<TAB>short_label`** for `source_library.label`.
2. **`config.py`** in the same folder — at minimum **`SOURCE_ID`**, **`CRAWL_NOTES`** (appended into DB `notes`), **`RESOURCE_KIND`** (default `index`). **`lib/sources/discovery.py`** walks adapters that have **`seed_urls.txt`** and seeds **`source_library`**.
3. **`stateconscious.db`** — default SQLite at repo root. Table **`source_library`** is what cron should query after **`python scripts/init_db.py`**.

**Optional:** **`src/config/`** for secrets/templates only (no central URL list required).

## Read order

1. Adapter **`seed_urls.txt`** + **`README.md`**
2. **`mds/agents/crawlerAgent.md`** — fetch policy
3. **`lib.sources.<region>.<adapter>`** — code

## Field mapping

| Concept | Config | SQLite `source_library` |
|--------|--------|-------------------------|
| URL | `seed_urls.txt` line | `url` (unique) |
| Label | tab part or URL | `label` |
| Adapter | `config.SOURCE_ID` | `adapter_id` |
| Kind | `config.RESOURCE_KIND` | `resource_kind` |
| Notes | `Seeded from …` + `CRAWL_NOTES` | `notes` |

## Adhoc vs random pages

Humans queue intent in **`adhoc/todo/`**; only URLs **added to an adapter `seed_urls.txt`** (and **`init_db`**) are operational seeds—not every page opened while debugging (`PROJECT_USE.md`).

## Precision vs recall (what belongs in `seed_urls.txt`)

| Strategy | Precision | Recall / drift | Typical use |
|----------|-----------|----------------|-------------|
| **Broad index / “default” home** | Low | High | Discovery seeds; harder automation |
| **Mid URLs** (`?uweb=dr`, `arkib=yes`, …) | Medium | Medium | **Best default** for parliament listings |
| **Literal `.pdf` URL** | High | Low | **Pin** must-haves; monitor failures |

Use **tiered seeds + bounded descent** in adapter code (`--follow-html`, `--discover-pdfs` on the parliament crawl module).

## Adding URLs

1. Edit the adapter’s **`seed_urls.txt`**.
2. If **`CRAWL_NOTES`** changes, edit **`config.py`**.
3. Run **`python scripts/init_db.py`**.

## Parliament crawl CLI

```bash
PYTHONPATH=src python -m lib.sources.my.parliament_my.crawl --help
```

Do **not** assume PDF-only; see `crawlerAgent.md`.
