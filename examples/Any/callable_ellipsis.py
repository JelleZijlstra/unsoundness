from typing import Callable

# Ellipsis in Callable is "gradual form" https://typing.python.org/en/latest/spec/glossary.html#term-gradual-form, so they'll just let you put any old thing in there. https://typing.python.org/en/latest/spec/callables.html#meaning-of-in-callable

f: Callable[..., str] = lambda x: x


def func(x: int) -> str:
    return f(x)
