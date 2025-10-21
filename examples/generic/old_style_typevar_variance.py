"""Variance in old-style `TypeVar`s is not thoroughly checked."""

from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class Foo(Generic[T_co]):
    def __init__(self) -> None:
        self._things: list[T_co] = []

    def add_many(self, values: list[T_co]) -> None:
        self._things.extend(values)

    def pop(self) -> T_co:
        return self._things.pop()


def _helper(foo: Foo[int | str], x: int) -> None:
    foo.add_many([x])


def func(x: int) -> str:
    foo: Foo[str] = Foo()
    _helper(foo, x)
    return foo.pop()
