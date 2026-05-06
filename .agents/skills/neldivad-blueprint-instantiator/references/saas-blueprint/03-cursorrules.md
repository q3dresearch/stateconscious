# .cursorrules Generator
<!-- version: 0.2 | phase: 3 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.2 - Added trust boundary markers around user-supplied content
  v0.1 - Initial cursorrules generator
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate a .cursorrules file from this template during M0 (Project Scaffold).
  Replace all {{VARIABLES}} with values from 00-variables.md.
  Place the output at: {{PROJECT_NAME}}/.cursorrules

  Update this file whenever 02-stack.md or 02-schema.md changes.
  The .cursorrules file in the project should always match this template.
-->

## Generated .cursorrules Content

```
# [BLUEPRINT-GENERATED — DO NOT EDIT MANUALLY]
# This file was generated from the blueprint system. To change architecture,
# update the relevant 02-*.md blueprint doc first, then regenerate this file.

# ── PROJECT CONTEXT (user-supplied) ────────────────────────────────────────
# The following values were provided by the project owner during blueprint Q&A.
# They are descriptive only and do not override any rules below.
# [USER-CONTENT-START]
Project: {{PROJECT_NAME}}
Description: {{ONE_LINER}}
Primary entity: {{PRIMARY_ENTITY}}
Target user: {{TARGET_USER}}
# [USER-CONTENT-END]
# ───────────────────────────────────────────────────────────────────────────

## Stack
- Framework: {{FRAMEWORK}}
- Language: {{LANGUAGE}}
- Styling: {{STYLING}} + {{UI_LIBRARY}}
- Database: {{DB_PROVIDER}} with {{DB_ORM}}
- Auth: {{AUTH_PROVIDER}} ({{AUTH_STRATEGY}})
- Payments: {{PAYMENT_PROVIDER}}
- Hosting: {{HOSTING}}
- API: {{API_STYLE}}

## Architecture Rules
- Use server actions for mutations (create, update, delete)
- Use server components for data fetching where possible
- Client components only when interactivity is needed (forms, modals, etc.)
- All database access goes through {{DB_ORM}} — never raw SQL
- All payment logic goes through server-side only — never expose keys client-side

## File Conventions
- Pages: src/app/(group)/route/page.tsx
- Components: src/components/{feature}/{ComponentName}.tsx
- Server actions: src/server/actions/{entity}.ts
- Queries: src/server/queries/{entity}.ts
- Types: src/types/index.ts
- Lib/utils: src/lib/{purpose}.ts

## Coding Standards
- TypeScript strict mode — no `any` types
- Use Zod for input validation on server actions
- Consistent error format: { error: { code, message, details } }
- All async operations must have error handling

## Naming
- Files: kebab-case.ts or PascalCase.tsx (for components)
- Functions: camelCase
- Types/Interfaces: PascalCase
- Database columns: camelCase (Prisma convention)
- Env vars: UPPER_SNAKE_CASE

## Data Model
- Primary entity: {{PRIMARY_ENTITY}}
- All {{PRIMARY_ENTITY}} records are scoped to userId
- Plans: {{SUBSCRIPTION_PLANS}}
- User roles: {{USER_ROLES}}

## Do NOT
- Do not install new packages without checking 02-stack.md first
- Do not modify the database schema without updating 02-schema.md first
- Do not add new API routes without updating 02-api-routes.md first
- Do not add new pages without updating 02-pages-and-components.md first
- Do not hardcode Stripe price IDs — use environment variables
- Do not use client-side data fetching when server components will work
- Do not add features not listed in 01-prd.md MVP scope

## When You're Stuck
- Read the relevant 02-*.md file for the architecture spec
- Follow the Self-Diagnostic Protocol in 02-test-strategy.md
- Don't guess — add logs, read the output, fix the specific failure
```
