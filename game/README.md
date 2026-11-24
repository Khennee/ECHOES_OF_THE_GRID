# ECHOES OF THE GRID — Developer Handbook

This document serves as the practical development handbook for Echoes of the Grid. It contains environment setup instructions, development commands, testing procedures, Git workflows, and troubleshooting guidelines.

For development policies, coding standards, architectural conventions, branching strategies, and contribution requirements, refer to the [Development Standards](../README.md).

---

## 1. Prerequisites

Before contributing to the project, ensure that the following tools are installed.

| Tool | Version | Purpose |
|---|---|---|
| Godot Engine | 4.7.2 Stable | Game development |
| Python | 3.12.x | Development tooling |
| Git | Recent stable version | Version control |
| Git LFS | Recent stable version | Large asset management |
| gdtoolkit | 4.5.0 | GDScript linting and formatting |
| pre-commit | 4.7.0 | Automated Git hooks |
| Visual Studio Code | Optional | External code editor |
| GUT | Pending | Automated testing |
| Godot SQLite | Pending | Local database management |
| Task | Pending | Development command automation |

### Supported platforms

- Windows — x86_64
- macOS — Apple Silicon
- macOS Intel support is subject to dependency compatibility verification.

Mobile platforms are not supported.

Python is required only for development tooling and is not a runtime dependency of the distributed game.

---

## 2. Repository Setup

Clone the repository using its GitHub repository URL.

```bash
git clone <repository-url>
cd ECHOES_OF_THE_GRID
```

Initialize Git LFS:

```bash
git lfs install
git lfs pull
```

Switch to the development branch:

```bash
git switch development
git pull origin development
```

Unless otherwise specified, all terminal commands in this handbook must be executed from the repository root, not from the `game/` directory.

---

## 3. Python Development Environment

The project uses a Python virtual environment to isolate development dependencies.

### 3.1 macOS

Install Python 3.12 using Homebrew if necessary:

```bash
brew install python@3.12
```

Create the virtual environment:

```bash
python3.12 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### 3.2 Windows

Install Python 3.12 from the official Python website.

Create the virtual environment:

```powershell
py -3.12 -m venv .venv
```

Activate the virtual environment using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 3.3 Install development dependencies

After activating the virtual environment:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### 3.4 Verify installation

```bash
python --version
python -m pip --version
gdlint --version
gdformat --version
pre-commit --version
```

### 3.5 Deactivate the environment

```bash
deactivate
```

The `.venv/` directory must not be committed to the repository.

Developers must reactivate the virtual environment when opening a new terminal session if it is not automatically activated.

---

## 4. Godot Editor Setup

1. Launch Godot Project Manager.
2. Select Import.
3. Navigate to the repository's `game/` directory.
4. Select `project.godot`.
5. Open the project.

The Godot project root is `game/`, represented internally by `res://`.

The Git repository root is `ECHOES_OF_THE_GRID/`.

These directories serve different purposes and must not be confused.

### Renderer

The project uses the Compatibility renderer.

Do not change the renderer without discussing the change with the development team.

### Running scenes

| Action | Shortcut |
|---|---|
| Run project | F5 |
| Run current scene | F6 |
| Stop running project | F8 |

On some keyboards, the Fn key may be required.

Running the entire project requires a configured main scene.

---

## 5. Visual Studio Code Setup

Visual Studio Code is optional. Developers may use Godot's built-in script editor.

Open the entire repository in Visual Studio Code:

```bash
code .
```

Do not open only the `game/` directory when working with repository-level development tools.

### Recommended extensions

- Godot Tools
- EditorConfig for VS Code
- GitHub Actions
- Conventional Commits
- GitLens

Workspace extension recommendations are provided in `.vscode/extensions.json`.

Shared editor settings are provided in `.vscode/settings.json`.

### External editor integration

Inside Godot, navigate to:

Editor > Editor Settings > Text Editor > External

Enable Use External Editor.

Set the executable path to the locally installed Visual Studio Code executable.

For macOS, the executable path can be located using:

```bash
which code
```

Set Exec Flags to:

```text
--reuse-window --goto "{file}:{line}:{col}"
```

This instructs Visual Studio Code to reuse its last active window instead of opening a separate Godot project workspace.

