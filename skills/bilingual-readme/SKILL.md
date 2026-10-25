---
name: bilingual-readme
description: Write or rewrite a repository README in English and Vietnamese (and, for larger projects, a docs/ set in both languages) from the Best-Readme-Template structure (awun0105/Best-Readme-Template) — overview, features, components, architecture, repository structure, requirements, getting started, documentation, contributing, security, license. Use when the user asks to write, rewrite, restructure or translate a README or project docs, wants a bilingual (EN + VI) README, or says the README is hard to read or badly organised.
---

# Bilingual README (English + Vietnamese)

Fills the templates from [awun0105/Best-Readme-Template](https://github.com/awun0105/Best-Readme-Template) with facts from the codebase, in English and Vietnamese. The templates are bundled in `templates/`:

| File | Use |
|---|---|
| `templates/README_TEMPLATE.md` | English README |
| `templates/README_VN_TEMPLATE.md` | Vietnamese README (same sections, Vietnamese headings) |
| `templates/docs/` | Larger projects: `docs/README.md` (map), `docs/EN/*` and `docs/VN/*` — overview, architecture, data flow, configuration, local development, operations, deployment setup, backup and restore |

`sync-templates.sh` refreshes `templates/` from the GitHub repo (run it when the user says the templates changed). `check_readme.py` checks the result.

**Vietnamese text follows the `vietnamese-writing` skill** (clear, natural, full sentences, no personal pronouns). Load it before writing the Vietnamese files.

## 1. Decide the shape

- **File names.** Default, as in the template repo: `README.md` in English and `README_VN.md` in Vietnamese, each linking to the other on the line under the title (`[Tiếng Việt: README_VN.md](README_VN.md)` / `[English: README.md](README.md)`). If the repo already has a convention (e.g. `README.md` in Vietnamese + `README.en.md`) or the user named a primary language, follow that instead and keep the existing file names so links elsewhere don't break.
- **Size.**
  - Small or medium project (a library, CLI, app without separate services): README only.
  - Large project (several services, deployment, configuration files, data pipelines, operations): README plus the `docs/` suite. Create only the docs pages that have real content; remove links to pages that don't exist (the Vietnamese docs map lists `api.md`, `scripts.md`, `evaluation.md` — keep them only if written).

## 2. Gather the facts (never invent)

Read before writing:
- Manifests and versions: `package.json`, `pyproject.toml`, `requirements*.txt`, `Cargo.toml`, `go.mod`, `.nvmrc`, `Dockerfile`, `docker-compose*.yml`.
- How it runs: scripts in the manifest, `Makefile`, entry points, CLI `--help`, `.env.example`, CI workflows (they show the real install / test commands).
- What it is: existing README and docs, `AGENTS.md` / `CLAUDE.md`, top-level folders, examples, screenshots and assets, `LICENSE`, the git remote (for clone URLs and badges).

Rules:
- Every command must exist (in a manifest, Makefile or the CLI). Run quick, safe ones (`--help`, `--version`, the test command if fast) to confirm.
- Versions, ports, paths and file names come from the code, not from memory.
- Badges only for real facts (license file present, language version from the manifest, CI workflow present).
- No invented features, numbers, contact details or roadmap. If a fact isn't available, drop the line or section instead of leaving a placeholder.

## 3. Fill the templates

1. Copy the template(s) into the repo with the final file names.
2. Write the **English** README from the facts:
   - Sections marked **[MANDATORY]** are filled. Sections marked **[OPTIONAL]** stay only if the project has something real for them (no screenshots → no Screenshots section; no hardware needs → no hardware table).
   - Keep the template's order. Keep `<a id="top"></a>` at the top and the "Back to Top" link at the end.
   - Replace every `[bracketed]` text; delete the *italic instruction notes*, the `**[MANDATORY]**` / `**[OPTIONAL]**` markers and the HTML comment blocks (the agent protocol at the top included).
   - Update the Table of Contents to the sections that remain.
   - Getting Started is a numbered path a newcomer can follow from a clean machine to a running result, with real commands, and ends with how to check it worked.
   - Repository Structure lists the real top-level folders and files that matter, one line each.
   - Icon-free: no emoji in headings or lists (the templates are designed without icons).
   - Plain, direct English; short paragraphs; one idea per sentence.
3. Write the **Vietnamese** README with the same sections, facts and commands, using the Vietnamese template's headings. Write it in natural Vietnamese following `vietnamese-writing` — do not translate the English sentence by sentence. Keep commands, code, paths and product names unchanged; Vietnamese anchors in the Table of Contents keep their diacritics (`#hướng-dẫn-bắt-đầu`).
4. If the user wants a banner or the repo has a logo, use the template's logo slot (centred under the title). The `repo-banner` skill makes one.
5. For the docs suite: same process per page, EN and VN; `docs/README.md` links only to pages that exist; each page ends with its "Back to" link.

## 4. Check before handing over

```bash
python3 ~/.agents/skills/bilingual-readme/check_readme.py README.md README_VN.md docs/
python3 ~/.agents/skills/vietnamese-writing/check_pronouns.py README_VN.md docs/VN/
```

- `check_readme.py` reports leftover placeholders and markers, instruction blocks, italic notes, broken `#anchors` (GitHub slug rules), links to missing files, emoji in headings, and EN/VN files with a different number of sections. Items marked "?" can be intentional (e.g. `[topic]` inside a sample prompt) — look at each.
- `check_pronouns.py` lists personal pronouns in the Vietnamese text; rewrite each one.
- Read both READMEs top to bottom once as a newcomer: does each section answer its question (what is it, how is it built, what do I need, how do I run it, how do I change it, what are the rules)? Do the two languages say the same things?
- If the repo is on GitHub and pushed, confirm the rendered page (`gh api repos/<owner>/<repo>/readme -H "Accept: application/vnd.github.html"`) shows the images and every TOC link resolves.

## 5. Report

Tell the user which files were written, which optional sections were dropped and why (one line), and anything that needs their input (e.g. no LICENSE file, so the License section says the project is unlicensed — suggest adding one).
