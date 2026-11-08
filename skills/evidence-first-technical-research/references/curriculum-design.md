# Curriculum architecture: evidence-based technical tutoring

Use this document for any request to plan a multi-lesson series, review a proposed syllabus, or continue a long technical course. A curriculum is a *provisional teaching design*, not evidence that its topics are complete, its claims are true, or its ordering is universal.

## Start from learner and destination

Capture only information relevant to instruction: learner goal, current practical ability (demonstrated or self-reported), prerequisites, desired depth, language, pacing preference, domain constraints, access to computing/labs, and target deliverable. Reuse known answers rather than repeatedly asking. If unknown, state assumptions and create a draft that can be adjusted. Do not infer mastery from enthusiasm, job title, or number of prior messages.

Specify a target competency as an observable action, e.g. "derive the covariance projection with coordinate assumptions, inspect a pinned implementation, and reproduce a numerical check", not "understand Gaussian Splatting". Separate conceptual understanding, mathematical reasoning, implementation, experimental literacy, and critical research evaluation.

## Plan with a prerequisite graph, not a fashionable topic list

1. Decompose the target into demonstrable competencies and underlying questions.
2. Identify necessary mathematical, scientific, implementation and experimental prerequisites. Mark each as required or optional rather than blindly adding every related field.
3. Build a directed acyclic graph (DAG): each lesson has `id`, `title`, `prerequisites`, measurable `learning_objectives`, `verification_plan`, `assessment_plan`, and `status`.
4. Topologically order lessons; group into units by shared outcomes. Each lesson should focus on one bounded core question unless the user requests an overview or intensive workshop.
5. Make bridges explicit. A lesson on CUDA kernels may require memory layout and parallel execution before architecture optimization; a lesson on differentiable rendering may require chain rule and coordinate frames.
6. Distinguish `CORE` from `OPTIONAL` or `RESEARCH_FRONTIER`: user can reach the core outcome without taking every optional branch.
7. For frontier topics, record a research cutoff and include a lesson-level fresh-source plan; dates, SOTA and package APIs must be rechecked when taught.
8. Mark outcome-level assessments and a capstone with a reproducible artifact (derivation, benchmark, small implementation, paper audit), not attendance alone.
9. Review the draft for missing prerequisites, duplicated lessons, unbounded lesson scope, unsupported promises, artificial specificity, and cross-domain transfers assumed without evidence.
10. Treat lesson count as a planning choice. Do not assert that exactly N lessons are necessary or sufficient, or guarantee expertise after completion.

## Required curriculum-level records

- **Curriculum contract:** goal, scope/out-of-scope, audience assumption, evidence standard, desired outcome, delivery cadence (one lesson per reply by default), optional practical environment, and boundaries.
- **Lessons:** unique stable IDs (do not silently renumber after revisions), titles, prerequisites, objectives expressed by observable verbs, knowledge checks, source-validation needs, optionality, and status (`not_started`, `in_progress`, `completed`, `needs_review`).
- **Milestones:** an assessment at the end of each unit; emphasize transfer to unfamiliar problems rather than recalling memorized text.
- **Audit schedule:** revisit central claims before high-dependency lessons, at major milestones, on source updates, and whenever a learner or agent discovers contradiction.
- **Provenance:** the curriculum's structure is pedagogical design; only its specific cited technical claims have external evidence.

## Curriculum acceptance gates

- Every lesson has at least one observable learning objective and one concrete assessment/check.
- All prerequisite IDs exist; no cycles or self-dependencies.
- Order respects prerequisites. A valid DAG can have multiple topological orders.
- The stated terminal competence is covered by at least one verified assessment plan. Coverage is a planning assertion to be tested, not an automatic guarantee.
- Each technical lesson has a plan to inspect primary sources *when it is delivered*. Do not falsely claim the entire syllabus was researched or verified in advance.
- User constraints (one topic per response, course depth, examples, language) are represented explicitly.

Run `python scripts/audit_curriculum.py <curriculum.json>` to check **structural** invariants. This script cannot verify pedagogy, scientific truth, or source authenticity. See `assets/curriculum.template.json` for schema.

## Changing a curriculum safely

- Keep stable IDs, record revision date, and explain added, removed, split or reordered lessons.
- Recompute prerequisite edges and refresh assessments and expected outcomes.
- If previous content was wrong, add a correction and reopen dependent lessons as `needs_review` instead of pretending everything remains mastered.
- Allow the learner to skip or test out of prerequisites with a demonstrated check; log the result and caveat.
- If a user requests "continue", choose the next eligible lesson consistent with state, not the next number guessed from chat history.
