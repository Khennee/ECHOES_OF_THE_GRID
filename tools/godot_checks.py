import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "game"


def find_godot():
    configured_path = os.environ.get("GODOT_PATH")

    if configured_path:
        executable = Path(configured_path).expanduser()

        if executable.is_file():
            return str(executable)

        raise RuntimeError(
            f"Invalid GODOT_PATH: {configured_path}"
        )

    system = platform.system()

    print(f"Detected operating system: {system}", flush=True)

    # Check executables available in PATH.
    for command in ("godot", "godot4", "godot.exe"):
        executable = shutil.which(command)

        if executable:
            return executable

    candidates = []

    if system == "Darwin":
        # macOS
        candidates = [
            Path("/Applications/Godot.app/Contents/MacOS/Godot"),
            Path.home() / "Applications/Godot.app/Contents/MacOS/Godot",
        ]

    elif system == "Windows":
        # Windows
        directories = [
            Path("C:/Godot"),
            Path("C:/Program Files/Godot"),
            Path("C:/Program Files (x86)/Godot"),
            Path.home() / "Downloads",
            Path.home() / "Desktop",
            Path.home() / "Documents/Godot",
            Path.home() / "AppData/Local/Godot",
        ]

        for directory in directories:
            if directory.is_dir():
                candidates.extend(
                    sorted(directory.glob("Godot*console.exe"))
                )
                candidates.extend(
                    sorted(directory.glob("Godot*.exe"))
                )

    elif system == "Linux":
        # Linux (CI environment)
        candidates = [
            Path("/usr/bin/godot"),
            Path("/usr/bin/godot4"),
            Path("/usr/local/bin/godot"),
            Path("/usr/local/bin/godot4"),
        ]

    for executable in candidates:
        if executable.is_file():
            print(f"Godot found: {executable}", flush=True)
            return str(executable)

    raise RuntimeError(
        f"Godot executable not found on {system}. "
        "Add Godot to PATH or set GODOT_PATH."
    )


def run_godot(*arguments):
    result = subprocess.run(
        [
            find_godot(),
            "--headless",
            "--path",
            str(PROJECT),
            *arguments,
        ],
        cwd=ROOT,
        timeout=300,
    )

    return result.returncode


def run_static_analysis():
    scripts = sorted(
        script
        for script in PROJECT.rglob("*.gd")
        if not any(
            part in {"addons", ".godot", "builds", "exports"}
            for part in script.relative_to(PROJECT).parts
        )
    )

    for script in scripts:
        relative_path = script.relative_to(PROJECT).as_posix()

        print(f"Checking {relative_path}", flush=True)

        result = run_godot(
            "--script",
            f"res://{relative_path}",
            "--check-only",
        )

        if result != 0:
            return result

    print(f"Successfully checked {len(scripts)} scripts.")
    return 0


def run_tests():
    return run_godot(
        "-s",
        "addons/gut/gut_cmdln.gd",
        "-gexit",
    )


def main():
    commands = {
        "import": lambda: run_godot("--editor", "--import"),
        "check": run_static_analysis,
        "test": run_tests,
    }

    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        print("Usage: godot_checks.py [import|check|test]")
        return 1

    try:
        return commands[sys.argv[1]]()
    except (
        RuntimeError,
        OSError,
        subprocess.TimeoutExpired,
    ) as error:
        print(f"Godot check failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
