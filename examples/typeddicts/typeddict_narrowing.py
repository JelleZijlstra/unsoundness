"""
This demonstrates an unsound narrowing that was recently re-added by Pyright,
hopefully as a stop-gap before PEP 728 closed typeddicts become widely available.

Mypy 1.16.1 does produce an error for this code.

By default, `TypedDict`s are considered "open", that is, they are allowed to have
arbitrary keys not mentioned in the typeddict definition:

```py
class Point2d(TypedDict):
    x: int
    y: int

class Point3d(TypedDict):
    x: int
    y: int
    z: int

p1: Point2d = {"x": 1, "y": 2}  # ok

p2: Point3d = {"x": 1, "y": 2, "z": 3}  # ok
p3: Point2d = p2  # ok!

p4: Point2d = {"x": 1, "y": 2, "z": 3}  # not allowed, but only because it's a literal dict
```
"""

from typing import TypedDict


class Foo(TypedDict):
    moo: str


class Bar(TypedDict):
    quack: str


class Baz(TypedDict):
    moo: int
    quack: str


def _helper(td: Foo | Bar) -> str:
    if "moo" in td:
        # `td` is inferred as `Foo`

        # this is a logical fallacy: just because the "moo" key is present
        # doesn't mean that `td` is not a `Bar`
        return td["moo"]
    else:
        return td["quack"]


def convert(x: int) -> str:
    baz: Baz = {"moo": x, "quack": "*quack*"}
    string = _helper(baz)  # call is allowed because `Baz` is assignable to `Bar`
    return string