"""Pickle, write: Python's own binary format keeps the exact objects and types."""
import pickle

from common import EMPLOYEES, PICKLE_FILE


def main() -> None:
    with PICKLE_FILE.open(mode="wb") as file:
        pickle.dump(EMPLOYEES, file)


if __name__ == "__main__":
    main()
