# Stack Decisions
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial stack selection from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  For EVERY choice below, provide:
  1. What you chose
  2. Why (1-2 sentences)
  3. What you considered and rejected (and why)
  Populate the corresponding variables in 00-variables.md after each decision.
-->

## System Overview

{{PROJECT_NAME}} allows {{TARGET_USER}} to {{CORE_ACTION}}.

## Core Stack

### Framework: {{FRAMEWORK}}
- **Why:**
- **Rejected:**

### Language: {{LANGUAGE}}
- **Why:**
- **Rejected:**

### Styling: {{STYLING}}
- **Why:**
- **Rejected:**

### UI Components: {{UI_LIBRARY}}
- **Why:**
- **Rejected:**

## Infrastructure

### Hosting: {{HOSTING}}
- **Why:**
- **Rejected:**

### Database: {{DB_PROVIDER}}
- **Why:**
- **Rejected:**

### ORM: {{DB_ORM}}
- **Why:**
- **Rejected:**

## Services

### Auth: {{AUTH_PROVIDER}}
- **Strategy:** {{AUTH_STRATEGY}}
- **Why:**
- **Rejected:**

### Payments: {{PAYMENT_PROVIDER}}
- **Why:**
- **Rejected:**

### Email: {{EMAIL_PROVIDER}}
- **Why:**
- **Rejected:**

### File Storage: {{FILE_STORAGE}}
- **Why:** (write "N/A — cut from MVP" if `{{FILE_UPLOAD_NEEDED}}` is no)
- **Rejected:**

### Analytics: {{ANALYTICS}}
- **Why:**
- **Rejected:**

## API Style: {{API_STYLE}}
- **Why:**
- **Rejected:**

## Cost Estimate (Monthly)

<!--
  AI INSTRUCTION: Estimate monthly cost at MVP scale (0-100 users).
  Include free tiers where applicable.
-->

| Service | Provider | Free Tier? | Est. Cost at MVP | Est. Cost at 1k Users |
|---|---|---|---|---|
| Hosting | {{HOSTING}} | | | |
| Database | {{DB_PROVIDER}} | | | |
| Auth | {{AUTH_PROVIDER}} | | | |
| Payments | {{PAYMENT_PROVIDER}} | | | |
| Email | {{EMAIL_PROVIDER}} | | | |
| **Total** | | | **$___/mo** | **$___/mo** |

## Package List

<!--
  AI INSTRUCTION: List every npm/pip package needed for the stack.
  This becomes the single source of truth for `npm install`.
-->

### Dependencies
```
# Core
# Auth
# Database
# Payments
# UI
# Utilities
```

### Dev Dependencies
```
# Testing
# Linting
# Types
```
