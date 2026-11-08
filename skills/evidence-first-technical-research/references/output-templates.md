# Output templates

These are adaptable structures, not a mandate to add tables to every short answer. Compact answers need explicit provenance and uncertainty even when no full table is shown.

## Template A: Verified technical lesson

```
# Lesson [n]: [single precise question]
Scope / cutoff / sources accessed: [date, revision, restrictions]

## Source audit (before lesson)
- [paper DOI/version, section/equation; what was read]
- [official repository, commit, file/function; what was inspected]
- [secondary independent corroboration or reason unavailable]

## Claims needing care
| Claim | Status | Evidence locator | Caveat |

## First principles
[What problem exists? What assumptions are needed?]

## Derivation and notation
[Define variables, units, dimensions, exact vs approximate.]

## Concrete example
[Clearly mark pedagogical simplification and calculate a checkable case.]

## Paper vs implementation
[Only if code was inspected; describe version/flags and mismatches.]

## Failure modes and domain limits
[When does the method break? What is not implied?]

## Mini-check / exercise
[2-3 conceptual or numeric questions with grounded answers.]

## Audit note
[Important unresolved items, nonexecuted tests, next verification.]
```

## Template B: Paper/method audit

```
Method: [title, DOI/arXiv version, publication state, date]
Access: [full-text/supplement/abstract-only]
Task/input/output/assumptions:
Key mechanism: [equations/sections]
Code: [official URL, commit, key paths, code available?]
Experiments: [dataset, split, metrics, hardware, training/inference distinction]
Verified claims: [locators]
Differences from alternatives: [strictly comparable conditions]
Limitations / unresolved evidence:
Independent reproduction: [seen/not seen]
Verdict: [evidence and use-case bounded; not categorical SOTA]
```

## Template C: Code review of claimed behavior

```
Question: [specific behavior]
Repo: [origin, SHA/tag, trust status]
Path: [entrypoint -> caller -> function -> test]
Observed lines/branches: [exact citations, not generated line numbers]
Paper/documentation claim: [evidence]
Agreement / divergence:
Test command and output: [actual; else "Not executed"]
Conclusion: [verified / inference / unresolved]
```

## Template D: Method comparison

```
Table columns: Method | Task | Inputs | Representation | Method/engine |
                Data/protocol | Training time | Inference time | Quality |
                Hardware | Code/weights | Publication state | Evidence status

After table: what is comparable, what is not, recommendation rationale,
missing evidence, and decisive benchmark design.
```

## Template E: Correction notice

```
Correction to earlier statement: [quote/paraphrase]
Inspected source: [version + locator]
What evidence actually supports: [specific]
Cause of mismatch: [unverified assumption, code version change, convention]
Updated technical takeaway: [bounded claim]
Remaining uncertainty: [if any]
```

## Template F: Research-verified multi-lesson course

```
# Curriculum: [goal as observable end competency]
Audience assumption: [observed / self-reported / unknown]
Scope and exclusion: [what is and is not included]
Source cutoff: [date; syllabus topics are not yet validated paper claims]
Instruction policy: [one lesson per requested turn; language/depth]

| Unit | Lesson ID | One bounded question | Prerequisites | Demonstrable outcome | Verification plan | Assessment |

Milestones: [derivation / implementation / experiment / paper audit]
Optional / frontier branches: [conditional, with fresh source checks]
Known unassessed prerequisites: [do not infer from chat]
Next eligible lesson: [ID]
Plan disclaimer: This is a provisional curriculum DAG, not a guarantee of completeness or mastery.
```

## Template G: Learner progress (coverage is not mastery)

```
Curriculum version: [ID, revision]
Coverage: [delivered/completed lessons] / [total]
Demonstrated objectives: [count with observed evidence] / [total assessed]
Unassessed objectives: [count]
Misconceptions needing repair: [precise issue + affected lesson ID]
Corrections to source claims: [claim ID + affected lessons]
Last delivered lesson: [stable ID]
Next eligible lesson / prerequisite gap: [ID, evidence]
State provenance: [observed this session / carried from prior artifact, not reverified]
```

## Template H: Multi-agent course resume / correction

```
Task and explicit user constraints: [no inferred preference]
Curriculum / learner-state / claim-ledger locations:
Pivotal source identifiers, revisions, exact locators:
Earlier assistant assertions to distrust:
Observations actually rechecked in this session:
Claims corrected / downgraded / still unresolved:
Learning outcomes demonstrated with actual answer/artifact:
Dependent lessons requiring review:
Single next lesson and research question:
Access gaps and decisive next checks:
```
