def func(x: int) -> str:
    union: int | str

    def helper():
        nonlocal union
        union = x

    union = "hello"
    helper()
    return union
