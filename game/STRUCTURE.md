## Project Directory Structure

The project follows a **hybrid feature-based architecture**, where related scenes, scripts, and resources are grouped according to their functionality and responsibility.

```text
ECHOES_OF_THE_GRID/
├── .github/
├── .vscode/
├── docs/
├── tools/
├── game/
│   ├── addons/
│   ├── assets/
│   │   ├── sprites/
│   │   ├── textures/
│   │   ├── audio/
│   │   └── fonts/
│   ├── core/
│   │   ├── bootstrap/
│   │   │   ├── bootstrap.tscn
│   │   │   └── bootstrap.gd
│   │   ├── scene_manager/
│   │   └── game_manager/
│   ├── features/
│   │   ├── player/
│   │   ├── storage/
│   │   ├── research/
│   │   ├── diagnostics/
│   │   ├── companion/
│   │   └── assessment/
│   ├── world/
│   │   ├── levels/
│   │   ├── rooms/
│   │   └── interactables/
│   ├── ui/
│   │   ├── main_menu/
│   │   │   ├── main_menu.tscn
│   │   │   └── main_menu.gd
│   │   ├── pause_menu/
│   │   ├── settings/
│   │   ├── hud/
│   │   └── components/
│   ├── resources/
│   ├── database/
│   │   ├── migrations/
│   │   ├── seeds/
│   │   └── services/
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   ├── fixtures/
│   │   └── helpers/
│   ├── .gutconfig.json
│   ├── project.godot
│   ├── export_presets.cfg
│   └── ART_DIRECTION.md
|   └── HANDBOOK.md
|   └── STRUCTURE.md
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── gdlintrc
├── requirements-dev.txt
├── Taskfile.yml
├── CONTRIBUTING.md
├── CHANGELOG.md
└── README.md
```

### Directory Responsibilities

| Directory | Responsibility |
|---|---|
| `addons/` | Third-party Godot plugins and extensions |
| `assets/` | Sprites, textures, audio, fonts, and other game assets |
| `core/` | Shared systems, initialization, and global game management |
| `features/` | Gameplay mechanics and feature-specific implementations |
| `world/` | Physical environments, levels, rooms, and world objects |
| `ui/` | Menus, HUD, and reusable interface components |
| `resources/` | Shared custom Godot resources and data definitions |
| `database/` | SQLite services, migrations, and seed data |
| `tests/` | Automated tests, fixtures, and testing utilities |
| `tools/` | Development automation and utility scripts |
| `docs/` | Technical documentation and architectural decisions |

### Feature Organization

Related scenes, scripts, and feature-specific resources must be grouped within the same feature directory.

**Simple feature example:**

```text
ui/
└── main_menu/
    ├── main_menu.tscn
    └── main_menu.gd
```

**Complex feature example:**

```text
features/
└── storage/
    ├── storage_terminal.tscn
    ├── storage_terminal.gd
    ├── storage_inventory.gd
    ├── components/
    │   ├── component_card.tscn
    │   ├── component_card.gd
    │   ├── data_spec_sheet.tscn
    │   └── data_spec_sheet.gd
    └── resources/
        └── component_data.gd
```

### File Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Directories | snake_case | `main_menu/` |
| Scenes | snake_case | `main_menu.tscn` |
| Scripts | snake_case | `main_menu.gd` |
| Resource
