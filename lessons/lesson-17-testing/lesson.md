# Lesson 17 — Testing with pytest (Tier: CORE)

Stage 3, first topic. Since Lesson 8 you have been *testing by hand*:
write a driver, run it, compare the output byte-for-byte against a
spec block, then check `mypy` on top. That discipline has served you
well — H1 clean sweeps, byte-exact Output blocks, a 25/25 WP2 matrix.
This lesson formalizes the same discipline into a tool that does the
checking for you: **pytest**.

A test is not a new idea for you. It is your existing verification
habit, written down as functions that check themselves.

CORE tier → Level 4 bar: explain, implement, debug, and combine
testing with everything you already know — without reliance on AI.
This is the last lesson where "I checked it by running it once" counts
as evidence. From Stage 3 on, review scores weight whether your code
has tests.

---

## Objective

By the end of this lesson you can:

- Explain what a test is, what it proves, and what it never proves.
- Write test files pytest discovers automatically, using plain `assert`.
- Read pytest's failure output to find the real value in an assertion.
- Write fixtures with `yield`, choose a correct `scope`, and share
  fixtures through `conftest.py`.
- Use the built-in fixtures `tmp_path`, `monkeypatch`, and `capsys`.
- Replace copy-pasted tests with `@pytest.mark.parametrize`, with
  readable `ids`.
- Verify raised errors with `pytest.raises`.
- Structure every test as Arrange → Act → Assert.
- Say when a test is trustworthy and when it is silently lying.

---

## Why This Matters

Every lesson so far ended with you pressing "run" and trusting your
eyes. That works for one script. It does not scale to a project with a
hundred functions, because:

- A change in `write.py` can silently break `main.py` in a way no
  human re-run notices.
- The 25/25 WP2 matrix was a *documented check* — a spreadsheet of
  expected results you ran by hand. A test suite is that matrix made
  executable, so a one-line code change re-runs every check
  automatically.

From Stage 3 onward, this is how engineering teams decide whether code
is done: not "it ran once", but "the suite is green". Your WP2
`object_hook` decode bug was caught by a re-read before the final run;
a test suite catches it forever.

Testing is also the heart of AI-engineering work: you will test data
pipelines, prompt contracts, and model outputs with exactly these
tools (pytest, fixtures, parametrize) throughout Stage 4.

---

## Mental Model

A test is a **function that checks one behavior**:

```python
def test_price_sets_two_decimals():
    assert format_price(2.5) == "2.50"
```

- pytest discovers any function named `test_*` in any file named
  `test_*.py`.
- A passing test prints nothing. A failing test prints a report that
  shows **exactly what was true and what was expected**.
- One test, one behavior. When a test fails, the name tells you what
  broke.

```text
Your habit until now:            This lesson:
write driver  ──►  read output    write test_*  ──►  run pytest
compare bytes   ──►  trust eyes    suite green   ──►  trust the check
```

The three things a test needs come from resources pytest hands to any
function that asks for them by name:

```text
test function            ── requests ──►   fixtures (data, files)
assert result == wanted  ──  checks   ──►   the behavior
@parametrize             ──  repeats  ──►   many inputs, one test
```

---

## Core Concept

### 1. `test_*` functions and plain `assert`

Test files collect automatically. A test is a plain function whose name
starts with `test_`:

```python
from price_utils import categorize

def test_income_is_positive():
    assert categorize(100.0) == "income"
```

pytest rewrites `assert` in test files so a failure shows the values:

```text
>       assert categorize(100.0) == "expense"
E       AssertionError: assert 'income' == 'expense'
E         - income
E         + expense
```

You do not need `assertEqual`, `assertTrue`, or any method names.
That is the entire difference from unittest — and the reason pytest
is the 2026 default.

### 2. What a test never proves

A test that calls a function but asserts **nothing** proves only that
the function did not crash. It is silent and counts as "passed". This
is the most dangerous test in any suite — a fake green.

### 3. Fixtures: the `@pytest.fixture` decorator

Setup lives in functions, not in the test. A fixture is requested by
naming it as a parameter:

```python
@pytest.fixture
def sample_amounts():
    return [12.5, -3.0, 42.0]

def test_sum(sample_amounts):
    assert sum(sample_amounts) == 51.5
```

- Default scope is `function`: a **fresh copy for every test**.
- `yield` turns a fixture into setup + teardown; the teardown runs
  even when the test fails:

```python
@pytest.fixture
def book():
    ledger = Ledger("ada")
    yield ledger
    ledger.close()
```

- Fixtures can request other fixtures — that is how you compose them.
- Scope may widen to `class`, `module`, `session` — only when setup is
  genuinely expensive. **A wider fixture may never request a narrower
  one** (root cause: the wider one outlives it) — that raises
  `ScopeMismatch`, and the error names both fixtures.

