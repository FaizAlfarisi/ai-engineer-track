# Weekly Project 1 — Library Manager CLI

**Reviewer:** AI Mentor
**Date:** 2026-09-02
**Hint Dependency:** Level 1 (decision-direction at project start; no code hints during build)
**Independent Fix Ratio:** 9/9 issues found by reviewer

---

## Strengths

**1. Clean module separation with real reasoning behind it.** Each action
lives in its own file, shared logic in `helper.py`, custom exceptions in
`custom_error.py`. The decision log shows *why* — not just what. That's
engineering thinking, not just coding. The `map_action` dispatcher in
`solution.py` is readable at a glance.

**2. The custom exception split is the right abstraction.** `ErrorBadRequest`
(user input) vs `ErrorCorruptData` (data file) are genuinely different
failure modes, and the L11 contract is applied: loaders raise on bad
data, never return error strings. The `load_json` function follows this
well.

**3. Good use of sets for duplicate checking** (`service_add.py:18`).
O(1) lookup is the right choice here, and the decision log explains the
alternative you considered. The `match` dispatch in `solution.py` is
idiomatic and clean.

---

## Issues

Nine things to work through, ordered from most to least serious.

---

### Issue 1 — `search` uses `==` instead of `in`

**Expected concept:** the brief says "list every book whose title or
author **contains** the text."

**Observed result:** `service_search.py:9` does
`book["title"].lower() == search_text` — exact match, not substring
containment.

**Question:** if you search `"the"` and you have "The Fellowship of
the Ring," does `"the fellowship of the ring" == "the"` ever return
True?

This is the most important bug in the project. It means search will
fail for almost every real query that isn't a perfect title/author
match.

---

### Issue 2 — `list` output does not match the spec block

**Expected concept:** Acceptance Criteria says "byte-exact to the spec
block below."

**Observed result:** `service_show_list.py:7-8` appends
`count_by_genre(data)` to the list output. The actual output is:

```text
Books (3):
1. The Fellowship of the Ring — Tolkien (1954) [Fantasy]
2. The Two Towers — Tolkien (1954) [Fantasy]
3. The Return of the King — Tolkien (1954) [Fantasy]
Genres (1):
1. Fantasy: 3
```

The spec block has only the `Books (N):` section. Two extra lines that
weren't requested.

**Question:** when `count_by_genre` was built as a stretch goal, what
made the decision to attach it to `list` rather than making it a
separate command? Does the spec block say `Genres (N):` anywhere?

This is a spec-literalness issue — the same pattern that haunted you
in L8 and L9. The habit held for exercise blocks in L10/L11, but it
slipped here at the project level.

---

### Issue 3 — `path.is_file` without parentheses (`helper.py:40`)

**Expected concept:** `path.is_file` is a bound method reference
(truthy), not a call.

**Observed result:** `not path.is_file` is always `False`. The guard
only checks `path.exists()`. A directory named `library_data.json`
would pass through to `path.read_text()` and crash with
`IsADirectoryError` (Linux) or `PermissionError` (Windows) — not
caught by `json.JSONDecodeError`.

**Question:** this is the same L10 H1 bug pattern — `.is_dir()` without
parentheses. Did you catch it there but miss it here? What made the
difference?

---

### Issue 4 — `add` duplicate check is case-sensitive; `remove` is not

**Expected concept:** if "The Ring" exists and you `add "the ring"`,
the duplicate check passes (set has `"The Ring"`). But
`remove "the ring"` finds it. The two commands disagree on what "the
same title" means.

**Observed result:** `service_add.py:20` does `title in existing_title`
(raw case). `service_remove.py:12` does
`book["title"].lower() == title` (lowered).

**Question:** which case is the source of truth — add's or remove's?
If a user adds "the ring" (different case), they now have two books
that remove treats as one.

---

### Issue 5 — `service_add.py:1` imports from `solution.py` instead of
`custom_error.py`

**Expected concept:** `ErrorBadRequest` lives in `custom_error.py`.
All other service modules import from there.

**Observed result:** `service_add.py` does
`from solution import ErrorBadRequest`. This creates a circular
dependency path: `solution.py` imports `service_add`, which imports
`solution`.

**Question:** `service_remove.py:1` and `service_search.py:1` both
import from `custom_error` correctly. What made `service_add` different?

---

### Issue 6 — `remove` and `search` crash with `IndexError` when no
title argument given

**Expected concept:** `python solution.py remove` (no title) →
`args[2:]` is `[]` → `raw[0]` raises `IndexError`.

**Observed result:** The `except Exception` catch-all in
`solution.py:39` catches it and prints "Unexpected error: ..." — but
the message is unhelpful and the pattern is wrong. Each service should
validate its own args.

**Question:** `add` validates arg count before doing anything. Why
don't `remove` and `search`?

---

### Issue 7 — `search` raises `ErrorBadRequest` for "no books found"

**Expected concept:** no matching books is a legitimate search result,
not a bad request.

