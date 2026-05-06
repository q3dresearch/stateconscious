# Test Strategy
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial test strategy from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  This defines HOW you test, not WHAT you test.
  The Self-Testing Protocol in 00-game-rules.md requires:
  "Before marking any milestone complete, run your own test suite."
  This document tells you how to build and run that suite.
-->

## Testing Stack

| Tool | Purpose |
|---|---|
| Vitest (or Jest) | Unit tests |
| Playwright (or Cypress) | E2E tests |
| Testing Library | Component tests |
| Stripe CLI | Webhook testing |
| {{DB_ORM}} | Test database seeding |

## Test Levels

### Level 1: Smoke Tests (run on every change)

Quick sanity checks that the app isn't fundamentally broken.

```
- [ ] App builds without errors
- [ ] Home page renders
- [ ] Sign-in page renders
- [ ] Dashboard page renders (with test user)
- [ ] {{PRIMARY_ENTITY}} list page renders
- [ ] No console errors in browser
```

**Run command:** `npm run test:smoke`
**When:** Before every commit. If this fails, nothing else matters.

### Level 2: Unit Tests (run on every change)

Test individual functions and server actions in isolation.

```
Priority order:
1. Server actions for {{PRIMARY_ENTITY}} CRUD
2. Subscription gating logic
3. Webhook signature verification
4. Input validation functions
5. Utility functions
```

**Run command:** `npm run test:unit`
**Coverage target:** 80% of server/ directory

### Level 3: Integration Tests (run before milestones)

Test that components work together.

```
Priority order:
1. Auth flow: sign up → session created → dashboard accessible
2. Payment flow: checkout → webhook → subscription active
3. CRUD flow: create {{PRIMARY_ENTITY}} → appears in list → edit → delete
4. Gating: free user blocked from pro features
```

**Run command:** `npm run test:integration`

### Level 4: E2E Tests (run before review gates)

Full user journey tests in a real browser.

```
Priority order:
1. New user: land on home → sign up → see dashboard
2. Existing user: sign in → create {{PRIMARY_ENTITY}} → verify in list
3. Billing: upgrade plan → verify access changes
```

**Run command:** `npm run test:e2e`

## Test Database

- Use a separate test database (not your dev database)
- Seed with known data before each test suite
- Reset between test runs
- Connection string: `DATABASE_URL_TEST` in `.env.local`

## What NOT to Test

- {{AUTH_PROVIDER}} internals (trust the SDK)
- {{PAYMENT_PROVIDER}} internals (trust the SDK)
- UI component library internals (trust shadcn/radix)
- Third-party API behavior (mock it)

## When Tests Fail

```
1. Read the error message (don't guess)
2. Check if it's a real bug or a flaky test
3. If real bug:
   a. Write a failing test that reproduces it (regression test)
   b. Fix the bug
   c. Verify test passes
   d. Log the bug and fix in changelog.md
4. If flaky test:
   a. Fix the test, not the code
   b. Add a comment explaining what was flaky and why
```

## Self-Diagnostic Protocol

<!--
  AI INSTRUCTION: When you encounter a bug during development,
  use this protocol instead of guessing. Reference strategy #5
  from game-rules: "Log-Driven Forensic Debugging."
-->

```
1. STOP guessing
2. Add console.log / debug output at the point of failure
3. Run the failing scenario
4. Read the logs
5. Identify the EXACT point where actual ≠ expected
6. Fix that specific point
7. Remove debug output
8. Add a regression test
```
