def func(x: int) -> str:
    return str(x)


func.__code__ = (lambda x: x).__code__
