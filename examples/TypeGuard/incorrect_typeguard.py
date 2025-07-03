"""An incorrectly written TypeGuard function can lead to unsoundness."""

from typing import TypeGuard


def is_str(x: object) -> TypeGuard[str]:
    return True


def func(x: int) -> str:
    if is_str(x):
        return x
    else:
        assert False
