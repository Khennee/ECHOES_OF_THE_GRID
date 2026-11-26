
---
name: godot-feature-development
description: Plan and implement Godot and GDScript gameplay features with architecture explanations, affected-file analysis, developer approval, and verification.
---

# Godot Feature Development

## Before Implementation

1. Understand the gameplay requirement.
2. Inspect relevant scenes, scripts, and resources.
3. Identify existing reusable components.
4. Propose the implementation approach.
5. List affected files and explain each change.
6. Request approval before editing.

## Implementation

- Follow existing architecture.
- Prefer typed GDScript.
- Avoid unnecessary scene dependencies.
- Keep gameplay logic separate from presentation
  where practical.
- Avoid unrelated refactoring.
- Do not add dependencies without approval.
- Preserve offline functionality.

## Verification

- Check affected scene references.
- Check scripts for syntax and type errors.
- Run available Godot validation or tests.
- Report what could not be tested.

## Developer Explanation

After implementation, explain:
- Scene and script responsibilities.
- Important signals and function calls.
- How data flows through the feature.
- Why the chosen approach was used.
- How the team can test the feature.
