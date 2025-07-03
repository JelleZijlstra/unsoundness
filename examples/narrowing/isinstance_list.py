"""The way mypy and pyright handle narrowing to a list is unsound.

Mypy narrows to list[Any], pyright narrows to list[object], both of which allow
appending arbitrary values. A sound solution could be to narrow to a type like
`forall T. list[T]` (which cannot be expressed in Python). Such a type would not
allow appending anything.
"""

from typing import Sequence


def doit(lst: Sequence[object], x: int):
    if isinstance(lst, list):
        lst.append(x)


def func(x: int) -> str:
    lst: list[str] = []
    doit(lst, x)
    return lst[0]
