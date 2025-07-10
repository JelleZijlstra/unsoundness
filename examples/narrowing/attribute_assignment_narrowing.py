"""Type checkers narrow attribute types on assignment, but do not usually
drop the narrowing on method calls, even though method calls may change the
type.

Based on an example by GameRoMan in https://github.com/JelleZijlstra/unsoundness/issues/19
"""

class SomeClass:
    x: int | str

    def func_a(self, y: int) -> None:
        self.x = y

    def func_b(self, y: int) -> str:
        self.x = "hi"
        self.func_a(y)
        x: str = self.x
        return x


def func(x: int) -> str:
    obj = SomeClass()
    return obj.func_b(x)
