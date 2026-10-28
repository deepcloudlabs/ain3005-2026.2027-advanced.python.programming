"""Text file, read: every field comes back as a str and has to be parsed by hand."""
from common import TEXT_FILE


def parse_employee(line: str) -> tuple[str, str, int, int, bool]:
    full_name, department, salary, birth_year, full_time = line.rstrip("\n").split(",")
    return full_name, department, int(salary), int(birth_year), full_time == "True"


def main() -> None:
    with TEXT_FILE.open(mode="rt", encoding="utf-8") as file:
        employees = [parse_employee(line) for line in file]
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
