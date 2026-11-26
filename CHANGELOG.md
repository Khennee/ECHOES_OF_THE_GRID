# Changelog

All notable changes to Echoes of the Grid will be documented in this file.

The format is based on Keep a Changelog, and the project follows Semantic Versioning.

## [Unreleased]

### Added

- Initial Godot project configuration using GDScript and the Compatibility renderer.
- Feature-based project directory structure.
- Initial application bootstrap scene.
- Windows x64 and macOS Universal export configurations.
- Git LFS configuration for large binary assets.
- Shared EditorConfig and Visual Studio Code configurations.
- GDScript linting and formatting using gdtoolkit.
- Godot static analysis and strict warning configurations.
- Pre-commit quality checks and Conventional Commit validation.
- GUT automated testing infrastructure.
- SQLite integration through the Godot SQLite addon.
- SQLite connection, operation, transaction, and persistence tests.
- Cross-platform continuous integration using GitHub Actions.
- Automated Windows and macOS desktop build workflows.
- Automated developer setup and development commands using Go Task.
- Environment diagnostic and generated build cleanup utilities.
- Development standards and developer handbook.
- Contribution guidelines.

### Changed

- Restricted official game distribution targets to Windows and macOS.
- Retained Linux dependencies for continuous integration validation.
- Removed unused mobile and web SQLite addon binaries.
- Standardized development commands across supported development platforms.

### Fixed

- Windows Godot executable detection in automated workflows.
- Windows desktop export process synchronization.
- Desktop export path resolution.
- Python package-name normalization in environment diagnostics.

### Pending Verification

- Final macOS distribution signing and notarization.
- Manual verification of downloadable build artifacts.
- SQLite runtime operations inside exported applications.
- Fresh-clone developer onboarding across supported platforms.
- Individual developer automation commands across supported platforms.

## Versioning Policy

The project uses Semantic Versioning:

- MAJOR: Incompatible or substantial breaking changes.
- MINOR: Backward-compatible functionality additions.
- PATCH: Backward-compatible defect corrections.

Changes must be recorded under Unreleased during development and transferred to the corresponding version section when an official release is created.

Each release section must include its version number and release date.
