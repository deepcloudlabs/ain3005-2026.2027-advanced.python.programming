"""Imperative style: total population of a continent, computed step by step with a loop."""
import json
from pathlib import Path

COUNTRIES_FILE = Path(__file__).parent / "resources" / "countries.json"


def total_population_of(continent: str, countries: list[dict]) -> int:
    total_population = 0
    for country in countries:
        if country["continent"] == continent:
            total_population += country["population"]
    return total_population


def main() -> None:
    with COUNTRIES_FILE.open(encoding="utf-8") as file:
        countries = json.load(file)
    print(f"Total population: {total_population_of('Asia', countries)}")


if __name__ == "__main__":
    main()
