# Structure, naming, and readability

Use this reference when placing code, defining names/contracts, starting a project, or repairing hard-to-follow AI output.

## Fit the repository before restructuring it

Choose placement by responsibility and ownership, then confirm how similar code is imported, tested, and built. A file belongs where a maintainer would look for that behavior, using the existing framework/subsystem conventions.

For an existing application, extend its established feature or layer. Do not introduce a feature-first island into an otherwise layered project without a concrete need, or reorganize the repository as part of a small fix. Avoid moving files solely to make the tree look symmetrical.

For a new application, start with its entry point and real behavior. Feature-based organization helps when features have different ownership and change independently; layer-based organization helps when a framework or small application has clear technical boundaries. A mixed organization can be appropriate when consistent and shallow. Decide from change locality and navigation, not fashion.

Example of a modest feature structure, only when these responsibilities exist:

```text
src/
  orders/
    create_order.py      # Use-case orchestration
    pricing.py           # Pricing rules used by order flows
    repository.py        # Actual persistence boundary/implementation
```

This is an illustration, not a scaffold. A small program may need one module. Do not create `domain/application/infrastructure/interfaces` in every feature by default. Tests belong in the repository's established test location. Dependencies between features should use deliberate public contracts rather than reaching into each other's private files.

`shared`, `common`, `core`, and `utils` are not destinations for code whose owner is unknown. Keep a helper near its first owner; move it when actual consumers share the same meaning, dependencies, and lifecycle. Name a shared module for the capability it provides, such as `currency` or `date_range`, instead of its generality.

Keep modules cohesive, and split when independent responsibilities, distinct dependency needs, or a genuine navigation burden justify it. A file per function/class and a large miscellaneous module are both possible failures. Avoid excessive package depth, redundant barrel re-exports, and filenames that repeat every ancestor's name unless local tooling requires them.

## Use a stable domain vocabulary

Use the terms in requirements and existing public contracts consistently. If an unfamiliar term is necessary, explain it once in the relevant API documentation. Do not create a glossary for a tiny change.

| Concern | Prefer | Avoid when ambiguous |
|---|---|---|
| Operation | `calculate_invoice_total`, `reserve_stock` | `process`, `handle_data`, `execute_logic` |
| Role | `InvoiceRepository`, `PaymentGateway` | `UniversalManager`, `BaseHelper`, `ProcessorV2` |
| Units | `timeout_ms`, `price_cents` | `timeout`, `value`, `amount` when units matter |
| Boolean | `is_expired`, `can_refund` | `flag`, `status` for a yes/no value |
| Collection | `orders`, `orders_by_id` | `data`, `items_map` without context |
| State | Existing domain enum/state type | Magic numbers or inconsistent strings |

These spellings illustrate semantics. Follow the language's and repository's casing and suffix conventions. Short names are fine in short scopes with conventional meaning. An intentionally generic collection algorithm may have generic names. Do not rename public APIs or serialized fields cosmetically without considering compatibility.

Names should expose what matters, not implementation trivia. A method that performs I/O should not masquerade as a pure getter. A monetary amount needs a currency/unit contract; a timestamp may need timezone semantics. Avoid names that embed an unmeasured claim such as `FastCache` or `OptimizedService`.

## Make the flow readable

Keep the successful business path easy to scan. Guard clauses can remove nesting; named helpers can expose a cohesive operation; a local expression can be clearer than a helper used once. Do not turn five understandable lines into five functions that force readers to jump files.

Example, preserving the project's error style:

```python
def reserve_stock(product, quantity):
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    if quantity > product.stock:
        raise InsufficientStock(product.id)
    product.stock -= quantity
```

This illustrates intent and invariant ownership, not a concurrency-safe inventory service. Concurrent persistence would require an atomic reservation/transaction at the real storage boundary. Do not imply an in-memory check proves distributed correctness.

Prefer explicit dependencies and state transitions to reflection, dynamic registries, clever metaprogramming, global service locators, and flags selecting unrelated behaviors. Use framework-supported dynamic mechanisms when they solve an actual requirement and are conventional in that framework.

A configuration object can clarify many related parameters; it can also hide a fat interface or create stamp coupling if only a tiny subset is needed. Pass a cohesive concept, not the entire application context.

Keep UI events, use-case orchestration, domain rules, and persistence from becoming entangled. Respect the actual scale: a simple screen need not have a presenter, controller, service, use-case class, repository interface, factory, and mapper for one operation.

## Refactor without hiding scope

For a large tangled module, identify the behavior and callers before extracting. Preserve behavior in small reviewable changes. Extract by independent responsibilities and dependency direction; do not just distribute the same coupling across more files. Keep intentional compatibility adapters when clients still use the old interface. A broad rename or directory migration deserves its own justified scope.

A reviewer should be able to explain: entry point → validation → business decision → side effects → result/error. If this needs an architecture lecture for a small feature, inspect the indirection.
