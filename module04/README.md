# Module 04: Files and Serialization

[← Module 03](../module03/README.md) · [Course overview](../README.md)

**Lecture notes:** [File Operations in Python](../lecture-notes/module04-file.operations.in.python.pdf) (PDF)

Programs need to save data and load it later, or hand it to other programs. **Serialization** turns objects in memory
into text or bytes; **deserialization** turns them back. This module writes the same seven employees in six formats,
reads each file back, and looks at what survives the round trip.

## Learning objectives

By the end of this module you can:

- open files in the right mode (text or binary, read or write) with an explicit encoding;
- choose between plain text, pickle, JSON, CSV, Excel and Protocol Buffers for a given job;
- predict which Python types survive a round trip through each format;
- define a Protocol Buffers schema and generate Python code from it.

## Running the exercises

The exercises come in writer/reader pairs. Run each **writer before its reader**:

```bash
uv run python module04/exercise01.py      # writes resources/employees.txt
uv run python module04/exercise02.py      # reads it back
```

Run them by file path, as above, not with `python -m`: the scripts import `common` and `employee_pb2` from this
folder. All output goes to [`resources/`](resources).

## The shared data: `common.py`

[`common.py`](common.py) defines the data once for every exercise:

- `EMPLOYEES`: seven tuples shaped like `("jack shephard", "Sales", 100_000, 1978, True)`;
- `FIELDS`: their column names, `full_name`, `department`, `salary`, `birth_year` and `full_time`;
- one path constant per output file, such as `TEXT_FILE` and `CSV_FILE`, all inside `resources/`.

## File modes at a glance

| Mode | Meaning | Data type | Used by |
|---|---|---|---|
| `"wt"` / `"rt"` | write / read **text** | `str` | exercises 00, 01–02, 05–06, 07–08 |
| `"wb"` / `"rb"` | write / read **binary** | `bytes` | exercises 00, 03–04, 11–12 |

- Text is the default, so `"w"` means `"wt"`. The code spells the `t` out to make the choice visible.
- Always pass `encoding="utf-8"` in text mode. Otherwise the encoding depends on the operating system's settings.
- Open CSV files with `newline=""` so that the `csv` module controls line endings itself.
- `with` closes the file when the block ends, even if an exception is raised.

## Exercises

### 0. Binary vs. text: `exercise00.py`

The integer `1_000_234_567` is written twice:

- **as binary**: `n.to_bytes(4, byteorder="big", signed=False)` gives exactly 4 bytes, most significant byte first.
  Any unsigned value below 2³² fits. `int.from_bytes` reads it back.
- **as text**: `"1000234567"`, one character per digit, 10 bytes.

`resources/out.bin` is 4 bytes long and `resources/out.txt` is 10. The script prints the number it read back:

```text
1000234567
```

### 1–2. Plain text: `exercise01.py` → `exercise02.py`

The writer formats each employee as one comma-separated line:

```text
jack shephard,Sales,100000,1978,True
kate austen,IT,200000,1985,False
```

Reading it back yields strings only, so `parse_employee` strips the newline, splits on commas and converts each field
itself: `int(salary)`, and `full_time == "True"` for the boolean. `bool("False")` would be `True`, because any
non-empty string is truthy.

```text
('jack shephard', 'Sales', 100000, 1978, True)
('kate austen', 'IT', 200000, 1985, False)
...
```

The weakness: a comma inside a field breaks the line apart. CSV (exercises 7–8) solves this with quoting.

### 3–4. pickle: `exercise03.py` → `exercise04.py`

`pickle.dump` and `pickle.load` save and restore Python objects exactly, here a list of tuples with their ints and
bools. Pickle handles almost any Python object, including instances of your own classes. In return, the format is
Python-only, and **loading a pickle can execute arbitrary code**, so only load files you created or trust.

```text
('jack shephard', 'Sales', 100000, 1978, True)
...
```

### 5–6. JSON: `exercise05.py` → `exercise06.py`

JSON is the lingua franca of web APIs. `json.dump(..., indent=2)` writes readable, indented text:

```json
[
  [
    "jack shephard",
    "Sales",
    100000,
    1978,
    true
  ],
```

Strings, numbers and booleans keep their types, but JSON has only arrays, not tuples. Each employee comes back as a
list:

```text
['jack shephard', 'Sales', 100000, 1978, True]
...
```

### 7–8. CSV: `exercise07.py` → `exercise08.py`

`csv.writer` writes a header row (`FIELDS`) followed by one row per employee, and puts quotes around any field that
contains a comma. `csv.DictReader` uses the header row as keys. Every value comes back as a `str`:

