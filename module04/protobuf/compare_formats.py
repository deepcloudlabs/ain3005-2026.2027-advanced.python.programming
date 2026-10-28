"""Size and speed of JSON, XML, pickle and Protobuf for the same employees.

Prints the measurements behind the "Protobuf Versus JSON, XML and pickle"
slide. Timings depend on the machine; the ranking usually does not.
"""
import json
import pickle
import timeit
import xml.etree.ElementTree as ET
from dataclasses import dataclass

import employee_pb2 as hr

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
RECORDS_FOR_TIMING = 100_000


@dataclass
class Employee:
    name: str
    department: str
    salary: int
    birth_year: int
    full_time: bool


def to_xml(records: list[dict]) -> bytes:
    root = ET.Element("employees")
    for record in records:
        employee = ET.SubElement(root, "employee")
        for key, value in record.items():
            ET.SubElement(employee, key).text = str(value)
    return ET.tostring(root, encoding="utf-8")


def from_xml(data: bytes) -> list[dict]:
    return [{child.tag: child.text for child in employee}
            for employee in ET.fromstring(data)]


def records(n: int) -> list[dict]:
    return [dict(zip(FIELDS, EMPLOYEES[i % len(EMPLOYEES)]))
            for i in range(n)]


def sizes() -> dict[str, int]:
    recs = records(len(EMPLOYEES))
    return {
        "JSON": len(json.dumps(recs).encode("utf-8")),
        "XML": len(to_xml(recs)),
        "pickle": len(pickle.dumps([Employee(**r) for r in recs])),
        "Protobuf": len(hr.Employees(employees=recs).SerializeToString()),
    }


def speeds() -> dict[str, float]:
    recs = records(RECORDS_FOR_TIMING)
    objects = [Employee(**r) for r in recs]
    staff = hr.Employees(employees=recs)
    round_trips = {
        "JSON": lambda: json.loads(json.dumps(recs)),
        "XML": lambda: from_xml(to_xml(recs)),
        "pickle": lambda: pickle.loads(pickle.dumps(objects)),
        "Protobuf": lambda: hr.Employees.FromString(
            staff.SerializeToString()),
    }
    return {name: min(timeit.repeat(fn, number=1, repeat=3))
            for name, fn in round_trips.items()}


def main() -> None:
    print(f"{'format':10}{'7 employees':>14}"
          f"{f'write + read {RECORDS_FOR_TIMING:,}':>26}")
    timings = speeds()
    for name, size in sizes().items():
        print(f"{name:10}{size:>12,} B{timings[name] * 1000:>23,.0f} ms")


if __name__ == "__main__":
    main()
