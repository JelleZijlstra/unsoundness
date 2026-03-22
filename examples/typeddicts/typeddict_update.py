"""Type checkers currently allow unsound .update() calls on TypedDicts.

In general, .update() is safe only when the argument is a closed TypedDict,
or when both have the same extra items.

After PEP 728 is implemented and widely available, type checkers should
consider closing this soundness hole.
"""

from typing import TypedDict


class Base(TypedDict):
    x: int


class Child1(Base):
    y: int


class Child2(Base):
    y: str


def do_it(td1: Base, td2: Base) -> None:
    td1.update(td2)


def func(x: int) -> str:
    c2: Child2 = {"x": x, "y": str(x)}
    c1: Child1 = {"x": x, "y": x}
    do_it(c2, c1)
    return c2["y"]
