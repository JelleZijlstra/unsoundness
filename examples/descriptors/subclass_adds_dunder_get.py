class MyStr(str):
    def __get__(self, instance: "C", owner: object) -> int:
        return instance.val


class C:
    def __init__(self, val: int):
        self.val = val

    x: str = MyStr()


def func(x: int) -> str:
    return C(x).x
