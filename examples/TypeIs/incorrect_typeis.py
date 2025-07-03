"""An incorrectly written TypeIs function can lead to unsoundness."""

from typing_extensions import TypeIs


def is_str(x: object) -> TypeIs[str]:
    return True


def foo(x: object) -> str:
    if is_str(x):
        return x
    else:
        assert False


def func(x: int) -> str:
    return foo(x)
