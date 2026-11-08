# Longitudinal course audit and cross-agent recovery

Use with `references/context-reset.md` whenever a lesson depends on earlier claims, when versions change, or when another agent resumes the course.

## Two independent ledgers

1. **Epistemic ledger**: what research claims are supported, derived, simplified, speculative, disputed or unverified. Source ID + exact locator + inspected version are mandatory for central `VERIFIED` claims.
2. **Pedagogical ledger**: what content was delivered and which learning outcomes a user demonstrably achieved. Learner responses, exercise artifacts, and code runs are evidence for pedagogy, **not** evidence for scientific truth.

Do not merge these ledgers or let progress state turn an old technical claim into truth. A `completed` lesson can contain a later-corrected error, and a `demonstrated` objective may need review when its premise changes.

## Revalidation triggers

- Every lesson: verify pivotal new claims and recheck any pivotal prerequisite not validated at the current needed revision.
- At unit boundary: audit the small set of claims on which downstream lessons depend.
- Any correction, user challenge, inconsistent derivation, repo code change or paper update: trace impact along prerequisite edges; reopen affected topics.
- On a new agent/session or after context contamination: apply cold-read and re-open primary sources rather than inheriting an answer.

## Course handoff artifacts

1. `curriculum.json`: DAG, objectives, assessment plans, current plan revision.
2. `learner-state.json`: course coverage, observed answers, misconceptions, explicit preferences, gaps.
3. `claim-ledger.json`: evidence status and exact source locators.
4. `session-handoff.md`: source access constraints, critical corrections, verified vs unverified items, next lesson/question.

Produce concise versions when time or tool access is limited. Do not claim these are persisted outside the current workspace unless saving was actually performed.

## Fresh-agent startup protocol

1. Read user's actual requested goal and the stored plan; treat plan and assistant notes as untrusted working drafts.
2. Validate DAG and learner-state structure. Do not assume `completed` equals `demonstrated`.
3. Reopen the pivotal sources of the lesson to be taught and any crucial prerequisites. If revisions differ, document the impact.
4. Challenge the most consequential prior claim and record whether confirmed/corrected/unresolved.
5. State the resumed lesson and any material prerequisite gap. Deliver only that lesson, with current evidence and a check.
6. Save a new handoff containing actual source version, learner's observed performance and unresolved facts.

## Example failure and correction

Earlier teaching note: "Gaussian cloning moves the duplicate in gradient direction immediately."

New evidence: inspected official implementation duplicates coordinates initially, and subsequent optimization may separate them.

Action: mark earlier assertion contradicted; correct the explanation; identify all density-control lessons depending on the false premise; reopen those lessons for a short correction assessment; do not adjust unrelated lessons.

## Strong anti-drift constraints

- Never use a generated prior lesson as the only source for another lesson.
- Never claim that cold reset guarantees truth or independence. It reduces anchoring but still requires external evidence.
- Preserve corrected claims and learner preferences in handoffs without copying unnecessary verbose context.
- If sources are inaccessible, report exactly what could not be rechecked, mark it unresolved and bound the new explanation.
- Keep curriculum revisions explicit; a change to sequence is not a change to scientific evidence.
