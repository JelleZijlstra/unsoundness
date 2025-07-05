"""
This example shows that setattr is not typed when setting instance variables
for a class. By doing this, it is possible to bypass the typing of the
variable and overwrite with a different type.
"""


class ToString:
    def __init__(self, x: int) -> None:
        self.str_x = str(x)

    def get_str_x(self) -> str:
        return self.str_x


def func(x: int) -> str:
    to_string = ToString(x)
    setattr(to_string, "str_x", x)

    return to_string.get_str_x()
