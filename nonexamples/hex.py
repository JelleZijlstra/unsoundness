"""Accepted by mypy but not pyright."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsHex(Protocol):
    def hex(self) -> str: ...


def helper(obj: float, x: int) -> str:
    if isinstance(obj, SupportsHex):
        return obj.hex()
    else:
        return x


def func(x: int) -> str:
    return helper(1, x)
