"""
Passing a protocol to type[Protocol] is banned, but not through a generic function.

Works with pyright but not mypy.
"""

from typing import Literal, Protocol


class Fooable(Protocol):
    def foo(self) -> Literal["banana"]: ...


class Banana:
    def foo(self) -> Literal["banana"]:
        return "banana"


def _impl[F: Fooable](t: type[F], inst: F, wrong: int) -> str:
    banana = t.foo(inst)
    return banana or wrong  # this type checks because `banana` is supposed
    # to always be truthy


def func(x: int) -> str:
    return _impl(Fooable, Banana(), x)


ACCEPTED_BY = {"mypy": False, "pyright": True}
