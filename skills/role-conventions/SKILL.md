---
name: role-conventions
description: Shared file layout and handoff rules for the three-role workflow (architect = Opus, engineer = Sonnet, summarizer = Haiku). Read before any role-architect, role-engineer or role-summarizer work.
---

# Three-role workflow: shared conventions

Three separate Claude Code sessions work on one project and talk only through files.

| Role | Model | Skill |
|---|---|---|
| Architect: design, plans, final review | Opus | `role-architect` |
| Engineer: code, test, fix | Sonnet | `role-engineer` |
| Summarizer: summary, edge cases, unit tests | Haiku | `role-summarizer` |

## File layout (project root)

```
.ai/
  architecture.md          # Architect: system design, stack, modules, UI/UX principles
  roadmap.md               # Architect: overall execution plan, sprints, ordered task list
  status.md                # Everyone: task board (one line per task)
  tasks/
    T-001/
      plan.md              # Architect: detailed plan for this task
      report.md            # Engineer: what was done, how it was tested
      summary.md           # Summarizer: condensed changes, edge cases, tests added
      review.md            # Architect: verdict (ACCEPTED / CHANGES REQUESTED)
```

- Task IDs: `T-001`, `T-002`, ... zero-padded, never reused.
- Only write the files your role owns. Read anything.
- Write in plain Markdown. Be concise.

## status.md format

One line per task, kept in roadmap order:

```
T-001 | <short title> | <state> | <owner of next step>
```

States, in order: `planned` -> `in-progress` -> `implemented` -> `summarized` -> `accepted`.
If review fails: `changes-requested` (goes back to the engineer, then `implemented` again).

Each role updates only the state of the task it just finished.

## Handoff order for one task

1. Architect writes `tasks/T-xxx/plan.md`, sets `planned`.
2. Engineer implements, writes `report.md`, sets `implemented`.
3. Summarizer writes `summary.md` (and unit tests), sets `summarized`.
4. Architect reads `summary.md` (and the diff when needed), writes `review.md`, sets `accepted` or `changes-requested`.
5. On `changes-requested`, the engineer fixes, appends a "Round N" section to `report.md`, and steps 3-4 repeat.
