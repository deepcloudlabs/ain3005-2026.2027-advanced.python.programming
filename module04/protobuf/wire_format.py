"""Field types and field numbers: the 8 bytes of a small Employee message."""
import json

import employee_pb2 as hr


def main() -> None:
    kim = hr.Employee(name="kim", salary=150)
    data = kim.SerializeToString()
    print(len(data), data.hex(" "))      # tags, length, UTF-8, varint
    print(len(json.dumps({"name": "kim", "salary": 150})))
    print(hr.Employee().salary, repr(hr.Employee().name))   # defaults


if __name__ == "__main__":
    main()
