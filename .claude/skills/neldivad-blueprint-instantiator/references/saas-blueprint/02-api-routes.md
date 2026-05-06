# API Routes
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial API routes from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate this AFTER 01-prd.md user stories and 02-auth-flow.md are finalized.
  Every route here must have a corresponding file in 02-file-tree.md.
  Every webhook here must match 02-payment-flow.md.
  Auth requirements must match 02-auth-flow.md protected routes.
  SYNC CHECK: If this file changes, also update 02-file-tree.md, 02-auth-flow.md.
-->

## API Style: {{API_STYLE}}

## Route Map

### {{PRIMARY_ENTITY}} CRUD

<!--
  AI INSTRUCTION: If using server actions, these aren't traditional API routes.
  Document them as server actions with the same structure.
-->

| Method | Route / Action | Auth | Description | Request Body | Response |
|---|---|---|---|---|---|
| GET | `/api/{{PRIMARY_ENTITY}}` | Yes | List all for current user | — | `{ items: [...], total }` |
| GET | `/api/{{PRIMARY_ENTITY}}/[id]` | Yes | Get single by ID | — | `{ item }` |
| POST | `/api/{{PRIMARY_ENTITY}}` | Yes | Create new | `{ ...fields }` | `{ item }` |
| PATCH | `/api/{{PRIMARY_ENTITY}}/[id]` | Yes | Update existing | `{ ...fields }` | `{ item }` |
| DELETE | `/api/{{PRIMARY_ENTITY}}/[id]` | Yes | Delete | — | `{ success }` |

### User & Account

| Method | Route / Action | Auth | Description |
|---|---|---|---|
| GET | `/api/user/me` | Yes | Get current user profile |
| PATCH | `/api/user/me` | Yes | Update profile |
| DELETE | `/api/user/me` | Yes | Delete account |

### Subscription & Billing

| Method | Route / Action | Auth | Description |
|---|---|---|---|
| POST | `/api/billing/checkout` | Yes | Create Stripe Checkout session |
| POST | `/api/billing/portal` | Yes | Create Stripe Customer Portal session |
| GET | `/api/billing/subscription` | Yes | Get current subscription status |

### Webhooks (no auth — signature verified)

| Method | Route | Source | Events Handled |
|---|---|---|---|
| POST | `/api/webhooks/stripe` | {{PAYMENT_PROVIDER}} | See 02-payment-flow.md |
| POST | `/api/webhooks/auth` | {{AUTH_PROVIDER}} | user.created, user.deleted (if applicable) |

## Error Response Format

<!--
  AI INSTRUCTION: Use this format for ALL error responses. Consistency matters.
-->

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable description",
    "details": {}
  }
}
```

### Standard Error Codes

| Code | HTTP Status | When |
|---|---|---|
| `UNAUTHORIZED` | 401 | No valid session |
| `FORBIDDEN` | 403 | Valid session but wrong role/plan |
| `NOT_FOUND` | 404 | Resource doesn't exist |
| `VALIDATION_ERROR` | 400 | Invalid input |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Unexpected server error |
| `PLAN_LIMIT_REACHED` | 403 | Feature not available on current plan |

## Rate Limiting

| Route Pattern | Limit | Window |
|---|---|---|
| `/api/webhooks/*` | none (verified by signature) | — |
| `/api/billing/*` | 10 requests | per minute |
| `/api/{{PRIMARY_ENTITY}}` POST | 30 requests | per minute |
| `/api/*` (default) | 60 requests | per minute |

## Validation Rules

<!--
  AI INSTRUCTION: Document input validation for each create/update route.
  These become the source of truth for both server and client validation.
-->

### Create {{PRIMARY_ENTITY}}

| Field | Type | Required | Constraints |
|---|---|---|---|
| | | | |
| | | | |

### Update {{PRIMARY_ENTITY}}

| Field | Type | Required | Constraints |
|---|---|---|---|
| | | | |
| | | | |
