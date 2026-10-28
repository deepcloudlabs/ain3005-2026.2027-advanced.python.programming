# Module 02: Functional Programming

[← Module 01](../module01/README.md) · [Course overview](../README.md) · [Module 03 →](../module03/README.md)

**Lecture notes:** [Functional Programming in Python](../lecture-notes/module02-functional.programming.in.python.pdf) (PDF)

Imperative code tells the computer **how** to get a result: loop, test, update a variable. Functional code describes
**what** the result is, as a pipeline of transformations over data. Python supports both styles. Its functional
toolkit includes first-class functions, lambdas, `filter`, `map`, `functools.reduce`, generators and `itertools`.

## Learning objectives

By the end of this module you can:

- rewrite an accumulator loop as a `filter` → `map` → `reduce` pipeline, and judge which version reads better;
- pass functions as arguments, either named functions or lambdas;
- write generator functions and explain lazy evaluation;
- flatten nested data and group it.

## The datasets

Both files are in [`resources/`](resources) and are loaded with `json.load` into lists of dictionaries.

| File | Records | Fields the exercises use | Other fields |
|---|---|---|---|
| `countries.json` | 239 countries, 7 continents | `continent`, `population` | `name`, `region`, `surfaceArea`, `gnp`, `lifeExpectancy`, `cities`, … |
| `movies.json` | 250 movies, 1940–2013 | `title`, `year`, `genres` (a list of `{"name", "_id"}`) | `directors`, `imdb` |

## Running the exercises

From the repository root:

```bash
uv run python module02/exercise01.py
```

## Exercises

### 1. Imperative style: `exercise01.py`

What is the total population of Asia? A `for` loop visits every country, an `if` picks the Asian ones, and an
accumulator variable, `total_population`, is updated as it goes.

```text
Total population: 3705025700
```

### 2. Functional style: `exercise02.py`

The same question, answered as a pipeline. Read it from the inside out:

```text
countries ──filter(continent matches)──► countries in Asia ──map(population)──► numbers ──reduce(add, 0)──► total
```

- `filter(predicate, items)` keeps the items for which the predicate returns `True`.
- `map(function, items)` transforms each item.
- `reduce(function, items, initial)` folds the items into one value: `((0 + p1) + p2) + …`. The initial `0` also makes
  an empty input safe.
- `filter` and `map` return **lazy iterators**: no country is examined until `reduce` starts pulling values.

The output is identical to exercise 1. In everyday Python, `sum(c["population"] for c in countries if ...)` says the
same thing even more directly. The comment in the code shows it.

### 3. Lazy evaluation with generators: `exercise03.py`

`bau_filter` and `bau_map` are home-made versions of `filter` and `map`. Each contains `yield`, which makes it a
**generator function**: calling it returns a generator object and runs none of its body. The body runs piece by piece,
each time someone asks for the next value.

The prints reveal the order in which work really happens:

```text
bau_map is just started          ← the for loop asks bau_map for its first value
bau_filter is just started       ← ...so bau_map asks bau_filter for one
inside is_odd: 4                 ← rejected
inside is_odd: 8                 ← rejected
inside is_odd: 15                ← accepted and passed straight to bau_map
3375                             ← 15³ is printed before 16 has even been looked at
inside is_odd: 16
inside is_odd: 23
12167
inside is_odd: 42
bau_filter is just completed     ← only once the input runs out
bau_map is just completed
```

Each value travels through the whole pipeline before the next one is read. Nothing is stored in between, so the same
code would work on a stream of numbers too large to fit in memory.

### 4. Composing predicates: `exercise04.py`

Drama movies from the 1970s, newest first.

- `is_from_70s` and `is_drama` are small named predicates. `is_drama` uses `any()` over a generator, which stops at
  the first match.
- Nesting `filter(is_from_70s, filter(is_drama, movies))` combines them, like a logical *and*.
- `sorted(..., key=lambda movie: movie["year"], reverse=True)` orders by year. `sorted` is **stable**, so movies from
  the same year keep their order from the file.

```text
1977  Der amerikanische Freund
1977  The Last Wave
1976  Network
1976  The Little Girl Who Lives Down the Lane
1975  Dog Day Afternoon
```

### 5. Flatten and group: `exercise05.py`

How many movies belong to each genre?

1. `map(lambda movie: movie["genres"], movies)` produces one list of genres per movie: a list of lists.
2. `chain.from_iterable(...)` flattens it into a single stream of genre objects, and another `map` keeps their names.
3. `reduce(count_genre, genre_names, defaultdict(int))` folds the stream into counts. A `defaultdict(int)` starts every
   unseen key at `0`, so `counts[genre_name] += 1` needs no special case.

`count_genre` updates the accumulator in place and returns it. That's a pragmatic shortcut: building a new dictionary
at every step would be purely functional, but needlessly slow.

```text
Drama        193
Thriller      70
Comedy        65
Romance       56
Crime         41
...
Documentary    1
```

There are 22 genres in all. The counts add up to more than 250 because most movies have several genres.

## Imperative vs. functional at a glance

| | Imperative (`exercise01.py`) | Functional (`exercise02.py`) |
|---|---|---|
| Describes | **how**: the steps and a changing variable | **what**: a pipeline of transformations |
| State | a mutable accumulator | no variable is reassigned |
| Evaluation | eager, one step after another | `filter` and `map` are lazy |
| Reuse | the logic is tangled inside the loop | each stage is a separate, testable function |

## Key takeaways

- Functions are values: you can pass them, return them, and write them inline as lambdas.
- `filter` and `map` are lazy, and generator functions let you build your own lazy stages.
- `reduce` is general but rarely the clearest choice. Prefer `sum`, `max`, `min`, `any`, `all` or
  `collections.Counter` when one of them fits.
- An iterator can be consumed only once. Build it again, or keep a `list`, if you need the data twice.

## Try it

1. In `exercise03.py`, make `bau_filter` build and return a list instead of yielding. Every `is_odd` call now happens
   before `bau_map` even starts: the pipeline has become eager.
2. In `exercise02.py`, replace the `reduce` call with `sum()` over a generator expression.
3. In `exercise05.py`, compute the counts with `collections.Counter` and compare them with `genre_counts`. Remember
   that `genre_names` has already been consumed, so build it again first.
4. In `exercise04.py`, sort by year descending and then by title, using `key=lambda movie: (-movie["year"],
   movie["title"])` without `reverse=True`.
5. Using `total_population_of`, build a dictionary with the population of every continent in a single comprehension.

## Further reading

- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [`functools`](https://docs.python.org/3/library/functools.html), [`itertools`](https://docs.python.org/3/library/itertools.html)
  and [`operator`](https://docs.python.org/3/library/operator.html)
- [Glossary: generator](https://docs.python.org/3/glossary.html#term-generator)
