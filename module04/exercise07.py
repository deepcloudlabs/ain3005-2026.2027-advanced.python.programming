"""CSV, write: a header row followed by one row per employee."""
import csv

from common import CSV_FILE, EMPLOYEES, FIELDS


def main() -> None:
    # newline="" lets the csv module control line endings itself
    with CSV_FILE.open(mode="wt", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(FIELDS)
        writer.writerows(EMPLOYEES)


if __name__ == "__main__":
    main()
