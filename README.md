# ECHOES_OF_THE_GRID

## 1. Development Tech Stack

| Component                    | Technology            |
| :--------------------------- | :-------------------- |
| Game Engine                  | Godot 4.x             |
| Programming Language         | GDScript              |
| Unit and Integration Testing | GUT (Godot Unit Test) |
| Local Database               | SQLite                |
| Database Integration         | Godot SQLite Plugin   |
| Linter                       | gdlint                |
| Code Formatter               | gdformat              |
| Version Control              | Git                   |
| Repository Hosting           | GitHub                |
| CI/CD                        | GitHub Actions        |
| Git Hooks                    | pre-commit            |
| Large Asset Management       | Git LFS               |
| Project Management           | GitHub Projects       |
| Documentation                | Markdown              |
| Versioning                   | Semantic Versioning   |

All developers must use the agreed-upon versions of the game engine, plugins, and development dependencies to maintain compatibility across development environments.

## 2. Branching Strategy

| Branch        | Purpose                                     |
| :------------ | :------------------------------------------ |
| `main`        | Stable and release-ready versions           |
| `development` | Integration of completed features and fixes |
| `feature/*`   | New features and gameplay mechanics         |
| `fix/*`       | Bug fixes                                   |
| `refactor/*`  | Code restructuring and improvements         |
| `docs/*`      | Documentation updates                       |
| `test/*`      | Automated testing and test improvements     |
| `hotfix/*`    | Urgent fixes for stable releases            |
| `chore/*`     | Maintenance and configuration updates       |

### Branch Naming Convention

Branches must use lowercase letters and kebab-case for descriptive names.

**Examples:**

- `feature/storage-inspection`
- `feature/dialogue-system`
- `feature/sqlite-save-system`
- `fix/player-interaction`
- `refactor/scenario-validator`
- `test/entity-validation`
- `docs/development-guidelines`
- `chore/update-dependencies`

### Branching Workflow

- Feature, fix, refactor, documentation, test, and maintenance branches must originate from `development`.
- Completed branches must be merged into `development` through pull requests.
- Stable and tested versions of `development` must be merged into `main`.
- Hotfix branches must originate from `main` and be merged back into both `main` and `development`.
- Completed branches should be deleted after merging.

## 3. Branch Protection Rules

- No direct pushes to `main` and `development`.
- At least one approving reviewer per pull request.
- All required CI checks must pass before merging.
- All review conversations must be resolved.
- Force pushes must be disabled.
- Protected branches must not be deleted.
- Pull requests must be reviewed by someone other than the author.
- Squash merging is preferred for feature branches.

## 4. Commit Message Conventions

The project follows the Conventional Commits specification.

**Format:** `type(scope): description`

| Type       | Purpose                                       |
| :--------- | :-------------------------------------------- |
| `feat`     | New feature                                   |
| `fix`      | Bug fix                                       |
| `docs`     | Documentation                                 |
| `style`    | Code formatting without behavioral changes    |
| `refactor` | Code restructuring without behavioral changes |
| `perf`     | Performance improvement                       |
| `test`     | Adding or modifying tests                     |
| `build`    | Build configuration or dependencies           |
| `ci`       | CI/CD configuration                           |
| `chore`    | Repository maintenance                        |
| `revert`   | Reverting changes                             |

### Commit Message Rules

- Use lowercase for commit types and scopes.
- Use the imperative mood for descriptions.
- Keep descriptions concise and meaningful.
- Avoid vague messages such as `update`, `changes`, or `fixed stuff`.
- Each commit should represent a single logical change.
- Breaking changes must be explicitly identified.

### Examples

- `feat(player): implement interaction system`
- `feat(storage): add component inspection`
- `feat(database): implement local save system`
- `fix(dialogue): prevent overlapping dialogue`
- `test(validation): add entity classification tests`
- `refactor(player): separate movement and interaction`
- `ci(github): configure automated GUT testing`
- `chore(deps): update SQLite plugin`

