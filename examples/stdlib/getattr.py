"""
This example shows that getattr returns an `Any` type allowing for unsoundness.
"""


class StoreX:
    def __init__(self, x: int) -> None:
        self.x: int = x


def func(x: int) -> str:
    store_x: StoreX = StoreX(x)
    str_x: str = getattr(store_x, "x")

    return str_x
