from typing import SupportsIndex, overload


class A(tuple[str, int]):
    @overload
    def __getitem__(self, item: SupportsIndex) -> int | str: ...

    @overload
    def __getitem__(self, item: slice) -> tuple[str, int]: ...

    def __getitem__(self, item: slice | SupportsIndex) -> int | str | tuple[str, int]:
        if isinstance(item, slice):
            return self
        else:
            return super().__getitem__(1)


def func(x: int) -> str:
    a: tuple[str, int] = A(("", x))
    return a[0]
