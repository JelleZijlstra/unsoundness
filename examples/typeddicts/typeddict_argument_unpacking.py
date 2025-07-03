"""
Type checkers allow you to unpack a `TypedDict` into a call
given that it matches the signature of the function. Unfortunately,
this doesn't take into account the fact that `TypedDict`s are open:
they allow arbitrary extra keys.

Hopefully this is going to be fixed once closed typed dicts (from PEP 728)
become widely available.


### Trivia

There is a similar soundness issue in TypeScript.
A JavaScript function is allowed to be called with more arguments that it
declared, which is often used in callbacks. This is respected by TypeScript,
but it leads to issues when a function has a parameter with a default value.
```ts
function fn1(f: (x: number, y: number) => number) {
    f(1, 5)
}

function fn2(x: number, y: string = ""): number {
    return y.toLowerCase().length + x
}

const fn: (x: number) => number = fn2
fn1(fn)  // Runtime error: y.toLowerCase is not a function!
```

"""

from typing import TypedDict


class Args(TypedDict):
    x: str
    y: str


class StinkyArgs(TypedDict):
    x: str
    y: str
    z: int


def _inner(*, x: str, y: str, z: str = "banana") -> str:
    return x or y or z


def _outer(args: Args) -> str:
    return _inner(**args)


def func(x: int) -> str:
    stinky: StinkyArgs = {"x": "", "y": "", "z": x}
    return _outer(stinky)