
import json
import re
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from godot_checks import find_godot


ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "game"
VENV = ROOT / ".venv"

EXPECTED_GODOT = "4.7.2"

EXPECTED_PACKAGES = {
    "gdtoolkit": "4.5.0",
    "pre-commit": "4.7.0",
}


def report(name, passed, details=""):
    status = "PASS" if passed else "FAIL"

    print(f"[{status}] {name}")

    if details:
        print(f"       {details}")

    return passed


def command_output(*arguments):
    result = subprocess.run(
        [str(argument) for argument in arguments],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
        timeout=30,
    )

    return result.stdout.strip()


def check_command(command, *arguments):
    try:
        output = command_output(command, *arguments)
        return report(command, True, output)

    except (
        OSError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
    ) as error:
        return report(command, False, str(error))


def check_godot():
    try:
        executable = find_godot()
        version = command_output(executable, "--version")

        passed = version.split(".")[:3] == EXPECTED_GODOT.split(".")

        return report(
            "Godot version",
            passed,
            f"{version} | Expected: {EXPECTED_GODOT}",
        )

    except (
        RuntimeError,
        OSError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
    ) as error:
        return report("Godot", False, str(error))


def check_virtual_environment():
    python = (
        VENV / "Scripts" / "python.exe"
        if platform.system() == "Windows"
        else VENV / "bin" / "python"
    )

    if not python.is_file():
        return report(
            "Virtual environment",
            False,
            "Run 'task setup' first.",
        )

    checks = [
        report("Virtual environment", True, str(python)),
    ]

    try:
        version = command_output(python, "--version")

        checks.append(
            report(
                "Virtual environment Python",
                version.startswith("Python 3.12."),
                version,
            )
        )

        packages = json.loads(
            command_output(
                python,
                "-m",
                "pip",
                "list",
                "--format=json",
            )
        )

        installed = {
            re.sub(r"[-_.]+", "-", package["name"]).lower(): package["version"]
            for package in packages
        }

        for name, expected in EXPECTED_PACKAGES.items():
            actual = installed.get(name, "Not installed")

            checks.append(
                report(
                    name,
                    actual == expected,
                    f"{actual} | Expected: {expected}",
                )
            )

    except (
        OSError,
        ValueError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
    ) as error:
        checks.append(
            report("Python dependencies", False, str(error))
        )

    return all(checks)


def check_project_files():
    required = [
        "game/project.godot",
        "game/export_presets.cfg",
        "game/.gutconfig.json",
        "game/addons/gut/plugin.cfg",
        "game/addons/godot-sqlite/plugin.cfg",
        "game/addons/godot-sqlite/gdsqlite.gdextension",
        "requirements-dev.txt",
        ".pre-commit-config.yaml",
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        "gdlintrc",
        "Taskfile.yml",
    ]

    checks = []

    for relative_path in required:
        checks.append(
            report(
                relative_path,
                (ROOT / relative_path).is_file(),
            )
        )

    return all(checks)


def check_git_hooks():
    checks = []

    for hook in ["pre-commit", "commit-msg", "pre-push"]:
        try:
            path = Path(
                command_output(
                    "git",
                    "rev-parse",
                    "--git-path",
                    f"hooks/{hook}",
                )
            )

            if not path.is_absolute():
                path = ROOT / path

            checks.append(
                report(
                    f"Git hook: {hook}",
                    path.is_file(),
                )
            )

        except (
            OSError,
            subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
        ) as error:
            checks.append(
                report(f"Git hook: {hook}", False, str(error))
            )

    return all(checks)


def main():
    print("=" * 60)
    print("ECHOES OF THE GRID - Environment Doctor")
    print("=" * 60)

    checks = []

    checks.append(
        report(
            "Operating system",
            platform.system() in {"Windows", "Darwin"},
            f"{platform.system()} {platform.machine()}",
        )
    )

    checks.append(
        report(
            "System Python",
            sys.version_info[:2] == (3, 12),
            sys.version.split()[0],
        )
    )

    print("\nSystem tools")
    print("-" * 60)

    checks.append(check_command("git", "--version"))
    checks.append(check_command("git", "lfs", "version"))
    checks.append(check_command("task", "--version"))
    checks.append(check_godot())

    print("\nDevelopment dependencies")
    print("-" * 60)

    checks.append(check_virtual_environment())

    print("\nProject configuration")
    print("-" * 60)

    checks.append(check_project_files())

    print("\nGit hooks")
    print("-" * 60)

    checks.append(check_git_hooks())

    print("\n" + "=" * 60)

    if all(checks):
        print("Environment is healthy.")
        return 0

    print("Environment issues detected.")
    print("Resolve the failed checks or run 'task setup'.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
