"""
Type checkers are generally happy to let users del attributes. However,
this can lead to unsound behavior.
"""


class HasGetAttr:
    def __init__(self, i: int):
        self.i = i
        self.s = str(i)

    def __getattr__(self, attr: str) -> int:
        return self.i


def func(i: int) -> str:
    hga = HasGetAttr(i)
    del hga.s
    return hga.s
