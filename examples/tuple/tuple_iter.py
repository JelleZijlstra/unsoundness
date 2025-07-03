"""Overriding `__iter__` in a tuple subclass can be unsound."""

from typing import Iterator

global_x: int = 0


class Foo(tuple[int, str]):
    def __iter__(self) -> Iterator[int | str]:
        yield from (("foo", global_x))


def func(x: int) -> str:
    global global_x
    global_x = x
    _, b = Foo((1, "bar"))
    return b
