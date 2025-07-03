"""
This example is concerned with the difficulty of typing binary operators.

When augmented assignment is performed on a mutable collection, the collection
is mutated in-place. In other words, `x += y` and `x = x + y` are not the same:

```py
xs = [1, 2, 3]
ys = xs
ys += [4]
assert x == [1, 2, 3 ,4]

# whereas:
xs = [1, 2, 3]
ys = xs
ys = ys + [4]
assert x == [1, 2, 3]
```
"""


from collections.abc import Set as AbstractSet


def _enhance_fruits(fruits: AbstractSet[str | int], fruit: int | str) -> AbstractSet[str | int]:
    fruits |= {fruit}
    return fruits


def convert(x: int) -> str:
    fruits: set[str] = {"apple", "banana"}
    _ = _enhance_fruits(fruits, x)
    return next(f for f in fruits if f not in {"apple", "banana"})

