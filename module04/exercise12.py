"""Protocol Buffers, read: parse the bytes back into typed Employee messages."""
import employee_pb2
from common import PROTOBUF_FILE


def main() -> None:
    employees_msg = employee_pb2.Employees()
    with PROTOBUF_FILE.open(mode="rb") as file:
        employees_msg.ParseFromString(file.read())

    for employee in employees_msg.employees:
        print(f"Name: {employee.name}, Dept: {employee.department}, "
              f"Salary: {employee.salary}, Birth Year: {employee.birth_year}, "
              f"Full-time: {employee.full_time}")


if __name__ == "__main__":
    main()
