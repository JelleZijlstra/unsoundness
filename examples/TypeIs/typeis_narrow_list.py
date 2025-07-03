"""Narrowing to a list with TypeIs is almost always unsound, because it is not
possible to know the type of a list in the type system at runtime."""

from typing import Sequence

from typing_extensions import TypeIs


def is_int_list(x: object) -> TypeIs[list[int]]:
    """Check if x is a list of integers."""
    return isinstance(x, list) and all(isinstance(i, int) for i in x)


def foo(x: Sequence[object], y: int):
    if is_int_list(x):
        x.append(y)


def func(x: int) -> str:
    lst: list[str] = []
    foo(lst, x)
    return lst[0]
