# ECHOES OF THE GRID — Developer Handbook

A quick-start guide for setting up, developing, testing, and contributing to Echoes of the Grid.

For detailed coding standards, architecture, and development policies, refer to the [Development Standards](../README.md) and [Contribution Guidelines](../CONTRIBUTING.md).

## 1. Prerequisites

Install the following before starting development:

| Tool | Required Version |
|---|---|
| Godot Engine | 4.7.2 Stable (Standard) |
| Python | 3.12.x |
| Git | Latest stable |
| Git LFS | Latest stable |
| Go Task | 3.54.0 reference version |
| Visual Studio Code | Optional |

The following dependencies are already included in the repository or installed automatically through `task setup`:

- gdtoolkit 4.5.0
- pre-commit 4.7.0
- GUT 9.7.1
- Godot SQLite 4.9

**Supported platforms:** Windows x64 and macOS Apple Silicon. macOS Intel runtime compatibility remains subject to verification.

### macOS Installation

Install Godot from the official website and move it to the Applications directory.

Install the remaining tools using Homebrew:

```bash
brew install python@3.12 git git-lfs go-task
```

### Windows Installation

Install Godot and Python 3.12 from their official websites. Ensure the Python launcher is available.

Install the remaining tools using Windows Package Manager:

```powershell
winget install Git.Git
winget install GitHub.GitLFS
winget install Task.Task
```

Restart your terminal after installation.

## 2. First-Time Project Setup

Execute all terminal commands from the repository root.

### Step 1 — Clone the repository

```bash
git clone https://github.com/Khennee/ECHOES_OF_THE_GRID.git
cd ECHOES_OF_THE_GRID
```

### Step 2 — Switch to the development branch

```bash
git switch development
git pull --ff-only origin development
```

### Step 3 — Initialize the environment

```bash
task setup
```

This automatically:

- Initializes Git LFS and downloads assets.
- Creates the Python virtual environment.
- Installs development dependencies.
- Configures Git hooks.
- Imports the Godot project.
- Runs quality checks and automated tests.

### Step 4 — Verify the environment

```bash
task doctor
```

Expected result:

```text
Environment is healthy.
```

### Step 5 — Open the project

```bash
task dev
```

Alternatively, import `game/project.godot` through the Godot Project Manager.

Manual Python virtual environment activation is not required when using Task commands.

## 3. Editor Setup

Developers may use either the Godot script editor or Visual Studio Code.

### Visual Studio Code (Optional)

Open the repository root:

```bash
code .
```

Install the recommended workspace extensions when prompted.

To use VS Code as Godot's external script editor:

1. Open Godot Editor Settings.
2. Navigate to Text Editor > External.
3. Enable Use External Editor.
4. Set Exec Path to your local VS Code executable.
5. Set Exec Flags to:

```text
--reuse-window --goto "{file}:{line}:{col}"
```

Configure the Godot Tools extension with your local Godot executable path.

Keep machine-specific paths in personal editor settings, not shared workspace settings.

### Godot Shortcuts

| Shortcut | Action |
|---|---|
| F5 | Run the entire game |
| F6 | Run the current scene |
| F8 | Stop the game |

## 4. Daily Development Procedure

### Step 1 — Check your assigned task

Review your assigned GitHub issue, requirements, and acceptance criteria before starting development.

### Step 2 — Update your local development branch

Ensure existing changes are committed or safely stored before switching branches.

```bash
git switch development
git pull --ff-only origin development
```

### Step 3 — Create a working branch

```bash
git switch -c feature/player-movement
```

Use the appropriate branch prefix:

| Prefix | Purpose |
|---|---|
| `feature/` | New functionality |
| `fix/` | Bug fixes |
| `refactor/` | Code improvements |
| `docs/` | Documentation |
| `test/` | Automated tests |
| `chore/` | Maintenance |
| `hotfix/` | Urgent release fixes |

Do not develop directly on `main` or `development`.

### Step 4 — Start development

```bash
task dev
```

Implement the assigned task, follow the development standards, and test the affected functionality.

To run the game:

```bash
task run
```

### Step 5 — Format and validate changes

Review your changes:

```bash
git status
git diff
```

Stage only the intended files:

```bash
git add <file-or-directory>
```

Format the code:

```bash
task format
```

If formatting modifies files, review and stage them again.

Run all quality checks:

```bash
task format:check
task check
git diff --cached
```

All applicable checks must pass before committing.

### Step 6 — Commit changes

```bash
git commit -m "feat: implement player movement"
```

Git automatically runs the configured quality checks and commit message validation.

### Step 7 — Push your branch

For the first push:

```bash
git push -u origin feature/player-movement
```

For subsequent pushes:

```bash
git push
```

### Step 8 — Submit a pull request

1. Open the GitHub repository.
2. Create a pull request targeting `development`.
3. Complete the pull request description.
4. Reference the corresponding GitHub issue.
5. Request a review from another team member.
6. Wait for automated checks and reviewer approval.
7. Resolve requested changes before merging.

Do not bypass repository protection rules.

## 5. Development Command Reference

Run `task --list` to view all available commands.

### Setup and Development

