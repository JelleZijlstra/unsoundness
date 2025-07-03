"""isinstance() can be used to narrow an object to a dict type, but if it is a TypedDict,
this allows unsound operations."""

from typing import TypedDict


class MyDict(TypedDict):
    key: str


def clear(x: object) -> None:
    if isinstance(x, dict):
        x.clear()


def func(x: int) -> str:
    d: MyDict = {"key": "value"}
    clear(d)
    if "key" in d:
        return d["key"]
    else:
        return x  # type checkers consider this unreachable
