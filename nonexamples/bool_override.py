from typing import Literal


class Foo:
    def __init__(self, value: int) -> None:
        self.value = value


class FalseyFoo(Foo):
    def __bool__(self) -> Literal[False]:
        return False


class Bar:
    def __init__(self, value: str) -> None:
        self.value = value

    def __bool__(self) -> Literal[False]:
        return False


def helper(x: Foo | Bar) -> str:
    if x:
        # x narrowed to `Foo` here
        return str(x.value)
    else:
        # x narrowed to `Bar` here
        return x.value


def func(x: int) -> str:
    return helper(FalseyFoo(x))


ACCEPTED_BY = {"mypy": False, "pyright": True}
