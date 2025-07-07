import contextlib
from collections.abc import Iterator


@contextlib.contextmanager
def yolo() -> Iterator[None]:
    try:
        yield
    except Exception:
        pass


def func(x: int) -> str:
    y: int | str = x
    with yolo():
        print(1 / 0)
        y = "hello"
    return y
