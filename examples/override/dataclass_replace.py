"""Type checkers synthesize a `__replace__` method on dataclasses, but
do not flag if this method in a subclass unsafely overrides the corresponding
method in the superclass."""

from dataclasses import dataclass


@dataclass(frozen=True)
class A:
    x: int | str

    def get_str(self) -> str:
        return ""


class B(A):
    x: str

    def get_str(self) -> str:
        return self.x


def func(x: int) -> str:
    a: A = B(x="")
    five: str = a.__replace__(x=x).get_str()
    return five
