"""
This example is concerned with the difficulty of typing binary operators.

When augmented assignment is performed on a mutable collection, the collection
is mutated in-place. In other words, `x += y` and `x = x + y` are not the same:

```py
xs = [1, 2, 3]
ys = xs
ys += [4]
assert xs == [1, 2, 3 ,4]

# whereas:
xs = [1, 2, 3]
ys = xs
ys = ys + [4]
assert xs == [1, 2, 3]
```
"""

from collections.abc import Set as AbstractSet


def func(x: int) -> str:
    # should not be mutable and should only contain ints
    result: AbstractSet[str] = set()
    other: AbstractSet[object] = result
    other |= {x}
    return next(iter(result))
