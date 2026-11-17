# Course provenance and interpretation

This skill was authored from the user's local Software Design collection, reviewed on 2026-11-17 in `/home/lqaq/Downloads/SD 2026`. Original materials remain in that folder; they are not bundled or required at runtime. This file records intellectual source mapping, not a prerequisite to open private course files.

## Mapping

| Skill decisions | Course source |
|---|---|
| Fitness for purpose, WHAT/HOW, partitioning, abstraction, modularity, coupling/cohesion, top-down/bottom-up, DFD/dictionary/structure chart, UI/coding, AI testability/contracts | `INTRODUCTION TO SOFTWARE DESIGN.pdf`, 57 pages; VN version, 57 pages |
| Static/dynamic evaluation, quality attributes, information hiding, hidden dependencies, viscosity, simplicity, review/prototyping, maturity/feedback | `DESIGN QUALITIES.pdf`, 37 pages; VN version, 36 pages |
| Conditional SOLID/DRY/KISS/YAGNI, smells, refactoring, metric caveats | `Software Design Principles.pdf` and `[Presenter view] - Software Design Principles.pdf`, 70 pages each |
| Patterns, trade-offs, classification, notification example | `[Presenter view] - Design Patterns.pdf`, 31 pages; Session 4 PPTX |
| Requirements, use cases, RUP flows/scenarios, OO relationships, Boundary/Control/Entity, interaction diagrams | `Slides/s-01a-Overview.pptx`, `s-01b-OOPReview.pptx`, `s-02-UsecaseModel.pptx`, supplemental, `s-03-StaticAnalysis.pptx`, `s-04-DynamicAnalysis.pptx`, including speaker notes |
| Class/table mapping, relational/XML, normalization, indexing, partitioning | `Slides/s-05-DataDesign.pptx` and `s-05-DataDesign_2.pptx` |
| Architecture styles, trade-offs, layers/tiers, ports/adapters, CQRS, dependency direction | `[Presenter view] - Software Architecture.pdf`, 40 pages; `Slides/Session 5/System Architecture.pptx`; `Slides/s-06-SoftwareArchitecture.pptx` |
| Distributed systems, persistence, replication, cache, queues, networking, locking/idempotency, resilience, security, observability | `Software Design _ Nguyen The Huy.pdf`, 94 pages, under the extracted course's Books directory |
| Topic scope | `Slides/d-00- Software Design Course.pptx`, `Slides/Syllabus_English_TBU.pdf`, Session 1–6 PPTX |

Read all extracted PDF text/PPTX text and notes; OCR both image-only VN PDFs; inspect key diagrams and image-based pages. Full native PPTX rendering/animation was not available. Some exported PDF code blocks are empty. Missing examples were supplemented from the instructor's [Principles HTML](https://nndkhoa.github.io/software-design-docs/D02/slides-en.html) and [Patterns HTML](https://nndkhoa.github.io/software-design-docs/D04/dp.html). The Session 6 D06 link returned HTTP 404 at review time. Linked external books/sites were not all read recursively.

## Deliberate adaptations

The skill operationalizes the course rather than reproducing every sentence. It does not preserve exam administration, grading, lecturer biography, tool brand lists, or slogans as coding rules. The compact GoF guide supplements the course's classification with trigger/cost reasoning; it does not claim the local PDF teaches all 23 implementations in detail.

In particular, the skill rejects universal line limits, coverage thresholds as quality proof, automatic interface-per-class designs, unconditional microservices/Clean Architecture, and the notion that every conditional violates OCP. Architecture and testing guidance is conditional on real scope and contracts.

Known technical qualifications carried into the skill:

- [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2): HTTP idempotency concerns intended effect; repeated responses need not be identical.
- [PostgreSQL foreign-key documentation](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK): declaring a FK does not automatically index the referencing columns. Check the chosen DBMS.
- The ebook's “few seconds/year” at 99.999% is corrected by arithmetic to about 315 seconds/year (365 days).
- Preserve Usability (ease of use) vs Availability (readiness) despite an ambiguous Vietnamese translation in the slides.
- CAP, quorum, optimistic locking, SQL/NoSQL, and protocol performance require explicit assumptions; lecture simplifications are not universal guarantees.

Use current official language/framework/provider documentation when implementation details need verification. Do not make live web access mandatory for applying the general design workflow.