Keep the repository workspace active when using this configuration.

### Godot executable configuration

Configure the Godot Tools extension with the local Godot executable path.

Example for macOS:

```json
{
  "godotTools.editorPath.godot4": "/Applications/Godot.app/Contents/MacOS/Godot"
}
```

Windows developers must use their own Godot executable path.

Machine-specific executable paths must be configured in personal editor settings and must not be committed to shared workspace settings.

---

## 6. GDScript Linting

The project uses gdlint to enforce GDScript coding standards.

The shared configuration is located in `gdlintrc` at the repository root.

### Lint the game

```bash
gdlint game/
```

### Lint a specific script

```bash
gdlint game/path/to/script.gd
```

### Expected successful output

```text
Success: no problems found
```

The linter checks naming conventions, function argument limits, file length, line length, unused arguments, whitespace, class definition ordering, and other maintainability rules.

Third-party addons and generated directories are excluded from project linting.

Developers must resolve linting violations before committing changes.

---

## 7. GDScript Formatting

The project uses gdformat to maintain consistent GDScript formatting.

The configured maximum line length is 100 characters.

### Format a specific script

```bash
gdformat --line-length 100 game/path/to/script.gd
```

### Check formatting without modifying files

```bash
gdformat --check --line-length 100 game/path/to/script.gd
```

### Format multiple scripts

```bash
gdformat --line-length 100 game/core game/features
```

Only supply directories that exist and contain project-owned scripts.

Do not run recursive formatting against third-party addons.

The pre-commit formatter automatically formats eligible GDScript files while excluding third-party addons and generated directories.

If formatting modifies a staged file, review and stage the corrected file before attempting another commit.

---

## 8. Godot Static Analysis

Godot provides engine-level static analysis in addition to gdlint.

The shared warning configuration is stored in `game/project.godot`.

The following warnings are currently configured as errors:

- Unassigned variables
- Unused variables
- Unused local constants
- Unused parameters
- Shadowed variables
- Shadowed global identifiers
- Unreachable code
- Unreachable patterns

Developers must resolve script errors before submitting changes.

### Checking diagnostics

1. Open the Godot project.
2. Open the affected GDScript file.
3. Review the script editor diagnostics.
4. If using Visual Studio Code, review the Problems panel while connected to Godot's language server.

### Headless project validation

The following command can be used as an initial project import and parsing check on macOS:

```bash
/Applications/Godot.app/Contents/MacOS/Godot \
  --headless --path game --editor --import
```

Windows developers must substitute their local Godot executable path.

Review the terminal output for script errors. A successful import alone does not guarantee that every script or gameplay feature has been validated.

Comprehensive automated static analysis and CI enforcement are pending.

---

## 9. Pre-commit Hooks

The project uses pre-commit to automatically enforce development standards before commits are created.

The shared configuration is located in `.pre-commit-config.yaml`.

### 9.1 Install Git hooks

After installing development dependencies:

```bash
pre-commit validate-config .pre-commit-config.yaml
pre-commit install
pre-commit install-hooks
```

Both the pre-commit and commit-msg hooks will be installed.

Every developer must complete this setup after cloning the repository.

### 9.2 Run all checks manually

```bash
pre-commit run --all-files
```

Newly created files must be staged before they are included in an all-files check.

### 9.3 Run checks against staged files

```bash
pre-commit run
```

### 9.4 Run checks against a specific file

```bash
pre-commit run --files game/path/to/script.gd
```

### 9.5 Run individual hooks

Run the GDScript linter:

```bash
pre-commit run gdlint --all-files
```

Run the GDScript formatter:

```bash
pre-commit run gdformat --all-files
```

### 9.6 Configured hooks

| Hook | Purpose |
|---|---|
| trailing-whitespace | Removes unnecessary trailing whitespace |
| end-of-file-fixer | Ensures proper file endings |
| check-yaml | Validates YAML syntax |
| check-json | Validates JSON syntax |
| check-merge-conflict | Detects unresolved merge markers |
| check-case-conflict | Detects conflicting filename capitalization |
| check-added-large-files | Checks newly added non-LFS files against the configured size limit |
| gdformat | Automatically formats GDScript |
| gdlint | Enforces GDScript coding standards |
| conventional-pre-commit | Validates commit message formatting |

