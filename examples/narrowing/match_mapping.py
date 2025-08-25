from collections.abc import Iterator, Mapping


class Foo:
    pass


class BananaSecret(Foo, Mapping[str, int]):
    def __init__(self, secret: int) -> None:
        self._secret = secret

    def __iter__(self) -> Iterator[str]:
        yield "banana"

    def __len__(self) -> int:
        return 1

    def __getitem__(self, key: str) -> int:
        if key != "banana":
            raise KeyError(key)
        return self._secret


def helper(mystery_object: Foo | dict[str, str]) -> str:
    match mystery_object:
        case {"banana": secret}:
            # Logical fallacy here: mapping pattern matches => mystery_object cannot be Foo
            return secret

        case _:
            return "hello"


def func(x: int) -> str:
    return helper(BananaSecret(x))
