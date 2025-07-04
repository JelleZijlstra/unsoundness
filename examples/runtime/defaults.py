def func(x: int, arg: int = 0) -> str:
    if isinstance(arg, int):
        return str(x + arg)
    else:
        return x


func.__defaults__ = ("",)
