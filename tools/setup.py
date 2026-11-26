
import platform
import shutil
import subprocess
import sys
import venv
from pathlib import Path

from godot_checks import find_godot


ROOT = Path(__file__).resolve().parent.parent
VENV = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements-dev.txt"


def print_step(message):
    print(f"\n{'=' * 60}", flush=True)
    print(message, flush=True)
    print("=" * 60, flush=True)


def run(*arguments):
    subprocess.run(
        [str(argument) for argument in arguments],
        cwd=ROOT,
        check=True,
    )


def get_venv_python():
    if platform.system() == "Windows":
        return VENV / "Scripts" / "python.exe"

    return VENV / "bin" / "python"


def verify_prerequisites():
    print_step("Checking system prerequisites")

    if platform.system() not in {"Windows", "Darwin"}:
        raise RuntimeError(
            "Official development platforms are Windows and macOS."
        )

    if sys.version_info[:2] != (3, 12):
        raise RuntimeError(
            "Python 3.12 is required."
        )

    for command in ["git", "git-lfs", "task"]:
        if not shutil.which(command):
            raise RuntimeError(
                f"Required command not found: {command}"
            )

    godot = find_godot()

    print(f"Operating system: {platform.system()}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Godot: {godot}")

    run("git", "--version")
    run("git", "lfs", "version")
    run("task", "--version")
    run(godot, "--version")


def setup_git_lfs():
    print_step("Initializing Git LFS")

    run("git", "lfs", "install", "--local")
    run("git", "lfs", "pull")


def setup_virtual_environment():
    print_step("Setting up Python virtual environment")

    if not get_venv_python().is_file():
        venv.EnvBuilder(with_pip=True).create(VENV)
        print("Virtual environment created.")
    else:
        print("Existing virtual environment detected.")

    python = get_venv_python()

    run(
        python,
        "-c",
        "import sys; assert sys.version_info[:2] == (3, 12), "
        "'Virtual environment must use Python 3.12'",
    )

    return python


def install_dependencies(python):
    print_step("Installing development dependencies")

    if not REQUIREMENTS.is_file():
        raise RuntimeError(
            "requirements-dev.txt was not found."
        )

    run(
        python,
        "-m",
        "pip",
        "install",
        "-r",
        REQUIREMENTS,
    )


def install_git_hooks(python):
    print_step("Installing Git hooks")

    run(python, "-m", "pre_commit", "install")
    run(python, "-m", "pre_commit", "install-hooks")


def validate_environment(python):
    print_step("Validating development environment")

    run(
        python,
        "-m",
        "pre_commit",
        "run",
        "--all-files",
        "--show-diff-on-failure",
    )


def main():
    try:
        verify_prerequisites()
        setup_git_lfs()

        python = setup_virtual_environment()

        install_dependencies(python)
        install_git_hooks(python)
        validate_environment(python)

        print_step("Setup completed successfully")

        print("Your development environment is ready.")
        print("Run 'task --list' to view available commands.")

        return 0

    except (
        RuntimeError,
        OSError,
        subprocess.CalledProcessError,
    ) as error:
        print(f"\nSetup failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
