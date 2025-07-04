"""
eval returns an `Any` which is an avenue to produce unsound code.
"""


def func(x: int) -> str:
    str_x: str = eval(str(x))

    return str_x
