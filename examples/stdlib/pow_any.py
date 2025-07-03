"""One of the overloads for `int.__pow__` is declared as returning Any. This can be exploited to
produce unsoundness."""


def func(x: int) -> str:
    z = x
    x = 1 + abs(x)
    x **= -x
    return str(x) if isinstance(x, int) else z
