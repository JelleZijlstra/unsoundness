ACCEPTED_BY = {"mypy": True, "pyright": False}

# If there are no type annotations, mypy will assume default types to Any, putting us back in the Any unsoundness situation. However, pyright does not do this.

def loser(x):
    return x

def func(x: int) -> str:
    return loser(x)
