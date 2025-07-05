"""
If a variable is captured with closure, it is stored in the dunder
__closure__ cell. It is possible to modify the cell contents manually,
thus modifying the underlying value.

This is not typically feasible without knowing the code, so this is
relatively limited in how it could be used in the real world.
"""

from typing import Callable


class ClosureTestClass:
    def __init__(self, x: int) -> None:
        str_x = str(x)

        def get_str_x() -> str:
            return str_x

        self.get_str_x = get_str_x


def func(x: int) -> str:
    closure_test_class = ClosureTestClass(x)

    # Since this can be None or have no items, save off and run
    # within an if statement
    closure = closure_test_class.get_str_x.__closure__
    if closure:
        closure[0].cell_contents = x

    return closure_test_class.get_str_x()
