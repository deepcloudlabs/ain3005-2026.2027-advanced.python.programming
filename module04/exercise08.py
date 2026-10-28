"""CSV, read: DictReader uses the header row as keys; every value is a str."""
import csv

from common import CSV_FILE


def main() -> None:
    with CSV_FILE.open(mode="rt", newline="", encoding="utf-8") as file:
        employees = list(csv.DictReader(file))
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
