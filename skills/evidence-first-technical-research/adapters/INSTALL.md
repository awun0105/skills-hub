# Install and reuse across agents

This folder is a portable instruction bundle. It does not, by itself, grant a model web access, repository read permission, independent execution, or protection from every hallucination. Agents must actually read `SKILL.md` and perform the evidence checks; a prompt alone cannot guarantee correctness.

## ChatGPT

Upload the packaged `skill.zip` via a supported Skills installation flow. If your ChatGPT client cannot install custom skills, keep `SKILL.md` as a file and explicitly ask the assistant to read/apply it. Installation procedures and availability vary by product and workspace.

## Agent platforms supporting SKILL.md

Place the entire `evidence-first-technical-research/` directory in the platform's documented skills directory. Common conventions include:

- Codex-style project skills: `.agents/skills/evidence-first-technical-research/`
- Claude Code-style project skills: `.claude/skills/evidence-first-technical-research/`

These are examples, not guarantees across all versions. Consult your agent's current skill discovery documentation. Ask the agent to show that it actually loaded `SKILL.md` and to use a fresh source pass.

## Generic coding agents / repositories

1. Put the folder somewhere stable, e.g. `./evidence-first-technical-research/`.
2. Copy `adapters/AGENTS.md` to the project root if the agent reads `AGENTS.md`, or copy `adapters/CLAUDE.md` to root for tools that honor that file. Edit paths so they point at the actual folder.
3. For Cursor, adapt `adapters/cursor-evidence-first.mdc` to the project's `.cursor/rules/` path and ensure it refers to the actual skill directory. Rule selection may depend on each client; when in doubt explicitly invoke it.
4. For other agents, paste the appropriate adapter into their project instructions and include a link/path to `SKILL.md`.
5. Keep the entire folder; do not copy only the adapter. Supporting references and scripts provide the actual checks.

## Use it as a cold-start remedy for long or contaminated chats

In a **new conversation or agent session**, provide the skill and `assets/session-handoff.template.md` filled with source IDs, not just earlier assistant conclusions. Example request:

> Apply evidence-first-technical-research in cold-read mode. Treat previous assistant statements as hypotheses. Independently verify the pivotal claims from primary papers and the pinned official code. Correct any conflicts and label unverified items. Teach only Lesson 6 after the audit.

A fresh context can reduce anchoring but does not establish the truth of a handoff. Verify pivotal evidence again.

## Example requests

- "Teach 3DGS SH colors from first principles. Research original paper and inspect code first. Cite equation/function locators and give one numeric example."
- "Audit this implementation against the paper; pin a commit and separate paper-method, actual-code, and my inference."
- "Research latest 3DGS optimization methods through [cutoff date]. Do not rank techniques with incompatible protocols."
- "Previous explanation may be hallucinated. Cold-read it and create a corrections table based on reinspection of primary sources."

## Local optional audit

Run:

```bash
python scripts/audit_claims.py assets/claim-ledger.template.json
python scripts/test_audit_claims.py
```

The template intentionally contains an `UNVERIFIED` example and a placeholder revision. A schema pass confirms *format only*, not factual verification. Create a new ledger for real work and never quote the template as proof.

## Updated mode: Evidence-Based Technical Tutor

The bundled instructions now support both stand-alone technical verification **and** complete learning workflows:

1. **Plan:** Use `references/curriculum-design.md` to build a lesson prerequisite graph. Save an instance based on `assets/curriculum.template.json`.
2. **Teach:** For each requested lesson, use `references/lesson-production.md` and `assets/lesson-brief.template.md`; inspect fresh primary evidence, verify calculations, show one checked worked example, and ask targeted questions.
3. **Assess:** Evaluate the actual learner answer or artifact, then update an instance based on `assets/learner-state.template.json` using `references/assessment-progress.md`. Lesson delivered != proficiency demonstrated.
4. **Audit:** If a previously taught claim is challenged, reopen evidence, issue correction and mark affected dependencies for review. Follow `references/longitudinal-audit.md`.
5. **Resume across agents:** Pass curriculum, learner state, claim ledger, and `assets/curriculum-handoff.template.md`. New agents must verify pivotal sources anew.

Suggested invocation:

> Design a first-principles technical curriculum about [topic] through [target competency]. Apply evidence-first-technical-research. Make prerequisites and assessments explicit. Teach only one lesson per reply, verify paper/math/source code before each lesson, clearly flag simplifications and uncertainties, and track observed mastery separately from delivered lessons. If previous responses may be wrong, use cold-read and fix downstream dependencies.

Run local structural checks from the installed skill folder:

```bash
python scripts/audit_curriculum.py assets/curriculum.template.json --state assets/learner-state.template.json
python scripts/test_audit_curriculum.py
python scripts/test_audit_claims.py
```

These structural scripts never verify paper accuracy, user learning, or source inspection. A passing test does not certify research truth.
