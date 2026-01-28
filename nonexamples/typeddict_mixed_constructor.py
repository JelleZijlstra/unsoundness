"""Mixing positional and keyword arguments to a TypedDict allows
for unsoundness.

Works only on pyright, not mypy, because mypy disallows positional arguments to TypedDict constructors.
"""

ACCEPTED_BY = {"mypy": False, "pyright": True}

from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


class Named(TypedDict):
    name: str


class Aged(TypedDict):
    age: int


class AgedAndIntNamed(Aged):
    name: int


def make_aged(age: int) -> Aged:
    d: AgedAndIntNamed = {"name": age, "age": age}
    return d


def func(x: int) -> str:
    p1: Person = {"name": "Alice", "age": x}
    p2 = Person(p1, **make_aged(x))
    return p2["name"]