## 5. Pull Request Guidelines

Every pull request must contain sufficient information for reviewers to understand and verify the proposed changes.

### Pull Request Requirements

- Clear and descriptive title following Conventional Commits.
- Summary of implemented changes.
- Reference to related GitHub issues, when applicable.
- Testing procedures and results.
- Screenshots or recordings for visual and gameplay changes, when applicable.
- Disclosure of known limitations or breaking changes.

Pull requests should remain focused on a single feature, fix, or technical task.

## 6. Linting and Formatting

| Tool            | Responsibility                                |
| :-------------- | :-------------------------------------------- |
| `gdlint`        | Detect code quality and convention violations |
| `gdformat`      | Maintain consistent code formatting           |
| Godot Parser    | Detect GDScript parsing errors                |
| `.editorconfig` | Standardize editor settings                   |
| `pre-commit`    | Run automated checks before committing        |

### Code Quality Rules

- All GDScript files must follow the project's linting configuration.
- Code must be formatted before committing.
- Linting and formatting checks must pass before merging.
- Unused variables, imports, and unnecessary code must be removed.
- Linting rules must not be disabled without justification.
- Third-party plugin code must be excluded from project-specific formatting and linting unless explicitly maintained by the team.
- Shared configurations must be committed to the repository.

## 7. GDScript Naming Conventions

| Element         | Convention         | Example                |
| :-------------- | :----------------- | :--------------------- |
| Classes         | PascalCase         | `ScenarioValidator`    |
| Variables       | snake_case         | `player_health`        |
| Functions       | snake_case         | `validate_component()` |
| Private Members | Leading Underscore | `_load_progress()`     |
| Constants       | UPPER_SNAKE_CASE   | `MAX_INVENTORY`        |
| Signals         | snake_case         | `inspection_completed` |
| Enums           | PascalCase         | `PlayerState`          |
| Enum Values     | UPPER_SNAKE_CASE   | `INTERACTING`          |
| Script Files    | snake_case         | `save_manager.gd`      |
| Scene Files     | snake_case         | `storage_room.tscn`    |
| Resource Files  | snake_case         | `component_data.tres`  |
| Nodes           | PascalCase         | `InteractionArea`      |
| Directories     | snake_case         | `save_system/`         |
| Test Files      | test\_ prefix      | `test_save_manager.gd` |

## 8. GDScript Coding Standards

- Prefer static typing for variables, parameters, and return values.
- Use descriptive and meaningful identifiers.
- Follow the single responsibility principle.
- Avoid unnecessary global variables and hardcoded values.
- Use constants for fixed configuration values.
- Prefer composition over inheritance.
- Use signals to reduce unnecessary dependencies between nodes and systems.
- Avoid unnecessary processing inside `_process()` and `_physics_process()`.
- Document complex logic and non-obvious implementation decisions.
- Remove temporary debugging statements before merging.
- Handle errors and unexpected game states appropriately.
- Keep functions and scripts focused on their intended responsibilities.

## 9. Project Architecture

The project follows a feature-based modular architecture to maintain separation of concerns, scalability, maintainability, and testability.

### Architectural Principles

| Principle                    | Application                                                  |
| :--------------------------- | :----------------------------------------------------------- |
| Separation of Concerns       | Separate gameplay, presentation, validation, and persistence |
| Single Responsibility        | Each module has a clearly defined responsibility             |
| Composition over Inheritance | Build reusable node-based components                         |
| Signal-Based Communication   | Reduce coupling between gameplay systems                     |
| Data-Driven Design           | Separate scenario content from implementation logic          |
| State Machines               | Manage player and gameplay states where appropriate          |
| Dependency Injection         | Improve modularity and testability                           |
| Repository Pattern           | Abstract SQLite persistence operations                       |

Educational validation logic must remain independent of scene presentation and player interaction logic to allow isolated automated testing.

