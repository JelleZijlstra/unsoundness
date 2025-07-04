"""
This example shows how functions, such as `in` may have different implementations
for an abstract type. Some of these implementations may have additional requirements
beyond what is specified for the function.

In this example, an unhashable data type is used as the type for an iterable. Some
types, like lists and tuples, will be able to use `in` since this is based on
iteration through the object. Others, like a dict or set, will fail since they rely
on the hashability of the input.

In the example below, a list input will work, but a dictionary input will not:

```py
check_is_in([], [1, 2, 3])  # This returns False, and does not error
check_is_in({}, [1, 2, 3])  # This throws a TypeError since [1, 2, 3] is not hashable.
```
"""

from collections.abc import Iterable


def check_is_in(input_iterable: Iterable[list[int]], value: list[int]) -> bool:
    return value in input_iterable


def func(x: int) -> int:
    # No error results when [] is the iterable type, unlike a dict or set
    # which will result in a TypeError
    return x if not check_is_in([], [x]) else x + 1
