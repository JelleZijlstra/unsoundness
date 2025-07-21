"""Type checkers generally have a diagnostic for overlapping overloads,
but they do not detect all cases. This can be exploited to achieve
unsound behavior by tricking the type checker into picking one overload,
while the other is actually used at runtime.

This could be worked around in the overload implementation by detecting
when the argument is an instance of both A and B. (In that case, it should
logically return int & str, which is Never, so it must raise an error.)
Thus, one could argue that this example is just an incorrect overload implementation,
but it is listed separately because this pattern is considerably more subtle.
"""

from typing import overload

class A: pass
class B: pass
class C(A, B): pass

@overload
def f(x: A, y: int) -> int: ...
@overload
def f(x: B, y: int) -> str: ...
def f(x: A | B, y: int) -> int | str:
    if isinstance(x, A):
        return y
    else:
        return str(y)

def wrapper(x: B, y: int) -> str:
    return f(x, y)

def func(x: int) -> str:
    return wrapper(C(), x)
