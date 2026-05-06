# Risk Registry
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial risk assessment from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Fill this out AFTER all other 02-*.md files are complete.
  For EVERY risk, you must provide a mitigation strategy.
  Most agents never think about failure — this document forces it.
  Review this document at every Review Gate and update based on what was learned.
-->

## Risk Severity Scale

| Level | Impact | Response |
|---|---|---|
| Critical | App is broken or unusable | Must fix before milestone completion |
| High | Major feature degraded | Fix within current milestone |
| Medium | Minor issue, workaround exists | Schedule for next milestone |
| Low | Cosmetic or edge case | Backlog |

## Technical Risks

### Auth Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| {{AUTH_PROVIDER}} SDK breaking change | Medium | Low | Pin SDK version, monitor changelog |
| Session token not propagating to API routes | High | Medium | Test middleware early in milestone 1 |
| OAuth redirect loop on production domain | High | Medium | Test with production URL before launch |
| User exists in {{AUTH_PROVIDER}} but not in our DB | Critical | Medium | Webhook handler creates local user; add fallback check |
| Rate limiting by {{AUTH_PROVIDER}} on free tier | Medium | Low | Monitor usage, know upgrade thresholds |

### Payment Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Stripe webhook not reaching server | Critical | Medium | Test with Stripe CLI locally; verify endpoint in Stripe dashboard |
| Webhook events arriving out of order | High | Medium | Make webhook handler idempotent; check event timestamps |
| User has active subscription but DB says "canceled" | Critical | Low | Add reconciliation job; trust Stripe as source of truth |
| Checkout succeeds but user record not updated | Critical | Medium | Webhook retry + manual fallback check on dashboard load |
| Price ID mismatch between environments | High | Medium | Use env vars for price IDs; never hardcode |
| Currency/tax handling incorrect | Medium | Low | Use Stripe Tax or document as post-MVP |

### Database Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Migration fails on production | Critical | Low | Test on staging first; always have rollback migration |
| N+1 query on {{PRIMARY_ENTITY}} list page | Medium | High | Use `include` in Prisma queries; add index |
| Connection pool exhaustion | High | Low | Set pool size in DATABASE_URL; use connection pooler |
| Data loss from accidental deletion | Critical | Low | Enable point-in-time recovery on {{DB_PROVIDER}} |

### Deployment Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Environment variables missing in production | Critical | Medium | Use .env.example as checklist; verify before deploy |
| Build fails on {{HOSTING}} but works locally | High | High | Match Node version; test build locally before pushing |
| Cold start latency on serverless functions | Medium | Medium | Keep functions small; use edge where possible |
| CORS issues between frontend and API | High | Medium | Configure CORS in {{FRAMEWORK}} config early |

### Integration Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Third-party API rate limit hit | Medium | Medium | Add retry with exponential backoff |
| {{EMAIL_PROVIDER}} emails going to spam | Medium | High | Configure SPF/DKIM; test with mail-tester.com |
| API key leaked in client-side code | Critical | Low | Use server-side env vars only; add .env to .gitignore |
| Vendor price increase / deprecation | Low | Low | Abstract vendor calls behind interfaces where cheap to do |

## Business Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Nobody signs up | Critical | Unknown | Validate idea before building everything — launch landing page first |
| Users churn after trial | High | Medium | Focus on onboarding UX; track activation metrics |
| Support requests overwhelm founder | Medium | Medium | Build self-serve docs; add FAQ page |
| Competitor launches similar feature | Medium | Medium | Ship fast; focus on niche {{TARGET_USER}} serves |

## Risk Review Schedule

- **Every Review Gate:** Check all "High" and "Critical" risks
- **Every milestone completion:** Update likelihood based on actual experience
- **If a new risk is discovered:** Add it here immediately, don't wait for review gate
