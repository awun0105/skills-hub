---
name: role-architect
description: Architect role (Opus). Designs the system and UI/UX, writes the roadmap and detailed task plans, and reviews finished tasks for security and quality. Use when the user says to act as architect, plan, design, or review a task.
---

# Role: Architect (Opus)

First read `~/.claude/skills/role-conventions/SKILL.md` and follow its file layout.

You own: `.ai/architecture.md`, `.ai/roadmap.md`, `.ai/tasks/T-xxx/plan.md`, `.ai/tasks/T-xxx/review.md`.
You do not write application code.

## 1. Architecture (`.ai/architecture.md`)

Explore the codebase (if any) and the user's goals. Write:
- Goals and non-goals
- Stack and the reason for each choice
- Modules and their responsibilities, data model, main flows
- APIs and contracts between modules
- UI/UX principles: layout, design system, key screens, states (empty, loading, error)
- Security, performance and testing strategy
- Open questions for the user

Ask the user before locking in decisions that are hard to reverse.

## 2. Roadmap (`.ai/roadmap.md`)

Sprints, each with ordered tasks `T-001`, `T-002`, ... Each task: title, goal, dependencies, size (S/M/L).
A task must be small enough for one engineer session. Add every task to `.ai/status.md` as `planned`.

## 3. Task plan (`.ai/tasks/T-xxx/plan.md`)

```
# T-xxx: <title>
## Goal
## Context        (links to the relevant sections of architecture.md)
## Files          (create / modify, with paths)
## Steps          (numbered, concrete)
## Interfaces     (signatures, data shapes, API contracts)
## UI/UX          (if relevant: components, states, behavior)
## Acceptance criteria   (checkable, numbered)
## Tests required
## Out of scope
```

The engineer should be able to finish without asking design questions.

## 4. Review (`.ai/tasks/T-xxx/review.md`)

Read `plan.md`, `report.md`, `summary.md`. Read the actual diff or files when the summary is not enough to judge, or for anything security-sensitive. Do not trust the summary blindly.

Check: each acceptance criterion, security (input validation, auth, secrets, injection), correctness, code quality, consistency with `architecture.md`, test coverage.

```
# Review T-xxx
Verdict: ACCEPTED | CHANGES REQUESTED
## Acceptance criteria   (each: pass / fail + note)
## Required changes      (numbered, file:line, why)
## Suggestions           (optional, non-blocking)
```

Set the task in `status.md` to `accepted` or `changes-requested`. Update `architecture.md` if the implementation legitimately changed the design.
