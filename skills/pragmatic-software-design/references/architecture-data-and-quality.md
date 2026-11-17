# Architecture, data, and quality decisions

Read only the sections relevant to the requested change. These decisions extend the same principle: start with purpose and constraints, choose the simplest adequate design, and verify important behavior. Do not add a distributed systems checklist to a local bug fix.

## Requirements and traceability

Distinguish WHAT from HOW. Capture observable behavior, failure cases, constraints, and quality goals before selecting infrastructure. A requirement such as “reserve a seat without double booking” is different from a proposed mechanism such as “use Redis locking.” Validate the mechanism against the requirement.

For a substantial feature, trace requirements to implementation owners and meaningful verification. Use existing issue/spec/test artifacts; no traceability spreadsheet is required for a small change.

Use cases express an actor's goal and result of value, rather than a list of button clicks or isolated CRUD operations. Define system boundaries; an actor is an external role, not automatically a domain class. Where useful, specify the main flow, alternatives, trigger, relevant pre/postconditions, and invariants. Preconditions are states, not commands to execute another use case. A scenario is a path through flows and can guide behavioral tests.

During analysis, Boundary handles environment interaction, Control coordinates a use case, and Entity owns domain information/behavior. These roles help allocate responsibilities; they do not require three classes for every action. A controller should delegate coherent work rather than own every rule; an entity should not become a bag of data solely to satisfy a folder diagram.

## Representation and diagrams

Use a small diagram when it resolves ambiguity, not as a compulsory deliverable:

- Class diagram: types, responsibilities, multiplicities, association vs dependency, ownership/lifecycle.
- Sequence diagram: message order, calls, side effects, exceptional paths.
- Communication diagram: collaboration structure and links.
- Activity diagram: branching, guarded transitions, parallel branches and joins.
- Component/deployment view: runtime and deployment boundaries. A C4-style view can separate levels of detail when helpful.
- DFD: transformations and data movement. Data dictionary: definitions, types, units, valid ranges. Structure chart: call hierarchy, fan-in/fan-out, data/control parameters.

Keep diagram detail consistent with the question. Do not confuse data flow with control flow or a physical deployment boundary with a logical class dependency. Keep diagrams and code synchronized when diagrams are maintained artifacts.

## Architecture selection

| Situation | Consider | Cost or boundary to make explicit |
|---|---|---|
| Small cohesive application | Direct modules or modular monolith | Do not assume microservices are a prerequisite for growth |
| Clear presentation/business/persistence responsibilities | Layered design consistent with framework | Layer is logical; tier is deployment. Avoid pass-through layers with no purpose |
| Streaming transformations | Pipe-and-Filter | Backpressure, failure, ordering, data contract between stages |
| Scheduled whole-dataset processing | Batch sequential | Latency, restartability, partial output, resource budget |
| Shared central service/data | Client–Server | Failure points, capacity, protocol boundary |
| Independent reactions to an event | Event-driven/pub-sub | Schema ownership, ordering, duplication, replay, debugging, delivery guarantees |
| Independent service ownership/deployment is necessary | SOA or microservices | Network latency/failure, data ownership, distributed transactions, operational cost |
| Replaceable I/O or frameworks must stay outside core policy | Hexagonal/Onion/Clean boundaries | Ports serve real dependencies; no mandatory rings of empty wrappers |
| Read/write workloads or models need genuinely different handling | CQRS | Synchronization and consistency; separate databases/event sourcing are not mandatory |
| Decentralized peer resource sharing is required | P2P | Discovery, trust, coordination, replication; extra peers do not automatically solve every bottleneck |

Technical partitioning groups by technical role; domain partitioning groups by business responsibility. Choose for ownership and change locality. MVC/MVP/MVVM may fit a UI framework; do not create all three roles outside the framework's needs.

An event producer may be decoupled from specific consumers while remaining coupled to an event contract and broker. A layer need not always be strict/closed; honor the chosen design rather than asserting all architectures forbid skipping layers. Source-code dependency direction and runtime call direction can differ through interfaces.

## Persistence and domain mapping

Choose from access patterns, data relationships, invariants, transaction boundaries, size, retention, and operational constraints. SQL/NoSQL labels alone do not determine ACID, consistency, scalability, or performance. Avoid premature sharding or a second datastore without evidence.

Course class-to-table rules are mapping options rather than commands for every class:

- Persisted entity → table/document according to its lifecycle; value objects and transient coordinators need not each become tables.
- One-to-one → merge or constrain a FK according to optionality, ownership, access, and lifecycle.
- One-to-many → FK on the many side; many-to-many → junction relation, including attributes of that relationship.
- Inheritance → concrete tables, single table/discriminator, or common + subtype tables; compare duplication, nullable columns, joins, and integrity.
- Structured/multivalued attributes → coherent value representation or child records; preserve ordering/uniqueness if required.
- Categories → reference data when identity/metadata/change needs justify it; a stable small enum may suffice.
- Parameters → typed columns or key/type/value records according to actual extensibility; avoid a universal string-valued configuration system by default.

Use appropriate types, primary/unique/foreign/check constraints, and nullability to enforce invariants. Separate missing/unknown/not-applicable values deliberately. Normalize transactional data to avoid contradictory facts; denormalize when a measured access pattern or analytics model justifies maintenance cost. XML/semi-structured data can suit interchange or nested documents; relational integrity and joins solve different needs.

