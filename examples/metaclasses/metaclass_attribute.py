"""Confusion between metaclass and class attributes."""


class Meta(type):
    def method(self, x: int) -> str:
        return str(x)


class Cls(metaclass=Meta):
    def method(self) -> object:
        return self


def run(t: Meta, x: int):
    return t.method(x)


def func(x: int) -> str:
    return run(Cls, x)
