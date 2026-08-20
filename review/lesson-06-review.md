# Lesson 6 Review — Collections

**Date:** 2026-08-13
**Score:** 90/100
**Topics:** lists, tuples, dicts, sets — alias/copy, membership, dict methods,
set algebra, nested collections, O(1) two-sum, dict-of-info CLI.

---

## Strengths

- **Exercises: perfect.** All 5 Easy, 3 Medium, and 2 Hard exercises produced
  byte-identical output on the first submission. Notably:
  - E1 alias-vs-copy verified with real mutation.
  - E2 swap via tuple unpacking (`b, a = a, b`) — the RHS is evaluated first,
    so it's a legit single-expression swap.
  - E3 correctly nailed the `92 in scores` trap (dicts check keys) and used
    `.values()` where required.
  - M3 built columns with the single nested comprehension as constrained.
  - H1 debug: all four bugs fixed in place with the required techniques
    (`.add()`, `set()`, fold-once, unpacking swap).
- **H2 two-sum: clean O(n) single-pass.** Set-based membership, correct
  (smaller, larger) ordering, `None` fallback. Interview-grade.
- **Excellent iterative debugging** on the challenge. Between review passes the
  learner fixed: `exist:` → `exists:`, `left:` → `left 6`, `{value:.2f}`
  formatting, space-joined categories, the invalid-command `continue`, and the
  low-stock filter (from wrong `min()` logic to a correct comprehension).
- Handlers return strings; only `main()`/`report()` print — the decomposition
  constraint held.

## Improvements

- **Guard against empty-state crashes.** `report()` on an empty inventory
  raised `UnboundLocalError` because `low_stock` was only bound inside the
  loop. Bind state *before* the loop (or compute after), and always provide a
  `none` fallback for list-style output.
- **Validate before you evaluate.** `float(price) <= 0` runs `float()` before
  the guard checks, so a non-numeric price crashed `main()` with `ValueError`.
  When an invalid input must not reach an operation, check what you can first
  (`qty.isdigit()`) and wrap risky conversions, then `continue` — don't let
  one bad line kill the whole session.
- **Place derived data outside loops.** The low-stock comprehension ran inside
  the per-product loop (recomputed on every iteration). Compute once, after
  the loop.
- **`min()` is not "filter then join".** `min(low_stock)` returned one name —
  the alphabetically smallest — instead of the full comma/space-separated
  low-stock list. A reduction (`min`) and a filter (`qty < 5`) are different
  operations.
- **Label exactly as spec'd** — `low stock:` not `low_stock:`; check the
  literal against the spec character-for-character.

## Suggestions

- `is_number()`-style guard helper: one small function that returns `True`/`False`
  for price validity would DRY the validation across `add`/`restock`/`sell`.
- Consider a `products.items()` iteration style in `report()` — it unpacks
  `name, product` directly and reads better than `products[name][...]` three
  times.
- The nested f-string `f"categories: {" ".join(...)}"` works on 3.12 (PEP 701)
  but is non-portable; building the joined string on its own line is safer
  for 3.11 and older.

## Learning Note

Sets are no longer a mystery: dedupe, O(1) membership, `& | - ^` algebra, and
the two-sum single-pass pattern are all in the toolkit now. The growth this
lesson was debugging discipline — the learner read their own output, chased
the failing case to the exact line, and fixed real bugs (the `min()` and the
empty-state crash) without hints. That is the habit the harder lessons are
training for.
