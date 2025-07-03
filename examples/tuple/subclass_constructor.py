"""Mypy and pyright do not check calls to the constructor of tuple subclasses."""


class Foo(tuple[int, str]):
    pass


def func(x: int) -> str:
    f = Foo(("x", x))
    return f[1]
