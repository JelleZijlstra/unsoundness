"""Use narrowing on assignment to smuggle values through a dict.

This is accepted by pyright but not mypy.
"""

ACCEPTED_BY = {"mypy": False, "pyright": True}


class CaseInsensitiveDict[VT](dict[str, VT]):
    def __setitem__(self, key: str, value: VT) -> None:
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key: str) -> VT:
        return super().__getitem__(key.lower())


def make_dict() -> dict[str, int | str]:
    return CaseInsensitiveDict()


def func(x: int) -> str:
    d = make_dict()
    d["key"] = str(x)
    d["KEY"] = x
    return d["key"]
