from typing import ClassVar, Self


class Fruit:
    def __init__(self) -> None:
        self._item: str = ""

    def put(self, item: str) -> None:
        self._item = item

    def get(self) -> str:
        return self._item

    instance: ClassVar[Self]


Fruit.instance = Fruit()


class Banana(Fruit):
    def put(self, item: object) -> None:
        super().put(str(item))


def func(x: int) -> str:
    # Banana.instance is considered by type checkers to be a `Banana`
    # but in reality it is the base `Fruit`.
    Banana.instance.put(x)
    return Banana.instance.get()
