# AIN3005: Advanced Python Programming

![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Exercise code for **AIN3005 – Advanced Python Programming** (2026–2027 academic year).

The course is organised in modules, one folder each. A module is a sequence of short, self-contained scripts that
build on one topic. Every exercise opens with a one-line docstring saying what it demonstrates, so the recommended way
to study is: **read the script, predict its output, run it, then change it.**

## Contents

- [Quick start](#quick-start)
- [Modules at a glance](#modules-at-a-glance)
- [Repository layout](#repository-layout)
- [Working with the code](#working-with-the-code)
- [Module guides](#module-guides)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Quick start

You need **Python 3.14 or newer** and [uv](https://docs.astral.sh/uv/) (recommended) or pip.

```bash
git clone https://github.com/deepcloudlabs/ain3005-2026.2027-advanced.python.programming.git
cd ain3005-2026.2027-advanced.python.programming
uv sync                                   # create .venv and install everything from pyproject.toml
uv run python module01/exercise01.py      # run an exercise
uv run pytest                             # run the test suite
```

<details>
<summary>Using pip instead of uv</summary>

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r module03/requirements.txt -r module04/requirements.txt
```

Then run the commands above without the `uv run` prefix.
</details>

## Modules at a glance

| # | Topic | You will practise | Python features |
|---|---|---|---|
| [01](#module-01-object-oriented-programming) | Object-oriented programming | encapsulation, inheritance, polymorphism, interfaces | properties, name mangling, `Enum`, `abc.ABC`, multiple inheritance |
| [02](#module-02-functional-programming) | Functional programming | imperative vs. functional style, lazy pipelines | `filter`, `map`, `functools.reduce`, lambdas, generators, `itertools` |
| [03](#module-03-unit-testing) | Unit testing | testing a small banking domain in isolation | pytest fixtures, parametrization, `pytest.raises`, pytest-mock, coverage |
| [04](#module-04-files-and-serialization) | Files and serialization | storing the same data in six formats | `pathlib`, `pickle`, `json`, `csv`, pandas, Protocol Buffers |

## Repository layout

```text
.
├── module01/                   object-oriented programming
├── module02/                   functional programming
│   └── resources/              countries.json, movies.json
├── module03/                   unit testing
│   ├── banking/                the code under test
│   ├── tests/                  the pytest suite
│   └── requirements.txt
├── module04/                   files and serialization
│   ├── common.py               sample data and file paths shared by all exercises
│   ├── employee.proto          Protocol Buffers schema
│   ├── employee_pb2.py         generated from employee.proto (do not edit)
│   ├── protoc.exe              Protocol Buffers compiler for Windows
│   ├── requirements.txt
│   └── resources/              files written and read by the exercises
├── pyproject.toml              dependencies and pytest settings
└── uv.lock                     pinned dependency versions
```

## Working with the code

### Running an exercise

Run a script by its file path, from any directory. Scripts find their data relative to their own location:

```bash
uv run python module02/exercise04.py
```

In PyCharm, open the repository folder, right-click a script and choose **Run**.

Use the file path rather than `python -m module04.exercise01`: module04 scripts import `common` and `employee_pb2`
from their own folder, which only works when Python starts from the script.

### Running the tests

pytest reads its settings from `pyproject.toml`, so it finds the suite in `module03/tests` from anywhere in the
repository:

```bash
uv run pytest
```

To see which lines and branches of the `banking` package the tests reach:

```bash
uv run pytest --cov=module03/banking --cov-branch --cov-report=term-missing
```

Swap in `--cov-report=html` and open `htmlcov/index.html` to browse the same report line by line.

### Conventions used in the code

The exercises are written to a consistent style that you can copy in your own work:

- **A docstring first.** Every exercise opens with one that says what it demonstrates.
- **A `main()` function** behind `if __name__ == "__main__":`, so a script can also be imported without running.
- **Type hints** throughout the exercises and the `banking` package, including PEP 695 generics
  (`def bau_map[T, R](...)`) in module02.
- **`pathlib` for data files**, resolved with `Path(__file__).parent`, never relative to the current directory.
- **PEP 8 names**: `PascalCase` classes, `snake_case` functions and variables, `UPPER_CASE` constants.

## Module guides

### Module 01: Object-oriented programming

The three pillars of OOP: classes and objects give **encapsulation**, inheritance gives **reusability**, and the two
together enable **polymorphism**.

| Script | What it shows |
|---|---|
| `exercise01.py` | **Encapsulation.** An `Account` hides its state in name-mangled attributes, exposes it through properties (with a read-only `balance`) and guards it with validation and business rules. `AccountStatus` is an `Enum`. |
| `exercise02.py` | **Inheritance and polymorphism.** `Square` and `Cube` override `area()` from a `TwoDimShape` → `ThreeDimShape` hierarchy; one loop treats them uniformly and uses `isinstance()` for the 3-D extras. |
| `exercise03.py` | **Interfaces vs. abstract classes.** `Pet` is an interface (abstract members only, including an abstract `name` property); `Animal` is an abstract class with state and a concrete `walk()`. `Cat(Animal, Pet)` combines both. |

**Try it**

- In `exercise01.py`, add `acc1.balance -= 1_000_000`: a property without a setter raises `AttributeError`. Then
  print `acc1._Account__balance` to see that name mangling only renames the attribute, it doesn't truly hide it.
- In `exercise03.py`, call `Animal(4)`, or delete `Cat.play`, and read the `TypeError` that `abc` raises.
- Add a `Circle` to `exercise02.py` without touching the loop in `main()`. That's polymorphism paying off.

### Module 02: Functional programming

The scripts answer questions about two datasets in `module02/resources/`: `countries.json` (population by continent)
and `movies.json` (titles, years, genres, directors).

| Script | What it shows |
|---|---|
| `exercise01.py` | **Imperative style.** Total population of Asia with a `for` loop and an accumulator. |
| `exercise02.py` | **Functional style.** The same total with `filter` → `map` → `reduce` and lambdas. |
| `exercise03.py` | **Laziness.** Hand-written `bau_filter` and `bau_map` generators; the interleaved prints show that each value flows through the whole pipeline before the next one is read. |
| `exercise04.py` | **Composing predicates.** Drama movies from the 1970s, newest first, with nested `filter` calls and `sorted(key=…)`. |
| `exercise05.py` | **Flatten and group.** Movies per genre, flattening with `itertools.chain.from_iterable` and counting with `reduce`. |

**Try it**

- In `exercise03.py`, make `bau_filter` build and return a list instead of yielding. Every `is_odd` call now happens
  before `bau_map` even starts: the pipeline has become eager.
- In `exercise02.py`, replace the `reduce` call with a generator expression inside `sum()`, and in `exercise05.py`
  with `collections.Counter`. Which version reads best?

### Module 03: Unit testing

The code under test is the `banking` package:

- **`Account`** supports deposits and withdrawals, enforces validation and business rules, and raises
  `InsufficientBalanceException` (which carries the deficit) when the funds don't cover a withdrawal. Its
  `AccountStatus` is `ACTIVE`, `CLOSED` or `BLOCKED`, and only active accounts accept transactions.
- **`CheckingAccount`** extends `Account` with an overdraft by overriding a single hook, `_available_funds()`.
- **`Customer`** owns accounts, and **`Bank`** owns customers and finds any account by IBAN.

| Test file | Technique |
|---|---|
| `test_account.py` | The four test phases (setup, exercise, verify, teardown), fixtures, `@pytest.mark.parametrize`, and `pytest.raises` for validation errors and business exceptions. |
| `test_customer.py` | Plain unit tests of `Customer`, including the read-only snapshot returned by `accounts`. |
| `test_bank.py` | **Isolation with mocks.** pytest-mock replaces each `Customer.get_account`, so a failing test points at `Bank` and nothing else. |

The suite covers 100% of the lines and branches in `banking`; the coverage command in
[Running the tests](#running-the-tests) shows it.

**Try it**

- In `banking/account.py`, change `amount > available` to `amount >= available` in `withdraw()` and run the tests.
  Three tests catch the off-by-one, among them `test_withdraw_should_decrease_balance`.
- Re-run the coverage command with `--ignore=module03/tests/test_customer.py` added. `customer.py` drops to 79%, and
  the `Missing` column lists the lines that only those tests reach.

### Module 04: Files and serialization

The same seven employees are written and read back in a different format by each pair of scripts. The data and the
output paths are defined once, in [`module04/common.py`](module04/common.py), and every file lands in
`module04/resources/`. Run each **writer before its reader**.

| Scripts | Format | What it shows |
|---|---|---|
| `exercise00.py` | Binary vs. text | One integer stored as 4 raw bytes (`int.to_bytes`) and as 10 decimal characters. |
| `exercise01.py` → `exercise02.py` | Plain text | Comma-separated lines; on the way back, every field is a `str` that must be parsed into `int` and `bool`. |
| `exercise03.py` → `exercise04.py` | `pickle` | Python's own binary format: tuples, ints and bools come back unchanged. |
| `exercise05.py` → `exercise06.py` | JSON | A portable text format; JSON has no tuples, so each employee comes back as a list. |
| `exercise07.py` → `exercise08.py` | CSV | `csv.writer` with a header row, read back with `csv.DictReader`; every value is a `str`. |
| `exercise09.py` → `exercise10.py` | Excel | A pandas `DataFrame` saved with `to_excel` (openpyxl engine) and loaded with `read_excel`. |
| `exercise11.py` → `exercise12.py` | Protocol Buffers | A compact, schema-driven binary format defined in `employee.proto`. |

> [!WARNING]
> Unpickling can execute arbitrary code. Only load pickle files that you created or trust.

**Try it**

- Run all the writers and compare the file sizes in `resources/`. For the same data you should see roughly:
  Protocol Buffers 197 B, pickle 226 B, text 237 B, CSV 287 B (with header), JSON 541 B (indented) and Excel about
  5 KB.
- Add a field to `employee.proto` and regenerate the code (see below). The existing `employees.bin` still parses,
  and the new field reads as its default value. That's schema evolution.

**Regenerating the Protocol Buffers code.** `employee_pb2.py` is generated from `employee.proto` and needs protobuf
runtime 6.32.1 or newer. After changing the schema, regenerate it from inside `module04` (on Windows, the bundled
`protoc.exe` works):

```bash
cd module04
protoc --python_out=. employee.proto
```

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `ModuleNotFoundError: No module named 'common'` (or `'employee_pb2'`) | The script was started with `python -m`. Run it by file path: `uv run python module04/exercise01.py`. |
| `ModuleNotFoundError: No module named 'pandas'` (or `'google'`, `'pytest'`) | The dependencies aren't installed in the active environment. Run `uv sync`, or activate your virtual environment and `pip install` the requirement files. |
| `ImportError: Missing optional dependency 'openpyxl'` | pandas needs openpyxl for `.xlsx` files: `uv sync` or `pip install openpyxl`. |
| `VersionError` from `google.protobuf.runtime_version` | Your protobuf runtime is older than the generated code. Upgrade with `uv sync` or `pip install -U "protobuf>=6.32.1"`. |
| A reader prints odd data, e.g. `exercise08.py` uses an employee as the header row | The file in `resources/` was written by an older version of its writer. Run the matching writer first. |

## License

Released under the [MIT License](LICENSE). © 2026 Binnur KURT
