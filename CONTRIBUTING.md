# Contributing

- **Product / gates:** see `blueprint/` and PRD files; do not skip agreed review gates when using the blueprint harness.
- **Roles and adhoc workflow:** `docs/PROJECT_USE.md` (read this first).
- **Layout / commands:** `docs/ARCHITECTURE.md`, `docs/OPERATIONS.md`.
- **Python:** 3.12+. Set `PYTHONPATH=src` or run `pytest` from repo root (see `pytest.ini`).
- **Tests:** Add fixtures under `tests/fixtures/` for crawl/parse behavior; keep samples minimal and rights-safe.
- **Schema changes:** add a new `sql/migrations/00N_*.sql` and document in `ARCHITECTURE.md` if tooling must apply it in order.
