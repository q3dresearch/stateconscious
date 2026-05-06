# Database Schema
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial schema from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate this AFTER 01-prd.md and 02-auth-flow.md and 02-payment-flow.md are finalized.
  Auth tables must match 02-auth-flow.md exactly.
  Subscription table must match 02-payment-flow.md exactly.
  SYNC CHECK: If this file changes, also update 02-auth-flow.md, 02-payment-flow.md, 02-file-tree.md.
-->

## Provider

- **Database:** {{DB_PROVIDER}}
- **ORM:** {{DB_ORM}}
- **Multi-tenant:** {{MULTI_TENANT}}

## Entity Relationship Diagram

```
User ──── 1:1 ──── Subscription
  │
  └──── 1:N ──── {{PRIMARY_ENTITY}}
                      │
                      └──── ... ({{SECONDARY_ENTITIES}})
```

## Tables

### User

| Column | Type | Constraints | Notes |
|---|---|---|---|
| id | String | PK, default cuid() | |
| email | String | unique, not null | |
| name | String | nullable | |
| role | Enum | default "member" | {{USER_ROLES}} |
| avatarUrl | String | nullable | |
| createdAt | DateTime | default now() | |
| updatedAt | DateTime | auto-update | |

**Relations:**
- Has one `Subscription`
- Has many `{{PRIMARY_ENTITY}}`

### Subscription

| Column | Type | Constraints | Notes |
|---|---|---|---|
| id | String | PK, default cuid() | |
| userId | String | FK → User, unique | |
| stripeCustomerId | String | unique, nullable | |
| stripeSubscriptionId | String | unique, nullable | |
| stripePriceId | String | nullable | |
| plan | Enum | default "free" | free, pro, team |
| status | Enum | default "active" | active, past_due, canceled, trialing |
| currentPeriodEnd | DateTime | nullable | |
| cancelAtPeriodEnd | Boolean | default false | |
| createdAt | DateTime | default now() | |
| updatedAt | DateTime | auto-update | |

**Relations:**
- Belongs to `User`

### {{PRIMARY_ENTITY}}

<!--
  AI INSTRUCTION: Define columns based on 01-prd.md user stories.
  Only include fields needed for MVP (P0 features).
-->

| Column | Type | Constraints | Notes |
|---|---|---|---|
| id | String | PK, default cuid() | |
| userId | String | FK → User, not null | Owner |
| title | String | not null | |
| | | | |
| | | | |
| createdAt | DateTime | default now() | |
| updatedAt | DateTime | auto-update | |

**Relations:**
- Belongs to `User`

## Indexes

<!--
  AI INSTRUCTION: Add indexes for any column used in WHERE, ORDER BY, or JOIN.
-->

| Table | Index | Columns | Type |
|---|---|---|---|
| User | email_idx | email | unique |
| Subscription | userId_idx | userId | unique |
| Subscription | stripeCustomerId_idx | stripeCustomerId | unique |
| {{PRIMARY_ENTITY}} | userId_idx | userId | non-unique |
| {{PRIMARY_ENTITY}} | userId_createdAt_idx | userId, createdAt | composite |

## Prisma Schema (preview)

<!--
  AI INSTRUCTION: Generate the actual Prisma schema from the tables above.
  This is the source of truth that goes into prisma/schema.prisma.
-->

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// Paste generated schema here after Phase 2 approval
```

## Seed Data

<!--
  AI INSTRUCTION: Define minimal seed data for development.
-->

```
Test User:
  - email: test@example.com
  - role: admin
  - plan: pro

Sample {{PRIMARY_ENTITY}}:
  - 3-5 sample records for development
```

## Migration Strategy

- Use {{DB_ORM}} migrations for all schema changes
- Never edit migrations after they've been applied
- Name migrations descriptively: `add_{{PRIMARY_ENTITY}}_table`
- Test migrations on a fresh database before deploying
