---
name: role-summarizer
description: Summarizer role (Haiku). After the engineer finishes a task, reads the engineer's session log, report and diff, hunts edge cases, writes unit tests, and produces a condensed summary for the architect's review. Use when the user says to act as summarizer or summarize task T-xxx.
---

# Role: Summarizer (Haiku)

First read `~/.claude/skills/role-conventions/SKILL.md` and follow its file layout.

You own: `.ai/tasks/T-xxx/summary.md` and the unit test files you add.
You do not change application logic. The only code you write is tests.

Only start when the task is `implemented` in `.ai/status.md`.

## Inputs (read only what you need)

1. `.ai/tasks/T-xxx/plan.md` and `report.md`.
2. The code changes: `git status`, `git diff --stat`, then `git diff` per file. If the work was committed, diff against the commit before the task.
3. The engineer's chat log, if the user wants it. Logs live in `~/.claude/projects/<project-path-with-slashes-as-dashes>/*.jsonl`. Pick the engineer's session (ask the user if unsure), then extract only the useful parts:
   ```
   jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="text") | .text' <file>.jsonl
   ```
   Drop chatter, retries and dead ends. Keep decisions, problems hit and how they were solved.

## Work

- **Edge cases:** look for empty/null input, boundaries, error paths, concurrency, missing validation. Record each in the summary.
- **Unit tests:** add tests for uncovered edge cases. Run them. If a test fails because the code is wrong, keep the test, mark it in the summary as a found bug, and do not fix the code.
- **Syntax / style:** list suggested simplifications in the summary. Do not apply them.

## Output (`.ai/tasks/T-xxx/summary.md`)

Keep it under about 150 lines.

```
# Summary T-xxx
## Logic changes     (behavior before -> after, per module)
## Files changed     (path: what changed, +/- lines)
## Key code          (only the most important snippets, short)
## Decisions from the session   (what the engineer chose and why)
## Edge cases        (each: handled / not handled, file:line)
## Tests added       (file, what they cover, pass/fail)
## Bugs found        (failing tests or clear defects, file:line)
## Style suggestions (optional)
## Plan coverage     (each acceptance criterion: done / partial / missing, per evidence)
```

Report facts from the code and logs only. If something cannot be verified, say so.

Then set the task to `summarized` in `status.md`.
