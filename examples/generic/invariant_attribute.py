"""Type checkers unsoundly allow covariant objects to have invariant attributes.

Inspired by https://github.com/python/mypy/issues/737
"""

from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class Covariant(Generic[T_co]):
    def __init__(self, lst: list[T_co]):
        self.__lst = lst

    def get_list(self) -> list[T_co]:
        return self.__lst


def add_one(cov: Covariant[object], obj: object) -> None:
    cov.get_list().append(obj)


def func(x: int) -> str:
    cov: Covariant[str] = Covariant([])
    add_one(cov, x)
    return cov.get_list()[0]
