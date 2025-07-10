"""'if TYPE_CHECKING' allows lying to the type checker."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    def convert(x: int) -> str:
        return str(x)

else:

    def convert(x):
        return x


def func(x: int) -> str:
    return convert(x)
