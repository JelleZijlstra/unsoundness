class X:
    a: int | str

    def __init__(self, a: int | str):
        self.a = a

    def sneak(self, x: int) -> None:
        self.a = x


def func(x: int) -> str:
    obj = X(str(x))
    if isinstance(obj.a, str):
        obj.sneak(x)
        return obj.a
    else:
        return str(obj.a)
