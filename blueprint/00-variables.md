# Variables Registry
<!-- version: 0.2 | phase: 1 | last-updated: 2026-04-03 -->
<!-- changelog:
  v0.2 - Phase 1: populated from Q&A + mds/notes/chat.md, chat1.md
  v0.1 - Initial template
-->

<!--
  INSTRUCTIONS FOR AI:
  This is the master variable registry. ALL templates reference these variables.
  During Phase 1 (Q&A), populate the "Value" column.
  During Phase 2 (Architecture), populate stack and architecture variables.
  When ANY variable changes, grep all 01-*.md and 02-*.md files and update every occurrence.
  Never leave a {{VARIABLE}} unresolved in a non-template file.
-->

## Project Identity

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{PROJECT_NAME}}` | stateconscious | 1 | Repo / project folder name |
| `{{ONE_LINER}}` | Tracks how laws change over time in one domain, compares each crawl to the previous version, and outputs structured “what changed” plus impact-oriented explanation. | 1 | Aligned with docs in `mds/notes/` |
| `{{TARGET_USER}}` | Initially the builder (solo operator); then knowledge workers—policy/legal analysts and technical builders who need durable, replayable legal change history. | 1 | No premature multi-user UX |
| `{{CORE_ACTION}}` | Ingest one scheduled legal source → snapshot → segment/semantics → diff vs prior snapshot → emit change + impact narrative (files/CLI, not a product web app). | 1 | MVP = pipeline correctness |
| `{{CORE_USER_ACTION}}` | Run the pipeline (cron or manual) and read outputs (markdown/JSON/Streamlit or plain HTML). | 1 | |
| `{{PRIMARY_ENTITY}}` | `SourceSnapshot` — immutable captured document state at fetch time `T`, hash-addressable, comparable to `T−1`. | 1 | Git-like snapshot, not “one row per PDF” |
| `{{MONETIZATION_MODEL}}` | None for MVP. Success = reliably detects and explains meaningful changes in a single domain over time. | 1 | Revenue/users not success criteria |

## User & Access

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{USER_ROLES}}` | Single operator only (no accounts). | 1 | Auth deferred |
| `{{MULTI_TENANT}}` | no | 1 | One workspace / repo / machine |
| `{{AUTH_PROVIDER}}` | n/a | 2 | MVP has no auth |
| `{{AUTH_STRATEGY}}` | n/a | 2 | |

## Stack Decisions

| Variable | Value | Justification | Set In Phase |
|---|---|---|---|
| `{{FRAMEWORK}}` | TBD — Python-first pipeline | 2 | User: no Next.js product frontend for MVP |
| `{{LANGUAGE}}` | Python (expected) | 2 | Streamlit optional; aligns with scripting/cron |
| `{{STYLING}}` | n/a or minimal | 2 | No marketing UI in MVP |
| `{{UI_LIBRARY}}` | Optional Streamlit / static HTML | 2 | |
| `{{PAYMENT_PROVIDER}}` | none | 2 | |
| `{{DB_PROVIDER}}` | TBD | 2 | Local store + append-only event/snapshot pattern |
| `{{DB_ORM}}` | TBD | 2 | |
| `{{HOSTING}}` | Local + cron | 2 | Periodic pull, not always-on agent |
| `{{EMAIL_PROVIDER}}` | none | 2 | |
| `{{FILE_STORAGE}}` | Local repo / object paths | 2 | Manual drop or minimal upload |
| `{{ANALYTICS}}` | none | 2 | |

## Architecture Decisions

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{SUBSCRIPTION_TYPE}}` | n/a | 1 | No billing in MVP |
| `{{SUBSCRIPTION_PLANS}}` | n/a | 2 | |
| `{{API_STYLE}}` | TBD | 2 | Likely CLI + files first |
| `{{DB_RELATIONS}}` | Snapshot → segments → semantic units → (optional) structured events; lineage between snapshot versions. | 2 | See `mds/notes/chat.md` pipeline |
| `{{SECONDARY_ENTITIES}}` | `document_segment`, `semantic_unit`, `change_event` (feed row), `interpretation_view` (numeric/policy/scope); post-MVP: geography/industry/market/stakeholder tags, votes, sponsors, dependency edges. | 2 | Vision: Git/dependency-graph queries; MVP one source |
| `{{KEY_INTEGRATIONS}}` | One primary legal publication source (URL/API TBD); LLM(s) for segmentation/semantic extraction and impact copy; optional embedding/R for retrieval. | 1 | |

## MVP Scoping Flags

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{REALTIME_NEEDED}}` | no | 1 | Batch daily (or on-demand) sufficient |
| `{{BACKGROUND_JOBS_NEEDED}}` | minimal | 1 | Simple cron / scheduler, not a heavy queue |
| `{{CACHING_NEEDED}}` | no | 1 | Default no unless profiling shows need |
| `{{ADMIN_PANEL_NEEDED}}` | minimal | 1 | Optional local pattern viz only—not a full admin product |
| `{{FILE_UPLOAD_NEEDED}}` | minimal | 1 | Streamlit upload optional; or manual copy into repo |
| `{{SEARCH_NEEDED}}` | no | 1 | Not MVP |
| `{{NOTIFICATIONS_NEEDED}}` | no | 1 | Not MVP |

## Domain-Specific

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{REFERENCE_PATTERNS}}` | Event sourcing; snapshot→diff→history (Git metaphor); point-in-time / as-known vs as-effective; quant filing pipeline analogy. | 1 | Documented in `mds/notes/chat.md` |
| `{{PIPELINE_LAYERS}}` | raw_document → document_segments → semantic_units → weak/strong interpretation → state/diff → insight. | 1 | `chat1.md` Turn 3–4 |
| `{{MVP_SOURCE_COUNT}}` | 1 | 1 | Single crawl source for MVP |
| `{{MULTI_COUNTRY_MVP}}` | no | 1 | Patterns must scale; data does not |
| `{{PERFECT_PARSING_MVP}}` | no | 1 | Iterative extraction; confidence flags |
