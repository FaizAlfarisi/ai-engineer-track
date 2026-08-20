# Lesson 6 — Collections

## Learning Objective

By the end of this lesson you can choose and drive Python's four built-in
collections deliberately: **lists** (ordered, mutable, duplicates), **tuples**
(fixed, immutable records), **dicts** (key → value lookup), and **sets**
(unique members, O(1) membership). You'll copy instead of alias, fold-and-count
case-insensitively, dedupe and combine with set algebra, build nested
structures, and know exactly when each collection is the right tool — the
vocabulary behind every data pipeline's data model.

---

## Motivation

Every program you've written so far stores things in *a* collection; this
lesson makes the choice deliberate. The difference between `[1, 2, 1]` and
`{1, 2}` isn't the brackets — it's the **guarantees**: order? duplicates?
mutation? O(1) membership? Choosing wrong costs correctness (aliasing bugs,
unhashable keys) or performance (`in` on a million-item list vs a set). In AI,
data is always shaped by collection choice: features as dicts, sequences as
lists, fixed metadata as tuples, unique IDs as sets.

---

## Mental Model

- **List** — a numbered shelf. Items stay in order, you can put duplicates up,
  and you can add/remove/replace at any position.
- **Tuple** — a sealed envelope with labeled slots. Order and contents are
  fixed once sealed — use it for records that shouldn't change (coordinates,
  `(name, score)`).
- **Dict** — a phonebook: you look people up *by name*, instantly. Order is
  insertion order; keys are unique; lookup is by key, not position.
- **Set** — a bouncer's guest list: only unique names, and "is this person on
  the list?" is answered instantly (O(1)). No order, no duplicates, no indexes.

```
LIST           TUPLE            DICT              SET
┌─┬─┬─┬─┐     ╔═══╦═══╦═══╗     key → value       { "ada",
│1│2│1│3│     ║ x ║ y ║ z ║     "ada" → 92        "ben",
└─┴─┴─┴─┘     ╚═══╩═══╩═══╝     "ben" → 88        "cyn" }
ordered       fixed            by-key lookup      unique only
duplicates    immutable        insertion-order    unordered
```

---

## Visualization

### Alias vs copy — the two-rooms trap

```
a = [1, 2, 3]
b = a            # two tags, ONE list  → mutating b moves a
c = a.copy()     # a second list       → mutating c leaves a alone
```

### `in` — where is it fast?

```
list of 1M names:  "cyn" in names   scans every slot   O(n)
set of 1M names:   "cyn" in names   hashes → instant   O(1)
dict keys:         "cyn" in d       hashes → instant   O(1)
```

### Set algebra — the Venn diagram in code

```
A = {"ada", "ben"}   B = {"ben", "cyn"}
A | B  union          {"ada", "ben", "cyn"}
A & B  intersection   {"ben"}
A - B  difference     {"ada"}
A ^ B  symmetric diff {"ada", "cyn"}
```

---

## Theory

### Aliasing: two names, one object

```python
original = [1, 2, 3]
alias = original          # alias and original are THE SAME list
alias.append(99)
print(original)           # [1, 2, 3, 99]  ← surprised?
```

Any mutation through one name is visible through the other. To get a separate
list: `copy = original.copy()` (or `list(original)`). For nested lists,
`.copy()` is still shallow — a shared inner list stays shared.

### `in` membership — pick by what it costs

```python
print(2 in [1, 2, 3])       # True  (scans)
print("b" in {"a": 1, "b": 2})   # True  — dicts check KEYS, not values
print(2 in {1, 2, 3})       # True  (hash, instant)
```

Dict `in` tests keys. To check a value, ask `d.values()` explicitly.

### dict methods that shape real code

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1     # .get: safe read with default
# {'b': 1, 'a': 3, 'n': 2}

groups = {}
for name, dept in [("ada", "eng"), ("ben", "ai")]:
    groups.setdefault(dept, []).append(name)   # setdefault: list-or-new