### 9.7 Handling failed hooks

If a hook reports that files were modified, this means automatic corrections were applied.

Review the changes:

```bash
git diff
```

Stage the corrected files:

```bash
git add <corrected-file>
```

Run the checks again:

```bash
pre-commit run --all-files
```

If a hook reports a coding violation, manually resolve the violation before retrying.

Do not bypass hooks using `--no-verify` during normal development.

### 9.8 Verify hook installation

macOS:

```bash
ls -la .git/hooks/pre-commit
ls -la .git/hooks/commit-msg
ls -la .git/hooks/pre-push
```

Windows PowerShell:

```powershell
Get-ChildItem .git/hooks/
```

The pre-push hook is used by Git LFS.

---

## 10. Daily Development Workflow

### 10.1 Before starting development

Synchronize the development branch:

```bash
git switch development
git pull origin development
```

Ensure that existing local changes have been committed or safely stored before switching branches.

Create a feature branch:

```bash
git switch -c feature/player-movement
```

Other branch examples:

```text
feature/storage-system
fix/entity-validation
refactor/inventory-manager
docs/developer-handbook
test/entity-validator
chore/project-initialization
```

Refer to the root Development Standards for the complete branching policy.

### 10.2 During development

Developers should:

1. Implement the assigned feature or task.
2. Follow the established directory structure.
3. Follow GDScript naming and coding conventions.
4. Test the affected functionality in Godot.
5. Resolve script errors and warnings.
6. Write or update relevant automated tests when applicable.
7. Update documentation when necessary.

### 10.3 Before committing

Review the working tree:

```bash
git status
git diff
```

Lint the game:

```bash
gdlint game/
```

Format affected GDScript files:

```bash
gdformat --line-length 100 game/path/to/script.gd
```

Run relevant automated tests once the testing framework is configured.

Stage the intended changes:

```bash
git add <file-or-directory>
```

Review staged changes:

```bash
git diff --cached
```

Run pre-commit checks:

```bash
pre-commit run
```

If automatic corrections are applied, review and stage the corrected files again.

### 10.4 Create a commit

```bash
git commit -m "feat: implement player movement"
```

Git automatically executes the installed pre-commit and commit-msg hooks.

### 10.5 Push changes

For the first push of a new branch:

```bash
git push -u origin feature/player-movement
```

For subsequent pushes:

```bash
git push
```

Create a pull request targeting the development branch according to the repository's contribution policies.

---

## 11. Conventional Commits

All commit messages must follow the Conventional Commits specification.

### Format

```text
<type>(optional-scope): <description>
```

### Examples

```text
feat: implement player movement
feat(storage): add component inspection
fix: resolve incorrect entity validation
refactor: simplify inventory manager
docs: update developer handbook
test: add entity validation tests
chore: configure pre-commit hooks
style: format GDScript files
perf: optimize inventory loading
ci: configure automated testing
build: update export configuration
```

### Invalid examples

```text
updated files
fixed bugs
changes
final update
asdf
```

Invalid commit messages are rejected by the commit-msg hook.

---

## 12. Automated Testing

**Status: Pending configuration**

The project will use GUT (Godot Unit Testing) for automated GDScript testing.

The planned directory structure is:

```text
game/tests/
├── unit/
├── integration/
├── fixtures/
└── helpers/
```

Testing documentation will include:

- Running tests through Godot.
- Running tests through the terminal.
- Writing unit tests.
- Writing integration tests.
- Test fixtures and helpers.
- Headless test execution.
- Automated testing through GitHub Actions.

Developers must continue manually testing affected functionality until the automated testing framework is configured.

---

## 13. Database Management

The project uses Godot SQLite version 4.9 for local database persistence.

SQLite is an embedded relational database engine that does not require a separate database server, internet connection, or database credentials.

### 13.1 Database dependency

The Godot SQLite addon is included in:

```text
game/addons/godot-sqlite/
```

Developers do not need to manually download or reinstall the addon after cloning the repository.

The project maintains a desktop-only distribution of the addon.

| Platform | Architecture | Purpose |
|---|---|---|
| Windows | x86_64 | Game development and distribution |
| macOS | ARM64 and x86_64 | Game development and distribution, subject to runtime verification |
| Linux | x86_64 | Continuous integration and headless testing |

