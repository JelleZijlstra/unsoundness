"""
This example shows how the mangled version of a variable is not seen as the
same as the non-mangled version, even when accessed from within the class.

A double-underscore (dunder) instance variable is mangled like:
`_<class_name><variable>`.

Thus, in the below example, `__str_x` can be accessed in the `HiddenDunderVariables`
class with the variable name `_HiddenDunderVariables__str_x`.

Typing the mangled variable will pass type checking, but allows overwrite of
the non-mangled variable with a new, different value type.
"""


class HiddenDunderVariables:
    def __init__(self, x: int) -> None:
        self.__str_x: str = str(x)
        self._HiddenDunderVariables__str_x: int = x

    def get_str_x(self) -> str:
        return self.__str_x


def func(x: int) -> str:
    hidden_dunder_variables: HiddenDunderVariables = HiddenDunderVariables(x)

    return hidden_dunder_variables.get_str_x()
