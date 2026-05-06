# MVP Reduction Checklist
<!-- version: 0.2 | phase: 1 | last-updated: 2026-04-03 -->
<!-- changelog:
  v0.2 - Completed for stateconscious from Q&A + notes
  v0.1 - Initial template
-->

<!--
  INSTRUCTIONS FOR AI:
  Run this checklist AFTER the Q&A is complete but BEFORE starting Phase 2.
  For every question, the default answer should be "no" unless the human
  provides a strong justification. Your job is to keep the MVP minimal.

  If the answer is "yes" — document WHY in the justification column.
  If the answer is "no" — the feature goes to "Explicitly Out of Scope" in 01-prd.md.
-->

## The Golden Rule

> Can the operator get value from stateconscious without this feature?  
> If yes → cut it from MVP.

## Complexity Audit

| Question | Answer | Justification (if yes) | Impact if cut |
|---|---|---|---|
| Can this be done **without real-time**? (use polling or refresh instead) | **yes** | MVP is batch/cron | — |
| Can this be done **without background jobs**? (use synchronous processing) | **partial** | Need **minimal** scheduling (cron); not a large worker pool | Runs are manual or single-machine cron |
| Can this be done **without caching**? (accept slower reads for now) | **yes** | | |
| Can this be done **without an admin panel**? (use DB GUI or scripts) | **mostly yes** | **Minimal** local viz optional to see patterns—not a hosted admin product | Use files + optional Streamlit |
| Can this be done **without file uploads**? (use links or text instead) | **mostly yes** | Optional Streamlit upload or **manual copy into repo** | Operator drops files in a folder |
| Can this be done **without full-text search**? (use simple filters) | **yes** | Explicitly out of MVP | |
| Can this be done **without email notifications**? (use in-app only) | **yes** | No notifications MVP | |
| Can this be done **without multiple user roles**? (one role for v1) | **yes** | Single operator | |
| Can this be done **without multi-tenancy**? (single namespace for v1) | **yes** | One workspace | |
| Can this be done **without OAuth/social login**? (email+password only) | **yes** | No auth MVP | |
| Can this be done **without a mobile-responsive design**? (desktop-first) | **yes** | No product UI requirement | |
| Can this be done **without third-party integrations**? (manual for now) | **partial** | **One** source + LLM is required; avoid extra vendors | |
| Can this be done **without usage analytics**? (add tracking later) | **yes** | | |
| Can this be done **without onboarding flows**? (simple landing → dashboard) | **yes** | No landing/dashboard product | |
| Can this be done **with only 1 subscription tier**? (add tiers later) | **yes** | No billing | |

## Feature Kill Count

- **Features entering checklist:** ~15 capability areas from vision (feed, multi-axis tags, drill-down, votes, dependency graph, search, realtime, etc.)  
- **Features surviving checklist:** **6** (one source, snapshots, change detection, layered extract, diff+insight, durable store)  
- **Features cut or deferred:** Multi-country product, alerts, search, auth, payments, Next.js app, full admin, voting/sponsor graph, package-manager legal graph (post-MVP)

> Target: Cut at least 40% of proposed features from MVP. **Met.**

## Survived Features → MVP Scope

1. One configured legal source, cron or manual ingest.  
2. Immutable snapshot + hash/version detection vs previous.  
3. Segmentation + semantic units (structure-later-friendly).  
4. Diff + “what changed” + impact-oriented narrative tied to stored artifacts.  
5. Optional minimal local visualization (Streamlit/static HTML only).  
6. No auth, payments, or product web frontend.

## Cut Features → Post-MVP Backlog

| Feature | Why Cut | Add Back In |
|---|---|---|
| Multi-country feeds | Scope; patterns must scale first | v1.1+ |
| Real-time / alerts | Not needed for correctness proof | v1.1+ |
| Full-text search product | Not MVP | v1.1+ |
| Auth, billing, Next.js app | Explicit non-goals | v2.0 / maybe-never for “thin” pipeline |
| Senator votes, sponsor history, pass/fail DB | Needs richer sources + graph | v1.2+ |
| Legal dependency graph (“law1.py imports”) | Research product on top of stable IDs | v2.0 |
