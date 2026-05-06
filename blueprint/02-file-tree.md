# File Tree
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial file tree from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate this tree AFTER 02-stack.md is finalized.
  Every file listed here must map to a feature in 01-prd.md.
  Every API route in 02-api-routes.md must have a corresponding file here.
  Every page in 02-pages-and-components.md must have a corresponding file here.

  Annotate each file with a one-line purpose comment.
  Mark files with [MVP] if needed for launch, [POST-MVP] if not.
-->

## Project Root

```
{{PROJECT_NAME}}/
├── .env.example                        # [MVP] Environment variables template
├── .env.local                          # [GITIGNORED] Local environment variables
├── .cursorrules                        # [MVP] AI coding rules (generated in Phase 3)
├── CLAUDE.md                           # [MVP] AI context file (generated in Phase 3)
├── package.json                        # [MVP] Dependencies and scripts
├── tsconfig.json                       # [MVP] TypeScript configuration
├── next.config.ts                      # [MVP] {{FRAMEWORK}} configuration
├── tailwind.config.ts                  # [MVP] {{STYLING}} configuration
│
├── prisma/                             # [MVP] Database layer
│   ├── schema.prisma                   # [MVP] DB schema (mirrors 02-schema.md)
│   ├── migrations/                     # [MVP] Migration history
│   └── seed.ts                         # [MVP] Seed data for development
│
├── src/
│   ├── app/                            # [MVP] {{FRAMEWORK}} app router
│   │   ├── layout.tsx                  # [MVP] Root layout with providers
│   │   ├── page.tsx                    # [MVP] Landing page
│   │   ├── (auth)/                     # [MVP] Auth route group
│   │   │   ├── sign-in/page.tsx        # [MVP] Sign in page
│   │   │   └── sign-up/page.tsx        # [MVP] Sign up page
│   │   ├── (dashboard)/                # [MVP] Protected route group
│   │   │   ├── layout.tsx              # [MVP] Dashboard layout with sidebar
│   │   │   ├── page.tsx                # [MVP] Dashboard home
│   │   │   └── {{PRIMARY_ENTITY}}/     # [MVP] Primary entity pages
│   │   │       ├── page.tsx            # [MVP] List view
│   │   │       ├── [id]/page.tsx       # [MVP] Detail view
│   │   │       └── new/page.tsx        # [MVP] Create view
│   │   ├── (marketing)/                # [MVP] Public pages
│   │   │   ├── pricing/page.tsx        # [MVP] Pricing page
│   │   │   └── about/page.tsx          # [POST-MVP] About page
│   │   └── api/                        # [MVP] API routes
│   │       ├── webhooks/
│   │       │   └── stripe/route.ts     # [MVP] Stripe webhook handler
│   │       └── ...                     # See 02-api-routes.md
│   │
│   ├── components/                     # [MVP] Shared components
│   │   ├── ui/                         # [MVP] Base UI components (shadcn, etc.)
│   │   ├── layout/                     # [MVP] Layout components (nav, sidebar, footer)
│   │   └── {{PRIMARY_ENTITY}}/         # [MVP] Entity-specific components
│   │
│   ├── lib/                            # [MVP] Shared utilities
│   │   ├── db.ts                       # [MVP] Database client
│   │   ├── auth.ts                     # [MVP] Auth helpers
│   │   ├── stripe.ts                   # [MVP] Payment helpers
│   │   └── utils.ts                    # [MVP] General utilities
│   │
│   ├── server/                         # [MVP] Server-side logic
│   │   ├── actions/                    # [MVP] Server actions
│   │   │   ├── {{PRIMARY_ENTITY}}.ts   # [MVP] CRUD actions for primary entity
│   │   │   └── subscription.ts         # [MVP] Subscription management
│   │   └── queries/                    # [MVP] Data fetching
│   │       ├── {{PRIMARY_ENTITY}}.ts   # [MVP] Entity queries
│   │       └── user.ts                 # [MVP] User queries
│   │
│   └── types/                          # [MVP] TypeScript types
│       └── index.ts                    # [MVP] Shared type definitions
│
├── tests/                              # [MVP] Test suite
│   ├── setup.ts                        # [MVP] Test configuration
│   ├── unit/                           # [MVP] Unit tests
│   ├── integration/                    # [POST-MVP] Integration tests
│   └── e2e/                            # [POST-MVP] End-to-end tests
│
└── docs/                               # [POST-MVP] Project documentation
    └── ...
```

## File Count Summary

| Category | MVP Files | Post-MVP Files | Total |
|---|---|---|---|
| Pages | | | |
| Components | | | |
| Server logic | | | |
| Config | | | |
| Tests | | | |
| **Total** | | | |
