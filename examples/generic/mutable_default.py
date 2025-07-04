"""Accepting a mutable default for a generic parameter can lead to unsoundness.

Based on an example by Anders Kaseorg in https://github.com/python/mypy/issues/13054
"""
def f[T](x: T, y: list[T] = []) -> list[T]:
    return y

def func(x: int) -> str:
    y_strs = f("a")
    y_ints = f(4)
    y_ints.append(x)
    return y_strs[0]
