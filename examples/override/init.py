"""Type checkers allow unsound overrides of `__init__`."""


class Base:
    def __init__(self, x: int) -> None:
        self.x = str(x)


class Child(Base):
    def __init__(self, x: str) -> None:
        self.x = x


def doit(t: type[Base], x: int) -> str:
    return t(x).x


def func(x: int) -> str:
    return doit(Child, x)
