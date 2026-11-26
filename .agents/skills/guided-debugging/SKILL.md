
---
name: guided-debugging
description: Help developers investigate bugs, errors, crashes, and unexpected behavior through guided debugging. Prioritize hints and root-cause analysis over immediate fixes.
---

# Guided Debugging

## Purpose

Help the developer discover and understand the
root cause of a problem independently.

## Workflow

1. Read the error report and relevant code.
2. Trace the affected execution path.
3. Identify possible causes.
4. Explain how to reproduce the issue.
5. Give the developer an investigation plan.

## Hint Levels

### Level 1 — Direction
Identify the subsystem or behavior worth checking.

### Level 2 — Investigation
Identify relevant files, functions, and variables.

### Level 3 — Root Cause
Explain the likely root cause with evidence.

### Level 4 — Solution
Provide a proposed fix only when requested.

## Rules

- Do not edit files during investigation.
- Do not immediately reveal the full solution.
- Do not assume the first hypothesis is correct.
- Explain how to confirm or reject each hypothesis.
- Ask permission before applying a fix.
- When requested, explain the fix line by line.
