# Choosing principles and patterns

Use this reference to diagnose a smell or choose a design. Begin with behavior and causes of change. A principle is a lens; a pattern is an optional response to a particular force. Neither is a checklist of objects to create.

## Principle decisions

| Principle | Concrete signal | Proportionate response | Misapplication to avoid |
|---|---|---|---|
| SRP | Unrelated stakeholders/rules change one component independently | Separate those responsibilities; leave cohesive calculations together | One class per verb; anemic objects with all behavior in managers |
| OCP | A supported axis of behavior varies and repeatedly changes stable policy | Put a stable contract at that axis; supply implementations | Never editing old code; polymorphism for every small switch |
| LSP | A subtype changes promised preconditions, postconditions, errors, invariants, or behavior | Preserve substitutability or model separate concepts/composition | Declaring inheritance correct because the real-world nouns have an is-a relation |
| ISP | A consumer depends on capabilities it cannot use or implement meaningfully | Expose a client-oriented capability boundary | An interface per method regardless of clients |
| DIP | Business policy is tied to volatile infrastructure or hard-to-control side effects | Depend on a policy-owned boundary; inject an adapter/function when useful | Wrapping stable language/library operations in interfaces; requiring a DI container |
| DRY | The same business rule must change atomically in several places | Give that knowledge one owner | Merging coincidentally similar code with different meanings |
| KISS | Layers/branches/configuration add more reasoning than benefit | Simplify the design while retaining required constraints | Fewest lines at the expense of clarity, errors, or correctness |
| YAGNI | Work is justified only by an unrequested hypothetical future | Defer unused feature/extension mechanism; keep current code easy to change | Omitting explicit security, correctness, or quality requirements |

An interface with one implementation can be appropriate for an external service, substitution in tests, or independent ownership. Conversely, three occurrences of similar code can still represent three different rules. Neither implementation count nor the Rule of Three replaces reasoning.

Coupling is about dependencies between components, not merely imports. Shared mutable state, access to another module's internals, and control flags commanding unrelated branches are useful warning signs. Cohesion is about responsibilities serving one purpose, not merely functions sharing the same data object.

Course taxonomy for recognition: coupling from no direct/data toward stamp/control/external/common/content; cohesion from functional/sequential/communicational toward procedural/temporal/logical/coincidental. Use these to explain actual consequences rather than assign a universal score. A cohesive DTO or an external API dependency is not inherently a defect.

## Pattern selection

Choose **no named pattern** when a direct function, conditional, plain object, or established framework facility expresses the current requirement well. Do not add a pattern just to label a principle. A pattern may help several principles and can also worsen coupling or readability if misused.

The following compact GoF decision guide supports recognition; it is not a requirement to implement the full catalog.

| Pattern | Trigger that may justify it | Simpler option / main cost |
|---|---|---|
| Factory Method | Construction must vary at a real subclass/framework extension point | Constructor or plain factory function; avoid a hierarchy just for `new` |
| Abstract Factory | Clients need compatible families of related objects | Explicit construction; adds several contracts |
| Builder | Complex staged construction has meaningful optional parts/invariants | Named/default arguments or validated config; avoid for a two-field object |
| Prototype | Clone configured objects with clearly defined copy semantics | Constructor; shared mutable internals make cloning hazardous |
| Singleton | One instance/lifecycle must actually be enforced | Explicit application-scoped instance; global access hurts isolation and concurrency reasoning |
| Adapter | Existing incompatible API must fit a required contract | Small conversion at boundary; do not wrap every dependency |
| Bridge | Two independent dimensions must evolve without subclass multiplication | Composition first; extra indirection needs real independent variation |
| Composite | Clients genuinely treat leaves and nested groups uniformly | Plain tree/loop; do not force leaf-only operations on groups |
| Decorator | Behaviors compose around the same contract in supported combinations | Direct call/framework middleware; ordering becomes significant |
| Facade | Repeated clients need a small coherent view over a complex subsystem | Call a few functions directly; avoid a god facade |
| Flyweight | Measured memory cost is dominated by shareable immutable state | Ordinary objects; split intrinsic/extrinsic state carefully |
| Proxy | Access requires real lazy loading, remote access, or access control semantics | Direct dependency; avoid concealing I/O/failure behind local-looking calls |
| Strategy | Interchangeable algorithms must be selected or supplied | Function/callback or small conditional; no mandatory class hierarchy |
| Observer | Multiple independent reactions subscribe to a changing subject | Explicit calls; subscription lifetime, ordering, and failure become contracts |
| Command | Operations must be queued, replayed, audited, or undone as values | Ordinary function call; define undo/idempotency explicitly |
| State | State-dependent transitions/actions cause tangled branching | Enum + transition function; use objects when behavior complexity merits them |
| Template Method | Stable algorithm skeleton with supported inheritance hooks | Composition/function parameters; fragile base-class coupling |
| Chain of Responsibility | Ordered handlers can independently accept/pass work | Clear pipeline/loop; define stop conditions and no-handler behavior |
| Iterator | A custom collection needs controlled traversal without leaking representation | Built-in iteration/generator; do not reimplement standard facilities |
| Mediator | Many-to-many collaboration needs a coherent coordinator | Explicit orchestration; mediator can become a god object |
| Memento | Snapshot/restore must preserve encapsulation | Immutable state/versioning; storage size and sensitive data matter |
| Visitor | Many operations over a stable element hierarchy justify double dispatch | Methods/pattern matching; adding element types becomes expensive |
| Interpreter | A small stable language has a real grammar and evaluation semantics | Simple parser or established library; avoid a homegrown language unnecessarily |

## Applying a pattern without overbuilding

For a notification requirement:

- One email on registration: call the existing email boundary; no strategy registry or event bus is implied.
- One of several runtime-selected delivery methods: a function table or Strategy may suffice.
- Several independent subscribers react to registration: Observer/pub-sub may help if subscription and decoupling have value.
- Reliable asynchronous delivery: a local Observer does not provide persistence or delivery guarantees. Address transactions, retries, duplicate handling, and monitoring at the actual infrastructure boundary if required.

For a payment requirement, a small fixed set of stable cases may be clearest as a conditional. An explicitly extensible payment-provider integration can justify a narrow PaymentGateway contract. Changing composition/registration code to wire a new provider is compatible with protecting stable business policy from provider-specific changes.

For Rectangle/Square, reason about the actual mutable setter contract. Do not generalize the lecture example into a prohibition on every square/rectangle relationship. An immutable geometry model can have different substitutability constraints.

## Smell diagnosis

Tie each recommendation to a concrete cost and smallest useful change:

- God class → unrelated reasons to change → extract actual responsibilities, not every method.
- Long method → mixed concerns or hard-to-follow logic → simplify or extract cohesive operations; length alone is insufficient.
- Duplicate code → shared knowledge drifting → unify the rule only if semantics/lifecycle match.
- Fat interface → unused/unsupported client obligations → split capabilities by consumers.
- Deep if/else → tangled policy/variation/state → first simplify conditions; consider Strategy/State only when the variation merits it.
- Tight coupling → brittle side effects or representation leaks → isolate the volatile boundary rather than abstracting everything.
- Dead/unused machinery → no current consumer → remove when compatible and in scope; public extension points need compatibility analysis.

Do not force all principles simultaneously if the result is harder to understand or fails the user's constraints.
