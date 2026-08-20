# Lesson 4 — Loops

## Learning Objective

By the end of this lesson you can make your programs *repeat*: iterate over
sequences with `for`, drive loops by a condition with `while`, control the
flow with `break`/`continue`, use loop `else` as the "was it found?" idiom,
pair indexes with values via `enumerate()` and `zip()`, and rewrite loops as
comprehensions — building the accumulators, filters, and reports behind every
batch process and data pipeline.

---

## Motivation

You have been writing `for`/`range` ad hoc since Lesson 1 — now it becomes
deliberate. Repetition is where data work actually happens: iterating over
batches of records, accumulating sums and counts, filtering rows, pairing
features with labels. A program that can loop is a program that can process a
thousand records instead of one. And a program that loops *wrong* is where
off-by-one bugs, infinite loops, and silent data corruption are born — which
is exactly why this lesson's debugging drill exists.

---

## Mental Model

A `for` loop is a **conveyor belt**: each item in a sequence arrives once, in
order, and your block handles it before the next arrives. When the belt is
empty, the loop is over.

```
for item in ["a", "b", "c"]:
    ...      ┌─────┬─────┬─────┐
             │ "a" │ "b" │ "c" │   → one visit each, left to right
             └─────┴─────┴─────┘
```

A `while` loop is a **bouncer at a door**: as long as the condition is truthy,
it lets one more person in. Someone must eventually make the condition false,
or the queue is infinite.

```
while condition:        condition truthy? ──yes→ body → re-check
    body                    ↑                    │
                            └────── condition false → loop ends
```

`range` is a **numbered ticket dispenser** that never hands out the stop
number — same ruler as slicing, stop always excluded.

---

## Visualization

`range` — stop excluded (the slicing ruler, again):

```
range(5)         → 0 1 2 3 4           # not 5!
range(1, 10, 2)  → 1 3 5 7 9           # start, stop(excl), step
range(10, 0, -2) → 10 8 6 4 2          # negative step counts down
```

Loop `else` — the "found / not found" switch:

```
for item in items:
    if item == target:
        print("found")
        break            # ← found → break, else SKIPPED
else:
    print("not found")   # ← only runs if NO break happened
```

`enumerate` — index and value at once:

```
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)
# 0 tic / 1 tac / 2 toe
```

`zip` — two belts side by side, paired item by item:

```
for name, score in zip(["ada", "ben"], [88, 92]):
    print(name, score)      # ada 88 / ben 92
```

---

## Theory

### `for` — iterate items, not indexes

```python
word = "python"
for char in word:
    print(char)                  # p y t h o n — one visit each

words = ["cat", "window"]
for w in words:
    print(w, len(w))             # cat 3 / window 6
```

Python's `for` walks the *items* of any sequence, in order. You almost never
need an index. When you do, reach for `enumerate`.

### `range()` — the numbered ticket dispenser

```python
list(range(5))          # [0, 1, 2, 3, 4]     stop excluded
list(range(5, 10))      # [5, 6, 7, 8, 9]     start at 5
list(range(0, 10, 3))   # [0, 3, 6, 9]        step 3
list(range(10, 0, -2))  # [10, 8, 6, 4, 2]    negative step
```

Sum of 1..n with an accumulator — the pattern you'll use everywhere:

```python
total = 0
for n in range(1, 11):      # 1..10, stop 11 excluded
    total += n              # accumulate
print(total)                # 55
```

### `while` — condition-driven

Use `while` when you don't know in advance how many times you'll loop:

```python
count = 0
while count < 3:
    print(count)
    count += 1              # ← the progress step. Without it: infinite loop
```

The loop only ends if the body makes progress toward falsifying the
condition. Forgetting the step is the classic infinite-loop bug.

### `break` / `continue` / loop `else`

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n // x)
            break            # exits the INNERMOST loop only
    else:
        print(n, "is prime") # ran because the inner loop never broke
```

- `break` exits the innermost loop immediately.
- `continue` skips the rest of the current iteration and moves to the next.
- **loop `else`** runs only if the loop ended WITHOUT a `break`. This is the
  canonical "was it found?" / "is it prime?" idiom — no flag variable needed.

### `enumerate()` / `zip()` — looping techniques

```python
names = ["ada", "ben", "cyn"]
for i, name in enumerate(names):     # index AND value
    print(f"{i}: {name}")

