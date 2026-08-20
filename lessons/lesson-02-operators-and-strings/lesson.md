# Lesson 2 — Operators & Strings

## Learning Objective

By the end of this lesson you can combine values with operators in the right
order, test and combine conditions with comparisons and logic, and manipulate
text with slicing and string methods — including building formatted reports.

---

## Motivation

Data is never handed to you clean. Every AI pipeline starts by *cleaning and
transforming text*: stripping whitespace, splitting into tokens, lowercasing,
checking what a string contains, rebuilding it. Operators and string methods
are the toolbox for that first mile. They are also how every `if` in your
future code gets built.

---

## Mental Model

An operator is a **verb applied to values**. Python decides the order verbs run
in via *precedence* — think of it as grammar: `**` speaks before `*`, `*`
speaks before `+`, comparisons speak before `and`, `and` speaks before `or`.

A string is a **sequence of characters with an invisible ruler underneath**.
Indexes point *between* characters, which is why slicing feels so clean.

```
"P y t h o n"
 0 1 2 3 4 5     ← indexes point BETWEEN chars
-6-5-4-3-2-1     ← negative indexes count from the right
```

---

## Visualization

Precedence ladder (top binds tightest):

```
( )  [ ]  .   call          ← highest
**                            ← power (right-associative)
+x  -x  ~x                    ← unary
*   /   //   %   @
+   -
<<  >>
&
^
|
in  not in  is  ==  !=  <  <=  >  >=    ← all equal
not
and
or                              ← lowest
```

Chained comparisons — one comparison, two checks:

```
0 <= score <= 100   ≡   0 <= score and score <= 100
```

---

## Theory

### Comparisons

Eight operators, all equal priority: `< <= > >= == != is is not`.
Different types never compare equal (except `int`/`float` numeric mix).

```python
1 < 5 < 10        # True  — chained, reads like math
"apple" < "banana"  # True  — lexicographic order
```

### Logical operators — the surprise

`and` and `or` **return one of their operands**, not a boolean. Only `not`
always returns a boolean.

```python
0 or "fallback"     # "fallback"   (0 is falsy → take right)
"hello" or "x"      # "hello"      (truthy → take left)
"" or 5             # 5
5 and "both"        # "both"       (truthy → take right)
0 and 5             # 0            (falsy → take left, short-circuit)
```

Both short-circuit: `and` stops early on a falsy left; `or` stops early on a
truthy left. This is the engine behind the H2 trick.

### Membership

```python
"py" in "python"     # True  — substring test
"x" not in "python"  # True
"" in "abc"          # True  — empty string is always a substring
```

### Augmented assignment

```python
count = 0
count += 1          # count = count + 1
total *= 2
name += "!"         # rebinds name to a NEW string
```

For immutable types this is always a *rebinding*, never an in-place change.

### Strings are immutable

```python
word = "Python"
word[0] = "J"       # TypeError: 'str' object does not support item assignment
```

You never edit a string — you build a new one and re-point the name.

### Slicing

```python
s = "python"
s[0:2]    # "py"   start included, stop EXCLUDED
s[2:]     # "thon" from index 2 to end
s[:2]     # "py"   from start to index 2
s[-2:]    # "on"   last two characters
s[::-1]   # "nohtyp" — reversed (step = -1)
s[::2]    # "pto"  every second character
```

`s[:i] + s[i:]` always equals `s`. The stop index is always excluded.

### Key string methods

| Method | What it does | Example result |
|---|---|---|
| `strip()` | remove surrounding whitespace | `" hi ".strip()` → `"hi"` |
| `split()` | split into list (whitespace by default) | `"a b".split()` → `["a", "b"]` |
| `",".join(items)` | join list into string | `",".join(["a","b"])` → `"a,b"` |
| `lower()` / `upper()` | case folding | `"Hi".lower()` → `"hi"` |
| `replace(a, b)` | swap substrings | `"cat".replace("c","r")` → `"rat"` |
| `count(x)` | count occurrences | `"bob".count("b")` → `2` |
| `find(x)` | index of first occurrence, `-1` if missing | `"abc".find("b")` → `1` |
| `startswith(x)` / `endswith(x)` | prefix/suffix check | `"py".endswith("y")` → `True` |
| `removeprefix(x)` / `removesuffix(x)` | delete prefix/suffix (3.9+) | `"Mr. X".removeprefix("Mr. ")` → `"X"` |

