from typing import NotRequired, TypedDict


class Person(TypedDict):
    name: str
    age: int
    string_age: NotRequired[str]


class Named(TypedDict):
    name: str


class Aged(TypedDict):
    age: int


class NamedAndStringAged(Named):
    string_age: int


def make_named(name: str, age: int) -> Named:
    d: NamedAndStringAged = {"name": name, "string_age": age}
    return d


def func(x: int) -> str:
    aged: Aged = {"age": x}
    named = make_named("Alice", x)
    person = Person(**aged, **named)
    return person.get("string_age", "unknown")
