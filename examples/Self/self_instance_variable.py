from typing import Self


class Fruit:
    def __init__(self: Self) -> None:
        # (for some reason mypy requires an explicit annotation, otherwise
        # it considers `self` to only be an `Fruit` and not `Self`)
        self.ref = self

    def accept(self, x: str) -> str:
        return x


class Banana(Fruit):
    def accept(self, x: object) -> str:
        return "banana accepted"


def reset(a: Fruit) -> None:
    a.ref = Fruit()


def func(x: int) -> str:
    banana = Banana()
    reset(banana)
    return banana.ref.accept(x)
