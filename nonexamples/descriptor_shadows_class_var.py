from typing import Callable, ClassVar

class Desc:
    def __call__[T](self, arg: T) -> T:
        return arg

    def __get__(self, instance: object, owner: object) -> Callable[[object], str]:
        return str


class C:
    desc: ClassVar[Desc]
    def __init__(self):
        self.desc = Desc()

def func(x: int) -> str:
    return C().desc(x)

ACCEPTED_BY = {"mypy": True, "pyright": False}
