"""JSON, read: numbers and booleans keep their types, but each employee comes back as a list."""
import json

from common import JSON_FILE


def main() -> None:
    with JSON_FILE.open(mode="rt", encoding="utf-8") as file:
        employees = json.load(file)
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
