def func(x: int) -> str:
    return str(x)


globals()["func"] = lambda x: x
