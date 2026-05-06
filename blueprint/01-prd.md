# Product Requirements Document
<!-- version: 0.2 | phase: 1 | last-updated: 2026-04-03 -->
<!-- changelog:
  v0.2 - Filled from Phase 1 Q&A + mds/notes (chat.md, chat1.md)
  v0.1 - Initial PRD template
-->

## Overview

**Project:** stateconscious  
**One-liner:** Tracks how laws change over time in one domain by ingesting a single publication source on a schedule, comparing each capture to the previous snapshot, and producing structured change plus impact-oriented explanation—without relying on a lossy chat context window.  
**Target user:** Initially the operator (you); later, knowledge workers—analysts and builders who need durable legal change history.

## Problem Statement

### The Problem

People usually see **current** or **final** legal text. They rarely have a **replayable, point-in-time** view of how a measure evolved, what changed relative to the last published version, and **who or what is affected** (stakeholder/industry/market framing)—especially when sources update quietly (PDF/HTML revisions).

### Current Solutions & Why They Fail

- **Ad hoc search and reading** — labor-intensive, no automatic diff, no stable lineage.  
- **Generic LLM chats** — forget context after limits; no append-only truth store; continuity hallucinations.  
- **Full legislative SaaS** — often overkill for MVP; optimizes for dashboards, alerts, and scale before core **change detection + explanation** is proven on one domain.

### Our Angle

Treat legal ingestion like **quant-style point-in-time data** plus **event-sourcing-style append-only history**: immutable snapshots, semantic layers (segments → units → optional structured events), then diff and impact narrative. Like “OpenClaw for law,” but **cron-driven**, **file/repo-grounded**, and **scoped to one source** until the pipeline is correct.

## Core Value Proposition

The operator (and later analysts/builders) can **run a repeatable pipeline** that answers: *what changed since last run, and why does it matter for affected parties?*—using **stateconscious** as the system of record for that domain’s published evolution.

## User Stories

| Priority | User Story | Acceptance Criteria |
|---|---|---|
| P0 | As the operator, I want to **schedule or manually run** ingestion from **one configured source**, so that each run stores an immutable snapshot. | New snapshot stored with fetch time, content hash, and link to prior snapshot when content changed. |
| P0 | As the operator, I want the system to **detect a new version** (e.g. hash/text change), so that I do not rely on memory or chat history. | Diff job only runs when prior snapshot exists and change is detected. |
| P0 | As the operator, I want **structured output** (segments → semantic units → change summary + impact), so that I can audit and extend the model. | Artifacts written to disk (e.g. JSON/MD) with provenance to snapshot IDs. |
| P1 | As an analyst, I want a **feed-like ordered list of changes** (region/industry/market/stakeholder tags when available), so that I can scan “what happened lately.” | Derived from change events; optional lightweight viz (e.g. Streamlit); still one primary source in MVP. |
| P1 | As an analyst, I want **drill-down history** (Git-like: what changed between revision A and B), so that I can trace evolution of a bill family. | Time-ordered snapshots + human-readable changelog between two snapshot IDs. |
| P2 | As an analyst, I want **voting patterns, sponsor history, pass/fail reasons**, and **dependency-style graphs** (“law1 affects industry X”). | Explicitly post-MVP; requires more sources and entity resolution. |

## MVP Scope

### In Scope (P0 only)

1. **One primary publication source** — configure URL/API or fetch path; cron or manual run.  
2. **Snapshot store** — immutable raw + metadata (`fetched_at`, hash, `source_url`, document type).  
3. **Change detection** — compare to previous snapshot; skip or emit pipeline on change only.  
4. **Layered extraction** — at minimum: segmentation + **semantic units** (loose attributes, tags, confidence); optional tightening to structured events where reliable.  
5. **Diff + insight output** — “what changed” + impact-oriented explanation grounded in stored text (not chat-only).  
6. **Durable context** — state lives in files/DB under repo control, not in conversation history.

### Explicitly Out of Scope (for now)

1. **Authentication, multi-user accounts, organizations.**  
2. **Payments and subscriptions.**  
3. **Product web app** (no Next.js marketing/dashboard product); optional Streamlit/static HTML only.  
4. **Real-time updates, alerts, notifications.**  
5. **Full-text search product** and **multi-country** datasets (architecture must allow scale; data stays single-domain/source for MVP).  
6. **Perfect parsing** — accept iterative extraction with confidence and human review path.  
7. **Senator voting graph, sponsor lineage, pass/fail encyclopedia, package-manager dependency graph** — vision; not MVP gates.

## Monetization

**Model:** None in MVP (validation via pipeline quality).  
**Subscription type:** n/a

| Plan | Price | Includes |
|---|---|---|
| n/a | — | — |

## User Roles & Permissions

| Role | Can Do | Cannot Do |
|---|---|---|
| Operator (single human) | Configure source, run pipeline, read all artifacts, edit repo | N/A — no other roles in MVP |

## Key Integrations

- **One legal publication source** (specific parliament/agency/gazette TBD).  
- **LLM(s)** for segmentation, semantic extraction, and impact narrative (provider TBD in Phase 2).  
- **Optional**: embeddings / retrieval for semantic query without rigid schemas first.

## Success Metrics

| Timeframe | Metric | Target |
|---|---|---|
| MVP | **Correct change detection** | Meaningful text/version changes from the single source are detected (no silent skip). |
| MVP | **Explainability** | For a sample set of real changes, outputs identify what changed and plausible affected parties at a **high-level** (bounded by source text). |
| MVP | **Repeatability** | Re-running on unchanged source yields no duplicate spurious “changes.” |
| Post-MVP | Users / revenue | TBD after core loop is trusted |

## Open Questions

1. **Which exact URL/API** is the first (and only) MVP source, and in what format (HTML, PDF, RSS)?  
2. **Primary jurisdiction + domain** (e.g. one bill type or one Act family) to bound extraction prompts?  
3. **LLM provider and budget** cap per run (for cost/latency in Phase 2)?  
4. **Storage choice**: SQLite vs plain files vs embedded doc store—for snapshots and semantic JSON lines?