Autoloads must be limited to systems that genuinely require global access or persistence across scenes.

## 10. Testing Strategy

The project uses GUT (Godot Unit Test) as its primary automated testing framework.

| Testing Type           | Scope                                                  | Method                    |
| :--------------------- | :----------------------------------------------------- | :------------------------ |
| Unit Testing           | Individual functions, validation rules, and game logic | GUT                       |
| Integration Testing    | Interactions between gameplay systems and persistence  | GUT                       |
| Scene Testing          | Node behavior, signals, and scene interactions         | GUT                       |
| Regression Testing     | Previously identified and resolved defects             | GUT / Manual              |
| Gameplay Testing       | Movement, exploration, and interactions                | Manual                    |
| Usability Testing      | Controls, navigation, and user experience              | Manual                    |
| Educational Validation | Scenario correctness and feedback accuracy             | Automated / Expert Review |
| Performance Testing    | Frame rate, memory usage, and loading times            | Godot Profiler            |
| Acceptance Testing     | Fulfillment of functional requirements                 | Manual                    |

### Testing Guidelines

- New gameplay logic should include relevant automated tests.
- Bug fixes should include regression tests where applicable.
- Tests must be independent and repeatable.
- Test cases must not modify actual player save data.
- Test fixtures must be separated from production data.
- Tests must cover valid inputs, invalid inputs, and relevant edge cases.
- All required automated tests must pass before merging.
- Visual and gameplay changes must undergo manual verification.

## 11. Continuous Integration and Continuous Delivery

The project uses GitHub Actions to automate code quality checks, testing, game builds, and release distribution.

### Continuous Integration

The CI pipeline must perform the following checks:

1. Development dependency installation.
2. GDScript linting using gdlint.
3. GDScript formatting verification using gdformat.
4. Godot headless project import and validation.
5. Automated unit and integration testing using GUT.
6. Commit or pull request title validation.

Failed required checks must prevent pull requests from being merged.

### Continuous Delivery

The CD pipeline is responsible for:

- Generating automated game builds.
- Exporting the game for supported platforms.
- Publishing build artifacts.
- Generating versioned releases.
- Maintaining release notes and changelogs.

### GitHub Actions Workflows

| Workflow          | Responsibility                                         |
| :---------------- | :----------------------------------------------------- |
| `ci.yml`          | Linting, formatting, validation, and automated testing |
| `build.yml`       | Automated game exports and build artifacts             |
| `release.yml`     | Versioned game releases                                |
| `commit-lint.yml` | Commit or pull request title validation                |

## 12. Local Database Management

SQLite is used for persistent local game data.

### Database Responsibilities

- Player profiles and save data.
- Gameplay progression.
- Scenario completion records.
- Player performance records, where required.
- Persistent game state.

### Database Guidelines

- Runtime databases must be stored within Godot's `user://` directory.
- Database operations must be separated from gameplay and presentation logic.
- Database schema changes must be managed through migrations.
- Parameterized queries must be used when handling dynamic values.
- Transactions must be used for related operations requiring atomicity.
- Database errors must be handled appropriately.
- Automated tests must use isolated test databases.
- Runtime save files must not be committed to the repository.
- Save compatibility and recovery must be considered when modifying the database schema.

## 13. Asset Management

Git LFS is used to manage large binary assets that are unsuitable for regular Git storage.

### Asset Guidelines

- Use consistent and descriptive file names.
- Organize assets according to their intended purpose.
- Avoid unnecessary duplicate assets.
- Optimize assets before integrating them into the game.
- Track large binary assets using Git LFS where appropriate.
- Maintain attribution and licensing information for third-party assets.
- Avoid committing temporary or unused assets.
- Coordinate modifications to shared scenes and binary assets to minimize merge conflicts.

### Version-Controlled Files

The following files must be tracked when applicable:

- GDScript files (`.gd`)
- Godot scenes (`.tscn`)
- Godot resources (`.tres`)
- Godot resource identifiers (`.uid`)
- Project configuration (`project.godot`)
- Export presets without sensitive credentials
- Database migration files
- Required game assets
- Automated tests

