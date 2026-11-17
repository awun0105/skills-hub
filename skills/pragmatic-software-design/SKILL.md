---
name: pragmatic-software-design
description: Implement or refactor software with readable control flow, consistent naming and project structure, cohesive responsibilities, and justified abstractions. Use when writing features, repairing AI-generated code, or evaluating principle and pattern choices; also supports read-only design review when requested.
---

# Pragmatic Software Design

Produce code a maintainer can locate, read, explain, test, and change. Optimize for fitness for purpose under the actual constraints. Complexity must buy a concrete benefit: preserve the simplest design that satisfies the current behavior, quality requirements, and established contracts.

This skill guides engineering judgment; it is not a universal architecture, style guide, or mandate to refactor. Explicit user requirements and applicable project instructions take priority. Keep review-only tasks read-only. Do not add dependencies, reorganize unrelated code, migrate architecture, commit, or deploy merely because this skill is active.

## Start from the actual project

Before changing code, establish just enough evidence to answer:

- What behavior changes, including relevant failure/edge cases? What must remain compatible?
- Where is this behavior owned and called? What conventions do the nearest maintained implementations use?
- Which quality attribute matters here, and how will success be checked?

Inspect applicable instructions, build/formatter/linter configuration, relevant tests, and representative neighboring files. Follow required graph/navigation tools when the repository provides them. Use focused searches and call paths; do not read the whole repository by default. Distinguish a verified requirement from an assumption. Ask only when an unresolved decision materially affects correctness, compatibility, or scope; otherwise choose a reversible convention-consistent default.

For an existing codebase, adapt to its idioms instead of introducing a personal style. If conventions conflict, prefer explicit configuration and the nearest maintained subsystem; avoid copying a known defect. In a greenfield project, derive a small structure from the runtime, framework, and actual features. Do not scaffold empty architectural layers.

Read [structure-and-readability.md](references/structure-and-readability.md) when choosing file placement, public names, module boundaries, or simplifying difficult code.

## Choose the design before adding machinery

For a nontrivial change, make a brief decision, in working notes or the existing task artifact:

1. The behavior and constraints being served.
2. The simplest adequate implementation and where it belongs.
3. Any added boundary, abstraction, pattern, dependency, or asynchronous component: the concrete variation/failure/change it handles and its cost.
4. How the behavior will be verified.

For a small fix, this may be one sentence; no new document, approval checkpoint, diagram, or pattern report is required. Keep the user-facing explanation proportional to the change.

**Default to direct code.** Add an abstraction when it isolates meaningful volatility, enforces a real contract, enables a required external boundary/test seam, or removes duplicated business knowledge. A single implementation can justify an interface at such a boundary; multiple similar snippets do not automatically justify a shared abstraction.

Before introducing a pattern, identify its trigger, compare a simpler alternative, and explain the trade-off. “SOLID,” “best practice,” “future scalability,” or “enterprise-ready” alone is not a justification. Do not invent future requirements. Read [principles-and-patterns.md](references/principles-and-patterns.md) when choosing or rejecting principles/patterns, or refactoring a smell.

## Implement for a human reader

- Keep the main business flow visible. Prefer explicit state transitions, bounded responsibilities, and names that use the project's domain vocabulary.
- Keep related behavior and the data/invariants it protects together. Separate independent reasons to change; do not split every operation into a class.
- Hide volatile implementation details behind the smallest useful boundary. Validate and translate at boundaries; preserve useful types and errors internally.
- Minimize coupling through shared mutable state, control flags, concrete infrastructure, dependency cycles, and leaked internal representations. Parameters and return values should expose a comprehensible contract.
- Keep one authoritative expression of each shared business rule. Similar text with independently changing meaning may remain separate. Prefer a little duplication over a misleading generic API.
- Reuse established libraries/framework facilities before adding custom infrastructure. A new dependency must solve a current problem without disproportionate operational or compatibility cost.
- Follow configured formatting, import order, naming, language idioms, and error conventions. Avoid sweeping formatting churn. Comments explain intent, invariants, units, or surprising trade-offs; do not narrate obvious statements.
- Optimize demonstrated bottlenecks or explicit workload constraints. Choose sensible algorithms and avoid obvious waste, but do not claim performance gains from aesthetics or add caching/concurrency without its correctness costs.

When changing architecture, persistence, protocols, concurrency, security boundaries, or reliability behavior, read the relevant section of [architecture-data-and-quality.md](references/architecture-data-and-quality.md). Do not apply the whole systems checklist to a local utility.

## Review the diff as the next maintainer

Before completing an implementation, inspect the actual diff and follow the changed flow from its entry point through relevant side effects:

- Can a reader locate the behavior from the file/name, trace the ordinary path, and understand the contract without mentally expanding a chain of trivial wrappers?
- Are responsibilities cohesive and dependency direction intentional? Is any new layer, generic parameter, factory, manager, shared helper, configuration knob, or file unnecessary?
- Do names say what is stored/performed and expose important units/states? Is there one consistent way to express the same concept?
- Are failure, cancellation, cleanup, and partial state handled where applicable? Have public behavior, types, transaction boundaries, and ordering guarantees changed unintentionally?
- Would deletion or inlining preserve behavior and make understanding easier? If so, simplify now within scope. Do not hide remaining defects behind a polished summary.

Run the repository's relevant formatter/linter/type checks and meaningful tests appropriate to the affected contract. Test externally observable behavior, important boundaries, and failure cases rather than the internal class arrangement. Use existing checks where possible; do not build elaborate tests for a trivial reversible edit. Broad checks are warranted when affected scope or uncertainty requires them. Follow project-required checks.

Line counts, complexity metrics, coverage targets, class counts, and pattern counts are diagnostic signals, not proof of design quality. Do not split readable code merely to meet an arbitrary threshold, and do not use fewer files/lines as the sole definition of simplicity.

For a requested read-only review, report actionable findings with source locations, evidence, impact, and the smallest useful recommendation. Do not implement recommendations without authorization. Do not manufacture a finding just to name a principle.

## Report the result honestly

Summarize the behavior changed, significant design choices and why, completed validation, and material limitations. Distinguish measured performance from expected effects, automated evidence from real environment acceptance, and tests that passed from checks not run. Do not claim that applying the skill guarantees readability or prevents every design defect.

## Source scope

Derived from the user's Software Design 2026 materials: design fundamentals/qualities, SOLID/DRY/KISS/YAGNI, patterns, OOAD/UML, data design, architecture, and System Design foundations. The references turn course concepts into conditional decisions rather than copying lecture slogans. See [course-provenance.md](references/course-provenance.md) for source mapping and known corrections. No access to the original course folder is required to use this skill.
