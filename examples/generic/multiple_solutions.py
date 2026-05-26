from dataclasses import dataclass


@dataclass
class Box[T]:
    value: T


@dataclass
class Holder[T]:
    value: str
    inner: T


def f[T](x: T | Holder[T]) -> T:
    if isinstance(x, Holder):
        return x.inner
    return x


def identity[T](x: T) -> T:
    return f(x)


def func(x: int) -> str:
    obj = identity(Holder(str(x), Box(x)))
    return obj.value
