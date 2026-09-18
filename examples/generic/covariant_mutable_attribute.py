"""Mutable covariant attributes are unsoundly allowed in covariant classes.

It is possible to mark an attribute as immutable with `typing.Final`, but
type checkers do not require this for the class to be covariant.
"""


class Banana[T]:
    def __init__(self, value: T) -> None:
        self.__secret: T = value

    def peel(self) -> T:
        return self.__secret

    def update_secret(self: "Banana[object]", val: int) -> None:
        self.__secret = val


def func(x: int) -> str:
    banana = Banana[str]("")
    banana.update_secret(x)
    return banana.peel()
