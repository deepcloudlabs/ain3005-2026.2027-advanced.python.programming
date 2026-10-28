# AIN3005: Advanced Python Programming

Course exercises for **AIN3005 – Advanced Python Programming** (2026–2027 academic year).
Each module is a folder of short, self-contained scripts on one topic, meant to be read and run in order.

| Module | Topic | Covers |
|---|---|---|
| [`module01`](module01) | Object-oriented programming | encapsulation, inheritance, polymorphism, abstract classes and interfaces |
| [`module02`](module02) | Functional programming | imperative vs. functional style, `filter` / `map` / `reduce`, lazy generators |
| [`module03`](module03) | Unit testing | a small banking domain tested with pytest fixtures, parametrization and mocks |
| [`module04`](module04) | Files and serialization | text, binary, pickle, JSON, CSV, Excel and Protocol Buffers |

## Setup

You need **Python 3.14+**. The project uses [uv](https://docs.astral.sh/uv/), which creates `.venv` and installs
everything declared in [`pyproject.toml`](pyproject.toml): the runtime libraries (pandas, openpyxl, protobuf) and the
`dev` group (pytest, pytest-cov, pytest-mock):

```bash
uv sync
```

Without uv, create and activate a virtual environment and install the per-module requirement files:

```bash
pip install -r module03/requirements.txt -r module04/requirements.txt
```

## Running the exercises

Every script resolves its data files relative to its own location, so you can run it from any directory:

```bash
uv run python module02/exercise01.py
```

Run the scripts as files, as above, rather than with `python -m`: module04 imports `common` and `employee_pb2` from
its own folder. In PyCharm, right-click a file and choose **Run**.

## Running the tests

The pytest configuration in `pyproject.toml` points at `module03/tests`, so from the repository root:

```bash
uv run pytest
```

Add a coverage report for the `banking` package:

```bash
uv run pytest --cov=module03/banking --cov-branch --cov-report=term-missing
```

## Modules

### module01: Object-oriented programming

The three pillars of OOP: classes and objects give **encapsulation**, inheritance gives **reusability**, and both
together enable **polymorphism**.

| File | What it shows |
|---|---|
| `exercise01.py` | Encapsulation: name-mangled "private" attributes, properties, a read-only `balance`, validation and business rules, an `Enum` for account status |
| `exercise02.py` | Inheritance and polymorphism: a `TwoDimShape` → `ThreeDimShape` hierarchy, overriding `area()`, `isinstance()` checks |
| `exercise03.py` | Interfaces vs. abstract classes with `abc.ABC`: an abstract `name` property, concrete and abstract methods, multiple inheritance (`Cat(Animal, Pet)`) |

### module02: Functional programming

Uses the datasets in `module02/resources/` (`countries.json`, `movies.json`).

| File | What it shows |
|---|---|
| `exercise01.py` | Imperative style: total population of Asia with a `for` loop and an accumulator |
| `exercise02.py` | The same result in functional style with `filter` → `map` → `reduce` |
| `exercise03.py` | Hand-written `bau_filter` / `bau_map` generators; the interleaved prints show that the pipeline is lazy |
| `exercise04.py` | Composing predicates with `filter` and ordering with `sorted(key=…)`: drama movies of the 1970s |
| `exercise05.py` | Flattening with `itertools.chain.from_iterable` and grouping with `reduce`: number of movies per genre |

### module03: Unit testing

The `banking` package is the code under test:

- `Account`: deposit and withdraw with validation, an `AccountStatus` (`ACTIVE`, `CLOSED`, `BLOCKED`) and an
  `InsufficientBalanceException` that carries the deficit.
- `CheckingAccount`: a subclass that overrides `_available_funds()` so that withdrawals may use an overdraft.
- `Customer` owns accounts. `Bank` owns customers and finds an account by IBAN.

The tests are in `module03/tests`:

- `test_account.py` follows the four test phases (setup, exercise, verify, teardown) and uses fixtures,
  `@pytest.mark.parametrize` and `pytest.raises`.
- `test_bank.py` isolates `Bank` from `Customer` by replacing `Customer.get_account` with a mock from pytest-mock.

### module04: Files and serialization

Each format comes as a writer/reader pair working on the same sample data, which is defined once in
[`module04/common.py`](module04/common.py) along with the output paths. The files are written to `module04/resources/`.

| Files | Format | What it shows |
|---|---|---|
| `exercise00.py` | Binary vs. text | One integer stored as 4 raw bytes (`int.to_bytes`) and as decimal text |
| `exercise01.py` / `exercise02.py` | Plain text | Writing comma-separated lines, then parsing the strings back into `int` and `bool` |
| `exercise03.py` / `exercise04.py` | `pickle` | Python's native binary format: objects and types come back unchanged |
| `exercise05.py` / `exercise06.py` | JSON | A portable text format: tuples come back as lists |
| `exercise07.py` / `exercise08.py` | CSV | `csv.writer` with a header row and `csv.DictReader`: every value comes back as `str` |
| `exercise09.py` / `exercise10.py` | Excel | `pandas.DataFrame.to_excel` and `pandas.read_excel`, with openpyxl as the engine |
| `exercise11.py` / `exercise12.py` | Protocol Buffers | A schema-driven binary format defined in `employee.proto` |

`employee_pb2.py` is generated from `employee.proto` and needs protobuf runtime 6.32.1 or newer. If you change the
schema, regenerate it with `protoc` (a Windows build, `protoc.exe`, is included in the folder):

```bash
cd module04
protoc --python_out=. employee.proto
```

## License

[MIT](LICENSE) © 2026 Binnur KURT
