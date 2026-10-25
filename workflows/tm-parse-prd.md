---
description: "Parse a PRD document into tasks and dependencies"
---

Parse a PRD requirements document into tasks:
1. Identify the PRD path from arguments or find candidates (`PRD.md`, `docs/prd.md`, `specs/prd.txt`).
2. Run `task-master parse-prd --input=<path>`.
3. Display the breakdown of newly created tasks, priorities, and dependency hierarchy.