features = [0.5, 1.0, 2.0]
labels = [0, 1, 1]
for x, y in zip(features, labels):   # parallel pairing
    print(x, y)
```

`enumerate` replaces the `range(len(x))` anti-pattern. `zip` pairs two
sequences and stops at the shorter one.

### Comprehensions — a loop that returns a value

```python
squares = [n ** 2 for n in range(1, 6)]          # [1, 4, 9, 16, 25]
evens = [n for n in range(10) if n % 2 == 0]      # [0, 2, 4, 6, 8]
pairs = [(i, s) for i, s in enumerate("abc")]     # [(0,'a'), (1,'b'), (2,'c')]
lengths = {w: len(w) for w in names}              # dict comprehension
```

Shape: `[expression for target in iterable if condition]`. It's a loop whose
result *is* a value. Same parts as the loop you already write — order of
`for`/`if` is the same as the nested-loop equivalent.

Prefer a comprehension when you're *building a collection*. Prefer an
explicit loop when you have side effects (`print`) or complex multi-step
logic per item. The official docs: prefer built-ins (`zip`) over complex
nested comprehensions.

### Never mutate what you're iterating

```python
users = {"ada": "active", "ben": "inactive"}
for name in users.copy():          # iterate over a COPY
    if users[name] == "inactive":
        del users[name]            # safe: loop is reading the copy
```

Deleting or adding to a collection while looping over it is a real bug
source. Loop over a copy, or build a new collection.

---

## Best Practice

- Iterate items, not indexes: `for x in seq`, not `for i in range(len(seq))`.
- When you need the index, `enumerate(seq)`.
- Prefer `for` when you know the sequence; use `while` only for
  condition-driven repetition (sentinel loops, polling).
- Guard your `while`s: make sure the body moves the condition toward False.
- Use loop `else` for "found / not found" — it removes flag variables.
- Use a comprehension to build a collection; keep explicit loops for side
  effects.
- Fold once, reuse: lowercase/copy your data before the loop, not inside it.
- `break` only exits the innermost loop — know which loop you're in.

---

## Common Mistakes

1. **Off-by-one in `range`.** `range(n)` is `0..n-1`. `sum(range(1, n+1))`
   for 1..n. Stop is always excluded — the slicing ruler.
2. **Infinite `while`.** Missing `count += 1`, or a condition that can never
   become False. Your program hangs; there is no error message.
3. **Mutating while iterating.** Deleting items from a list you're looping
   over skips elements. Loop over a copy.
4. **`break` escaping the wrong loop.** `break` exits only the innermost
   loop — a nested loop's `break` doesn't stop the outer one.
5. **Misplacing loop `else`.** It belongs to the loop, not the last `if`.
   It runs only when no `break` fired.
6. **Accumulator reset inside the loop.** `total = 0` must live BEFORE the
   loop, or every iteration starts over.
7. **`continue` skipping needed work.** Placement after the work, not before.
8. **Comprehension overkill.** A 40-character nested comprehension that
   could be `zip` or an explicit loop — readability wins.

---

## Applied AI Perspective

- **Batch iteration**: training loops iterate epochs; each epoch iterates
  batches. Accumulators (`total_loss`, `correct`) are exactly the pattern in
  this lesson.
- **Metrics accumulation**: sums, counts, min/max over a dataset — the
  accumulator pattern.
- **Parallel sequences**: `zip(features, labels)` pairs inputs with targets;
  `enumerate` tracks sample indexes.
- **Filtering pipelines**: comprehensions with `if` are the declarative form
  of row filtering before a model sees data.
- **"Found" search patterns**: loop `else` is how retrieval and validation
  answer "does this exist?" without a flag.
- **Streaming / generators**: `for x in stream` iterates one item at a time —
  the same loop shape processes infinite data sources.

---

## Mini Summary

- `for` iterates the *items* of any sequence, in order.
- `range(start, stop, step)` — stop excluded; negative step counts down.
- Accumulator: `total = 0` before the loop, `total += x` inside.
- `while` is condition-driven; the body must make progress or it hangs.
- `break` exits the innermost loop; `continue` jumps to the next iteration.
- Loop `else` runs only if no `break` fired — the "not found" idiom.
- `enumerate(seq)` gives `(index, value)`; `zip(a, b)` pairs in parallel.
- Comprehension `[expr for x in seq if cond]` builds a collection.
- Prefer comprehensions for building, loops for side effects.
- Never mutate a collection while iterating it — loop over a copy.