### Excluded Files

The following must not be committed:

- Godot-generated cache directories (`.godot/`)
- Temporary files
- Local save databases
- Exported game builds
- Python virtual environments
- Machine-specific configurations
- Credentials and sensitive information

## 14. Versioning Strategy

The project follows Semantic Versioning.

**Format:** `MAJOR.MINOR.PATCH`

| Version | Purpose                                                                            |
| :------ | :--------------------------------------------------------------------------------- |
| MAJOR   | Incompatible changes to established project interfaces or compatibility guarantees |
| MINOR   | Backward-compatible features                                                       |
| PATCH   | Backward-compatible bug fixes                                                      |

### Pre-release Versions

- `v0.1.0-alpha.1`
- `v0.5.0-beta.1`
- `v1.0.0-rc.1`

### Release Guidelines

- Development versions use `0.x.x` until the initial stable release.
- Stable releases must originate from `main`.
- Releases must be identified using Git tags.
- Significant changes must be recorded in `CHANGELOG.md`.
- Release builds must pass the required quality checks.

## 15. Project Management

GitHub Projects and GitHub Issues are used to manage development tasks, feature requests, bug reports, and project milestones.

### Task Workflow

1. Backlog
2. Ready
3. In Progress
4. In Review
5. QA / Testing
6. Done

### Issue Requirements

Each development task should include:

- Descriptive title.
- Task description.
- Acceptance criteria.
- Assigned developer.
- Relevant labels.
- Priority level.
- Associated milestone, when applicable.

## 16. Definition of Done

A development task is considered complete when:

- [ ] All acceptance criteria are satisfied.
- [ ] Implementation follows the project's architectural principles.
- [ ] Code follows GDScript naming and coding standards.
- [ ] Linting and formatting checks pass.
- [ ] Relevant automated tests are implemented and passing.
- [ ] Manual gameplay verification is completed, when applicable.
- [ ] No unintended regressions are introduced.
- [ ] Relevant documentation is updated.
- [ ] All required CI checks pass.
- [ ] Pull request is reviewed and approved.
- [ ] Changes are merged into the appropriate branch.
- [ ] The associated GitHub issue is updated.

## 17. Documentation Standards

Project documentation must be maintained throughout the development lifecycle.

| Document                   | Purpose                                       |
| :------------------------- | :-------------------------------------------- |
| `README.md`                | Technical overview and development guidelines |
| `CONTRIBUTING.md`          | Contribution procedures                       |
| `CHANGELOG.md`             | Version history and significant changes       |
| `docs/architecture.md`     | Technical architecture                        |
| `docs/testing-strategy.md` | Testing procedures and quality assurance      |
| `docs/database-design.md`  | Local database structure and persistence      |
| `docs/game-design.md`      | Gameplay mechanics and design specifications  |
| `docs/asset-guidelines.md` | Asset management and optimization             |
| `docs/adr/`                | Architecture Decision Records                 |

Documentation must be updated whenever significant changes are made to project architecture, development procedures, or system behavior.

## 18. Target Operating Systems and Export Platforms

Echoes of the Grid is developed as an offline desktop game targeting Windows and macOS.

| Operating System | Architecture | Development | Export |
| :--- | :--- | :--- | :--- |
| Windows | x86_64 | Supported | Supported |
| macOS | ARM64 (Apple Silicon) | Supported | Supported |
| macOS | x86_64 (Intel) | Subject to compatibility | Subject to compatibility |
| Linux | — | Not officially supported | Not supported |
| Android | — | Not supported | Not supported |
| iOS | — | Not supported | Not supported |
| Web | — | Not supported | Not supported |

### Platform Specifications

