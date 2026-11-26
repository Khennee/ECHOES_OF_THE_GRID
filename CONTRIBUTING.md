# Contributing to Echoes of the Grid

## 1. Introduction

This document establishes the contribution workflow for Echoes of the Grid. All contributors are expected to follow these guidelines to maintain code quality, project consistency, traceability, and effective team collaboration.

Before contributing, developers must familiarize themselves with:

- [Development Standards](README.md)
- [Developer Handbook](game/HANDBOOK.md)

## 2. Development Environment

Contributors must configure their development environment according to the project's documented requirements.

The officially supported development platforms are Windows and macOS.

After installing the required system dependencies and cloning the repository, execute:

```bash
task setup
task doctor
```

Contributors may use either Visual Studio Code or the Godot script editor. All contributions must satisfy the same automated quality standards regardless of the editor used.

## 3. Branching Strategy

The repository follows a structured branching strategy.

| Branch | Purpose |
|---|---|
| `main` | Stable and approved releases. |
| `development` | Integration of approved development contributions. |
| `feature/*` | New gameplay features and functionality. |
| `fix/*` | Bug fixes. |
| `refactor/*` | Internal code improvements. |
| `docs/*` | Documentation changes. |
| `test/*` | Automated testing improvements. |
| `chore/*` | Maintenance and development tooling. |
| `hotfix/*` | Urgent fixes to stable releases. |

Direct pushes to protected branches are prohibited.

Regular development branches must originate from `development`. Hotfix branches may originate from `main` when addressing an urgent release issue.

Branch names must use lowercase kebab-case and clearly describe their purpose.

Examples:

```text
feature/player-movement
feature/storage-inventory
feature/research-interaction
fix/incorrect-attribute-validation
refactor/database-service
test/entity-validation
docs/gameplay-mechanics
chore/update-development-tools
```

## 4. Issue Management

Development work should be associated with a GitHub issue or an assigned project task.

Before starting implementation:

1. Review the assigned issue and its acceptance criteria.
2. Confirm the expected functionality and scope.
3. Assign yourself to the issue when appropriate.
4. Update the corresponding GitHub Project status.
5. Create the appropriate development branch.

Contributors should avoid implementing unrelated changes within the same issue or pull request.

## 5. Development Workflow

### 5.1 Synchronize the Development Branch

```bash
git switch development
git pull --ff-only origin development
```

### 5.2 Create a Development Branch

```bash
git switch -c feature/player-movement
```

### 5.3 Begin Development

```bash
task dev
```

Implement the assigned functionality while following the project's architecture, coding conventions, and testing standards.

### 5.4 Validate Changes

Stage the intended changes:

```bash
git add -A
```

Review staged changes to ensure unrelated files are not included.

Execute the formatter:

```bash
task format
```

If formatting modifies files, review and stage the changes again.

```bash
git add -A
task format:check
task check
```

Additional commands may be executed when necessary:

```bash
task lint
task analyze
task test
```

All applicable quality checks must pass before submitting a contribution.

### 5.5 Commit Changes

```bash
git commit -m "feat: implement player movement"
```

### 5.6 Push the Development Branch

```bash
git push -u origin feature/player-movement
```

### 5.7 Submit a Pull Request

Create a pull request targeting `development`, complete the pull request template, and request a review from another contributor.

## 6. Commit Message Standards

The project follows the Conventional Commits specification.

Commit messages must follow this structure:

```text
<type>(<optional-scope>): <description>
```

Supported commit types include:

| Type | Purpose |
|---|---|
| `feat` | Introduce new functionality. |
| `fix` | Correct an existing defect. |
| `docs` | Update documentation. |
| `style` | Apply formatting-only changes. |
| `refactor` | Restructure code without changing intended behavior. |
| `perf` | Improve performance. |
| `test` | Add or modify tests. |
| `build` | Modify build configurations or dependencies. |
| `ci` | Modify continuous integration workflows. |
| `chore` | Perform maintenance tasks. |
| `revert` | Revert a previous commit. |

Examples:

```text
feat(storage): implement component inspection
feat(research): add information discovery interaction
fix(validation): correct entity classification feedback
test(database): verify transaction rollback
refactor(core): reorganize scene management
docs: update developer handbook
ci: improve desktop build verification
```

Commits should be focused, descriptive, and logically grouped.

Generic commit messages such as `update`, `changes`, `final`, and `fixed stuff` are not acceptable.

Commit messages are automatically validated through local Git hooks and GitHub Actions.

## 7. Pull Request Requirements

Every pull request must:

- Have a clear and descriptive title.
- Identify the purpose and scope of the changes.
- Reference the relevant GitHub issue when applicable.
- Describe significant implementation decisions.
- Include testing and verification information.
- Identify known limitations or incomplete functionality.
- Include screenshots or recordings for relevant visual changes.
- Pass all required automated checks.
- Receive the required independent reviewer approval.
- Resolve outstanding review conversations before merging.

Pull requests should remain reasonably scoped to simplify review and reduce integration risks.

Draft pull requests may be used when implementation is incomplete or early feedback is required.

## 8. Code Review

Code reviews are intended to maintain quality, identify defects, improve maintainability, and encourage shared understanding of the codebase.

