"""Excel, write: build a pandas DataFrame and save it as .xlsx (openpyxl does the writing)."""
import pandas as pd

from common import EMPLOYEES, EXCEL_FILE, FIELDS


def main() -> None:
    df = pd.DataFrame(EMPLOYEES, columns=FIELDS)
    df.to_excel(EXCEL_FILE, index=False)


if __name__ == "__main__":
    main()
