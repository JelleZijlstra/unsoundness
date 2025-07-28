"""
This example is concerned with the difficulty of typing binary operators.

When augmented assignment is performed on a mutable collection, the collection
is mutated in-place. In other words, `x += y` and `x = x + y` are not necessarily the same.
It depends on the specific implementation of the runtime type (whether it implements
__iadd__ or not). Therefore it is not safe to make assumptions on the abstract level:

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
    # At the time of writing, pyright seems to ignore the annotation on other in favor of its inferred type.
    # reveal_type reveals that it considers other a built-in set. As a result, pyright is unsound for this example, like mypy,
    # but for a different root cause. For a more elaborate example that showcases the same root cause for pyright, see
    # mutable_inplace_indirect.
    other |= {x}
    return next(iter(result))
