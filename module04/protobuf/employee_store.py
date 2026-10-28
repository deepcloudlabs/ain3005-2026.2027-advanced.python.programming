"""Writing messages to a binary file, with a safe update and error handling."""
from pathlib import Path

from google.protobuf.message import DecodeError

import employee_pb2 as hr

OUTPUT_DIR = Path(__file__).parent / "output"


def save(staff: hr.Employees, path: Path) -> None:
    tmp = path.with_suffix(".tmp")
    with tmp.open("wb") as f:          # binary: no encoding
        f.write(staff.SerializeToString())
    tmp.replace(path)                  # all or nothing


def load(path: Path) -> hr.Employees:
    staff = hr.Employees()
    try:
        with path.open("rb") as f:
            staff.ParseFromString(f.read())
    except FileNotFoundError:
        print(f"{path.name} not found: starting empty")
    except DecodeError as err:
        raise ValueError(f"corrupt file: {path.name}") from err
    return staff


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    staff = hr.Employees()
    staff.employees.add(name="jack shephard", salary=100_000)
    staff.employees.add(name="kate austen", salary=200_000)

    path = OUTPUT_DIR / "employees.bin"
    save(staff, path)
    print(path.stat().st_size, "bytes")
    print(load(path) == staff)
    print(len(load(OUTPUT_DIR / "missing.bin").employees))

    notes = OUTPUT_DIR / "notes.txt"
    notes.write_text("hello", encoding="utf-8")
    try:
        load(notes)
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
