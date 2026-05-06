# Payment Flow
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial payment flow from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate this AFTER 02-stack.md confirms {{PAYMENT_PROVIDER}}.
  Every webhook endpoint must exist in 02-api-routes.md.
  Every plan must match the pricing in 01-prd.md.
  SYNC CHECK: If this file changes, also update 02-api-routes.md, 02-schema.md, 02-auth-flow.md.
-->

## Provider

- **Payment provider:** {{PAYMENT_PROVIDER}}
- **Subscription type:** {{SUBSCRIPTION_TYPE}}
- **Monetization model:** {{MONETIZATION_MODEL}}

## Subscription Plans

<!--
  AI INSTRUCTION: Must match 01-prd.md monetization section exactly.
-->

| Plan Name | Price | Billing | Features | Stripe Price ID |
|---|---|---|---|---|
| {{SUBSCRIPTION_PLANS}} | | | | (set after Stripe setup) |
| | | | | |
| | | | | |

## Payment Flows

### New Subscription

```
1. User signs up (see 02-auth-flow.md)
2. User visits /pricing
3. User selects plan
4. Redirect to {{PAYMENT_PROVIDER}} Checkout
5. User completes payment
6. {{PAYMENT_PROVIDER}} sends checkout.session.completed webhook
7. Webhook handler:
   a. Verify webhook signature
   b. Find user by customer email or metadata
   c. Create/update subscription record in DB
   d. Update user's plan field
8. User redirected to /dashboard with active subscription
```

### Plan Upgrade / Downgrade

```
1. User visits /dashboard/billing (or /dashboard/settings)
2. User clicks "Change Plan"
3. Redirect to {{PAYMENT_PROVIDER}} Customer Portal
   OR handle inline with API call
4. {{PAYMENT_PROVIDER}} sends customer.subscription.updated webhook
5. Webhook handler updates subscription in DB
```

### Cancellation

```
1. User visits /dashboard/billing
2. User clicks "Cancel"
3. {{PAYMENT_PROVIDER}} sets subscription to cancel at period end
4. Webhook: customer.subscription.updated (cancel_at_period_end = true)
5. At period end: customer.subscription.deleted webhook
6. Webhook handler:
   a. Downgrade user to free tier (if exists) or disable access
   b. Update subscription status in DB
```

### Failed Payment

```
1. {{PAYMENT_PROVIDER}} retry logic runs (3 attempts over ~3 weeks)
2. invoice.payment_failed webhook on each failure
3. Webhook handler:
   a. Flag subscription as "past_due" in DB
   b. Send email notification to user via {{EMAIL_PROVIDER}}
   c. Optionally: show banner in dashboard
4. If all retries fail: customer.subscription.deleted webhook
5. Downgrade or disable access
```

## Webhooks

<!--
  AI INSTRUCTION: Every webhook must have a corresponding route in 02-api-routes.md.
-->

| Webhook Event | Route | Action |
|---|---|---|
| `checkout.session.completed` | `/api/webhooks/stripe` | Create subscription |
| `customer.subscription.updated` | `/api/webhooks/stripe` | Update plan/status |
| `customer.subscription.deleted` | `/api/webhooks/stripe` | Revoke access |
| `invoice.payment_failed` | `/api/webhooks/stripe` | Flag past_due, notify user |
| `invoice.paid` | `/api/webhooks/stripe` | Clear past_due flag |

## Database: Payment-Related Tables

<!--
  AI INSTRUCTION: Must match 02-schema.md exactly.
-->

```
Subscription
  - id
  - userId            (FK → User)
  - stripeCustomerId
  - stripeSubscriptionId
  - stripePriceId
  - plan              (free, pro, team, etc.)
  - status            (active, past_due, canceled, trialing)
  - currentPeriodEnd
  - cancelAtPeriodEnd
  - createdAt
  - updatedAt
```

## Gating Logic

<!--
  AI INSTRUCTION: How does the app check if a user can access a feature?
-->

```typescript
// Pseudocode for feature gating
function canAccess(user, feature) {
  const plan = user.subscription.plan
  const features = PLAN_FEATURES[plan]
  return features.includes(feature)
}
```

| Feature | Free | Pro | Team |
|---|---|---|---|
| {{CORE_ACTION}} | limited | unlimited | unlimited |
| | | | |
| | | | |

## Environment Variables

```env
# {{PAYMENT_PROVIDER}} configuration
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
STRIPE_WEBHOOK_SECRET=
# Price IDs (from Stripe dashboard)
STRIPE_PRICE_FREE=
STRIPE_PRICE_PRO=
STRIPE_PRICE_TEAM=
```

## Testing Checklist

- [ ] Checkout flow works with test card (4242...)
- [ ] Webhook signature verification works
- [ ] Subscription created in DB after successful checkout
- [ ] Plan upgrade/downgrade reflected in DB
- [ ] Cancellation sets cancel_at_period_end correctly
- [ ] Failed payment flags subscription as past_due
- [ ] Access correctly gated based on plan
- [ ] Customer portal accessible from dashboard
