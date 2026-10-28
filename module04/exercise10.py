"""Excel, read: load the .xlsx back into a DataFrame."""
import pandas as pd

from common import EXCEL_FILE


def main() -> None:
    df = pd.read_excel(EXCEL_FILE)
    print(df)


if __name__ == "__main__":
    main()
