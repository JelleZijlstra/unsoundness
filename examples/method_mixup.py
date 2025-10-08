class Fooable:
    def foo(self) -> str:
        return ""


class Apple(Fooable):
    def __init__(self, x: object) -> None:
        self._x = x

    def foo(self) -> str:
        return str(self._x)


class Banana(Fooable):
    def __init__(self, x: str) -> None:
        self._x = x

    def foo(self) -> str:
        return self._x


def _impl(first: type[Fooable], second: Fooable) -> str:
    return first.foo(second)


def func(x: int) -> str:
    # This is going to call `Banana.foo` with an instance of `Apple`
    return _impl(Banana, Apple(x))