Reviewers should evaluate:

- Correctness and expected behavior.
- Compliance with project requirements.
- Architectural consistency.
- Code readability and maintainability.
- Naming and formatting conventions.
- Error handling.
- Automated test coverage.
- Potential regressions.
- Performance implications.
- Security and data integrity concerns.

Review feedback must remain constructive, specific, and professional.

Contributors must address requested changes before merging.

Authors must not approve their own pull requests. Approval requirements and merge restrictions are enforced through the configured repository rulesets.

## 9. Continuous Integration

GitHub Actions performs automated validation across Windows, macOS, and Linux environments.

Linux is used for continuous integration validation and is not an officially supported game distribution platform.

Automated checks include:

- Repository file validation.
- GDScript formatting.
- GDScript linting.
- Godot project import.
- Godot static analysis.
- GUT automated testing.
- Conventional Commit validation.

Desktop build workflows generate Windows and macOS application artifacts.

A successful automated build does not replace manual gameplay testing or distribution verification.

Contributors must investigate and resolve failed checks associated with their changes.

## 10. Testing Requirements

New functionality should include appropriate automated tests whenever practical.

Testing should cover:

- Expected behavior.
- Invalid inputs.
- Boundary conditions.
- Relevant failure scenarios.
- Regression prevention.

Tests must be organized within the appropriate directories:

```text
game/tests/
├── unit/
├── integration/
├── fixtures/
└── helpers/
```

Execute automated tests using:

```bash
task test
```

Gameplay interactions, visual presentation, audio, navigation, and other behavior that cannot be adequately validated through automated tests must undergo manual verification.

## 11. Godot Development Guidelines

Contributors must follow the established project directory structure and feature-based architecture.

Project-authored GDScript files must be maintained as external `.gd` files rather than embedded scripts inside scenes.

When creating scripts through Godot, the Built-in Script option must remain disabled.

Godot resource files and their associated metadata must be committed when required.

Scene and resource renaming should preferably be performed through the Godot editor to preserve resource references.

Contributors must coordinate before simultaneously modifying shared scenes or resources that may produce difficult merge conflicts.

Third-party addon modifications must be intentional, documented, and reviewed.

## 12. Database Contributions

Database-related functionality must follow the project's SQLite architecture.

Contributors must:

- Use parameterized queries when handling dynamic values.
- Avoid hardcoded machine-specific database paths.
- Maintain database integrity.
- Use migrations for production schema changes.
- Include appropriate integration tests.
- Keep test databases isolated from production player data.

Runtime player databases must not be committed to the repository.

## 13. Asset Management

Game assets must be stored in their appropriate project directories.

Large binary assets must follow the project's Git LFS configuration.

Contributors must ensure that externally obtained assets have appropriate usage permissions and licensing.

Generated builds, temporary files, local caches, personal editor settings, and unnecessary binary files must not be committed.

Third-party licenses and attribution requirements must be preserved.

## 14. Merge Conflict Resolution

Contributors are responsible for resolving merge conflicts associated with their development branches.

To synchronize a development branch:

```bash
git fetch origin
git rebase origin/development
```

Resolve conflicts carefully, preserving the intended behavior of both contributions.

After resolving conflicts:

```bash
git add <resolved-files>
git rebase --continue
```

Run the quality checks again:

```bash
task check
```

If an already-published personal development branch has been rebased, use:

```bash
git push --force-with-lease
```

Force pushing must never be performed against protected branches. Contributors must coordinate before rewriting the history of a shared development branch.

## 15. Contribution Traceability

All contributors must use their own GitHub accounts and correctly configured Git identities.

Verify the configured identity:

```bash
git config user.name
git config user.email
```

The configured email address should be associated with the contributor's GitHub account.

Contributions should remain traceable through:

- Individual commits.
- GitHub issues.
- Assigned project tasks.
- Pull requests.
- Code reviews.
- Automated test contributions.
- Documentation improvements.

Contribution records support project accountability and academic evaluation.

Artificially splitting commits, misrepresenting authorship, or submitting another contributor's work under an incorrect identity is prohibited.

## 16. Security and Repository Privacy

The repository is publicly accessible for project transparency and academic evaluation.

Contributors must never commit:

- Passwords.
- API keys.
- Authentication credentials.
- Personal or confidential information.
- Private configuration files.
- Restricted third-party assets.
- Sensitive research participant data.

Public repository visibility does not automatically grant permission to reuse or redistribute project-owned content.

Potential security issues involving sensitive information should be reported privately to the project team rather than disclosed through a public issue.

## 17. Definition of Done

A development task is considered complete when:

- The assigned requirements and acceptance criteria are satisfied.
- The implementation follows project development standards.
- Relevant automated and manual tests have been completed.
- All required quality checks pass.
- Relevant documentation has been updated.
- Known limitations have been documented.
- The associated pull request has been reviewed and approved.
- The contribution has been merged into the appropriate target branch.
- The corresponding GitHub issue or project task has been updated.

## 18. Team Responsibilities

All contributors are responsible for maintaining the quality, reliability, and consistency of the project.

Contributors are expected to communicate implementation concerns, report defects, participate in code reviews, respect assigned responsibilities, and maintain accurate documentation throughout the development lifecycle.
