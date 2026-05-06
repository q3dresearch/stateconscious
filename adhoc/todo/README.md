# `adhoc/todo` inbox (human)

**Rules:** [`docs/PROJECT_USE.md`](../../docs/PROJECT_USE.md).

## Will anything move these files automatically?

**No.** There is no scheduled job in this repo that archives or deletes `adhoc/todo`. Moving items to `adhoc/done/` is a **human** step (or an explicit call to `cron.lib.adhoc.archive_completed` that you run on purpose).

## Adding a real prompt

Create a new file, e.g. `20260415-bills.md` (any name except `README.md` or `_draft.md`). Agents that scan the inbox should use `list_todo_markdown()`—it **ignores** `README.md` and `_*.md` so instructions are not treated as work.

After you agree on new poll URLs, add them to the right adapter’s **`src/lib/sources/.../seed_urls.txt`** (one per line), run **`python scripts/init_db.py`**, then archive this prompt.

## Template (copy into a new file)

```markdown
# …

## What I want

- …

## Done when

- …

When satisfied, move this file to `adhoc/done/` or delete it.
```
