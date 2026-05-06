# Pages & Components
<!-- version: 0.1 | phase: 2 | last-updated: YYYY-MM-DD -->
<!-- changelog:
  v0.1 - Initial page map from Phase 2
-->

<!--
  INSTRUCTIONS FOR AI:
  Generate this AFTER 01-prd.md user stories are finalized.
  Every page here must exist in 02-file-tree.md.
  Auth requirements must match 02-auth-flow.md.
  SYNC CHECK: If this file changes, also update 02-file-tree.md, 02-auth-flow.md.
-->

## Page Map

### Public Pages (no auth)

| Page | Route | Purpose | Key Components |
|---|---|---|---|
| Landing | `/` | Convert visitors to sign-ups | Hero, Features, CTA, Pricing preview |
| Pricing | `/pricing` | Show plans, drive conversions | PricingCards, FAQ |
| Sign In | `/sign-in` | Authenticate users | {{AUTH_PROVIDER}} Sign In form |
| Sign Up | `/sign-up` | Register new users | {{AUTH_PROVIDER}} Sign Up form |

### Protected Pages (auth required)

| Page | Route | Purpose | Key Components |
|---|---|---|---|
| Dashboard | `/dashboard` | Overview / home for logged-in users | Stats, RecentActivity, QuickActions |
| {{PRIMARY_ENTITY}} List | `/dashboard/{{PRIMARY_ENTITY}}` | Browse all user's entities | DataTable, Filters, CreateButton |
| {{PRIMARY_ENTITY}} Detail | `/dashboard/{{PRIMARY_ENTITY}}/[id]` | View/edit single entity | DetailView, EditForm, DeleteButton |
| {{PRIMARY_ENTITY}} Create | `/dashboard/{{PRIMARY_ENTITY}}/new` | Create new entity | CreateForm |
| Billing | `/dashboard/billing` | Manage subscription | CurrentPlan, UpgradeButton, PortalLink |
| Settings | `/dashboard/settings` | Account settings | ProfileForm, DangerZone |

## Component Inventory

### Layout Components

| Component | Used On | Description |
|---|---|---|
| `MarketingNav` | Public pages | Logo, links, sign-in CTA |
| `DashboardLayout` | Protected pages | Sidebar, topbar, main content area |
| `Sidebar` | Protected pages | Navigation for dashboard sections |
| `Footer` | Public pages | Links, copyright |

### Shared Components

| Component | Used On | Description |
|---|---|---|
| `Button` | Everywhere | Primary, secondary, destructive variants |
| `Card` | Everywhere | Content container |
| `DataTable` | List pages | Sortable, filterable table |
| `Modal` | Various | Confirmation dialogs, forms |
| `Toast` | Various | Success/error notifications |
| `EmptyState` | List pages | When no data exists yet |
| `LoadingSpinner` | Various | Loading indicator |

### Entity-Specific Components

| Component | Used On | Description |
|---|---|---|
| `{{PRIMARY_ENTITY}}Card` | List page | Summary card for single entity |
| `{{PRIMARY_ENTITY}}Form` | Create/Edit pages | Form for creating/editing entity |
| `{{PRIMARY_ENTITY}}Detail` | Detail page | Full view of entity |

### Auth Components

| Component | Used On | Description |
|---|---|---|
| `SignInForm` | Sign In page | {{AUTH_PROVIDER}} sign-in widget |
| `SignUpForm` | Sign Up page | {{AUTH_PROVIDER}} sign-up widget |
| `UserMenu` | Dashboard topbar | Avatar, dropdown with settings/sign-out |

### Billing Components

| Component | Used On | Description |
|---|---|---|
| `PricingCards` | Pricing page, Billing page | Plan cards with features and CTA |
| `CurrentPlan` | Billing page | Shows active plan and status |
| `UpgradeBanner` | Dashboard | Shows if user is on free tier |

## Page Wireframes

<!--
  AI INSTRUCTION: Describe the layout of each key page in text form.
  This gives the coding AI enough to build without a Figma file.
-->

### Dashboard Home

```
┌──────────────────────────────────────────────┐
│ [Sidebar]  │  Welcome back, {name}           │
│            │                                  │
│ Dashboard  │  ┌─────────┐ ┌─────────┐       │
│ {{ENTITY}} │  │ Stat 1  │ │ Stat 2  │       │
│ Billing    │  └─────────┘ └─────────┘       │
│ Settings   │                                  │
│            │  Recent {{PRIMARY_ENTITY}}        │
│            │  ┌─────────────────────────┐    │
│            │  │ Item 1                  │    │
│            │  │ Item 2                  │    │
│            │  │ Item 3                  │    │
│            │  └─────────────────────────┘    │
│            │                                  │
│            │  [+ Create New]                  │
└──────────────────────────────────────────────┘
```

### {{PRIMARY_ENTITY}} List

```
┌──────────────────────────────────────────────┐
│ [Sidebar]  │  {{PRIMARY_ENTITY}}              │
│            │                                  │
│            │  [Search...] [Filter▾] [+ New]  │
│            │                                  │
│            │  ┌─────────────────────────┐    │
│            │  │ Name │ Status │ Date │ ⋮ │   │
│            │  │──────│────────│──────│───│   │
│            │  │ ...  │ ...    │ ...  │ ⋮ │   │
│            │  │ ...  │ ...    │ ...  │ ⋮ │   │
│            │  └─────────────────────────┘    │
│            │                                  │
│            │  [← Prev] Page 1 of N [Next →]  │
└──────────────────────────────────────────────┘
```
