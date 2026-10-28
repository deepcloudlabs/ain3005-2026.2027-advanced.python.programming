"""JSON, write: a portable text format; JSON has no tuple type, so tuples become arrays."""
import json

from common import EMPLOYEES, JSON_FILE


def main() -> None:
    with JSON_FILE.open(mode="wt", encoding="utf-8") as file:
        json.dump(EMPLOYEES, file, indent=2)


if __name__ == "__main__":
    main()
