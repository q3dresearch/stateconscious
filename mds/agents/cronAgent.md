# Cron agent — short brief

**Read first:** [`docs/PROJECT_USE.md`](../docs/PROJECT_USE.md) — human vs agent roles, `adhoc/todo`, `adhoc/agentHumanChat`, ideal state, failure handling.

**On wake:** run scheduled work; scan **`adhoc/todo/`** and treat each file as a prompt; use deterministic code in **`src/lib/`**; keep **`pytest`** passing.

**Seeds / DB:** after changing an adapter **`seed_urls.txt`** or **`config.py`** (notes / metadata), run `python scripts/init_db.py`. Cron should read **`source_library`** in **`stateconscious.db`**. See `sitesCrawl.md`.

**Helpers:** `cron.lib.adhoc` (e.g. list todo files)—archiving **`adhoc/todo` → `adhoc/done`** is a **human** step after review unless you have an explicit team policy otherwise.
