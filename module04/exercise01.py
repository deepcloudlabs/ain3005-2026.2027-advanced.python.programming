"""Text file, write: one comma-separated line per employee."""
from common import EMPLOYEES, TEXT_FILE


def main() -> None:
    with TEXT_FILE.open(mode="wt", encoding="utf-8") as file:
        for full_name, department, salary, birth_year, full_time in EMPLOYEES:
            file.write(f"{full_name},{department},{salary},{birth_year},{full_time}\n")


if __name__ == "__main__":
    main()
