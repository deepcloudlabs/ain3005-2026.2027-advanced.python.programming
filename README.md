# AIN3005: Advanced Python Programming

![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Exercise code for **AIN3005 – Advanced Python Programming** (2026–2027 academic year).

The course is organised in modules, one folder each. A module is a sequence of short, self-contained scripts that
build on one topic. Every exercise opens with a one-line docstring saying what it demonstrates, so the recommended way
to study is: **read the script, predict its output, run it, then change it.**

Each module folder has its own README: a full guide that explains every exercise, shows its expected output and
suggests experiments to try.

## Contents

- [Quick start](#quick-start)
- [Modules at a glance](#modules-at-a-glance)
- [Repository layout](#repository-layout)
- [Working with the code](#working-with-the-code)
- [Module summaries](#module-summaries)
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

| Guide | Topic | You will practise | Python features |
|---|---|---|---|
| [Module 01](module01/README.md) | Object-oriented programming | encapsulation, inheritance, polymorphism, interfaces | properties, name mangling, `Enum`, `abc.ABC`, multiple inheritance |
| [Module 02](module02/README.md) | Functional programming | imperative vs. functional style, lazy pipelines | `filter`, `map`, `functools.reduce`, lambdas, generators, `itertools` |
| [Module 03](module03/README.md) | Unit testing | testing a small banking domain in isolation | pytest fixtures, parametrization, `pytest.raises`, pytest-mock, coverage |
| [Module 04](module04/README.md) | Files and serialization | storing the same data in six formats | `pathlib`, `pickle`, `json`, `csv`, pandas, Protocol Buffers |

## Repository layout

```text
.
├── module01/                   object-oriented programming
│   └── README.md               the module guide (every module has one)
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

## Module summaries

A quick map of each module. Follow the links for the full guides.

### Module 01: Object-oriented programming

The three pillars of OOP: classes and objects give **encapsulation**, inheritance gives **reusability**, and the two
together enable **polymorphism**.

| Script | What it shows |
|---|---|
| `exercise01.py` | **Encapsulation.** An `Account` hides its state in name-mangled attributes, exposes it through properties (with a read-only `balance`) and guards it with validation and business rules. `AccountStatus` is an `Enum`. |
| `exercise02.py` | **Inheritance and polymorphism.** `Square` and `Cube` override `area()` from a `TwoDimShape` → `ThreeDimShape` hierarchy; one loop treats them uniformly and uses `isinstance()` for the 3-D extras. |
| `exercise03.py` | **Interfaces vs. abstract classes.** `Pet` is an interface (abstract members only, including an abstract `name` property); `Animal` is an abstract class with state and a concrete `walk()`. `Cat(Animal, Pet)` combines both. |

**Full guide:** [module01/README.md](module01/README.md), with class diagrams, expected output and experiments.

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

**Full guide:** [module02/README.md](module02/README.md), with the datasets, an annotated trace of the lazy
pipeline and experiments.

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

**Full guide:** [module03/README.md](module03/README.md), with the domain model, the business rules, each testing
technique and how to read the coverage report.

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

**Full guide:** [module04/README.md](module04/README.md), with file modes, a format-by-format walkthrough, a
size and type comparison, and how to regenerate the Protocol Buffers code.

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
