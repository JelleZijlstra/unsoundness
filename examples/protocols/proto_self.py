"""Protocols that use Self can be exploited to smuggle in the wrong type.

See https://github.com/python/typing/issues/2051
"""

from __future__ import annotations

from typing import Protocol, Self


class Proto(Protocol):
    x: int

    def g(self) -> Self: ...


class Base:
    def __init__(self, x: int) -> None:
        self.x = x

    def g(self) -> Sub1:
        return Sub1(self.x)


class Sub1(Base):
    def __init__(self, x: int) -> None:
        super().__init__(x)
        self.y = x


class Sub2(Base):
    def __init__(self, x: int) -> None:
        super().__init__(x)
        self.y = str(x)


def get_it1[BaseT: Base](obj: BaseT) -> BaseT:
    return get_it2(obj)


def get_it2[ProtoT: Proto](obj: ProtoT) -> ProtoT:
    return obj.g()


def func(x: int) -> str:
    obj = Sub2(x)
    obj2 = get_it1(obj)
    return obj2.y
