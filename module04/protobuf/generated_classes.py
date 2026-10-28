"""From .proto to Python classes: what protoc puts into employee_pb2.py."""
import employee_pb2 as hr


def main() -> None:
    print(hr.Employee.DESCRIPTOR.full_name)
    print(hr.Employee.Address.DESCRIPTOR.full_name)
    print(hr.Employee.SALARY_FIELD_NUMBER)


if __name__ == "__main__":
    main()
