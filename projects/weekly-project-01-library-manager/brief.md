# Weekly Project 1 — Library Manager CLI

## Type

[REAL-WORLD]

## Problem

A small community library tracks its books on paper. They want a
command-line tool so staff can add, find, and remove books and keep the
collection saved between sessions. The tool must be small enough for one
person to run, and reliable enough that a typo never crashes it.

A book has: **title**, **author**, **year**, **genre**.

## Requirements

1. **add** — add a book:
   `python solution.py add "The Fellowship of the Ring" Tolkien 1954 Fantasy`
   - Title and author must not be blank; the year must be a sensible
     number; genre is optional (use a default when missing).
   - Reject a duplicate title with a clear message.
2. **remove "TITLE"** — remove a book by its title. Matching is
   case-insensitive (extra spaces trimmed). Removing a title that does
   not exist gives a clear message.
3. **search "TEXT"** — list every book whose title or author contains
   the text, case-insensitive. No matches → a clear "no books found"
   message.
4. **list** — show all books sorted by title, in a defined column layout
   (exact output format is in the Acceptance Criteria).
5. The collection survives restarts: add some books, run again in a
   fresh command, still there.

## Constraints

- Use only topics covered so far through Lesson 11. No new libraries
  beyond what has already been drilled (no CSV, no classes).
- Data persists as JSON, read/written through pathlib with
  `encoding="utf-8"`.
- Loaders follow the L9/L11 contract: clean data in, raise on bad input
  — never return an error string.
- Edge cases handled, never a raw crash: corrupt data file, missing data
  file, blank input.
- Organize into functions and modules where it genuinely helps
  readability. Handle input from `sys.argv`.
- Git commit at meaningful milestones.

## Acceptance Criteria

- [ ] Add three books, then `list` in a fresh process — all three
      present, sorted by title, byte-exact to the spec block below.
- [ ] Duplicate title is rejected; collection unchanged.
- [ ] Run with no data file — works, list shows empty, adding a book
      creates the file.
- [ ] Corrupt the data file by hand — program reports it clearly and
      exits cleanly (no traceback, no data loss).
- [ ] `search` matches title and author case-insensitively; the "no
      books found" message is exact.
- [ ] `remove` works on a real title and gives a clear message for a
      missing one.
- [ ] No loader returns an error string.
- [ ] `git log` shows more than one commit.

## Spec output block for `list`

```text
Books (3):
1. The Fellowship of the Ring — Tolkien (1954) [Fantasy]
2. The Two Towers — Tolkien (1954) [Fantasy]
3. The Return of the King — Tolkien (1954) [Fantasy]
```

## Stretch Goals (optional)

- A `count-by-genre` report.
- A `data/` subfolder for storage.
- Keep books in a stable order regardless of the order they were added
  (think about what your collection guarantees).

## Deliverables

- Source code (`solution.py` starts blank — learner writes all)
- Short README
- Technical reflection (technical template)

## Decisions Log (filled by learner during build)

| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
|          |     |                        |

NO step-by-step plan is provided. The AI clarifies requirements and
reviews code — it never implements.