```text
{'full_name': 'jack shephard', 'department': 'Sales', 'salary': '100000', 'birth_year': '1978', 'full_time': 'True'}
...
```

### 9–10. Excel: `exercise09.py` → `exercise10.py`

pandas builds a `DataFrame` from the tuples and the column names, and writes it with `to_excel`. openpyxl does the
actual `.xlsx` work. `index=False` leaves out pandas' row numbers, which would otherwise become an extra first column.
`read_excel` loads the sheet back:

```text
       full_name department  salary  birth_year  full_time
0  jack shephard      Sales  100000        1978       True
1    kate austen         IT  200000        1985      False
...
```

pandas infers each column's type when it reads: `salary` and `birth_year` become `int64`, and `full_time` becomes
`bool`.

### 11–12. Protocol Buffers: `exercise11.py` → `exercise12.py`

Protocol Buffers, Google's schema-driven binary format, starts from a schema in [`employee.proto`](employee.proto):

```proto
syntax = "proto3";

message Employee {
    string name = 1;
    string department = 2;
    int32 salary = 3;
    int32 birth_year = 4;
    bool full_time = 5;
}

message Employees {
    repeated Employee employees = 1;
}
```

- The **field numbers**, not the names, are what's written to the file. That keeps the output small and makes the
  schema safe to evolve.
- `protoc` compiles the schema into [`employee_pb2.py`](employee_pb2.py), which provides the `Employee` and
  `Employees` classes. Don't edit it by hand.
- The writer adds one message per employee with `employees_msg.employees.add(name=..., ...)` and saves
  `SerializeToString()`, which returns `bytes` despite its name. The reader calls `ParseFromString()`.

```text
Name: jack shephard, Dept: Sales, Salary: 100000, Birth Year: 1978, Full-time: True
...
```

#### Changing the schema

`employee_pb2.py` needs protobuf runtime 6.32.1 or newer. After editing `employee.proto`, regenerate the code from
inside this folder. On Windows, the bundled `protoc.exe` works:

```bash
cd module04
protoc --python_out=. employee.proto
```

To keep old files readable, add new fields with **new** numbers, and never reuse or renumber an existing field. A
field that's missing from older data reads as its default value: `0`, `""` or `False`.

## Comparing the formats

| Format | Kind | What comes back | Other languages | Size* |
|---|---|---|---|---|
| Plain text | text | every field as a `str`, parsed by hand | yes | 237 B |
| CSV | text | every value as a `str`, keyed by the header | yes | 287 B |
| JSON | text | strings, numbers and booleans; tuples become lists | yes | 541 B |
| pickle | binary | the exact Python objects | no, Python only | 226 B |
| Excel | binary (zipped XML) | column types inferred by pandas | yes, spreadsheets | ~5 KB |
| Protocol Buffers | binary | typed values, defined by the schema | yes, via generated code | 197 B |

\* The size of the same seven employees as written by these exercises. JSON is indented, and CSV includes the header
row.

## Key takeaways

- Decide between text and binary deliberately, and always name the encoding for text.
- Text formats are easy to read and debug; binary formats are compact and fast.
- Every format except pickle loses some Python type information. Know what you'll get back.
- Never unpickle data you don't trust.
- Schema-based formats such as Protocol Buffers buy compactness, types and safe evolution with an extra build step.

## Try it

1. Run all the writers, list `resources/`, and compare the sizes with the table above.
2. In `exercise02.py`, replace `full_time == "True"` with `bool(full_time)`. Every employee becomes full-time.
3. Rename an employee in `common.py` to `"shephard, jack"`, then run exercises 01–02 and 07–08. The plain-text reader
   fails with `ValueError: too many values to unpack`, while CSV quotes the comma and reads it back intact.
4. In `exercise09.py`, remove `index=False`, then run both Excel scripts. An extra `Unnamed: 0` column appears.
5. Add `string email = 6;` to `employee.proto`, regenerate the code, and run `exercise12.py` without rewriting the
   file. The old data still parses, and every `email` is empty.

## Further reading

- [Python tutorial: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [`pathlib`](https://docs.python.org/3/library/pathlib.html), [`pickle`](https://docs.python.org/3/library/pickle.html),
  [`json`](https://docs.python.org/3/library/json.html) and [`csv`](https://docs.python.org/3/library/csv.html)
- pandas: [`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) and
  [`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- Protocol Buffers: [Python tutorial](https://protobuf.dev/getting-started/pythontutorial/) and
  [proto3 language guide](https://protobuf.dev/programming-guides/proto3/)