**Observed result:** `service_search.py:12` raises
`ErrorBadRequest("no books found")`, which gets caught in `solution.py`
and printed as `"bad request:\nno books found"`.

**Question:** if a user searches and gets "bad request" for a
perfectly valid query that just returned no results, what does that
communicate about the tool's quality?

---

### Issue 8 — `search_index` field is dead data

**Observed result:** `service_add.py:28` creates
`new_data["search_index"] = f"{author} | {title}"` for every book,
stored in JSON. But `service_search.py` never reads it — it iterates
and checks `title.lower()` and `author.lower()` directly.

**Question:** what happens to a field that's written to every record
but never read? What does that cost in disk, in cognitive load, and in
the next person maintaining this?

---

### Issue 9 — `write_json` ends with an explicit `return`
(`helper.py:49`)

**Observed result:** bare `return` at the end of a void function.
Python functions return `None` implicitly. The explicit `return`
signals intent to return something, but it returns nothing.

**Question:** what does an explicit `return` at the end of a function
communicate to the next reader?

---

## Refactoring Suggestions

1. **Search: `==` → `in`** — this is a fix, not a refactor. Change
   the match operator.
2. **Attach `count_by_genre` to a new `genres` command** rather than
   `list`. Keeps the spec block clean. `map_action` gets one new case.
3. **Fix `path.is_file` → `path.is_file()`** — one character. The
   silent failure is worse than a crash.
4. **Normalize case on add** — lowercase the title before storing or
   before comparison, so add and remove agree.
5. **Import from `custom_error` in `service_add`** — breaks the
   circular path. One-line fix.
6. **Validate arg count in `remove` and `search`** — same pattern as
   `add`: `if len(raw) < 1: raise ErrorBadRequest(...)`.
7. **Delete `search_index`** — dead code in data is dead weight.
8. **Omit the `return`** in `write_json`.

---

## Learning Notes

**Working output with broken reasoning is a fail; correct reasoning
with a small bug is a win.** The architecture, the module split, the
error abstraction, the decision log — that's strong reasoning. The bugs
are all fixable. The concerning pattern is the *same class of bug
repeating*: `is_file` without parentheses (L10 H1 bug, now in a new
file), case sensitivity inconsistency between add and remove (L3
validation pattern revisited), and spec-literalness slipping at the
project level after holding for exercises. Each of these was a lesson
you already learned. The question for next time: how do you build a
*check* that catches these before they ship? A short self-review pass
— "does every method call have parens?" "does every case-sensitive
comparison have a reason?" — would catch three of these nine issues
before the code leaves your hands.

---

## Final Score

| Dimension       | Score  |
|-----------------|--------|
| Correctness     | 16/25  |
| Logic           | 15/20  |
| Readability     | 13/15  |
| Naming          | 8/10   |
| Maintainability | 7/10   |
| Pythonic Style  | 7/10   |
| Performance     | 4/5    |
| Testing         | 0/5    |
| **Overall**     | **70/100** |

**Spec-literalness:** `list` output does not match spec block (genres
appended). Search output uses `==` instead of `in` (correctness miss,
not just format). The L10/L11 byte-exact streak slipped at project
scale.

---

## Second-Pass Verification (2026-09-02)

| # | Issue | Status | Fix |
|---|-------|--------|-----|
| 1 | search `==` → `in` | ✅ | Uses `search_index` with `in`; stored lowered |
| 2 | list spec-literalness | ✅ | `genres` is a separate command; `list` matches spec block |
| 3 | `is_file()` parens | ✅ | `path.is_file()` with call |
| 4 | case-sensitive duplicate | ✅ | Both sides `.lower()` in add; consistent with remove |
| 5 | circular import | ✅ | `service_add.py` imports from `custom_error` |
| 6 | IndexError on missing args | ✅ | Dedicated `except IndexError` in `solution.py:41-42`; empty-input checks in remove/search |
| 7 | no-results error framing | ✅ | Prints directly, no exception |
| 8 | search_index | ✅ | Kept and wired up; stored lowered; used in search |
| 9 | explicit return | ✅ | Removed entirely |

**All nine issues resolved.**

### Updated Score

The fixes addressed two correctness bugs (search `==`, spec block), two
consistency issues (case sensitivity, circular import), one silent
failure (`is_file`), one error-handling gap (IndexError), one error
framing issue (no-results), and one dead-data decision (search_index →
kept and used). Each fix was independent and targeted.

| Dimension       | First Pass | Second Pass |
|-----------------|------------|-------------|
| Correctness     | 16/25      | 23/25       |
| Logic           | 15/20      | 18/20       |
| Readability     | 13/15      | 14/15       |
| Naming          | 8/10       | 9/10        |
| Maintainability | 7/10       | 9/10        |
| Pythonic Style  | 7/10       | 8/10        |
| Performance     | 4/5        | 4/5         |
| Testing         | 0/5        | 0/5         |
| **Overall**     | **70/100** | **85/100**  |

**Independent fix ratio:** 9/9 fixes applied independently by the
learner after reviewer guidance.