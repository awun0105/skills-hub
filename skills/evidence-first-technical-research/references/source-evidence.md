# Evidence acquisition and provenance

## 1. Claim first, then source

Make a list of the claims that must be true for the requested answer to be reliable. Search to *test* each claim, including counterexamples and failed replications. Avoid searching solely for supportive phrasing.

For every source, record:

- Title, author/organization, publication state (peer reviewed, preprint, docs, code, issue, blog).
- Stable locator: DOI/arXiv ID and version, stable URL, file path and commit SHA, issue or documentation version.
- Date published/updated and date retrieved; do not silently equate the two.
- What was actually inspected: abstract, specific section, supplement, source function, table, commit, test output.
- Scope: task, dataset, training conditions, hardware, metric, constraints.
- Independence: who made the claim, who verified/reproduced it, possible shared underlying source.

## 2. Source preference (by claim type)

| Claim | Most relevant evidence | Common trap |
| --- | --- | --- |
| Paper's stated algorithm | Original paper + supplementary and corrections | Survey paraphrase omits assumptions |
| Actual implementation | Official code at pinned commit, exact call path, tests | Paper pseudocode differs from code |
| Dataset or benchmark record | Original benchmark protocol, official results, independent reproduction | Mixing datasets/hardware or leaderboard dates |
| Mathematical identity | Primary definition/theorem and independently checked derivation | Incorrect frames/normalization |
| Product integration/API | Versioned official docs, release notes and code | Stale blog or changed API |
| Historical first claim | Dated primary evidence, earlier candidate works | Unchecked "first"/"novel" |
| General recommendation | Verified constraints + comparative trade-off analysis | Presenting engineering judgment as a paper finding |

Secondary sources are useful for discovery and synthesis; they are not substitutes for primary evidence of implementation, timing, accuracy, or a mathematical definition.

## 3. Search and follow-through

1. Start with canonical keywords and aliases; record cutoff date and query terms if freshness matters.
2. Locate the original publication and official repository. Verify they refer to the same method/revision.
3. Read the method and experiment sections relevant to the question; examine supplementary material for implementation details.
4. For influential or surprising results, check independent benchmarks, follow-ups, negative results, and issue threads.
5. Search for contradictory variants ("not reproducible", "failure case", "bug", "ablation", "erratum").
6. Extract a **smallest sufficient quote or paraphrase** linked to exact section, figure, equation, table or code locator. Do not exceed source-quotation limits imposed by the platform.
7. Preserve source identity when moving across tools or sessions. If only a snippet was visible, mark "snippet-only".

## 4. SOTA comparisons

A valid SOTA comparison should align at minimum:

- **Task and output**: NVS, geometric reconstruction, simulation, feed-forward inference, per-scene fitting, dynamic actor prediction, etc.
- **Input assumptions**: number/type of views, camera calibration, poses, depth, LiDAR, masks, training data.
- **Evaluation**: same benchmark split, metric definitions, masked regions, held-out views, sequence lengths, scene scale.
- **Compute**: GPU, VRAM, image resolution, iteration count, multi-GPU settings, preprocessing time included/excluded.
- **Artifact and code**: public weights or source, reproduction conditions, license constraints.
- **Date and review state**: a 2026 arXiv preprint cannot be silently presented as a peer-reviewed CVPR result.

When conditions differ, use "author-reported under different protocols"; do not construct a global rank. Treat "newest" as a dated search conclusion rather than an enduring fact.

## 5. Claim ledger provenance

The ledger schema lives at `assets/claim-ledger.template.json`. Keep evidence IDs and claims separate. Cite `source_id` plus `locator`; a website domain alone is insufficient for a specific quantitative claim. Re-use only claims that survive a fresh audit. Set `inspected_at` for evidence you actually read; never fill an inspected timestamp to imply tool access you did not have.
