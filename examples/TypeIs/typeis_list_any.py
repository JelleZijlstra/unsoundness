"""Given a TypeIs[T], in the negative branch of an if statement,
the type should be narrowed from its original type U to U & ~T.
In this case, the original type is Holder | Sublist[str],
and mypy and pyright incorrectly simplify the narrowed type
(Holder | Sublist[str]) & ~list[Any] to just Holder.

"""

from typing import Any
from typing_extensions import TypeIs


def is_exactly_list(x: object) -> TypeIs[list[Any]]:
    """Check if x is exactly a list."""
    return type(x) is list


class Holder:
    def __init__(self, attr: str) -> None:
        self.attr = attr


class Sublist[T](list[T]):
    def __init__(self, attr: int) -> None:
        super().__init__()
        self.attr = attr


def make_something(x: int) -> Holder | Sublist[str]:
    return Sublist[str](x)


def func(x: int) -> str:
    lst = make_something(x)
    if is_exactly_list(lst):
        return lst[0]
    else:
        return lst.attr
