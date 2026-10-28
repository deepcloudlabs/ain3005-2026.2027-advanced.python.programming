"""Hands-on exercise: a course grade book stored with Protocol Buffers."""
import csv
from pathlib import Path
from statistics import mean

from google.protobuf.message import DecodeError

import gradebook_pb2 as gb

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
SCORES = ("midterm", "final", "project")


def import_csv(path: Path, course: str) -> gb.GradeBook:
    book = gb.GradeBook(course=course)
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            book.students.add(
                id=int(row["id"]), name=row["name"],
                scores=[int(row[k]) for k in SCORES])
    return book


def save(book: gb.GradeBook, path: Path) -> None:
    with path.open("wb") as f:
        f.write(book.SerializeToString())


def load(path: Path) -> gb.GradeBook:
    try:
        with path.open("rb") as f:
            return gb.GradeBook.FromString(f.read())
    except DecodeError as err:
        raise ValueError(f"not a grade book: {path}") from err


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / "gradebook.bin"
    book = import_csv(HERE / "grades.csv", "AIN3005")
    save(book, path)

    book = load(path)
    print(f"{book.course}: {len(book.students)} students")
    for s in book.students:
        print(f"{s.id} {s.name:<13}{mean(s.scores):5.1f}")
    print(path.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
