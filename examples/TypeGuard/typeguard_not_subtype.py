"""TypeGuard can narrow to a type that is not a subtype of the original type."""

from typing import TypeGuard


def is_int_list(x: object) -> TypeGuard[list[int]]:
    """Check if x is a list of integers."""
    return isinstance(x, list) and all(isinstance(i, int) for i in x)


def foo(x: list[str], y: int):
    if is_int_list(x):
        x.append(y)


def func(x: int) -> str:
    lst: list[str] = []
    foo(lst, x)
    return lst[0]
