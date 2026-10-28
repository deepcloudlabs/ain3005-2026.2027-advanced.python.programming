"""Combining predicates with filter() and ordering the result with sorted()."""
import json
from pathlib import Path

MOVIES_FILE = Path(__file__).parent / "resources" / "movies.json"


def is_from_70s(movie: dict) -> bool:
    return 1970 <= movie["year"] < 1980


def is_drama(movie: dict) -> bool:
    return any(genre["name"] == "Drama" for genre in movie["genres"])


def main() -> None:
    with MOVIES_FILE.open(encoding="utf-8") as file:
        movies = json.load(file)
    # drama movies of the 70s, newest first
    drama_movies_in_70s = sorted(
        filter(is_from_70s, filter(is_drama, movies)),
        key=lambda movie: movie["year"],
        reverse=True,
    )
    for movie in drama_movies_in_70s:
        print(f"{movie['year']}  {movie['title']}")


if __name__ == "__main__":
    main()
