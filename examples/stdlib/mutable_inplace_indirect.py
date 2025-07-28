"""
This example is conceptually the same as mutable_inplace, but it adds another layer of indirection.

Pyright seems to have a feature where it ignores annotations in favor of the inferred type. This causes the same unsoundness
as highlighted by mutable_inplace, but for a different root cause: the inferred type is built-in set rather than ABC set.
See the comment on `other` in mutable_inplace.

This example is therefore a more indirect reproduction of the same root cause as in mutable_inplace, working around the pyright
behavior, to showcase that even below the incorrectly inferred type, it suffers from the same issue that mypy does.
"""

from collections.abc import Set as AbstractSet


def _enhance_fruits(
    fruits: AbstractSet[str | int], fruit: int | str
) -> AbstractSet[str | int]:
    fruits |= {fruit}
    return fruits


def func(x: int) -> str:
    fruits: set[str] = {"apple", "banana"}
    _ = _enhance_fruits(fruits, x)
    return next(f for f in fruits if f not in {"apple", "banana"})
