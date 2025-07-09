"""When using TypeIs to confirm that an object has type float,
the difference between the runtime and typing interpretations
of the float type can lead to unsoundness.
"""

from typing import TypeIs

def is_float(x: object) -> TypeIs[float]:
    return isinstance(x, float)

def func(x: int) -> str:
    return hider(x)

def hider(x: float) -> str:
    if not is_float(x):
        return x
    return "OK"