Indexes must serve actual filtering, joins, sorting, or uniqueness. Consider composite column order, selectivity, write cost, and execution plans. Foreign-key index creation varies by DBMS; do not assume the referencing columns are automatically indexed. Partitioning may be vertical or horizontal; distributed sharding adds routing, hotspots, rebalancing, and cross-shard constraints.

## External calls, concurrency, and reliability

For asynchronous or concurrent behavior, identify the invariant and its atomicity boundary. An in-memory check before a database write does not prevent races. Optimistic version checks and pessimistic locking can both enforce correctness when used appropriately; select using contention and transaction behavior, not “optimistic means inaccurate.” Understand isolation, lock scope/duration, deadlocks, and conflict handling.

Idempotency means repeating an identical request has the same intended effect as performing it once; response bodies/status may differ. For retriable effects, consider an atomic idempotency record/key scoped to the operation, conflict behavior for different payloads, and retention. Do not promise exactly-once external effects from an in-memory set or an ordinary queue.

For retried external side effects, preserve the logical operation identity and selected external target across retries when routing/configuration can change. Coordinate concurrent retries through a durable claim or the provider's documented atomic idempotency semantics; a unique local record alone does not prevent duplicate outbound calls. For example, do not reroute an unresolved charge to a different payment provider merely because tenant configuration changed.

For queue-based work, consider delivery/acknowledgment semantics, duplicate handling, ordering, bounded retries, poison messages, worker failure, backlog limits, and backpressure as needed. If a DB commit and event publication must be coordinated, evaluate the failure between them; choose an established transactional publication mechanism when the contract requires it. Distinguish competing consumers from fan-out subscribers.

For network calls, use explicit timeouts/deadlines and bounded retries where safe; backoff/jitter can reduce retry storms. Circuit breakers isolate persistent failures; bulkheads limit resource/failure propagation. Apply only when the relevant failure is real. Preserve cancellation and cleanup; log with sufficient context without leaking secrets.

Replication improves redundancy but is not a substitute for backups against corruption/deletion. Failover must consider detection time, replica lag, lost writes, and split-brain. Fault tolerance is relative to specified failures, not immunity to all failures. Define backup restoration and recovery goals when relevant.

CAP concerns consistency/availability during a partition, not a permanent menu of any two properties. Quorum intersection (`R + W > N`) is not by itself a complete proof of linearizability under concurrent writes, failures, or every replication protocol. Specify the system's actual guarantees rather than inferring them from a label.

## Performance and cache decisions

Separate latency, throughput, availability, reliability, and scalability. Use workload, dataset size, concurrency, latency percentiles, error rate, memory, and cost where relevant. Avoid unverified claims of “optimized” from a refactor alone. Select sensible data structures; remove repeated I/O or pathological complexity when evident. Benchmark proportionally and record environment/limits.

A cache needs ownership, key correctness, expiry/invalidation, freshness requirements, and a failure policy. Cache-aside, write-through, write-back, and refresh-ahead have different read/write and durability costs; write-back can lose unflushed writes. A cache is not free consistency or automatic speed. Consider client/CDN/proxy/application/database placement only as needed.

Load balancing routes traffic and supports horizontal scaling; L4/L7 choices depend on protocols and routing requirements. Account for health checks and the balancer's own availability. REST is an architectural style, RPC a communication model, and TCP/UDP transports; they are not mutually exclusive alternatives at the same layer. Choose protocol/serialization based on interoperability, behavior, workload, and actual constraints.

## Security, UX, and operation

Preserve applicable project security requirements even for small implementations. Validate input and authorize server-side at the relevant boundary; use parameterized queries and contextual output encoding rather than a generic “sanitize everything” function. Treat authentication, authorization, and transport protection as different responsibilities.

Use established identity/crypto facilities. Store password hashes using appropriate password-hashing algorithms and salts; do not invent cryptography. Session vs JWT depends on lifecycle/revocation and trust needs, not fashion. OAuth2 is authorization; identity commonly uses OIDC. Apply cookie Secure/HttpOnly/SameSite and CSRF protections according to the application's actual browser flow. CORS is not authentication or a server-to-server access control mechanism.

For UI behavior, preserve structure, simplicity, visibility, feedback, and tolerance for errors. Do not replace an important error with silent failure for a cleaner-looking flow. Naming, comments, and consistent layout reduce cognitive load; hidden dependencies and early technology commitments increase maintenance difficulty.

Instrument meaningful logs/metrics/traces when operational needs justify them. Monitoring detects known symptoms; observability helps investigate internal behavior through telemetry. A list of tools or three telemetry streams does not prove a system is diagnosable. Distinguish SLI (measurement), SLO (objective), and SLA (agreement). Define MTTR/MTBF precisely when used. At 99.999% time availability, a 365-day year permits about 315 seconds of downtime, not a few seconds.

## Quality feedback

Static checks establish syntax/style/type and some structural properties; runtime tests establish behavior under specified conditions. Both matter and neither replaces the other. Review and prototypes can expose misunderstanding before code grows.

Treat process maturity concepts (Initial, Repeatable, Defined, Managed, Optimizing) as motivation for repeatable checks and feedback, not a maturity certification to assign to a repository. Testability, explicit contracts, modularity, and reviewable changes make AI output easier to verify. No amount of design documentation replaces checking the actual diff and executing relevant verification.
