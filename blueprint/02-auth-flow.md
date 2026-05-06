# Auth Flow
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial auth flow from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate this AFTER 02-stack.md confirms {{AUTH_PROVIDER}} and {{AUTH_STRATEGY}}.
  Every route/page mentioned here must exist in 02-file-tree.md.
  Every middleware mentioned here must be in 02-api-routes.md.
  SYNC CHECK: If this file changes, also update 02-api-routes.md, 02-schema.md, 02-file-tree.md.
-->

## Provider

- **Auth provider:** {{AUTH_PROVIDER}}
- **Strategy:** {{AUTH_STRATEGY}}
- **Multi-tenant:** {{MULTI_TENANT}}

## User Roles

| Role | Description | Default? |
|---|---|---|
| {{USER_ROLES}} | | |
| | | |

## Auth Flows

### Sign Up

```
1. User visits /sign-up
2. User enters {{AUTH_STRATEGY}} credentials
3. {{AUTH_PROVIDER}} creates user record
4. Webhook/callback creates user in our DB (prisma)
5. User redirected to /dashboard
6. If {{SUBSCRIPTION_TYPE}} requires payment → redirect to /pricing first
```

### Sign In

```
1. User visits /sign-in
2. User enters credentials
3. {{AUTH_PROVIDER}} validates and returns session
4. User redirected to /dashboard
```

### Sign Out

```
1. User clicks sign out
2. Session destroyed in {{AUTH_PROVIDER}}
3. User redirected to /
```

### Password Reset (if applicable)

```
1. User clicks "forgot password" on /sign-in
2. {{AUTH_PROVIDER}} sends reset email via {{EMAIL_PROVIDER}}
3. User clicks link → resets password
4. User redirected to /sign-in
```

## Protected Routes

<!--
  AI INSTRUCTION: List every route and whether it requires auth.
-->

| Route Pattern | Auth Required? | Role Required | Redirect If Unauthorized |
|---|---|---|---|
| `/` | No | — | — |
| `/sign-in` | No | — | `/dashboard` if already signed in |
| `/sign-up` | No | — | `/dashboard` if already signed in |
| `/pricing` | No | — | — |
| `/dashboard` | Yes | any | `/sign-in` |
| `/dashboard/{{PRIMARY_ENTITY}}/*` | Yes | any | `/sign-in` |
| `/api/webhooks/*` | No (verified by signature) | — | — |

## Middleware

```
middleware.ts:
  - Check session on every request to /dashboard/*
  - Redirect unauthenticated users to /sign-in
  - Redirect authenticated users away from /sign-in, /sign-up
  - Attach user context to request
```

## Database: Auth-Related Tables

<!--
  AI INSTRUCTION: These must match 02-schema.md exactly.
  If {{AUTH_PROVIDER}} manages users externally (e.g., Clerk),
  we still need a local user table for app-specific data.
-->

```
User
  - id            (from {{AUTH_PROVIDER}} or generated)
  - email
  - name
  - role          ({{USER_ROLES}})
  - createdAt
  - updatedAt

Session (if managed locally)
  - id
  - userId
  - token
  - expiresAt
```

## Environment Variables

```env
# {{AUTH_PROVIDER}} configuration
# Add exact env var names from {{AUTH_PROVIDER}} docs
```

## Security Considerations

- [ ] Session tokens are httpOnly, secure, sameSite=strict
- [ ] CSRF protection enabled
- [ ] Rate limiting on auth endpoints
- [ ] Account lockout after N failed attempts
- [ ] Email verification before full access (if applicable)
