# Cold-read, independence and context recovery

## Threat model

Long chats and previous assistant explanations cause anchoring, confirmation bias, invented continuity and citation laundering. Tool summaries may compress away crucial caveats. A reset mitigates these risks only if **source verification resumes**, not if prior conclusions are copied forward under a new label.

## When to activate

- User explicitly alleges bias/hallucination or requests independent verification.
- Important citations cannot be traced to content viewed in the current session.
- Earlier lessons/claims conflict with paper, code, equations, updated docs, or each other.
- Several agents hand off one research task or context is near its length limit.
- A new source/version invalidates an earlier recommendation.

## Cold-read protocol

1. Freeze the task statement and user constraints; exclude previous assistant factual claims from the evidence pool.
2. Create a clean list of research questions without seeding answers.
3. List candidate primary sources from *source IDs*, not memory-based assertions. Reacquire the pivotal sources, if accessible, and record what was reread.
4. Attempt to falsify the top claims via conflicting variants, counterexamples, experimental conditions, or actual code.
5. Mark each old claim as confirmed, corrected, unresolved or dropped. Never quietly retain an unsupported statement for continuity.
6. Produce corrected explanation and an explicit difference note: "Earlier X; inspected evidence supports Y."
7. Save `session-handoff.md` using `assets/session-handoff.template.md`; keep verified, derived and unverified items separate.

## Fresh-agent handoff

Provide: task; source cutoff; exact questions; trusted source IDs/links and revision; claim status and location; conflicting evidence; mathematical assumptions; code commands *actually run* and results; open tests; answer boundaries; user preferences relevant to this specific task.

Do **not** put "the previous assistant concluded X" in the VERIFIED section. Place that in "Claims to re-check" and require renewed confirmation. Exclude secret tokens, user private data, and oversized raw source copies. Preserve citation restrictions and copyright.

## If browsing or repository access is missing

- State which checks cannot be performed in this environment.
- Provide a logically limited explanation based on stable, clearly marked background or user-provided evidence.
- Never assert a latest status, source-code detail, or primary-source inspection without access.
- Hand off URLs/paths only when known, not guessed. Request accessible files only if necessary for the requested degree of certainty.

## Anti-drift checkpoint in an ongoing series

At the start of each lesson, record:

- Lesson number and one bounded learning objective.
- 2-5 facts required from earlier lessons (revalidated if pivotal).
- New sources and revisions checked for this lesson.
- Misconceptions and limitations from previous lesson that are being corrected.
- Items deliberately deferred.

At the end, state the next *question*, not the next unverified conclusion. Keep a concise handoff after every major chapter or after any correction.
