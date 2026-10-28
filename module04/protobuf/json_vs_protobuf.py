"""Protobuf binary files versus JSON text files for the same employees."""
import json
from pathlib import Path

import employee_pb2 as hr

OUTPUT_DIR = Path(__file__).parent / "output"

# The same employees as ../common.py
EMPLOYEES = [
    ("jack shephard", "Sales", 100_000, 1978, True),
    ("kate austen", "IT", 200_000, 1985, False),
    ("ben linus", "Finance", 150_000, 1967, True),
    ("james sawyer", "HR", 70_000, 1979, True),
    ("kim kwon", "Sales", 120_000, 1986, True),
    ("sun kwon", "IT", 170_000, 1984, False),
    ("hugo reyes", "IT", 120_000, 1992, True),
]
FIELDS = ("name", "department", "salary", "birth_year", "full_time")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    json_path = OUTPUT_DIR / "employees.json"
    bin_path = OUTPUT_DIR / "employees.bin"
    records = [dict(zip(FIELDS, e)) for e in EMPLOYEES]

    # JSON: text mode plus an encoding
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f)
    with open(json_path, encoding="utf-8") as f:
        from_json = json.load(f)

    # Protocol Buffers: binary mode, no encoding
    staff = hr.Employees(employees=records)     # dicts work here too
    with open(bin_path, "wb") as f:
        f.write(staff.SerializeToString())
    with open(bin_path, "rb") as f:
        from_pb = hr.Employees.FromString(f.read())

    print(json_path.stat().st_size, "bytes of JSON,",
          bin_path.stat().st_size, "bytes of Protobuf")
    print(type(from_json[0]).__name__, type(from_pb.employees[0]).__name__)
    try:
        hr.Employee(salary="100")
    except TypeError as err:
        print("TypeError:", err)


if __name__ == "__main__":
    main()
