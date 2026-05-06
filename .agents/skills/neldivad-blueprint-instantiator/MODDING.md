# Modding Guide
<!-- version: 0.1 | last-updated: YYYY-MM-DD -->

> This is the harness mod SDK. Read this before changing how the game engine works.
> Changing the *product* (scope, features) is handled by the Scope Request Ritual in `00-game-rules.md`.
> This guide is for changing the *harness itself* — phases, templates, variables, milestone structure.

---

## What Is the Harness?

The harness is the system that runs underneath every project:

```
references/saas-blueprint/
├── 00-*.md        → Engine (state, rules, variables)
├── 01-*.md        → Phase 1 templates (PRD, Q&A, MVP checklist)
├── 02-*.md        → Phase 2 templates (architecture docs)
├── 03-*.md        → Phase 3 templates (milestones, AI rules)
└── saves/         → Checkpoint system
```

When you run `/neldivad-blueprint-instantiator <project-name>`, the harness is copied
into `<project-name>/blueprint/`. Changes to `references/` affect all *future* projects.
Changes to a project's `blueprint/` only affect that project.

---

## Mod Types

### Type 1 — Template Edit (Safe)
> Change what gets generated inside an existing phase doc.

**Example:** Add a `02-analytics.md` template. Add a new Q&A question to `01-qna-script.md`.

**Rules:**
- Add the file to `references/saas-blueprint/`
- Register any new `{{VARIABLES}}` it uses in `00-variables.md`
- Update the File Map table in `00-readme.md`
- Update `SKILL.md` Template Reference table
- Bump version on all modified files
- Test: instantiate a dummy project, verify the new template copies correctly

---

### Type 2 — Variable Addition (Safe)
> Add a new `{{VARIABLE}}` to the system.

**Rules:**
1. Add it to `00-variables.md` with: name, description, example value, which phase sets it
2. Add the Q&A question that extracts it to `01-qna-script.md`
3. Use it in the appropriate `02-*.md` or `03-*.md` templates
4. Grep all templates to confirm it resolves — no orphaned `{{PLACEHOLDERS}}`

**Never:** Invent a variable inline in a template without registering it first.

---

### Type 3 — New Phase (Moderate)
> Add a phase between existing phases (e.g., a "02.5-integrations" phase).

**Rules:**
1. Use the correct prefix for ordering (`02-`, `02b-`, etc.)
2. Add a gate for the new phase in `00-game-rules.md` Review Gates section
3. Add the phase to the route map in `00-state.md` template
4. Add the phase to the File Map in `00-readme.md`
5. Update `SKILL.md` workflow section to include the new phase steps
6. Ensure the new phase has: a template doc, a gate, a save slot trigger

**Watch out for:** Phase ordering. The save slot system has max 5 slots — if you add
phases, re-evaluate which phases deserve permanent saves vs. just autosave.

---

### Type 4 — Milestone Structure Change (Moderate)
> Change the M0-M4 campaign structure (rename, reorder, merge, split milestones).

**Rules:**
1. Edit `03-milestones.md` route map ASCII art to reflect the new structure
2. Update the Milestone Status Tracker table at the bottom
3. Verify dependencies still form a valid DAG (no circular dependencies)
4. If a milestone is removed: check if any `02-*.md` template references it
5. Update `SKILL.md` "Post-Blueprint: Start Building" section if the entry milestone changes

**The non-negotiables (don't remove these):**
- A scaffold milestone (M0 equivalent) — always first
- A "done when deployed" milestone (M4 equivalent) — always last in core campaign
- The Campaign Complete checklist — the win condition must exist

---

### Type 5 — Game Rules Change (High Risk)
> Modify `00-game-rules.md` — how the AI operates, gate behavior, scope rules.

**This is the game engine. Changes here affect every session of every project.**

**Rules:**
1. Write down WHY the current rule is wrong before changing it
2. Write down what breaks if the rule is removed
3. Don't remove rules — deprecate them with a comment explaining the replacement
4. Gate changes: if you change gate behavior, verify all gate references in `SKILL.md` still match
5. Scope rules: if you change the Scope Request Ritual, ensure the Scope Queue format
   in `00-state.md` is updated to match

**High-risk changes to avoid without good reason:**
- Removing the "no mid-milestone scope" rule — this is the core anti-creep guard
- Changing the save system layer count — breaks rollback behavior
- Making gates optional — destroys the campaign structure

---

### Type 6 — Skill Workflow Change (High Risk)
> Modify `SKILL.md` — the instantiation and resume workflow.

**Rules:**
1. Always test both `new` and `resume` paths after any change
2. If you add a new phase to the workflow, add it to the phase progression in `00-state.md`
3. If you add external skill dependencies (like `find-skills`), document them in:
   - `SKILL.md` Phase 0 setup check
   - `CLAUDE.md` Required External Skills table
4. Keep `SKILL.md` under 500 lines — move detail to `references/` docs

---

## Harness Versioning

Each template file carries its own version header:
```
<!-- version: 0.1 | phase: 0 | last-updated: YYYY-MM-DD -->
```

When you mod a template:
- Bump the version
- Add a changelog entry in its header block
- Note the change in `changelog.md` of any active projects that should receive the update

**Backporting to existing projects:**
Harness changes don't automatically apply to projects already in progress.
To backport: manually apply the change to the project's `blueprint/` folder,
bump the version there too, and log it in that project's `changelog.md`.

---

## Checklist Before Shipping a Mod

```
[ ] All new {{VARIABLES}} registered in 00-variables.md
[ ] All new files added to File Map in 00-readme.md
[ ] All new files added to Template Reference in SKILL.md
[ ] Version headers bumped on all modified files
[ ] Changelog entries written
[ ] Tested: dummy project instantiates without errors
[ ] Tested: resume path still works on existing project
[ ] No orphaned {{PLACEHOLDERS}} (grep for {{ in all templates)
```
