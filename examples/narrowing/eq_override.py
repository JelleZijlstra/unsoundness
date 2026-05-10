"""Overriding __eq__ and __hash__ on a str subclass allows unsound narrowing.

This one doesn't currently work in ty, because it does not do unsound narrowing on __eq__.
"""

from typing import TypedDict


class TD(TypedDict):
    a: int
    b: str


class Evil(str):
    def __eq__(self, other: object) -> bool:
        return True

    def __hash__(self) -> int:
        return hash("a")


def get(td: TD, key: str) -> str:
    if key == "b":
        return td[key]
    return "hi"


def func(x: int) -> str:
    td: TD = {"a": x, "b": str(x)}
    return get(td, Evil("b"))
