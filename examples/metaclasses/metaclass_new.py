value: int


class IntGetter:
    def get(self) -> int:
        return value


class StrGetter:
    def get(self) -> str:
        return "hello"


class Meta(type):
    def __new__(cls, name, bases, attrs) -> type[StrGetter] | type[IntGetter]:
        return IntGetter


class C(StrGetter, metaclass=Meta):
    pass


def func(x: int) -> str:
    global value
    value = x
    return C().get()
