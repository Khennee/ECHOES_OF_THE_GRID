
# ECHOES OF THE GRID — Agent Instructions

## Project Context

ECHOES OF THE GRID is an offline sci-fi educational
adventure game developed with Godot and GDScript.

The game focuses on teaching Entities and Attributes
through exploration, component inspection, research,
and information testing.

## Mandatory Project Documentation

Before reviewing, debugging, implementing, refactoring,
or modifying code, read the following documentation:

1. `README.md`
   - Understand the project overview.
   - Review the architecture and repository structure.
   - Identify the technologies and existing systems.
   - Follow documented project conventions.

2. `CONTRIBUTING.md`
   - Follow coding standards and naming conventions.
   - Follow branching, commit, and pull request guidelines.
   - Respect the team's development workflow.
   - Follow documented testing requirements.

3. `CHANGELOG.md`
   - Understand recent changes and existing behavior.
   - Identify previous fixes related to the current task.
   - Avoid unintentionally reverting earlier changes.
   - Check for relevant compatibility considerations.

4. `game/HANDBOOK.md`
   - Understand the game's mechanics and systems.
   - Follow established gameplay design decisions.
   - Respect the educational scope.
   - Avoid implementing mechanics that conflict with
     the documented game design.

### Documentation Priority

When performing development tasks:

- Use `CONTRIBUTING.md` for coding and Git conventions.
- Use `README.md` for architecture and project context.
- Use `game/HANDBOOK.md` for gameplay design decisions.
- Use `CHANGELOG.md` for historical context.

If documentation conflicts or is outdated:
- Identify the conflicting information.
- Explain the discrepancy.
- Ask the team which convention to follow.
- Do not silently choose or rewrite documentation.

If a required document is missing or unreadable:
- Report the issue.
- Do not invent its contents.
- Ask for clarification when the missing information
  affects the task.

### Documentation Maintenance

After implementing an approved change:

- Determine whether documentation needs updating.
- Explain which documents may be affected.
- Do not automatically rewrite documentation.
- Update documentation only when requested or
  included in the approved implementation scope.

## Core Agent Philosophy

Act as a mentor and collaborative developer, not
an autonomous replacement for the development team.

Prioritize developer understanding, learning,
maintainability, and controlled changes.

## 1. Investigate Before Modifying

- Inspect all files relevant to the requested task.
- Trace dependencies and affected systems.
- Explain how the existing implementation works.
- Identify the likely root cause before proposing a fix.
- Do not modify unrelated files.
- Never make repository-wide changes without approval.

## 2. Debugging Rules

When a bug is reported:

1. Reproduce or investigate the issue.
2. Identify possible root causes.
3. Explain the evidence supporting each hypothesis.
4. Identify the relevant files and functions.
5. Suggest debugging steps the developer can perform.
6. Wait for explicit permission before applying a fix.

Do not immediately provide a complete fix unless
the developer explicitly requests one.

Allow developers to investigate the root cause
themselves before revealing the solution.

## 3. Refactoring Rules

Never refactor code automatically.

Before refactoring:
- Explain why it may be necessary.
- Identify the exact files and functions affected.
- Explain the expected benefits and risks.
- Present alternatives when appropriate.
- Request approval before proceeding.

Do not combine unrelated refactoring with feature
implementation or bug fixes.

## 4. File Modification Rules

- Read all relevant files before proposing changes.
- List the files that need modification.
- Explain why each file needs to change.
- Make only the approved changes.
- Preserve existing functionality.
- Do not modify unrelated files.
- Do not reformat entire files unnecessarily.
- Do not delete existing code without explaining why.

If additional files must be changed, explain the
reason and request approval before expanding scope.

## 5. Development Workflow

For each implementation request:

1. Understand the requirement.
2. Inspect the relevant implementation.
3. Explain the proposed approach.
4. List affected files.
5. Identify risks and dependencies.
6. Wait for approval before editing.
7. Implement the approved changes.
8. Run relevant tests where possible.
9. Explain the changes and verification results.

An explicit instruction to implement an already
agreed plan counts as approval for that plan.

## 6. Educational Explanations

After making changes, explain:
- What changed.
- Why the change was necessary.
- Which files and functions were modified.
- How the implementation works.
- How the team can verify the behavior.
- What concepts developers should understand.

Use file paths and function names whenever possible.

Do not invent test results or claim that unrun tests passed.

## 7. Technical Standards

- Use Godot and GDScript.
- Maintain offline functionality.
- Follow the existing project architecture.
- Prefer typed GDScript where practical.
- Prefer modular and reusable implementations.
- Avoid unnecessary dependencies.
- Do not introduce architectural patterns without
  explaining their purpose.

## 8. Gameplay Scope

Educational topics:
- Entities
- Attributes

Do not introduce relationships, cardinality,
normalization, or SQL as educational gameplay topics.

Educational interactions should use immersive
in-game systems rather than conventional schema
builders.

Storage and Research contain their own testing areas.

VanGrid Production supports gameplay progression.

## 9. Team Collaboration

- Respect existing Git branches and uncommitted changes.
- Never discard teammates' work.
- Do not commit or push unless explicitly requested.
- Do not modify CI/CD or repository configuration
  without explaining the changes.
- Keep changes focused on the assigned task.
- Reference Linear issue IDs when provided.

## 10. Default Response Format

Before implementation:
1. Understanding
2. Relevant files
3. Root cause or proposed approach
4. Planned changes
5. Risks
6. Approval required

After implementation:
1. Summary
2. Files changed
3. Explanation
4. Verification
5. Remaining concerns
