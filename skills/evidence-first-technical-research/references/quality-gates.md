# Quality gates and failure handling

## Evidence gates

**G0 - Scope gate**: Can you state the exact question, scope, date, inputs, and whether an answer is conceptual, historical, current, implementation-level, or experimental?

**G1 - Provenance gate**: Are key claims tied to evidence actually examined? Do the sources support the *specific* claim (not merely the general area)? Are source versions and access boundaries explicit?

**G2 - Reproducibility gate**: Are formulas unit/shape checked? Are code assertions based on an actual path/function/version? Are quantitative comparisons bounded by protocols?

**G3 - Contradiction gate**: Have you looked for conflicting code, errata, limitations, or counterexamples? If a disagreement persists, is the answer explicitly qualified?

**G4 - Presentation gate**: Can a skeptical reader trace each consequential statement to source or derivation? Are analogies labeled and uncertainties visible? Is the final summary no stronger than the evidence?

**Fail-closed policy:** If a pivotal gate fails, stop claiming verification. Offer a limited conceptual answer with visible caveat or ask only for truly essential missing access; propose a decisive verification action. Do not hide a missing source behind a confident summary.

## Labels and allowable verbs

- `VERIFIED`: "The inspected paper states ..." / "The pinned function does ..."; NOT "This is scientifically proven."
- `DERIVED`: "Under assumptions A, B, it follows ..." with steps.
- `SIMPLIFIED`: "For intuition, ignoring X ..." and state what changes in real code.
- `INFERENCE`: "I recommend ... because ..." distinguishing trade-offs.
- `UNVERIFIED`: "I could not confirm ..." or "I have not run this."
- `CONTRADICTED`: "Paper says X; source code at SHA Y does Z" without choosing a winner by rhetoric.

## Red flags (trigger a re-audit)

- A claim repeated earlier without fresh source inspection.
- Numerical values without units, hardware/dataset, or protocol.
- "Latest", "newest", "best", "SOTA", "the only" without a dated search and precise task.
- Paper and code references without file/function/section locators.
- Figure/citation does not actually portray or support the described thing.
- Too-clean derivation that ignores coordinate conventions, singularity or clipping.
- "Successfully tested" with no command/output or available execution environment.
- Model-generated citations or URLs not observed in source evidence.
- Unsupported extrapolation from visual quality to collision, geometry, or closed-loop readiness.

## Adversarial audit before delivery

Ask three falsification questions:

1. What single observation would disprove the central explanation?
2. Is there an alternative implementation, benchmark split, or convention that changes the conclusion?
3. What is the strongest assertion made without directly inspected evidence?

Resolve or downgrade those assertions. For long outputs, provide an audit note listing unresolved claims. Do not assign arbitrary confidence percentages; label evidence quality and remaining uncertainty instead.

## Examples of compliant correction

Bad: "Cloning displaces Gaussians toward high-loss pixels" (when the cited official version copies positions).

Better: "In the inspected reference implementation, cloning duplicates position initially. New Gaussians may diverge in later optimization; the visual diagram is conceptual."

Bad: "Paper X is SOTA because PSNR=35 dB."

Better: "Paper X reports 35 dB under dataset/protocol Y; no apples-to-apples evidence was found for a global rank."

Bad: "I checked all papers." (only abstracts read).

Better: "I screened abstracts and inspected full text for A and B; the rest remain discovery leads."
