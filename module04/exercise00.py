"""Binary vs. text files: the same integer stored as 4 raw bytes and as 10 decimal characters."""
from common import RESOURCES_DIR

BINARY_FILE = RESOURCES_DIR / "out.bin"
TEXT_FILE = RESOURCES_DIR / "out.txt"


def main() -> None:
    n = 1_000_234_567

    with BINARY_FILE.open(mode="wb") as file:
        file.write(n.to_bytes(4, byteorder="big", signed=False))  # 4-byte unsigned

    with BINARY_FILE.open(mode="rb") as file:
        data = file.read(4)  # read exactly 4 bytes
        n = int.from_bytes(data, byteorder="big", signed=False)

    print(n)
    with TEXT_FILE.open(mode="wt", encoding="utf-8") as file:
        file.write(f"{n}")


if __name__ == "__main__":
    main()
