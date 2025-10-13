ACCEPTED_BY = {"mypy": True, "pyright": True}

# Neither mypy nor pyright elect to infer more precise types for these functions, so they default to Any-style unsound semantics.
# This is allowed by https://typing.python.org/en/latest/spec/annotations.html#the-meaning-of-annotations, but also it "is the result of a deliberate choice by that type checker", for both typecheckers, which is our criterion for a "nonexample".


def loser2(x):
    return x


def loser(x):
    return loser2(x)


def func(x: int) -> str:
    return loser(x)
