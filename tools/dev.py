
import platform
import subprocess
import sys
from pathlib import Path

from godot_checks import find_godot, run_godot


ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "game"
VENV = ROOT / ".venv"


def get_venv_python():
    if platform.system() == "Windows":
        python = VENV / "Scripts" / "python.exe"
    else:
        python = VENV / "bin" / "python"

    if not python.is_file():
        raise RuntimeError(
            "Virtual environment not found. Run 'task setup' first."
        )

    return python


def run(*arguments):
    result = subprocess.run(
        [str(argument) for argument in arguments],
        cwd=ROOT,
    )

    return result.returncode


def run_pre_commit(*arguments):
    return run(
        get_venv_python(),
        "-m",
        "pre_commit",
        "run",
        *arguments,
    )


def open_editor():
    return run(
        find_godot(),
        "--editor",
        "--path",
        PROJECT,
    )


def run_game():
    return run(
        find_godot(),
        "--path",
        PROJECT,
    )


def lint():
    return run_pre_commit(
        "gdlint",
        "--all-files",
    )


def format_scripts():
    return run_pre_commit(
        "gdformat",
        "--all-files",
    )


def check_format():
    scripts = sorted(
        script
        for script in PROJECT.rglob("*.gd")
        if not any(
            part in {"addons", ".godot", "builds", "exports"}
            for part in script.relative_to(PROJECT).parts
        )
    )

    if not scripts:
        print("No GDScript files found.")
        return 0

    python = get_venv_python()

    executable = python.parent / (
        "gdformat.exe"
        if platform.system() == "Windows"
        else "gdformat"
    )

    return run(
        executable,
        "--check",
        "--line-length",
        "100",
        *scripts,
    )


def run_tests():
    result = run_godot("--editor", "--import")

    if result != 0:
        return result

    return run_godot(
        "-s",
        "addons/gut/gut_cmdln.gd",
        "-gexit",
    )


def check_all():
    return run_pre_commit(
        "--all-files",
        "--show-diff-on-failure",
    )


def import_project():
    return run_godot(
        "--editor",
        "--import",
    )


def static_analysis():
    result = import_project()

    if result != 0:
        return result

    return run(
        get_venv_python(),
        ROOT / "tools" / "godot_checks.py",
        "check",
    )


def main():
    commands = {
        "dev": open_editor,
        "run": run_game,
        "lint": lint,
        "format": format_scripts,
        "format:check": check_format,
        "test": run_tests,
        "check": check_all,
        "import": import_project,
        "analyze": static_analysis,
    }

    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        print("Available commands:")

        for command in commands:
            print(f"  {command}")

        return 1

    try:
        return commands[sys.argv[1]]()

    except (
        RuntimeError,
        OSError,
        subprocess.TimeoutExpired,
    ) as error:
        print(f"Command failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
