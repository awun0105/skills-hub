---
name: taskmaster
description: AI-driven task management system for software projects. Use when planning complex features, parsing PRDs, organizing tasks, breaking down subtasks, resolving dependencies, checking project status, or tracking development momentum.
allowed-tools: Bash(task-master:*)
license: MIT WITH Commons-Clause
compatibility: Requires task-master CLI (task-master-ai) or task-master-mcp.
metadata:
  author: eyaltoledano
  version: "0.43.1"
---

# Taskmaster AI Skill

Taskmaster AI provides intelligent task decomposition, dependency graphing, complexity analysis, and workflow automation.

## Quick CLI Reference

Run via shell or MCP tools:

```bash
# Initialize Taskmaster in current project
task-master init

# Configure AI model providers (Anthropic, OpenAI, Gemini, etc.)
task-master models --setup

# Parse a PRD or requirements document into tasks
task-master parse-prd --input=<path/to/prd.txt>

# List all tasks and statuses
task-master list
task-master list --status=pending
task-master list --status=in-progress

# View next actionable task (respecting dependencies)
task-master next

# View detailed task info
task-master show <id>

# Add a task
task-master add-task --prompt="Implement user profile page" --dependencies="1,2"

# Break down / expand a complex task into subtasks
task-master expand --id=<id> --num=5

# Update task status
task-master set-status --id=<id> --status=in-progress
task-master set-status --id=<id> --status=done
task-master set-status --id=<id> --status=review
task-master set-status --id=<id> --status=deferred

# Validate and repair task dependency graph
task-master validate-dependencies
task-master fix-dependencies

# Export tasks to README.md
task-master sync-readme --with-subtasks
```

## MCP Tools Integration

When running with MCP enabled (`task-master-mcp`), you can also access task tools directly:
- `initialize_project`: Initialize `.taskmaster/` configuration and files.
- `get_tasks`: Retrieve current tasks, subtasks, and their status.
- `add_task`: Add a new task with description, priority, and dependencies.
- `update_task`: Update task properties or status.
- `next_task`: Retrieve the next logical task to work on.
- `expand_task`: Decompose a task into actionable subtasks.
- `analyze_complexity`: Calculate complexity score and recommend breakdowns.
