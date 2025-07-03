"""Illustrates that a type-ignore in one place can lead to unsoundness elsewhere."""


class Base:
    def meth(self, x: int) -> str:
        return str(x)


class Derived(Base):
    def meth(self, x: int) -> int:  # type: ignore
        return x


def foo(b: Base, x: int) -> str:
    return b.meth(x)


def func(x: int) -> str:
    return foo(Derived(), x)
