from typing import Any, TypeVar, overload

T = TypeVar("T")


@overload
def f(x: list[T]) -> T: ...


@overload
def f(x: T) -> T: ...


def f(x: Any) -> Any:
    if isinstance(x, list):
        return x[0]
    return x


def wrapper(x: T) -> T:
    return f(x)


def func(x: int, cond: bool = False) -> str:
    res = wrapper([x]) if not cond else "hi"
    if isinstance(res, list):
        return str(res[0])
    else:
        return res
