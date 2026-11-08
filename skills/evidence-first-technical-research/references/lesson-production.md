# Verified technical lesson production

Use this document when delivering a lesson, a technical tutorial, or a lesson revision. Apply the full evidence workflow in `SKILL.md` before drafting technical assertions. Pedagogical clarity cannot override correctness.

## Before teaching: lesson preparation gate

1. Read the curriculum entry and prerequisite evidence, but treat prior assistant prose as leads, not sources. If a prerequisite contains a pivotal unresolved claim, re-audit it before building on it.
2. State **one central question** and 1-3 observable outcomes. Set the lesson's scope and explicitly defer adjacent topics.
3. Build a claim ledger for the **pivotal** scientific and implementation assertions. Read actual primary-source content (paper equations, repository code, official docs), with revision/locator. Separate `VERIFIED`, `DERIVED`, `SIMPLIFIED`, `INFERENCE`, `UNVERIFIED`, `CONTRADICTED`.
4. Perform the mathematical and implementation audit: symbols, units, shape, coordinate conventions, assumptions, boundary cases, software revision, flags and executable call path. Run a small test/calculation if available; never imply execution otherwise.
5. Try to falsify 2-3 pivotal claims with a counterexample, errata, alternative convention, source-code divergence, or changed method version.
6. If pivotal evidence is missing, downgrade the lesson to a provisional conceptual explanation with explicit limits. Avoid detailed exact algorithms or default values without adequate support. Do not stall on minor missing context.

## Teaching sequence (adapt to learner intent)

**A. Establish the problem.** Begin with the real problem or failure that motivates the technique. Explain the objects and quantities before naming advanced concepts. For first-principles teaching, state which facts are axioms/definitions, which follow by derivation, and which are modeling assumptions.

**B. Construct intuition.** Use a small counterexample, minimal diagram, analogy, or thought experiment. State the analogy's boundary. Never present an invented diagram as a figure from a paper; cite an actual paper figure only after inspecting it.

**C. Derive the mechanism.** Introduce notation locally. Show intermediate steps for the key formula, check dimensions/signs, identify exact equalities versus local approximations (e.g. first-order projection), and use one numerically checkable example. Never skip the exact point the learner asks about.

**D. Cross-check implementation.** If teaching implementation details, read the pinned code: entrypoint -> caller -> function -> flags/state, compare to paper, and mention differences. If code is inaccessible, explicitly say so; use clearly labeled pseudocode only.

**E. Explain boundaries.** Discuss 1-3 relevant failure modes or counterexamples, what the technique does *not* establish, and domain-specific caveats (e.g. rendering fidelity does not imply collision geometry).

**F. Assess understanding.** End with 1-3 targeted questions or a small code/math exercise that tests a stated objective. For an ongoing series, do not claim mastery before learner response or observed solution. Avoid unnecessarily long quizzes if the learner prefers quick progression.

**G. Handoff.** Mark verified and unresolved items, lessons to revisit if needed, and one next question. Update learner state only using observed evidence; store nothing if persistence isn't available, but give the learner a portable state note.

## Instructional adaptation

- For a novice: use concrete examples and explicitly define every new symbol; reduce notation density without sacrificing correctness.
- For a mathematically advanced learner: show derivation, assumptions and failure cases before analogies.
- For a coding agent: ground explanations in actual code, tests, tensor shapes and reproduction steps.
- For a research learner: compare objectives, assumptions, implementation discrepancies, benchmark protocols and counterevidence.
- If a learner says "I don't understand X", respond only to X first. Diagnose whether the bottleneck is vocabulary, prerequisites, an algebraic jump, or a false prior claim. Provide a smaller worked example and ask one discriminating question if it would help.
- When the learner answers incorrectly, distinguish arithmetic error, conceptual misconception, ambiguous question or possible problem in the lesson. Reinspect sources if an explanation is contested.
- Use spaced retrieval/review at natural milestones if the learner benefits, never as an imposed schedule. Completion means "lesson delivered" unless an assessment was observed; preserve distinct states.

## Visual and executable examples

- Use visuals when they materially improve understanding of geometry, dataflow, tensors, motion or comparative behavior and a supported tool exists. Text-only is fine if it conveys the point better.
- Label schematic figures as *illustrative*, approximate plots as *approximations*, and actual measurements as *observed* with source/conditions.
- Make interactive controls truly update a valid model and do not pass off toy behavior as an exact algorithm. Test formulas, endpoints, units, constraints and visible labels before showing.
- Do not invent screenshots, paper figure numbering, architecture diagrams, source code or benchmark traces. For third-party imagery, verify what it depicts before relating it to a paper.
- Pseudocode is not executable source. State which conditions, normalization, schedules, randomness and state handling it omits.

## Per-lesson release gate

A lesson is **ready** only if the core scientific claims are supported or explicitly bounded, derivation is internally checked, key illustrative examples are mathematically consistent, uncertainty is visible, and assessment measures the lesson outcome. If these conditions fail, correct or scope down rather than decorate with unsubstantiated precision.
