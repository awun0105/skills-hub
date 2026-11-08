# Assessment, mastery claims, misconception tracking and learner state

Use this file to review answers, resume a course, decide whether to advance, or revise a lesson. Avoid pretending to know whether a learner understood material without seeing a response or artifact.

## Evidence-based proficiency levels

Assign separately for each *objective*, not whole person:

- `unassessed`: lesson may have been delivered; no answer/work was observed.
- `attempted`: learner submitted an answer/artifact but correctness is unsettled.
- `needs_review`: check shows a concrete error, prerequisite gap or unresolved source issue.
- `demonstrated`: learner correctly explains, derives, implements or applies the outcome under stated conditions; record the observed evidence.

Do not equate fluent repetition, attendance, self-reported comfort or multiple completed chats with mastery. A quiz with ambiguous wording does not justify a proficiency downgrade; fix the question.

## Assessment construction

1. Match each objective to the smallest valid demonstration. Use: concept distinction, numeric calculation, debugging, derivation, critique of a paper claim, or transfer to a changed setting.
2. Include at least one question that exposes a likely misconception rather than only checking memorization. Do not require advanced prerequisites not yet taught.
3. Keep answer keys grounded in sources/derivation. For multiple-choice, rule out accidental ambiguity; avoid "always" when there are known exceptions.
4. Evaluate process when visible (reasoning steps, assumptions, unit checks, code test), not only a final number.
5. For uncertain answers, identify precisely what is missing and propose one targeted remedial exercise. Explain alternative correct conventions when applicable.
6. For coding exercises, distinguish **proposed** from **executed** code and tests. Record environments, seed, dependency versions and actual output only if observed.

## Adaptive progression policy

- Default: one lesson per requested turn; never force several lessons into a single response.
- Before moving, consult observed objective status and prerequisites. If a prerequisite is `needs_review`, briefly repair or offer a diagnostic; do not assume it resolved itself.
- A learner may explicitly choose to proceed despite gaps. Honor pace while stating the dependency, risk and what was deferred; do not secretly mark the gap as demonstrated.
- For already demonstrated skills, offer a concise recap and harder transfer exercise rather than repeating the entire unit.
- When a question jumps ahead, answer it with necessary minimal prerequisites and then resume the planned order, or adjust the DAG with explanation.
- Change depth based on response evidence, not invented user traits or psychological profiling.

## Portable learner state (not an external memory promise)

See `assets/learner-state.template.json`; maintain a local/visible copy if persistence is supported. Track:

- curriculum ID and version, last requested/covered lesson, next eligible lesson;
- per-objective proficiency and a short description of *observed evidence*;
- precise misconceptions and remediation status;
- lessons delivered vs genuinely assessed;
- sources and revisions for pivotal claims, and corrections that invalidate downstream lessons;
- learner's explicit language/pacing preferences and deferred topics;
- session timestamp and open audit questions.

Never silently mark `demonstrated` because assistant previously said "correct" or because the state template says so. In a cold session, past assessments are **reported state** until evidence or artifacts can be independently inspected. Preserve real user answers, not secrets or unnecessary personal data.

## Progress reports

Report lesson coverage and demonstrated objectives separately. Example: "8/20 lessons delivered; 5 objectives demonstrated in observed exercises; remaining objectives unassessed." If the learner has not answered checks, report progress in coverage only. Do not promise capability, grades or timeframe from this metric.

## Corrections and downstream effects

If a technical foundation is corrected, identify every lesson whose prerequisites rely on it. Mark those lessons `needs_review` and provide a minimal correction/verification exercise. For a claim previously cited but not re-accessible, preserve as an unresolved reference, not a verified basis for advancing.