# {'eng': ['ada'], 'ai': ['ben']}
```

`d[k]` raises `KeyError` on a missing key. `d.get(k, default)` returns the
default instead. `d.setdefault(k, [])` returns the existing value or inserts a
fresh one — the one-liner for building "dict of lists" without an `if`.

### Sets: unique, unordered, O(1)

```python
unique = {3, 1, 3, 2, 1}     # {1, 2, 3} — duplicates collapse
print(3 in unique)           # True, instant
unique.add(4); unique.discard(2)   # discard won't raise if missing
```

`{}` is an **empty dict**. An empty set is `set()` — the classic one-char bug.
Sets can't hold lists or dicts (unhashable); they *can* hold tuples.

### Comprehensions for every collection

```python
squares = [n ** 2 for n in range(5)]        # list
even_nums = {n for n in range(10) if n % 2 == 0}   # SET comprehension
lengths = {w: len(w) for w in ["ada", "ben"]}       # dict comprehension
```

### `sorted()` — deterministic order for unordered things

```python
print(sorted({3, 1, 2}))       # [1, 2, 3] — sorted() returns a LIST
```

Sets are unordered, so printing them directly gives no guaranteed order.
`sorted()` makes output deterministic and testable — and doesn't mutate.

---

## Best Practice

- **Copy before mutating shared data**: `b = a.copy()` when you intend to edit
  one of them. Know whether a shared list is a bug or a feature.
- **Choose by guarantee, not convenience**: dict for by-key lookup, set for
  uniqueness + membership, list for ordered sequences, tuple for fixed records.
- **Check membership on a set, not a list**, when the collection is large and
  the check is hot.
- **`d.get` / `d.setdefault` over try/except and manual `if`** for dictionary
  reads and building "dict of lists".
- **`{}` is a dict, `set()` is a set.** Internalize it.
- **Fold once, reuse** (the standing pattern): `ch = ch.lower()` once before
  counting, then feed the folded value everywhere.
- **Use `sorted()` on sets for stable, testable output.**
- Understand shallow copy: `.copy()` on a list of lists doesn't deep-copy the
  inner lists.

---

## Common Mistakes

1. **Aliasing when you meant a copy.** `b = a` shares; `b.append` moves `a`.
   Mutation through an alias is invisible until a "surprise" in the original.
2. **`{}` instead of `set()`.** An empty dict is not a set — `.add()` then
   throws `AttributeError`, and membership semantics differ.
3. **Dict membership = keys, not values.** `2 in d` asks about keys; checking
   values silently returns `False`.
4. **Unhashable keys.** Lists and dicts can't be dict keys or set members
   (`TypeError: unhashable type`). Use tuples for composite keys.
5. **Mutating a collection while iterating it** (Lesson 4 callback): deleting
   items shifts indexes and skips elements. Iterate a copy.
6. **Trusting set order.** Sets are unordered — code that assumes an order
   passes sometimes, fails occasionally. Sort before printing.
7. **`KeyError` crashes.** `d[k]` on a missing key throws; `d.get(k, default)`
   doesn't.
8. **Forgetting `values()`/`items()`.** `for k in d` iterates keys only;
   reaching values needs `d[k]`, `d.values()`, or `d.items()`.

---

## Applied AI Perspective

- **Data rows as tuples, not lists**: fixed-column records (`(id, name, label)`)
  — immutable, hashable, cheap. Libraries return tuples for fixed shapes.
- **Features as dicts**: `{"age": 32, "income": 5.4}` — keyed access, sparse
  fields via `.get`, and natural JSON mapping (Stage 2).
- **Unique IDs as sets**: O(1) "have I seen this sample?" — the dedupe guard
  before training; intersection/union are cohort comparisons.
- **Folds and aggregates**: `dict.get` counting is the same accumulator
  pattern as token frequency, class counts, and histogram building.
- **Batch lookup**: model predictions keyed by sample ID in a dict make
  evaluation a loop of O(1) lookups instead of O(n²) scans.
- **Set algebra on labels**: which classes appear in both train and test?
  `set(train_labels) & set(test_labels)` — one line.

---

## Mini Summary

- List = ordered shelf (mutable, duplicates OK); tuple = sealed envelope
  (immutable record); dict = phonebook (key → value); set = guest list
  (unique, unordered).
- `b = a` aliases (one object); `b = a.copy()` makes a second list.
- `in` on a set/dict keys is O(1); on a list it's O(n).
- Dict `in` checks keys — ask for `.values()` explicitly to check values.
- `d.get(k, dflt)` reads safely; `d.setdefault(k, [])` builds dicts of lists.
- `{}` is a dict; an empty set is `set()`.
- Sets can't contain unhashable items (lists/dicts); tuples are fine.
- Comprehensions build lists, sets, and dicts — same shape, different brackets.
- `sorted()` gives deterministic order for sets (returns a list).
- Fold once, reuse; never mutate while iterating; choose by guarantee.
