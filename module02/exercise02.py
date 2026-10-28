"""Functional style: the same question as exercise01, answered with filter -> map -> reduce."""
import json
import operator
from functools import reduce
from pathlib import Path

COUNTRIES_FILE = Path(__file__).parent / "resources" / "countries.json"


def total_population_of(continent: str, countries: list[dict]) -> int:
    # idiomatic equivalent: sum(c["population"] for c in countries if c["continent"] == continent)
    return reduce(
        operator.add,
        map(lambda country: country["population"],
            filter(lambda country: country["continent"] == continent, countries)),
        0,
    )


def main() -> None:
    with COUNTRIES_FILE.open(encoding="utf-8") as file:
        countries = json.load(file)
    print(f"Total population: {total_population_of('Asia', countries)}")


if __name__ == "__main__":
    main()
