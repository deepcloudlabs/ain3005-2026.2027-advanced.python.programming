"""Serializing and deserializing: object -> bytes -> equal object."""
import employee_pb2 as hr


def main() -> None:
    jack = hr.Employee(
        name="jack shephard", department="Sales",
        salary=100_000, birth_year=1978, full_time=True,
    )
    jack.address.city = "Los Angeles"      # nested message
    jack.address.country = "USA"

    data = jack.SerializeToString()        # object -> bytes
    print(type(data).__name__, len(data))
    print(data[:16])

    copy = hr.Employee()
    copy.ParseFromString(data)             # bytes -> object
    print(copy.name, copy.address.city, copy == jack)
    print(hr.Employee.FromString(data).salary)


if __name__ == "__main__":
    main()
