
import platform
import subprocess
import sys
from pathlib import Path

from godot_checks import find_godot, run_godot


ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "game"
BUILDS = ROOT / "builds"

TARGETS = {
    "windows": {
        "preset": "Windows Desktop",
        "output": BUILDS / "windows" / "EchoesOfTheGrid.exe",
        "dependencies": [
            "libgdsqlite.windows.template_release.x86_64.dll",
        ],
    },
    "macos": {
        "preset": "macOS",
        "output": BUILDS / "macos" / "EchoesOfTheGrid.app",
        "dependencies": [],
    },
}


def export_game(target):
    config = TARGETS[target]
    output = config["output"]

    if target == "macos" and platform.system() != "Darwin":
        raise RuntimeError(
            "macOS application exports must be performed on macOS "
            "using this development workflow."
        )

    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Target: {target}")
    print(f"Export preset: {config['preset']}")
    print(f"Output: {output}")

    print("\nImporting project resources...", flush=True)

    result = run_godot("--editor", "--import")

    if result != 0:
        return result

    print("\nExporting release build...", flush=True)

    subprocess.run(
        [
            find_godot(),
            "--headless",
            "--path",
            str(PROJECT),
            "--export-release",
            config["preset"],
            str(output),
        ],
        cwd=ROOT,
        check=True,
        timeout=600,
    )

    if not output.exists():
        raise RuntimeError(
            f"Export output was not generated: {output}"
        )

    for dependency in config["dependencies"]:
        dependency_path = output.parent / dependency

        if not dependency_path.is_file():
            raise RuntimeError(
                f"Missing export dependency: {dependency_path}"
            )

    if target == "macos":
        framework = (
            output
            / "Contents"
            / "Frameworks"
            / "libgdsqlite.macos.template_release.framework"
        )

        if not framework.is_dir():
            raise RuntimeError(
                "SQLite macOS framework is missing."
            )

    print("\nExport completed successfully.")
    print(f"Build location: {output.parent}")

    if target == "macos":
        print(
            "Note: Distribution signing and notarization "
            "are not verified by this command."
        )

    return 0


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in TARGETS:
        print("Usage: build.py [windows|macos]")
        return 1

    try:
        return export_game(sys.argv[1])

    except (
        RuntimeError,
        OSError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
    ) as error:
        print(f"Build failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
