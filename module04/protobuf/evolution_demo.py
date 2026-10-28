"""Schema evolution: backward and forward compatibility of two versions."""
import employee_pb2 as v1       # fields 1-6
import employee_v2_pb2 as v2    # adds skills = 7, contract = 8, email = 9


def main() -> None:
    # Backward: new code reads old data
    old = v1.Employee(name="ben linus", salary=150_000)
    new = v2.Employee.FromString(old.SerializeToString())
    print(new.name, list(new.skills), new.HasField("email"))

    # Forward: old code reads new data and keeps what it does not know
    new.skills.append("chess")
    back = v1.Employee.FromString(new.SerializeToString())
    print(back.name, back.salary)
    print(back.SerializeToString() == new.SerializeToString())


if __name__ == "__main__":
    main()
