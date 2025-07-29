from typing import Callable, ParamSpec, TypeVar, Generic, Concatenate

_I = TypeVar("_I")
_T = TypeVar("_T")
_P = ParamSpec("_P")

class WrapperOrDesc(Generic[_T, _P]):
    def __init__(self, func:Callable[_P, _T]):
        self.func = func
    def __call__(self, *args:_P.args, **kwds:_P.kwargs) -> _T:...
    def __get__(self: "WrapperOrDesc[Concatenate[_I, _P], _T]", instance:_I, owner:type[_T]) -> "WrapperOrDesc[_P, _T]":...


class Class(object):
    @WrapperOrDesc
    def method(self, i:int) -> int:...

@WrapperOrDesc
def func(i:int) -> int:...

func(1)
Class().method(1)

