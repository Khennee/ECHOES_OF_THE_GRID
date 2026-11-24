
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

GENERATED_DIRECTORIES = [
    ROOT / "builds",
    ROOT / "exports",
    ROOT / "game" / "builds",
    ROOT / "game" / "exports",
]


def main():
    try:
        for directory in GENERATED_DIRECTORIES:
            if directory.is_symlink():
                raise RuntimeError(
                    f"Refusing to remove symbolic link: {directory}"
                )

            if directory.is_dir():
                shutil.rmtree(directory)
                print(f"Removed: {directory.relative_to(ROOT)}")
            else:
                print(f"Skipped: {directory.relative_to(ROOT)}")

        print("\nBuild cleanup completed.")
        return 0

    except (RuntimeError, OSError) as error:
        print(f"Cleanup failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