### 4. Sharing fixtures: `conftest.py`

Fixtures used by more than one test file live in `conftest.py` in the
same folder. pytest finds it automatically. **You never write
`from conftest import ...`** — you just name the fixture in the test
signature. That import is an anti-pattern; it breaks pytest's wiring.

### 5. The built-in fixtures you will use all the time

```text
tmp_path      a fresh temporary directory as a pathlib.Path, unique
              per test, cleaned up automatically
monkeypatch   replace any attribute/environment value for one test;
              restored automatically afterwards
capsys        capture everything the test prints to stdout/stderr
```

File-based code is tested against `tmp_path`, never against files in
the repo — your L12 `students.csv` mutation scar is exactly the bug
`tmp_path` exists to prevent.

### 6. `@pytest.mark.parametrize`: one test, many inputs

Where you used to copy a test and change two numbers, write a table:

```python
@pytest.mark.parametrize("amount, expected", [
    (2.5, "2.50"),
    (0.0, "0.00"),
    (-12.5, "-12.50"),
    (1234567.891, "1,234,567.89"),
])
def test_format_price(amount, expected):
    assert format_price(amount) == expected
```

Each row becomes its own test with its own pass/fail. A failure names
the exact row. `ids=` gives rows readable names in the report. Do not
loop with `for` inside one test — a failure then shows only "the loop
failed", and the first error hides the rest.

### 7. `pytest.raises`: asserting that something fails

```python
with pytest.raises(ValueError):
    int("not a number")
```

Use it for code that is *supposed* to fail — the counterpart of an
`assert` for happy paths. Never catch with a bare `try/except` in a
test: a swallowed error turns a failure into a silent pass.

### 8. Arrange → Act → Assert

Every test reads in three blocks, separated by blank lines:

```python
def test_report_from_file_builds_net(tmp_path):
    # Arrange
    source = tmp_path / "tx.txt"
    source.write_text("food,-12.50\nsalary,100.00\n", encoding="utf-8")

    # Act
    report = report_from_file(source)

    # Assert
    assert report == "food: -12.50\nsalary: +100.00\nnet: +87.50\n"
```

Setup, run, verify. This is not decoration — it forces every test to
say clearly what it is checking.

---

## Practical Examples

**1. A pure-function test with parametrize (E1 / E5):**

```python
@pytest.mark.parametrize("price, percent, expected", [
    (100.0, 10, 90.0),
    (79.99, 25, 59.99),
])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected
```

**2. Reading a failure instead of guessing (E2):** run a test with the
wrong expected value once on purpose. The report shows the actual value
in the diff — that is the tool teaching you the fact you forgot.

**3. File-based code against `tmp_path` (E4):**

```python
def test_report_from_file_missing_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        report_from_file(tmp_path / "missing.txt")
```

**4. A square function tested by table (M3–style):** the parametrize
table you write *is* the spec — named, reviewable, and green.

---

## Engineering Notes

- **Green is not the goal; the goal is green *and* meaningful.** A suite
  where every test asserts something real, runs in any order, and makes
  you trust a refactor is valuable. A suite that asserts nothing is
  decoration.
- **Tests are evidence, and review scores now weight them.** A CORE
  topic closes at Level 4 on evidence — the test suite is part of that
  evidence (REVIEW.md, SCORING.md).
- **Name tests by behavior.** `test_load_amounts_skips_junk_lines`, not
  `test_1`. The name is documentation.
- **`tmp_path` replaces your manual temp-copy ritual.** During WP2 you
  verified in a "temp copy" to avoid touching real files. A test does
  this per-run, automatically, and cannot corrupt fixtures (L12 scar).
- **`mypy` and `pytest` are different gates.** `mypy` checks the types;
  pytest checks the behavior. Keep both.
- **`requirements.txt` should stay lean.** Pinning just what a project
  needs lets a teammate `pip install -r requirements.txt` and get the
  same pytest. Your global-env freeze (278 packages, WP2 review-2
  note) is exactly the state the lesson on environments warned about.
- **Failing tests fail fast, then the rest still run.** One red test
  does not stop the suite; pytest reports every failure in one run —
  that is the "full picture" your H1 drills trained.

---

## Common Pitfalls

1. **A test with no assertion** — it runs, passes, and proves nothing.
   Silent fake green (planted in H1).
2. **Mutating a shared fixture** — a `session`- or `module`-scoped
   fixture returning a mutable list leaks one test's changes into the
   next. Order-dependent failures are the hardest bugs to find.
   Default to `function` scope (planted in H1).
