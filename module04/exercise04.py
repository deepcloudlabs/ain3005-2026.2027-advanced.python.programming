"""Pickle, read: tuples, ints and bools come back unchanged."""
import pickle

from common import PICKLE_FILE


def main() -> None:
    # unpickling can run arbitrary code: only load pickles you created or trust
    with PICKLE_FILE.open(mode="rb") as file:
        employees = pickle.load(file)
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