Android, iOS, and Web binaries have been removed because these platforms are outside the project's supported distribution scope.

The original addon license must be retained.

### 13.2 Database directory structure

```text
game/database/
├── migrations/
├── seeds/
└── services/
```

| Directory | Responsibility |
|---|---|
| migrations/ | Version-controlled SQL schema changes |
| seeds/ | Initial and reference data |
| services/ | Database connection and persistence services |

### 13.3 Runtime database storage

Runtime databases must be stored using Godot's `user://` storage location.

Proposed production database path:

```text
user://echoes_of_the_grid.db
```

The production database schema and initialization service are pending gameplay implementation.

Runtime databases and player save data must not be committed to the repository.

### 13.4 Opening an in-memory database

```gdscript
var database: SQLite = SQLite.new()
database.path = ":memory:"

if database.open_db():
	database.query("SELECT 1 AS result;")
	print(database.query_result)
	database.close_db()
```

In-memory databases are recommended for isolated database testing.

### 13.5 Parameterized queries

Use parameter binding when passing dynamic values into SQL queries.

```gdscript
database.query_with_bindings(
	"INSERT INTO components (id, name) VALUES (?, ?);",
	[1, "Core"]
)
```

Do not construct SQL queries by directly concatenating untrusted input.

The components table shown above is an illustrative example and is not part of the production database schema.

### 13.6 Database integration tests

Database integration tests are located in:

```text
game/tests/integration/database/
├── test_sqlite_connection.gd
├── test_sqlite_operations.gd
└── test_sqlite_persistence.gd
```

The database test suite covers:

- SQLite GDExtension registration.
- Database connection.
- SQL query execution.
- Record insertion.
- Record retrieval.
- Record modification.
- Record deletion.
- Parameter binding.
- Transaction commit.
- Transaction rollback.
- File-based persistence.

Database tests must use isolated in-memory databases or dedicated temporary database files.

Tests must never modify production save data.

### 13.7 Run database integration tests

Execute from the repository root.

macOS:

```bash
/Applications/Godot.app/Contents/MacOS/Godot \
  --headless \
  --path game \
  -s addons/gut/gut_cmdln.gd \
  -gdir=res://tests/integration/database \
  -ginclude_subdirs \
  -gexit
```

Windows PowerShell:

```powershell
& "C:\path\to\Godot.exe" --headless --path game -s addons/gut/gut_cmdln.gd -gdir=res://tests/integration/database -ginclude_subdirs -gexit
```

Replace the executable path with the actual Godot installation path.

Alternatively, execute the standard GUT command documented in Section 12 to run the entire automated test suite.

### 13.8 Updating Godot SQLite

When upgrading the SQLite addon:

1. Review Godot version compatibility.
2. Verify Windows, macOS, and Linux binary availability.
3. Preserve the original addon license.
4. Remove unsupported Android, iOS, and Web binaries.
5. Update the GDExtension configuration accordingly.
6. Run all database integration tests.
7. Verify supported platform compatibility.
8. Update the dependency version in this handbook.
9. Submit the changes through a pull request.

Do not upgrade native dependencies without verifying their compatibility.

### 13.9 Database migration commands

Migration execution, database initialization, seed execution, and development database reset commands will be documented after the production database service is implemented.

## 14. Git LFS and Asset Management

Git LFS is used to manage selected large binary assets.

Tracking rules are defined in `.gitattributes`.

### Initialize Git LFS

```bash
git lfs install
```

### Download LFS assets

```bash
git lfs pull
```

### View configured tracking patterns

```bash
git lfs track
```

### View tracked LFS files

```bash
git lfs ls-files
```

### Check LFS status

```bash
git lfs status
```

### Check whether an asset uses Git LFS

```bash
git check-attr filter -- path/to/asset
```

Do not modify shared LFS tracking patterns without consulting the development team.

---

## 15. Building and Exporting

**Status: Pending configuration**

The project will support desktop exports for Windows and macOS.

The planned export workflow includes:

- Windows x86_64 exports.
- macOS Apple Silicon exports.
- macOS Intel compatibility evaluation.
- Export preset configuration.
- Automated build generation.
- GitHub Actions build artifacts.

