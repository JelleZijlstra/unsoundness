"""
A simplified typeshed definition for `dict[_KT, _VT].__init__`:

@overload
def __init__(self) -> None: ...
@overload
def __init__(self, map: SupportsKeysAndGetItem[_KT, _VT], /) -> None: ...
@overload
def __init__(self, iterable: Iterable[tuple[_KT, _VT]], /) -> None: ...

An issue arises when you provide something that's a mapping at runtime
but only an `Iterable` (of two-element tuples) at type checking time.
"""

from collections.abc import Iterable


def _iterable_to_dict(things: Iterable[tuple[int, str]]) -> dict[int, str]:
    return dict(things)


def convert(x: int) -> str:
    dict1 = {(x, "apple"): x}
    dict2 = _iterable_to_dict(dict1)
    # dict2 is a `dict[int, str]` from a type checker's point of view,
    # but it's a `dict[tuple[int, str], int]` at runtime.
    return next(iter(dict2.values()))
