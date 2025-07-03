from typing import overload


@overload
def overl(x: int) -> str: ...
@overload
def overl(x: str) -> int: ...


def overl(x: object) -> object:
    return x


def func(x: int) -> str:
    return overl(x)
