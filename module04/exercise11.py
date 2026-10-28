"""Protocol Buffers, write: a compact binary format described by employee.proto."""
import employee_pb2
from common import EMPLOYEES, PROTOBUF_FILE


def main() -> None:
    employees_msg = employee_pb2.Employees()
    for name, department, salary, birth_year, full_time in EMPLOYEES:
        employees_msg.employees.add(
            name=name,
            department=department,
            salary=salary,
            birth_year=birth_year,
            full_time=full_time,
        )

    with PROTOBUF_FILE.open(mode="wb") as file:
        file.write(employees_msg.SerializeToString())


if __name__ == "__main__":
    main()
