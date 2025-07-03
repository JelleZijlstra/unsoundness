"""Adding __get__ in a child class can lead to unsoundness, but type checkers do not flag it."""


class Box:
    def __init__(self, x: int):
        self.x = x


class Base:
    def __init__(self, x: str):
        self.x = x


class Child(Base):
    def __init__(self, x: str, y: int):
        self.x = x
        self.y = y

    def __get__(self, instance: object, owner: type) -> Box:
        return Box(self.y)


class Holder:
    attr: Base


def func(x: int) -> str:
    Holder.attr = Child("x", x)
    return Holder.attr.x
