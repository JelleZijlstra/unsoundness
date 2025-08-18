"""Very similar to typeddict_update.py but uses the |= operator."""

from typing import TypedDict


class Base(TypedDict):
    x: int


class Child1(Base):
    y: int


class Child2(Base):
    y: str


def do_it(td1: Base, td2: Base) -> None:
    td1 |= td2


def func(x: int) -> str:
    c2: Child2 = {"x": x, "y": str(x)}
    c1: Child1 = {"x": x, "y": x}
    do_it(c2, c1)
    return c2["y"]
