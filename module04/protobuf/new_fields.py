"""Repeated fields, enums and optional, defined in employee_v2.proto."""
import employee_v2_pb2 as hr


def main() -> None:
    kate = hr.Employee(name="kate austen",
                       contract=hr.CONTRACT_PART_TIME)
    kate.skills.append("python")         # like a list
    kate.skills.extend(["sql", "docker"])
    print(list(kate.skills), len(kate.skills))
    print(kate.contract, hr.Contract.Name(kate.contract))
    print(kate.HasField("email"), repr(kate.email))
    kate.email = ""                      # set, but empty
    print(kate.HasField("email"))
    try:
        kate.HasField("salary")          # plain scalar: no presence
    except ValueError as err:
        print("ValueError:", err)


if __name__ == "__main__":
    main()
