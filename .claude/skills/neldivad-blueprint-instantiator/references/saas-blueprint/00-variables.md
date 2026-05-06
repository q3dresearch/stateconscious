# Variables Registry
<!-- version: 0.1 | phase: 0 | last-updated: YYYY-MM-DD -->

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
| `{{PROJECT_NAME}}` | | 1 | |
| `{{ONE_LINER}}` | | 1 | One sentence: what does this do? |
| `{{TARGET_USER}}` | | 1 | Who pays for this? |
| `{{CORE_ACTION}}` | | 1 | The one thing the user does |
| `{{PRIMARY_ENTITY}}` | | 1 | The main "thing" in the DB |
| `{{MONETIZATION_MODEL}}` | | 1 | How does this make money? |

## User & Access

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{USER_ROLES}}` | | 1 | e.g., admin, member, viewer |
| `{{MULTI_TENANT}}` | | 1 | yes/no — does each org get isolated data? |
| `{{AUTH_PROVIDER}}` | | 2 | better-auth, clerk, next-auth, supabase-auth |
| `{{AUTH_STRATEGY}}` | | 2 | email+password, magic-link, oauth, etc. |

## Stack Decisions

| Variable | Value | Justification | Set In Phase |
|---|---|---|---|
| `{{FRAMEWORK}}` | | | 2 |
| `{{LANGUAGE}}` | | | 2 |
| `{{STYLING}}` | | | 2 |
| `{{UI_LIBRARY}}` | | | 2 |
| `{{PAYMENT_PROVIDER}}` | | | 2 |
| `{{DB_PROVIDER}}` | | | 2 |
| `{{DB_ORM}}` | | | 2 |
| `{{HOSTING}}` | | | 2 |
| `{{EMAIL_PROVIDER}}` | | | 2 |
| `{{FILE_STORAGE}}` | | | 2 |
| `{{ANALYTICS}}` | | | 2 |

## Architecture Decisions

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{SUBSCRIPTION_TYPE}}` | | 1 | flat, tiered, usage-based, freemium |
| `{{SUBSCRIPTION_PLANS}}` | | 2 | e.g., free, pro ($19/mo), team ($49/mo) |
| `{{API_STYLE}}` | | 2 | REST, tRPC, GraphQL, server-actions-only |
| `{{DB_RELATIONS}}` | | 2 | Key relationships between entities |
| `{{SECONDARY_ENTITIES}}` | | 2 | Other important DB models |
| `{{KEY_INTEGRATIONS}}` | | 1 | External services the app talks to |

## MVP Scoping Flags

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{REALTIME_NEEDED}}` | | 1 | yes/no — websockets, SSE, polling? |
| `{{BACKGROUND_JOBS_NEEDED}}` | | 1 | yes/no — cron, queues, async processing? |
| `{{CACHING_NEEDED}}` | | 1 | yes/no — Redis, edge cache? |
| `{{ADMIN_PANEL_NEEDED}}` | | 1 | yes/no — internal dashboard? |
| `{{FILE_UPLOAD_NEEDED}}` | | 1 | yes/no — user-uploaded files? |
| `{{SEARCH_NEEDED}}` | | 1 | yes/no — full-text search? |
| `{{NOTIFICATIONS_NEEDED}}` | | 1 | yes/no — email, push, in-app? |

## Domain-Specific

<!--
  Add project-specific variables here as they emerge during Q&A.
  Format: | `{{VARIABLE_NAME}}` | value | phase | notes |
-->

| Variable | Value | Set In Phase | Notes |
|---|---|---|---|
| `{{CORE_USER_ACTION}}` | | 1 | Verb phrase: what the user DOES |
| | | | |
| | | | |
