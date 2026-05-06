# Pipeline agent — Act 2 brief

**Who may edit what:** [`docs/PROJECT_USE.md`](../docs/PROJECT_USE.md).  
**Repo layout + artifact paths:** [`docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md).  
**Shell commands:** [`docs/OPERATIONS.md`](../docs/OPERATIONS.md).

You run the pipeline that turns a discovered bill URL into a structured impact analysis. Discovery and index crawling belong to the crawler agent; you take over once `pdf_url` exists in the CSV.

---

## Pipeline stages

| Stage | Skill | Implementation |
|-------|-------|----------------|
| Download PDFs | `sc-download` | `src/lib/pipeline/download.py` |
| Extract text | `sc-extract` | `src/lib/pipeline/extract.py` |
| Analyze (LLM) | `sc-analyze` | `src/lib/pipeline/analyze.py` |

Run stages in order. Each stage is idempotent — skip if artifact already exists.

---

## Operating principles

- **Hash = idempotency key.** SHA-256 of raw bytes determines the artifact path for every stage.
- **Log everything.** Every stage outcome (success / skip / error) goes into `crawl_history` or a stage log — never silently drop failures.
- **Budget before LLM.** Use `--max N` to cap downloads and LLM calls per run; cron should never run open-ended.
- **No parallel LLM calls** in MVP. One bill at a time.
- **Suspect PDFs.** If text extraction yields < 100 chars, mark as suspect and skip LLM; flag for human review.

---

## Read order for new session

1. `docs/ARCHITECTURE.md` — pipeline module layout and artifact paths
2. `docs/OPERATIONS.md` — CLI commands
3. `.agents/skills/sc-download/SKILL.md`, `sc-extract/SKILL.md`, `sc-analyze/SKILL.md` — stage outlines
4. `src/lib/pipeline/` — existing implementation (if any)
5. `mds/agents/crawlerAgent.md` — upstream; do not duplicate crawl logic