3. **`ScopeMismatch`** — a session fixture requesting a function
   fixture. Direction is one-way: narrow depends on wide, never
   reverse.
4. **`from conftest import ...`** — that is a maintenance smell that
   breaks pytest's name wiring. Fixtures are requested by name, never
   imported.
5. **Looping `for` inside a test** instead of `parametrize` — hides
   which input failed and stops at the first error.
6. **Swallowing a desired error with `try/except`** instead of
   `pytest.raises` — a bug that should fail the test passes silently.
7. **Testing implementation, not behavior** — asserting the exact
   sequence of internal calls makes any refactor break the test. Assert
   observable output, state, or raised errors.
8. **Reading assertions as truth** — a test is only as good as its
   expected value. A wrong expected value is a wrong test (planted in
   H1).

---

## Connection to Previous Knowledge

- **Exception handling & the loader contract (L8, L9, L11):** a safe
  loader returns `[]` on a missing file and *never* an error string;
  `report_from_file` *raises* at the boundary. You have done this by
  hand for six lessons. Now you **prove it with pytest.raises and
  `[]` equality** — the contract becomes a test (M3).
- **File handling / pathlib (L9, L10):** `tmp_path` gives you a real
  `Path` — your `.is_file()` guard, `read_text`/`write_text`, and the
  "canonicalize at save time" habit all transfer as assertions.
- **Commands you already run:** your `mypy main.py` gate stays; pytest
  is the behavior gate that replaces the manual driver + byte-compare.
- **Environment (WP2 kickoff):** pytest is installed exactly the way
  `mypy` was — a lean `requirements.txt` in your venv.
- **Functions (L5):** tests are functions that return nothing and
  assert everything. Fixtures are functions that return resources.
  Composition ("a fixture requesting a fixture") is the L13
  module-composition idea, at test level.
- **The 25/25 WP2 matrix:** a parametrized test is a matrix row you
  can read. Your T1–T17 spreadsheet is the spec; pytest executes it.
- **Your debugging protocol (`notes/DEBUGGING.md`):** a failing test is
  the friendliest reproducer in the world — it names the file, the
  line, and the values. H1 is this lesson's drill.

---

## Quick Recall

Answer from memory before starting Practice:

1. Your `load_amounts` safe loader returns `[]` on a missing file and
   skips junk lines. How do you turn that contract into tests — what
   two checks prove it?
2. What makes a function a test in pytest, and what does the file
   name have to be?
3. A test runs, turns green, and contains no `assert`. What does the
   green prove?
4. A `session`-scoped fixture requests a `function`-scoped fixture.
   Legal or not, and what does pytest say?
5. Why is `@pytest.mark.parametrize` better than a `for` loop inside
   the test body?
6. You used to verify WP2 by hand with a temp copy and a T1–T17
   matrix. Which two built-in fixtures replace the temp copy, and what
   does a suite add that the matrix could not?

---

## Practice

Volume follows the CORE pipeline: multiple easy exercises → combined
medium (current + previous) → complex hard (ambiguity, edge cases,
debugging) → challenge. Work top to bottom. Full specs are in
`exercises.ipynb`; write each exercise's files yourself, then run
pytest from the lesson folder and check the Driver cell output.

**Setup (once, before you start):** activate a venv that has pytest —
create `.venv` at the repo root if you do not have one in this project —
then `pip install pytest`. From now on, "run pytest" means, from the
lesson folder:

```text
python -m pytest test_something.py -q
```

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | first tests: `assert`, discovery, running pytest |
| E2 | Easy | [REAL-WORLD] | read a failure report; fix the test, not the code |
| E3 | Easy | [REAL-WORLD] | first fixture: supply data by name |
| E4 | Easy | [REAL-WORLD] | `tmp_path` + a shared fixture in `conftest.py` |
| E5 | Easy | [REAL-WORLD] | `@pytest.mark.parametrize` replaces copy-paste |
| M1 | Medium | [REAL-WORLD] | parametrize + `tmp_path` on file-based reports |
| M2 | Medium | [REAL-WORLD] | `capsys` captures prints; `monkeypatch` swaps a dependency |
| M3 | Medium | [REAL-WORLD] | `pytest.raises` + the loader contract you built in L9–L11 |
| H1 | Hard | [REAL-WORLD] | debug drill: four planted bugs in a test suite |
| H2 | Hard | [REAL-WORLD] | integration suite: load → format → report end to end |
| Challenge | Micro Build | [REAL-WORLD] | the full test suite `price_utils.py` deserves |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation of every exercise, the H1 drill resolved through the
DEBUGGING protocol, and a finished suite that is green, meaningful
(every test asserts), order-independent, and uses fixtures +
parametrize + raises as designed — ready to apply to every lesson and
project that follows.