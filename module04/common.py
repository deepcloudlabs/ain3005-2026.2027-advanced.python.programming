"""Sample data and file locations shared by the module04 file-format exercises."""
from pathlib import Path

RESOURCES_DIR = Path(__file__).parent / "resources"

TEXT_FILE = RESOURCES_DIR / "employees.txt"
PICKLE_FILE = RESOURCES_DIR / "employees.pkl"
JSON_FILE = RESOURCES_DIR / "employees.json"
CSV_FILE = RESOURCES_DIR / "employees.csv"
EXCEL_FILE = RESOURCES_DIR / "employees.xlsx"
PROTOBUF_FILE = RESOURCES_DIR / "employees.bin"

FIELDS = ("full_name", "department", "salary", "birth_year", "full_time")

EMPLOYEES = [
    ("jack shephard", "Sales", 100_000, 1978, True),
    ("kate austen", "IT", 200_000, 1985, False),
    ("ben linus", "Finance", 150_000, 1967, True),
    ("james sawyer", "HR", 70_000, 1979, True),
    ("kim kwon", "Sales", 120_000, 1986, True),
    ("sun kwon", "IT", 170_000, 1984, False),
    ("hugo reyes", "IT", 120_000, 1992, True),
]