| Component | Specification |
| :--- | :--- |
| Application Type | Desktop Game |
| Connectivity | Offline |
| Input Method | Keyboard and Mouse |
| Local Persistence | SQLite |
| Windows Distribution | Executable (.exe) and required dependencies |
| macOS Distribution | Application Bundle (.app) |

### Cross-Platform Development Guidelines

- Use Godot's `res://` directory for project resources.
- Use Godot's `user://` directory for persistent local data.
- Avoid hardcoded absolute file paths.
- Maintain consistent file and directory capitalization.
- Ensure third-party plugins support the target operating systems and architectures.
- Use platform-independent development scripts where possible.
- Maintain consistent LF line endings across operating systems.
- Verify gameplay functionality and local persistence on both supported operating systems.
- Test exported builds before publishing releases.
- Mobile and browser-based platforms are outside the project scope.

## 19. Repository Structure

The project follows a hybrid feature-based directory structure that separates repository management, development tooling, documentation, and game implementation.

### Repository Root

```
ECHOES_OF_THE_GRID/
├── .github/
├── .vscode/
├── docs/
├── game/
├── tools/
├── .gitignore
├── .gitattributes
├── .editorconfig
├── .pre-commit-config.yaml
├── gdlintrc
├── requirements-dev.txt
├── CONTRIBUTING.md
├── CHANGELOG.md
└── README.md
```

