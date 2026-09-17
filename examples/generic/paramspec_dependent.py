"""
ParamSpec does not handle the possibility of the return type
depending on argument types gracefully.

See also: https://discuss.python.org/t/109091
"""

from collections.abc import Callable


def _call_once[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
    cached: R | None = None

    def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
        nonlocal cached
        if cached is None:
            cached = fn(*args, **kwargs)
        return cached

    return wrapped


def func(x: int) -> str:
    @_call_once
    def _identity[T](arg: T, /) -> T:
        return arg

    _identity(x)
    return _identity("banana")
