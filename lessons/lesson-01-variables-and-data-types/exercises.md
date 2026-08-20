# Lesson 1 — Exercises

## Easy

### E1 — First Binding

Bind your age to a variable and your name to another. Print both with an
f-string: `"My name is X and I am Y years old."`

### E2 — Type Reporter

Create three variables holding an `int`, a `str`, and a `bool`. Print the type
of each with `type()`.

### E3 — Type Check

Without running code, predict: `type(3.0)`, `type(3)`, `type("3")`. Then verify
with `type()`.

### E4 — Swap Values

`a = 5` and `b = 10`. Swap them so `a == 10` and `b == 5`. Python has a trick.

### E5 — Lengths

Assign `greeting = "hello"` and print its length, its first character, and its
last character using the shortest expressions you know.

## Medium

### M1 — Rectangle Calculator

Prompt the user for width and height. Compute area and perimeter. Print with
one f-string each. Handle the fact that `input()` returns strings.

### M2 — Age in Days

Ask the user for their age, convert it to an `int`, compute the number of days
(ignore leap years), and print the result with an f-string.

### M3 — Tip Calculator

Ask for the bill amount (`float`) and the tip percentage (`float`). Compute the
tip and the total, rounded to 2 decimals, and print both.

## Hard

### H1 — Type Detective

Given `values = [1, 2.5, "3", True, None]`, write a loop-free program that
prints each value and its type on one line, e.g.
`1 -> <class 'int'>`. Then explain why `type(True)` is what it is.

### H2 — FizzBuzz Data

**The labelling rule (classic FizzBuzz)**

For a number `n`:

- if `n` is divisible by **3** → label is `"fizz"`
- if `n` is divisible by **5** → label is `"buzz"`
- if `n` is divisible by **both 3 and 5** → label is `"fizzbuzz"`
- if `n` is divisible by **neither** → label is the number itself

So `3` → fizz, `5` → buzz, `15` → fizzbuzz, `4` → 4.

**Your task**

For each number **1 to 15**, print one line of the form:
`<number>  <even?>  <label>`

where `<even?>` is `True`/`False` and `<label>` follows the rule above.

Example lines:

```
1  False  1
3  False  fizz
5  False  buzz
6  True   fizz
15 True   fizzbuzz
```

**Constraints**

No `if` statements. You may use `%`, `==`, `*`, `+`, and `or`.

Hint: `bool` is a subclass of `int` — `True` behaves as `1`, `False` as `0`.
What does `True * "fizz"` produce? What does `False * "fizz"` produce?

For the 1–15 repetition: writing 15 lines is fine (Loops is a later lesson) —
or use `for n in range(1, 16):` if you already know it.