| Directory / File | Responsibility |
| :--- | :--- |
| `.github/` | GitHub Actions workflows, issue templates, and pull request templates |
| `.vscode/` | Shared VS Code configurations and recommended extensions |
| `docs/` | Project documentation and architecture decisions |
| `game/` | Main Godot game project |
| `tools/` | Development and automation scripts |
| `.gitignore` | Files and directories excluded from version control |
| `.gitattributes` | Git file attributes, line endings, and Git LFS configuration |
| `.editorconfig` | Shared editor formatting standards |
| `.pre-commit-config.yaml` | Automated pre-commit checks |
| `gdlintrc` | GDScript linting configuration |
| `requirements-dev.txt` | Python-based development dependencies |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CHANGELOG.md` | Version history and significant changes |
| `README.md` | Main project overview |

### Godot Project Directory

```
game/
├── addons/
├── assets/
├── core/
├── features/
├── world/
├── ui/
├── resources/
├── database/
├── tests/
├── project.godot
├── export_presets.cfg
└── README.md
```

| Directory / File | Responsibility |
| :--- | :--- |
| `addons/` | Third-party Godot plugins and dependencies |
| `assets/` | Shared sprites, textures, audio, fonts, and shaders |
| `core/` | Shared infrastructure, utilities, persistence, and validation systems |
| `features/` | Individual gameplay mechanics and feature-specific components |
| `world/` | Physical environments, levels, rooms, and environmental objects |
| `ui/` | Shared user interface components, menus, and HUD |
| `resources/` | Shared structured game data and configuration resources |
| `database/` | SQLite schema definitions, migrations, and seed data |
| `tests/` | Automated tests and test fixtures |
| `project.godot` | Main Godot project configuration |
| `export_presets.cfg` | Game export configurations |
| `README.md` | Technical documentation and development guidelines |

### Directory Organization Guidelines

- Related scripts, scenes, and feature-specific resources must be grouped together.
- Shared assets must be stored within `assets/`.
- Reusable technical infrastructure must be stored within `core/`.
- Gameplay-specific implementations must be stored within `features/`.
- Physical environments and level layouts must be stored within `world/`.
- Shared user interface components must be stored within `ui/`.
- Educational validation logic must remain independent of visual presentation.
- Third-party plugins must remain within `addons/`.
- Automated tests must remain separate from production implementations.
- Runtime save databases must not be stored within the project directory.
- Directories must be introduced incrementally as development requirements arise.
- Godot-generated cache directories must not be committed to version control.

## 20. Linting and Formatting Configuration

The project uses gdlint, gdformat, and Godot's built-in static analyzer to maintain code consistency, readability, correctness, and maintainability.

### 20.1 Code Correctness Rules

| Rule | Enforcement Tool |
| :--- | :--- |
| No unused local variables | Godot Static Analyzer |
| No unused constants, where detectable | Godot Static Analyzer |
| No unused function parameters | gdlint / Godot Static Analyzer |
| No unused private members, where detectable | Godot Static Analyzer |
| No unreachable code | Godot Static Analyzer |
| No variable shadowing | Godot Static Analyzer |
| No unnecessary pass statements | gdlint |
| No duplicated resource loading | gdlint |
| No GDScript parsing errors | Godot Parser |
| Consistent naming conventions | gdlint |
| Unsafe type access detection | Godot Static Analyzer |
| Consistent code formatting | gdformat |

Intentionally unused variables or parameters may use a leading underscore where supported by the relevant analysis rules.

### 20.2 Code Maintainability Rules

| Rule | Limit / Standard |
| :--- | :--- |
| Maximum Line Length | 100 characters |
| Maximum Script Length | 500 lines |
| Maximum Public Methods | 20 per class |
| Maximum Function Parameters | 5 per function |
| Class Naming | PascalCase |
| Function Naming | snake_case |
| Variable Naming | snake_case |
| Constant Naming | UPPER_SNAKE_CASE |
| Signal Naming | snake_case |
| Private Member Naming | Leading underscore |

Exceptions to maintainability limits must be justified when necessary.

### 20.3 Formatting Rules

| Rule | Standard |
| :--- | :--- |
| Indentation | Tabs |
| Tab Width | 4 |
| Maximum Line Length | 100 characters |
| File Encoding | UTF-8 |
| Line Endings | LF |
| Final Newline | Required |
| Trailing Whitespace | Removed |
| String Quotation | Double quotes preferred |
| Operator Spacing | Standardized |
| Argument Spacing | Standardized |
| Blank Lines | Managed by gdformat |

### 20.4 Static Typing Guidelines

- Prefer typed function parameters.
- Prefer explicit function return types.
- Prefer typed member variables.
- Use type inference when the resulting type is clear.
- Avoid unnecessary use of Variant.
- Address unsafe type access where practical.
- Maintain type consistency throughout gameplay systems.
- Avoid unnecessary type casting.

### 20.5 Linting and Formatting Scope

Linting and formatting must apply to all project-maintained GDScript files, including automated tests.

The following directories and files must be excluded where applicable:

- Third-party plugins within `addons/`.
- Godot-generated cache directories.
- Generated files.
- Exported game builds.
- Temporary development files.
- External dependencies.

Third-party source code must not be automatically reformatted or modified by project-specific tooling.

### 20.6 Quality Enforcement

| Violation | Enforcement |
| :--- | :--- |
| GDScript Parsing Errors | Block Merge |
| Failed Automated Tests | Block Merge |
| Formatting Violations | Block Merge |
| Naming Convention Violations | Block Merge |
| Unused Local Variables | Block Merge where configured |
| Unused Constants | Block Merge where detectable and configured |
| Unused Function Parameters | Block Merge unless intentionally unused |
| Unreachable Code | Block Merge where configured |
| Maintainability Limit Violations | Block Merge unless justified |
| Unsafe Type Access | Warning |
| Missing Static Typing | Warning / Code Review |
| Performance Concerns | Code Review |
| Architectural Violations | Code Review |

### 20.7 Automated Quality Checks

| Development Stage | Quality Check |
| :--- | :--- |
| During Development | Editor diagnostics and Godot static analysis |
| Before Commit | Automated linting and formatting through pre-commit |
| During Pull Request | Linting, formatting verification, parsing validation, and automated testing |
| Before Merge | All required CI checks and code review requirements must pass |
| Before Release | Automated checks and platform-specific gameplay verification |

Local formatting tools may automatically correct formatting violations. Continuous integration must verify formatting without automatically modifying committed source code.

All developers must follow the same repository-level quality standards regardless of their preferred code editor.
