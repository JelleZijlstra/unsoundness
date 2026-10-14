"""Explicit covariance allows unsafe assignment to a public attribute.

Inspired by https://github.com/python/typing/discussions/2367
"""

from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class Box(Generic[T_co]):
    def __init__(self, value: T_co) -> None:
        self.value = value


def overwrite(box: Box[object], x: int) -> None:
    box.value = x


def func(x: int) -> str:
    box: Box[str] = Box("")
    overwrite(box, x)
    return box.value