| Command | Purpose |
|---|---|
| `task setup` | Initialize or repair the environment |
| `task doctor` | Diagnose environment issues |
| `task dev` | Open Godot Editor |
| `task run` | Run the game |
| `task import` | Import project resources |

### Code Quality and Testing

| Command | Purpose |
|---|---|
| `task lint` | Check GDScript coding standards |
| `task format` | Automatically format tracked or staged GDScript files |
| `task format:check` | Check formatting without modifying files |
| `task analyze` | Run Godot static analysis |
| `task test` | Run GUT automated tests |
| `task check` | Run all automated quality checks |

### Builds and Maintenance

| Command | Purpose |
|---|---|
| `task build:windows` | Export Windows x64 application |
| `task build:macos` | Export macOS Universal application |
| `task clean` | Delete generated build outputs |

## 6. Conventional Commits

All commit messages must follow this format:

```text
<type>(optional-scope): <description>
```

Examples:

```text
feat: implement player movement
feat(storage): add component inspection
fix: resolve incorrect entity validation
refactor: simplify inventory manager
test: add database integration tests
docs: update developer handbook
chore: update development dependencies
style: format GDScript files
perf: optimize inventory loading
ci: update automated workflows
build: update export configuration
```

Avoid generic commit messages such as `update`, `changes`, or `final`.

## 7. Updating an Existing Working Branch

If changes have been merged into `development` while you are working on a feature, synchronize your branch.

Ensure your working tree is clean before rebasing.

```bash
git fetch origin
git rebase origin/development
```

If merge conflicts occur, resolve the affected files and execute:

```bash
git add <resolved-files>
git rebase --continue
```

After synchronization:

```bash
task check
```

If your personal working branch was previously pushed and its history was rewritten:

```bash
git push --force-with-lease
```

Never force push to protected branches or rewrite shared branch history without coordination.

## 8. Testing

Run the complete automated test suite:

```bash
task test
```

Test directories:

```text
game/tests/
├── unit/
├── integration/
├── fixtures/
└── helpers/
```

New functionality should include relevant automated tests.

Gameplay interactions, animations, navigation, audio, and visual behavior must also be tested manually.

GitHub Actions automatically validates contributions across Windows, macOS, and Linux. Linux is used for CI validation only.

## 9. Database Development

The project uses Godot SQLite for offline database persistence. No external database server or credentials are required.

```text
game/database/
├── migrations/
├── seeds/
└── services/
```

Database guidelines:

- Use `user://` for runtime database storage.
- Use parameterized SQL queries.
- Use migrations for schema changes.
- Use in-memory or temporary databases for testing.
- Never commit runtime databases or player save data.

Run database integration tests as part of the complete test suite:

```bash
task test
```

Production database initialization, migration, and seed commands will be documented once implemented.

## 10. Building the Game

Install the matching Godot export templates through:

```text
Godot > Editor > Manage Export Templates
```

### Windows

Available from Windows and macOS:

```bash
task build:windows
```

### macOS

Available from macOS:

```bash
task build:macos
```

### Build Output

```text
builds/
├── windows/
│   ├── EchoesOfTheGrid.exe
│   └── libgdsqlite.windows.template_release.x86_64.dll
└── macos/
    └── EchoesOfTheGrid.app
```

Remove generated builds when necessary:

```bash
task clean
```

Generated builds must not be committed.

GitHub Actions also generates desktop build artifacts. Final distribution signing, manual artifact verification, and SQLite testing inside exported applications remain pending.

## 11. Troubleshooting

| Problem | Solution |
|---|---|
| Environment or dependency errors | Run `task doctor` |
| Missing development dependencies | Run `task setup` |
| Git hooks not installed | Run `task setup` |
| Missing assets | Run `git lfs pull` |
| Formatting check fails | Run `task format`, review and stage changes |
| Godot resource errors | Run `task import` |
| Script errors | Run `task analyze` |
| Automated test failures | Run `task test` |
| Invalid commit message | Follow Conventional Commits |
| Export fails | Verify matching Godot export templates |
| VS Code autocomplete unavailable | Open Godot and verify Godot Tools settings |

### Godot Executable Not Found

If automatic detection fails, configure the `GODOT_PATH` environment variable.

macOS:

```bash
export GODOT_PATH="/Applications/Godot.app/Contents/MacOS/Godot"
```

Windows PowerShell:

```powershell
$env:GODOT_PATH = "C:\path\to\Godot.exe"
```

Replace the example path with your actual installation path.

Then run:

```bash
task doctor
```

### Automatic Formatting Modified Files

This is expected when the formatter or pre-commit applies corrections.

Review and stage the corrected files, then rerun:

```bash
task check
```

Do not bypass Git hooks using `--no-verify`.

## 12. Essential Rules

- Always work on an appropriate development branch.
- Follow the established project directory structure.
- Use external `.gd` scripts instead of embedded scene scripts.
- Do not modify third-party addons without team approval.
- Do not commit generated builds, caches, credentials, or runtime databases.
- Follow Git LFS tracking rules for large assets.
- Run quality checks before committing.
- Request independent review before merging.
- Keep GitHub issues and project task statuses updated.

Refer to the root README and contribution guidelines for complete development policies.
