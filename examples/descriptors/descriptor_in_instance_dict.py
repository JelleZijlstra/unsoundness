from typing import Callable

class Desc:
    def __call__[T](self, arg: T) -> T:
        return arg

    def __get__(self, instance: object, owner: object) -> Callable[[object], str]:
        return str

class C:
    desc: Desc
    def __init__(self):
        self.desc = Desc()

def func(x: int) -> str:
    return C().desc(x)
