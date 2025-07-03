"""@runtime_checkable does not check parameter types, so it is unsound."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Proto(Protocol):
    def method(self, x: int) -> str: ...


class Implementation:
    def method(self, x: int) -> int:
        return x


def doit(obj: object, x: int) -> str:
    if isinstance(obj, Proto):
        return obj.method(x)
    else:
        return str(x)


def func(x: int) -> str:
    impl = Implementation()
    return doit(impl, x)
