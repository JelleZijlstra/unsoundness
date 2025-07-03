import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass
from types import ModuleType

ROOT_DIR = Path(__file__).resolve().parent.parent


GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def print_red(message: str) -> None:
    print(f"{RED}{message}{RESET}")


def print_green(message: str) -> None:
    print(f"{GREEN}{message}{RESET}")


def run_mypy(path: Path) -> bool:
    print(f"Running mypy on {path}")
    mypy = subprocess.run(
        ["mypy", "--pretty", "--color-output", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if mypy.returncode != 0:
        print(mypy.stdout)
        return False
    return True


def run_pyright(path: Path) -> bool:
    print(f"Running pyright on {path}")
    pyright = subprocess.run(
        ["pyright", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if pyright.returncode != 0:
        print(pyright.stdout)
        return False
    return True


def validate_runtime(path: Path, module: ModuleType) -> bool:
    if not hasattr(module, "func"):
        print_red(f"No func() in {path} {module} {module.__dict__}")
        return False
    for i in [-5, 0, 42]:
        try:
            result = module.func(i)
        except Exception as e:
            print_red(f"Error calling func in {path}: {e}")
            return False
        if result != i:
            print_red(f"Unexpected result {result} != {i} in {path}")
            return False
    return True


def load(path: Path) -> ModuleType:
    """Load the module at the given path."""
    module_name = path.stem
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@dataclass
class ExampleSpec:
    mypy: bool
    pyright: bool


def get_spec(mod: ModuleType, path: Path) -> tuple[bool, ExampleSpec]:
    """Get the example spec from the module or path."""
    if hasattr(mod, "ACCEPTED_BY"):
        accepted_by = getattr(mod, "ACCEPTED_BY")
        spec = ExampleSpec(
            mypy=accepted_by["mypy"],
            pyright=accepted_by["pyright"],
        )
        if "nonexamples" not in path.parts:
            print_red(
                f"Example {path} has ACCEPTED_BY but is not in nonexamples folder: {spec}"
            )
            ok = False
        else:
            ok = True
        return ok, spec
    elif "nonexamples" in path.parts:
        print_red(f"Non-example {path} does not have ACCEPTED_BY")
        return False, ExampleSpec(mypy=True, pyright=True)
    else:
        return True, ExampleSpec(mypy=True, pyright=True)


def validate(path: Path) -> bool:
    mod = load(path)
    runtime_ok = validate_runtime(path, mod)
    spec_ok, spec = get_spec(mod, path)
    mypy_ok = run_mypy(path)
    pyright_ok = run_pyright(path)

    ok = runtime_ok and spec_ok
    if spec.mypy and not mypy_ok:
        print_red(f"mypy validation failed for {path}")
        ok = False
    elif not spec.mypy and mypy_ok:
        print_red(
            f"mypy validation passed for {path} but should not have according to spec {spec}"
        )
        ok = False
    if spec.pyright and not pyright_ok:
        print_red(f"pyright validation failed for {path}")
        ok = False
    elif not spec.pyright and pyright_ok:
        print_red(
            f"pyright validation passed for {path} but should not have according to spec {spec}"
        )
        ok = False
    return ok


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
        paths = sorted(
            file
            for dir in ["examples", "nonexamples"]
            for file in (ROOT_DIR / dir).glob("**/*.py")
        )
    success = True
    for path in paths:
        print(f"\nValidating {path}")
        if not validate(path):
            success = False
    if not success:
        print_red("Validation failed.")
        sys.exit(1)
    print_green("All examples validated successfully.")


if __name__ == "__main__":
    main()
