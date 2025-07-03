import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"


def run_typecheck(path: Path) -> bool:
    print(f"Running mypy on {path}")
    mypy = subprocess.run(
        ["mypy", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    if mypy.returncode != 0:
        print(mypy.stdout)
        print(f"mypy failed on {path}")
        return False
    print(f"Running pyright on {path}")
    pyright = subprocess.run(
        ["pyright", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if pyright.returncode != 0:
        print(pyright.stdout)
        print(f"pyright failed on {path}")
        return False
    return True


def run_runtime(path: Path) -> bool:
    if path.stat().st_size == 0:
        print(f"Skipping empty file {path}")
        return True
    module_name = path.stem
    spec = importlib.util.spec_from_file_location(module_name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "func"):
        print(f"No func() in {path}")
        return False
    for i in [-5, 0, 42]:
        try:
            result = module.func(i)
        except Exception as e:
            print(f"Error calling func in {path}: {e}")
            return False
        if result != i:
            print(f"Unexpected result {result} != {i} in {path}")
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the examples")
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific files to validate. If not provided, all examples will be validated.",
    )
    args = parser.parse_args()
    if args.files:
        paths = [Path(file) for file in args.files]
    else:
        paths = sorted(EXAMPLES_DIR.rglob("*.py"))
    success = True
    for path in paths:
        print(f"\nValidating {path}")
        if not run_typecheck(path):
            success = False
        if not run_runtime(path):
            success = False
    if not success:
        print("Validation failed.")
        sys.exit(1)
    print("All examples validated successfully.")


if __name__ == "__main__":
    main()
