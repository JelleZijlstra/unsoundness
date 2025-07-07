from typing import Literal


class CoolCtxManager:
    def __enter__(self) -> list[str]:
        return ["b", "a", "n", "a", "n", "a"]

    def __exit__(self, *args: object) -> Literal[True]:
        return True


def func(x: int) -> str:
    a: int | str = x

    # binding (assignment into targets after `as`) is considered part of the
    # context manager body, so exceptions during the binding can be silenced
    with CoolCtxManager() as [a, _b]:
        pass

    return a
