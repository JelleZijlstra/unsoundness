from typing import Callable, Concatenate


class WrapperOrDesc[**_P, _T]:
    def __init__(self, func: Callable[_P, _T], i: object | None = None):
        self.func = func
        self.i = i

    def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _T:
        if self.i:
            return self.func(self.i, *args, **kwds)
        return self.func(*args, **kwds)

    def __get__[_I](
        self: "WrapperOrDesc[Concatenate[_I, _P], _T]", instance: _I, owner: type[_T]
    ) -> "WrapperOrDesc[_P, _T]":
        return WrapperOrDesc(self.func, instance)


class Class(object):
    @WrapperOrDesc
    def method(self, i: int) -> int:
        return i


@WrapperOrDesc
def func(i: int) -> int:
    return i


func(1)
c = Class()
c.method(1)
