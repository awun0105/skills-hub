# Conditional task playbooks

Use one matching pattern only when needed. TD/BU select direction; DIV/CON select
breadth; S/D select depth. An arrow means a possible next operation, not a nested
skill call. Skip a stage whose artifact already exists and is reliable. These
patterns do not override the user's requested scope, permissions, or domain checks.

## 1. Learn a new concept
TD map -> BU worked example -> TD corrected explanation.
Use S for orientation, D for a difficult mechanism. Finish at the requested learning
outcome, not an exhaustive roadmap. A conceptual lesson need not invoke all modes.

## 2. Read an unfamiliar codebase
TD locate entrypoints -> BU inspect a real code path -> TD update the map.
Ground execution claims in source; use traces/tests when needed and available.
Report inaccessible files instead of inferring their contents from names.

## 3. Debug an uncertain defect
BU inspect/reproduce -> DIV only if explanation remains open -> CON discriminate
-> TD scope the fix -> authorized implementation and regression checks.
Do not fabricate reproducibility. For intermittent failures, scope conclusions to
observed runs rather than claim universal absence. Assess the fix's own risk.

## 4. Design a system
TD map goal/contracts -> DIV for genuinely needed alternatives -> CON compare
-> BU probe the highest-impact uncertainty -> TD recompose the chosen plan.
A design-only request ends with a plan and unperformed validation labeled as such.
A build request still requires implementation and its mandated checks.

## 5. Investigate a research anomaly
BU inspect measurements/controls -> DIV plausible mechanisms -> TD predictions
-> BU/CON controlled tests -> bounded conclusion.
Use D where confounding or interacting assumptions matter. Do not turn one run
into a general rule or claim novelty without the relevant prior-art check.

## 6. Explore a product problem
BU inspect actual user evidence -> TD frame need -> DIV solution mechanisms
-> CON choose a test when requested -> BU prototype/interview only with access.
Distinguish proposed interview questions from real interviews. A desk-research or
ideation request does not require pretending that market validation was performed.

## 7. Optimize end-to-end performance
TD define target -> BU measure actual bottleneck -> DIV distinct interventions
-> CON choose experiment -> BU benchmark/regressions -> authorized rollout.
Finish all required stages; there is no global three-stage cap. Preserve correctness
and measure the actual target rather than only a convenient local kernel.

## 8. Make a consequential decision
TD clarify criteria -> DIV only if options are inadequate -> CON compare
-> BU verify decisive claims -> conditional/supported recommendation.
Check current facts when material. Preserve uncertainty about future outcomes;
do not invent probabilities, preferences, or permission to transact.

## 9. Generate creative ideas
TD frame outcome or BU examine supplied examples -> DIV distinct candidates.
For ideas only, stop here without ranking. If selection or validation is also
requested, add CON and an appropriately scoped check. D is not compulsory.

## 10. Handle an urgent incident
Inspect immediate impact -> apply already authorized safe containment/runbook
-> verify containment -> BU/D diagnose -> scoped remediation and prevention.
Do not delay useful containment for unrestricted brainstorming. Do not infer
rollback approval, silently delete data, or call mitigation a proven root cause.

## 11. Prove or refute a claim
State proposition/assumptions -> choose proof, counterexample, or empirical test
appropriate to the claim -> verify -> deliver a proof or a bounded conclusion.
Examples can refute a universal claim when a valid counterexample exists; passing
examples alone cannot prove it. Missing premises must remain visible.

## 12. Perform a routine task
Use the known method directly with required checks. Skip full orchestration.
A short answer can still need careful verification; a long mechanical task can
remain straightforward. Judge the actual uncertainty, not the word count.

## Unlisted scenarios and lack of progress
Compose only the operations needed for the deliverable. At milestones, check
remaining obligations and evidence changes. After two consecutive no-progress
actions, choose a materially different permitted check or reframe once. If no
productive path remains, return the partial result and blocker without claiming
completion. A request to continue is not permission to invent progress.