### f-string format specifiers

```python
price = 9.5
f"{price:>10}"      # right-align in 10 chars:  "       9.5"
f"{price:<10}"      # left-align
f"{price:^10}"      # center
f"{price:.2f}"      # two decimals: "9.50"
f"{price:010.2f}"   # zero-padded width 10: "0000009.50"
f"{price:>10.2f}"   # combine: "      9.50"

width, precision = 10, 4          # nested expressions in spec
f"{12345.6789:{width}.{precision}}"   # "   12346.0"
```

---

## Best Practice

- Precedence is for reading; **parentheses are for certainty**. When in doubt,
  `(a or b) and c` beats hoping.
- Never test `if x == True` — write `if x`. `if x is None`, never `== None`.
- Prefer `removeprefix`/`removesuffix` (3.9+) over `lstrip`/`rstrip` when
  deleting exact prefixes — `lstrip("Mr. ")` strips *character sets*, not the
  literal prefix.
- Use `in` over `find() != -1` for "is it in there?" — it reads as English.
- Build strings with `join`, not `+` in a loop (quadratic → linear).
- Use `and`/`or` for *selection*, not as cleverness the reader must decode.

---

## Common Mistakes

1. **`and`/`or` returning operands.** `print(5 and "no")` prints `no` — people
   expect a boolean. If you need a boolean, wrap in `bool()` or a comparison.
2. **`lstrip`/`strip` strip character sets.** `"bottle".strip("bo")` → `"ttle"`
   — it removes any leading/trailing character in the set, not the word "bo".
3. **Off-by-one slicing.** `s[0:2]` excludes index 2. The stop is never included.
4. **Trying to mutate a string.** `s[0] = "x"` → `TypeError`.
5. **`int("9.5")`** → `ValueError`. Use `float()` for decimals.
6. **Forgetting precedence in compound conditions.** `x or y == "a"` parses as
   `x or (y == "a")`, not `(x or y) == "a"`.
7. **`-1` from `find` used as an index.** `s[s.find("z")]` silently grabs the
   last character when "z" is absent.

---

## Applied AI Perspective

- **Tokenization**: `split()` is the first step of nearly every text pipeline —
  the poor man's tokenizer before you meet real ones.
- **Normalization**: `lower()`, `strip()`, `casefold()` dedupe
  "Hello"/"hello"/" hello " into the same token — critical for embeddings,
  search, and clustering.
- **Validation**: `in`, `startswith`, `chained comparisons` enforce data
  contracts (e.g. `0 <= temperature <= 45`) before a model sees bad data.
- **Masking/redaction**: `replace` is how you scrub PII like emails and phone
  numbers from training corpora.
- **Formatting output**: format specs build the neat tables and progress bars
  you see in MLOps tooling.

---

## Mini Summary

- Precedence: `**` > unary > `* / // %` > `+ -` > comparisons/`in` > `not` > `and` > `or`.
- `and`/`or` return operands; only `not` returns a boolean; both short-circuit.
- Comparisons chain: `0 <= x <= 100` is valid Python.
- `in` checks substrings; `"" in s` is always `True`.
- `+=` rebinds a new object; strings can never be mutated in place.
- Slicing: start included, stop excluded; `s[::-1]` reverses.
- `strip`/`split`/`join`/`replace`/`find`/`count` are the core text tools.
- Use `removeprefix`/`removesuffix` for exact prefix/suffix removal.
- Format specs: `{value:width.precision}` with `< ^ >` alignment.
- Prefer parentheses over memory when precedence is doubtful.
- Never `x == True`; use `x` or `x is True` — and `x is None` for None.
