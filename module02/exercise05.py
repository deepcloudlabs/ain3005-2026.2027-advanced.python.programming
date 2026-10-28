"""Group-and-count with reduce(): how many movies belong to each genre."""
import json
from collections import defaultdict
from functools import reduce
from itertools import chain
from pathlib import Path

MOVIES_FILE = Path(__file__).parent / "resources" / "movies.json"


def count_genre(counts: defaultdict[str, int], genre_name: str) -> defaultdict[str, int]:
    counts[genre_name] += 1
    return counts


def main() -> None:
    with MOVIES_FILE.open(encoding="utf-8") as file:
        movies = json.load(file)
    # flatten each movie's genre list into one stream of genre names
    genre_names = map(lambda genre: genre["name"],
                      chain.from_iterable(map(lambda movie: movie["genres"], movies)))
    # idiomatic equivalent: collections.Counter(genre_names)
    genre_counts = reduce(count_genre, genre_names, defaultdict(int))
    for genre, count in sorted(genre_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{genre:<12}{count:>4}")


if __name__ == "__main__":
    main()
