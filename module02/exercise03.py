"""Generators are lazy: the interleaved prints show when each pipeline step actually runs."""
from collections.abc import Callable, Iterable, Iterator


def is_odd(number: int) -> bool:
    print(f"inside is_odd: {number}")
    return number % 2 == 1


def bau_filter[T](predicate: Callable[[T], bool], items: Iterable[T]) -> Iterator[T]:
    print("bau_filter is just started")
    for item in items:
        if predicate(item):
            yield item
    print("bau_filter is just completed")


def bau_map[T, R](function: Callable[[T], R], items: Iterable[T]) -> Iterator[R]:
    print("bau_map is just started")
    for item in items:
        yield function(item)
    print("bau_map is just completed")


def main() -> None:
    numbers = [4, 8, 15, 16, 23, 42]
    # building the pipeline prints nothing: no generator body runs until the loop asks for a value
    cubed_odds = bau_map(lambda x: x ** 3, bau_filter(is_odd, numbers))
    for value in cubed_odds:
        print(value)


if __name__ == "__main__":
    main()
