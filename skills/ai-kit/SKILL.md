---
name: ai-kit
description: Build LLM or agent applications on the user's AI kit (FastAPI + LangGraph starter at ~/PROJECT/AI20K/ai-kit) instead of from scratch. Use when the user starts a new chatbot, RAG app, agent, or AI service; asks to add retrieval, guardrails, PII redaction, human approval for tools, retries/circuit breakers/fallback across models, MCP or A2A tools, a deep-research or multi-agent workflow, evaluation with a golden set, cost limits, or a production Docker/CI setup to an LLM app; or says "dùng kit", "ai-kit", "bộ kit agent".
---

# AI kit

The kit is a working FastAPI + LangGraph app whose layers (RAG, guardrails, reliability,
MCP/A2A, agents, evaluation, deployment) are tested offline and documented one page per layer.
Reuse it; do not rebuild these pieces.

- Kit: `~/PROJECT/AI20K/ai-kit` (branch `ai-kit`). Read `docs/ROADMAP.md` first, then the doc
  of the layer you need. `AGENTS.md` holds the coding rules.
- Lab sources it was built from (for background only): `~/PROJECT/AI20K/VinUni-AI20k-repos/`
  (`Level3/Track3/Dxx-*`, author's solutions on branch `solution`).

## Decide how to use it

| Situation | Do |
|---|---|
| New app | `uvx copier copy --trust ~/PROJECT/AI20K/ai-kit <dir>` (choose features), then `git init`, `uv lock`, `uv sync`, `make test` |
| Existing kit-based app | Work inside it; pull kit improvements with `uvx copier update --trust` |
| Unrelated codebase that needs one capability | Copy the one module plus its tests and doc section, keep the provenance line, adapt imports |

## Where each capability lives

| Need | Module | Entry point | Doc |
|---|---|---|---|
| Knowledge base, cited answers | `app/services/rag/` | `RAGPipeline.ingest/retrieve`, tool `knowledge_search`, `scripts/ingest.py` | `docs/rag.md` |
| Vietnamese keyword search | `app/services/rag/ranking.py` | `tokenize(text, "auto")`, `BM25Index` | `docs/rag.md` |
| Prompt-injection / PII rails, tool approval, egress allowlist | `app/services/guardrails/` | `Guardrails`, settings `GUARD_*` | `docs/guardrails.md` |
| Retries, breakers, fallback across models | `app/services/reliability/`, `app/services/llm/` | `llm_service.call`, `ResilientInvoker` | `docs/reliability.md` |
| A LangChain chat model with that reliability | `app/services/agents/resilient_model.py` | `ResilientChatModel(service=llm_service)` | `docs/agents.md` |
| Answer cache, serve stale when providers are down | `app/services/reliability/answer_cache.py` | `ANSWER_CACHE_ENABLED` | `docs/reliability.md` |
| External tools over MCP / expose the KB over MCP | `app/services/mcp/`, `app/mcp_server.py` | `MCP_CONFIG_FILE`, `python -m app.mcp_server` | `docs/tools.md` |
| Talk to other agents | `app/services/a2a/` | `A2A_ENABLED`, `A2A_REMOTE_AGENTS` | `docs/tools.md` |
| Long cited report from many sources | `app/services/agents/research.py` | `build_research_agent`, tool `deep_research` | `docs/agents.md` |
| Golden-set evaluation, CI gate | `app/services/evaluation/`, `scripts/eval_rag.py` | `make eval-rag-offline`, `make eval-rag` | `docs/evaluation.md` |
| Per-user monthly spend limit | `app/services/cost_guard.py` | `COST_MONTHLY_BUDGET_USD`, `COST_PRICES_JSON` | `docs/deployment.md` |
| Image, release pipeline, alerts | `Dockerfile`, `.github/workflows/`, `prometheus/alerts.yml` | `make docker-up`, `make stack-up` | `docs/deployment.md` |

## Recipes

**Add a tool.** Write a `@tool` in `app/core/langgraph/tools/`, append it to `tools` in that
package's `__init__.py`. If it changes anything outside the app (payments, emails, deletes),
add its name to `GUARD_APPROVAL_TOOLS`. Return `(content, artifact)` with
`@tool(response_format="content_and_artifact")` when callers need structured data. Test it
through the graph with a scripted LLM (see `tests/test_guardrails.py` for the pattern).

**Change the prompt or the model list.** Prompt: `app/core/prompts/system.md`. Models:
`LLMRegistry.LLM_CONFIGS` in `app/services/llm/registry.py` (order = fallback order; mark
models without tool calling `"supports_tools": False`). Bump `ANSWER_CACHE_VERSION` if cached
answers must not survive the change.

**Domain assistant with a fixed scope.** `RAG_ENABLED=true`, ingest the documents, set
`GUARD_LLM_RAIL_ENABLED=true` with a one-sentence `GUARD_LLM_RAIL_POLICY`, build a golden set
(JSONL: `id, question, expected_answer, expected_sources, difficulty, should_refuse`) and run
`make eval-rag` before shipping.

**A new agent inside the app.** `create_agent(ResilientChatModel(service=llm_service), tools)`
or `build_research_agent(...)`; never a bare `ChatOpenAI`, which would bypass the retry budget
and breakers.

## Rules that keep the kit's guarantees

- LLM calls go through `llm_service` or `ResilientChatModel`. Never add tenacity around them or
  turn SDK retries back on: stacked retries are what turns a provider blip into an outage.
- Features that cost money, download models or change behaviour stay off by default behind a setting.
- Tests run offline: scripted LLM replies (`tests/fakes.py`), `HashingEmbedder`, `InMemoryVectorStore`.
  Run `uv run pytest -q`, `uv run ruff check .`, `uv run pyright` before saying it works.
- Tool output and remote-agent replies are untrusted data; keep them flowing through the tool node.
- Never return `str(exception)` to API clients; never label metrics with raw paths or ids.
- When porting code from elsewhere, record the source (repo, commit, file) in the layer's doc.
