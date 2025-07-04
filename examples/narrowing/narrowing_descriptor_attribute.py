class Desc:
    def __get__(self, instance: "C", owner: object) -> int | str:
        return instance.val

    def __set__(self, instance: "C", value: int | str) -> None:
        pass


class C:
    def __init__(self, val: int):
        self.val = val

    x: Desc = Desc()


def func(x: int) -> str:
    c = C(x)
    c.x = "foo"
    return c.x