Generated builds and export credentials must not be committed to the repository.

Build commands will be documented after export presets and platform dependencies have been verified.

---

## 16. Automated Development Commands

**Status: Pending configuration**

A Taskfile-based development command system is planned to simplify environment setup and common development operations.

Proposed commands:

```bash
task setup
task dev
task lint
task format
task format:check
task test
task check
task build:windows
task build:macos
```

These commands are not yet available.

Until the Taskfile is implemented, use the manual commands documented in this handbook.

---

## 17. Troubleshooting

### 17.1 Command not found: gdlint, gdformat, or pre-commit

The Python virtual environment may not be active.

macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If the commands remain unavailable, reinstall the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

### 17.2 Virtual environment activation fails

Ensure that the directory is named `.venv`, not `venv`.

If the environment does not exist, create it using the instructions in Section 3.

### 17.3 Pre-commit configuration file not found

Ensure that `.pre-commit-config.yaml` exists at the repository root.

Run:

```bash
pre-commit validate-config .pre-commit-config.yaml
```

Then reinstall the hooks if necessary:

```bash
pre-commit install
pre-commit install-hooks
```

### 17.4 Pre-commit reports files were modified

This is expected when automatic formatting or file correction occurs.

Review the changes, stage the corrected files, and rerun the checks.

### 17.5 Commit message rejected

Ensure that the commit message follows Conventional Commits formatting.

Example:

```bash
git commit -m "fix: resolve player movement issue"
```

### 17.6 Godot opens a duplicate Visual Studio Code window

Check the external editor Exec Flags:

```text
--reuse-window --goto "{file}:{line}:{col}"
```

Keep the repository-level Visual Studio Code workspace active.

### 17.7 Godot executable not found

Verify that Godot is installed and that the Godot Tools extension points to the correct executable.

On macOS:

```bash
ls /Applications/Godot.app/Contents/MacOS/
```

Avoid using temporary macOS AppTranslocation executable paths.

### 17.8 Godot autocomplete or diagnostics unavailable

- Ensure the Godot project is open.
- Verify that the Godot Tools extension is installed.
- Check the configured Godot executable path.
- Verify the language server connection.
- Reload Visual Studio Code if necessary.

### 17.9 Git LFS assets are missing

```bash
git lfs install
git lfs pull
```

### 17.10 Project cannot run using F5

Ensure that the project has a configured main scene.

Individual scenes can be tested using F6.

---

## 18. Quick Command Reference

| Action | Command |
|---|---|
| Check repository status | `git status` |
| View unstaged changes | `git diff` |
| View staged changes | `git diff --cached` |
| Activate environment (macOS) | `source .venv/bin/activate` |
| Activate environment (Windows) | `.\.venv\Scripts\Activate.ps1` |
| Install dependencies | `python -m pip install -r requirements-dev.txt` |
| Check Python version | `python --version` |
| Lint project | `gdlint game/` |
| Format script | `gdformat --line-length 100 <script>` |
| Check formatting | `gdformat --check --line-length 100 <script>` |
| Validate hook configuration | `pre-commit validate-config .pre-commit-config.yaml` |
| Install hooks | `pre-commit install` |
| Install hook environments | `pre-commit install-hooks` |
| Run all checks | `pre-commit run --all-files` |
| Check staged files | `pre-commit run` |
| Run linter hook | `pre-commit run gdlint --all-files` |
| Run formatter hook | `pre-commit run gdformat --all-files` |
| Download LFS assets | `git lfs pull` |
| View LFS files | `git lfs ls-files` |
| Create branch | `git switch -c <branch-name>` |
| Stage changes | `git add <file>` |
| Commit changes | `git commit -m "<message>"` |
| Push changes | `git push` |

---

## 19. Documentation Maintenance

This handbook must be updated whenever:

- Development dependencies change.
- New development commands are introduced.
- Git hooks are added or modified.
- Testing procedures change.
- Database workflows change.
- Build and export procedures change.
- New troubleshooting procedures are identified.

Development policies and standards belong in the root README.

Practical instructions and executable commands belong in this developer handbook.

Both documents must remain consistent with the actual repository configuration.
