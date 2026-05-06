# Milestones
<!-- version: 0.2 | phase: 3 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.2 - Expanded New Game+ with backlog triage, scope queue intake, campaign complete section
  v0.1 - Initial milestone plan from Phase 3
-->

<!--
  INSTRUCTIONS FOR AI:
  This is the game route. You propose milestones, human approves.
  Each milestone must:
  1. Have clear dependencies (what must be done first)
  2. Have a "done" definition (how do we know it's complete)
  3. Have a test checkpoint (what tests prove it works)
  4. Estimate which 02-*.md files it implements

  After completing a milestone, update its status and log learnings.
  At each Review Gate, present this document with progress.
-->

## Milestone Route Map

```
M0: Project Setup ─────► M1: Auth ─────► M2: Core CRUD ─────► M3: Payments ─────► M4: Polish ─────► LAUNCH
     (tutorial)           (unlock)         (main quest)          (boss fight)        (side quests)       │
                                                                                                          │
                                                                                              ┌───────────┘
                                                                                              ▼
                                                                                     NEW GAME+
                                                                                     M5, M6, M7...
                                                                                     (backlog queue)
```

## M0: Project Scaffold (Tutorial Zone)

**Dependencies:** All Phase 2 documents approved
**Implements:** 02-file-tree.md, 02-stack.md

| Task | Status | Notes |
|---|---|---|
| Initialize {{FRAMEWORK}} project | | |
| Install all packages from 02-stack.md | | |
| Set up {{DB_ORM}} with {{DB_PROVIDER}} | | |
| Create initial schema from 02-schema.md | | |
| Run first migration | | |
| Set up test framework from 02-test-strategy.md | | |
| Generate .cursorrules from 03-cursorrules.md | | |
| Generate CLAUDE.md from 03-claude-md.md | | |
| Create .env.example with all required variables | | |
| Verify: `npm run dev` works, `npm run test` works | | |

**Done when:** App runs locally, tests pass, DB connected, all env vars documented.

**Review Gate:** Present scaffold to human. Verify file tree matches 02-file-tree.md.

---

## M1: Authentication (Unlock Basic Access)

**Dependencies:** M0 complete
**Implements:** 02-auth-flow.md

| Task | Status | Notes |
|---|---|---|
| Set up {{AUTH_PROVIDER}} | | |
| Create sign-up page | | |
| Create sign-in page | | |
| Add auth middleware | | |
| Create local User table + sync with {{AUTH_PROVIDER}} | | |
| Protect /dashboard routes | | |
| Test: sign up → dashboard accessible | | |
| Test: unauthenticated → redirected to /sign-in | | |

**Done when:** User can sign up, sign in, sign out. Dashboard is protected.

**Review Gate:** Demo auth flow. Check 02-auth-flow.md for completeness.

---

## M2: Core CRUD (Main Quest)

**Dependencies:** M1 complete
**Implements:** 02-api-routes.md, 02-schema.md, 02-pages-and-components.md

| Task | Status | Notes |
|---|---|---|
| Create {{PRIMARY_ENTITY}} model in DB | | |
| Build server actions: create, read, update, delete | | |
| Build list page with data table | | |
| Build detail page | | |
| Build create/edit form | | |
| Add delete with confirmation | | |
| Test: full CRUD cycle works | | |
| Test: user can only see own {{PRIMARY_ENTITY}} | | |

**Done when:** User can create, view, edit, delete {{PRIMARY_ENTITY}}. Data is scoped to user.

**Review Gate:** Demo CRUD flow. This is the core product — get human feedback on UX.

---

## M3: Payments (Boss Fight)

**Dependencies:** M2 complete
**Implements:** 02-payment-flow.md

| Task | Status | Notes |
|---|---|---|
| Set up {{PAYMENT_PROVIDER}} account + products | | |
| Create checkout session endpoint | | |
| Build pricing page | | |
| Set up webhook endpoint | | |
| Handle checkout.session.completed | | |
| Handle subscription.updated / deleted | | |
| Build billing dashboard page | | |
| Add plan-based feature gating | | |
| Test: full purchase flow with test card | | |
| Test: webhook handles all events from 02-payment-flow.md | | |
| Test: downgrade restricts access correctly | | |

**Done when:** User can subscribe, upgrade, downgrade, cancel. Access is gated by plan.

**Review Gate:** Demo payment flow end-to-end. Review 02-risk-registry.md payment risks.

---

## M4: Polish & Launch Prep (Side Quests)

**Dependencies:** M3 complete

| Task | Status | Notes |
|---|---|---|
| Build landing page | | |
| Add error handling for all edge cases | | |
| Add loading states and empty states | | |
| Mobile responsiveness (if in MVP scope) | | |
| SEO basics (meta tags, OG images) | | |
| Set up production environment on {{HOSTING}} | | |
| Configure production env vars | | |
| Run full E2E test suite | | |
| Test Stripe webhooks in production mode | | |
| Set up error monitoring (optional) | | |

**Done when:** App deployed to production. All smoke tests pass on production URL.

**Review Gate:** Final review before "launch." Walk through 02-risk-registry.md one last time.

---

---

## Campaign Complete

<!--
  AI INSTRUCTION: When M4 Review Gate is approved and production smoke tests pass,
  run this section in order. This is the credits roll.
-->

**Win condition:** App is deployed, paying users can sign up, core CRUD works, payments process.

### Credits Roll Checklist

| Task | Status |
|---|---|
| Production URL resolves | |
| Sign up → onboard → dashboard flow works end-to-end | |
| Payment checkout completes with real card (or test mode confirmed) | |
| All smoke tests pass on production | |
| `00-state.md` marked: Phase → SHIPPED | |
| Final save written to `saves/gate-4-shipped.md` | |
| `changelog.md` entry: "v1.0 — shipped" | |

**When all checked:** Tell the human:

```
Campaign complete. The MVP is live.

Here's what shipped: [one paragraph summary from 01-prd.md core value prop]
Here's what was cut: [list from 01-mvp-reduction-checklist.md]
Here's what's queued: [Scope Queue + Backlog count]

When you're ready to continue, say "New Game+" and we'll triage the backlog.
```

Then stop. Do not start New Game+ work until the human explicitly says so.

---

## New Game+ (Post-Launch Backlog)

<!--
  AI INSTRUCTION:
  This section is populated from two sources:
  1. Features cut during Phase 1 (01-mvp-reduction-checklist.md)
  2. Scope Queue items that received "Backlog" verdict during the campaign

  New Game+ milestones follow the same rules as M0-M4:
  - Each needs a done condition
  - Each needs a blast radius check before starting
  - Each needs human approval at its own gate
  - Number them M5, M6, M7... in order of priority

  To start New Game+:
  1. Pull all Backlog items from Scope Queue in 00-state.md
  2. Pull all cut features from 01-mvp-reduction-checklist.md
  3. Present the full list to human for triage
  4. Human assigns priority order
  5. Generate M5, M6... milestones below using the same format as M0-M4
-->

### Backlog Intake

When entering New Game+, run this triage with the human:

**From the cut list** — pull every row from `01-mvp-reduction-checklist.md` marked "Cut":

| Feature | Why Cut | Still Needed? | Priority |
|---|---|---|---|
| (populate from mvp-reduction-checklist.md) | | | |

**From the Scope Queue** — pull every item from `00-state.md` Scope Queue with verdict "Backlog":

| Request | Date Logged | Priority |
|---|---|---|
| (populate from 00-state.md scope queue) | | |

**Triage rules:**
- Assign each item: `ship-next` / `ship-later` / `never`
- Items marked `never` get archived — remove from queue, note why in changelog
- Items marked `ship-next` become the next numbered milestone (M5, M6...)
- Items marked `ship-later` stay in backlog

### M5+: (Generated from Backlog)

<!--
  AI INSTRUCTION: Generate milestone blocks here, one per approved backlog item.
  Use the same format as M0-M4 above. Each block needs:
  - Dependencies
  - Implements (which 02-*.md files, or note if docs need updating first)
  - Task table
  - Done when
  - Review Gate

  Before writing code for any M5+ milestone, run Impact Assessment from
  00-game-rules.md. If it requires updating any 02-*.md, do that first.
-->

---

## Milestone Status Tracker

| Milestone | Status | Started | Completed | Learnings |
|---|---|---|---|---|
| M0: Scaffold | not started | | | |
| M1: Auth | not started | | | |
| M2: Core CRUD | not started | | | |
| M3: Payments | not started | | | |
| M4: Polish | not started | | | |
| — LAUNCH — | | | | |
| M5+: (backlog) | not started | | | |
