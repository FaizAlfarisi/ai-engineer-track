# Lesson 26 — Regex (Tier: SUPPORTING)

Stage 3, tenth topic. You have parsed logs with `in`, `split`, and
`strip` since Lesson 9. This lesson replaces string luck with shape:
patterns that match what you mean, capture what you need, and fail
loudly on what you don't.

SUPPORTING tier — Level 3 bar: write and apply patterns independently
on real text. One focused sitting, then the skill transfers into the
Stage project (log parsing, input validation, report extraction) and
every dirty-text pipeline after it.

Business domain for this lesson is fresh: the log-pattern extractor.
No publishers, no telemetry, no clinic. New business, same engineering
discipline.

---

## Objective

By the end of this lesson you can:

- Compile patterns with `re.compile` and choose `search` vs `match`
  vs `fullmatch` vs `findall`/`finditer` deliberately.
- Capture groups honestly and convert captures at the boundary.
- Apply `re.IGNORECASE` and `re.MULTILINE` where the data demands it.
- Validate lines with anchored patterns and exact error messages.
- Name lookahead/lookbehind, backreferences, and catastrophic
  backtracking as deliberate omissions — recognized, not drilled.

---

## Why This Matters

The extractor reads last night's service log and counts incidents.
Version 1 uses substring checks: `"alert" in line`. Last week a deploy
note said "alert system rebooted" and the incident count jumped by one
— a line about the alert system counted as an alert. The week before,
`"ERROR:disk full"` (no space) slipped past a split-on-space parser.
The week before that, `"error"` in lowercase missed a case-sensitive
filter entirely.

Why are the previous tools insufficient? Substring matching cannot say
*where* a word sits (prefix vs anywhere). Splitting cannot survive
format drift (one space vs two, colon vs dash). Case-folding by hand
forgets once per dozen call sites.

What capability do we need? Describe the *shape* of a valid line once
— anchored, grouped, flagged — and let the engine enforce it the same
way on every line.

What feature provides it? Regular expressions: a compiled pattern that
matches shape, captures fields, and rejects rot with one verdict.

Practical consequence — what breaks without it? The overcount class:
green drivers on well-formed fixtures, wrong counts on adversarial
text. The H1 drill plants exactly it.

Urgency, stated plainly: every report you have shipped since Lesson 9
parses text. Regex is what makes those parsers survive contact with
real logs. Ten lines of pattern replace a hundred lines of brittle
slicing.

Deliberate omissions: lookahead/lookbehind (zero-width assertions —
real, deferred); backreferences (`\1` — real, deferred); catastrophic
backtracking internals (named so you respect greedy quantifiers, not
drilled); `re.VERBOSE` deep use (sighted only).

---

## Mental Model

A regex is a **stencil laid over the line**.

```text
line:    "error 12: disk full"
stencil: ^error (\d+): (.+)$
          ^      ^      ^
          |      |      +-- capture the message
          |      +-- capture the id
          +-- anchor: must start here ($: must end here)
```

Three rules run everything:

1. The engine tries to fit the stencil somewhere (`search`), at the
   start (`match`), or over the whole line (`fullmatch`). Same
   stencil, three different questions — pick the question deliberately.
2. Parentheses capture: whatever fits inside comes back as data.
   The pattern validates shape; the groups deliver fields.
3. Flags change the light: `IGNORECASE` folds case, `MULTILINE`
   makes `^`/`$` see line edges inside a block.

---

## Core Concept

### 1. Compile once, ask three questions (`search`/`match`/`fullmatch`)

Problem: bare `re.search(pattern, line)` recompiles the pattern on
every call and buries the *question* inside a one-off call.

Why one-off calls are insufficient: a parser applies the same shape
to thousands of lines. Recompiling per line wastes work; worse, the
call site never states whether it wants *anywhere*, *start*, or
*whole*.

Capability needed: one compiled object, three explicit questions.

Feature: `PAT = re.compile(r"...")`, then `PAT.search(line)`
(anywhere), `PAT.match(line)` (start), `PAT.fullmatch(line)`
(whole line, no leftovers).

```python
import re

ERROR = re.compile(r"error (\d+): (.+)")
ERROR.search("xx error 12: disk full")    # Match — found anywhere
ERROR.match("error 12: disk full")        # Match — starts here
ERROR.fullmatch("error 12: disk full")    # Match — nothing left over
ERROR.fullmatch("error 12: disk full!")   # still Match (.+ eats "!")
```

Consequence of missing this: `match` used where `search` was meant
silently drops mid-line hits; `search` used where `fullmatch` was
meant silently accepts trailing rot.

### 2. Groups capture; the boundary converts (the honest contract)

Problem: a match tells you *that* a line fits. Reports need *fields*
— the id, the value, the message.

Why slicing captures is insufficient: fixed offsets die on the first
format drift. The capture must ride the same shape that validated.

Capability needed: shape and extraction in one act.

Feature: parentheses. `m.group(1)`, `m.group(2)` return the captured
text; conversion (`int()`, `float()`) happens at the boundary with
exact errors, per L8 habits.

```python
m = ERROR.fullmatch("error 12: disk full")
m.group(1)   # "12" — still text; int() it where it enters
m.group(2)   # "disk full"
```

Consequence of missing this: captures trusted as numbers without
conversion discipline — the annotation-honesty class in new clothes.

### 3. Greed is the default; anchors are the leash (the overcapture trap)

Problem: `r"error (.+)"` on `"error 1: x, error 2: y"` captures
`"1: x, error 2: y"` — `.+` eats to the last possible end.

Why `.+` fails silently: greedy quantifiers match *maximally* while
still fitting. Fixtures with one incident per line never reveal it;
real logs with two do.

Capability needed: bound the capture — by shape (`\d+`, `[^,]+`) or
by anchors (`^...$` forcing whole-line intent).

Feature: prefer precise atoms (`\d+` for ids, `[^\n]+` for messages
within a line), anchor validation patterns (`^...$`), and reach for
non-greedy (`.+?`) only with a stated reason.

Consequence of missing this (Pitfall 1, H1 plants it): overcapture
that is byte-exact on every single-incident fixture and wrong on the
first doubled line.

### 4. Flags: case and lines (data-driven, never decorative)

Problem: `"ERROR"` vs `"error"`; one giant block vs line-by-line.
Hard-coding both casings doubles every pattern; splitting blocks by
hand re-implements line semantics.

Why manual folding is insufficient: `line.lower()` before matching
destroys the original for capture, and forgets once per dozen sites.

Capability needed: engine-level case folding and line-aware anchors.

Feature: `re.compile(r"error", re.IGNORECASE)` matches all casings
while capturing original text; `re.compile(r"^error", re.MULTILINE)`
lets `^` match at every line start inside a block.

```python
import re
E = re.compile(r"^error (\d+)", re.IGNORECASE | re.MULTILINE)
E.findall("ERROR 1\nok\nError 2")   # ["1", "2"] — case folded, lines seen
```

Consequence: flags stated at compile time, visible to every reader —
never a silent `.lower()` three lines above the match.

### 5. `findall`/`finditer`: harvest loops (the assessable habit)

Problem: `search` finds one; reports need all — so authors loop
`search` with advancing offsets and go off-by-one.

Why hand loops are insufficient: offset bookkeeping is exactly the
manual-cursor class L23 retired.

Capability needed: iterate all non-overlapping matches directly.

Feature: `PAT.findall(text)` (list of captures) and
`PAT.finditer(text)` (lazy match objects, L24 posture honored).

```python
E = re.compile(r"error (\d+)")
E.findall("error 1 ok error 2")   # ["1", "2"]
```

Consequence: no offsets, no cursors, no off-by-one — the engine owns
the walk.

### 6. Validate with anchored patterns (boundary discipline, new tool)

Problem: streams carry rot (blank lines, truncated writes, version
headers). Business logic must never see unvalidated text.

Why substring validation is insufficient: `"error" in line` admits
the reboot note. Only a full-shape verdict separates signal from rot.

Capability needed: accept-or-reject per line with exact messages.

Feature: `fullmatch` as the gate — match returns the fields, `None`
returns the rejection path:

```python
LINE = re.compile(r"(error|skip) (\d+): (.+)")
def parse(line):
    m = LINE.fullmatch(line.strip())
    if m is None:
        raise ValueError("invalid line: bad shape")
    return m.group(1), int(m.group(2)), m.group(3)
```

Consequence: rot rejected where it enters, with verbatim messages —
L8 habits, new engine.

---

## Practical Examples

Example A — the three questions, one stencil (E1 is this):

```python
import re

PING = re.compile(r"ping (\d+)")
PING.search("xx ping 3 yy").group(1)      # "3" — anywhere
PING.match("ping 3").group(1)             # "3" — at start
PING.fullmatch("ping 3").group(1)         # "3" — whole line
PING.fullmatch("ping 3!")                 # None — leftover "!" rejected
```

Example B — capture + convert at the boundary:

```python
import re

READING = re.compile(r"temp (-?\d+(?:\.\d+)?)")
m = READING.fullmatch("temp 41.5")
value = float(m.group(1))   # 41.5 — conversion where it enters
```

Example C — flags on real log text:

```python
import re

E = re.compile(r"^error (\d+): (.+)$", re.IGNORECASE | re.MULTILINE)
E.findall("ERROR 1: disk full\nok\nError 2: net down")
# [("1", "disk full"), ("2", "net down")]
```

(`(?:...)` is a non-capturing group — taught here, first use in M1:
groups without capturing, so `group(1)` stays the field you want.)

---

## Engineering Notes

- **Compile at module scope.** Patterns are constants: `NAME =
  re.compile(...)` at the top, used everywhere. Never recompile per
  line, never inline raw strings at call sites.
- **Raw strings always.** `r"\d+"` — without the `r`, `\d` is an
  invalid escape today and a deprecation warning tomorrow.
- **Anchor validation patterns.** Gates use `fullmatch` (or explicit
  `^...$`); `search` is for finding, never for validating.
- **Escape literal dots.** `r"v1\.2"` — an unescaped `.` matches
  anything, including the `v1x2` that ships at 2 AM (Pitfall 3).
- **Prefer precise atoms over `.+`.** `\d+`, `[^\n,]+`, `\S+` —
  greed is a todo, not a default.
- **Convert captures at entry.** `int(m.group(1))` where the value
  crosses into logic; exact errors on failure.
- **Annotate patterns as what they are:**

```python
import re
from collections.abc import Iterator

LINE: re.Pattern[str] = re.compile(r"(error|skip) (\d+): (.+)")
def scan(block: str) -> Iterator[tuple[str, int, str]]: ...
```

- **When NOT regex:** fixed prefixes want `startswith` (faster,
  clearer); single splits want `split`; `in` is fine for
  contains-checks that truly mean contains. Regex is for *shape*.

---

## Common Pitfalls

1. **Greedy `.+` overcapture** — one-incident fixtures green, doubled
   lines wrong. Precise atoms or anchors first.
2. **`match` vs `search` vs `fullmatch` confusion** — mid-line hits
   dropped, trailing rot accepted. Name the question per call.
3. **Unescaped `.`** — `v1.2` matches `v1x2`. Escape literals.
4. **Missing flag** — case drift or block text silently unmatched.
   Flags at compile time, stated visibly.
5. **Validating with `search`** — the reboot-note class returns;
   gates use `fullmatch`.
6. **Trusting captures unconverted** — groups are text; numbers need
  `int()`/`float()` at the boundary.

---

## Connection to Previous Knowledge

- **Boundary validation (L8):** same rule, new engine — exact
  messages, reject where text enters.
- **Prefix discipline (L22–L25):** `startswith` still owns fixed
  prefixes; regex owns *shape*. Use each where it wins.
- **Iterators/Generators (L23/L24):** `finditer` streams matches
  lazily — consumed inside the owner's span, one-shot discipline
  unchanged.
- **Typing (L14/L23):** `re.Pattern[str]` joins the honest-annotation
  habit; captures annotate as text until converted.
- **Project structure (L20–L25 house):** Challenge keeps `main(argv)`
  (full `sys.argv`) + guard, Path-first I/O, no module-level
  executable code.
- **Spec-literalness (standing watch):** every Driver must match its
  Expected block byte-exact.

---

## Quick Recall

Answer from memory before coding:

1. One stencil, three calls: which of `search` / `match` /
   `fullmatch` answers *anywhere*, *at start*, *whole line*?
2. `ERROR.fullmatch("error 1: x!")` where the pattern ends `(.+)` —
   Match or None, and why does that answer indict `.+` as a validator?
3. `re.compile(r"v1.2").fullmatch("v1x2")` — Match or None? What
   single character fixes the pattern?
4. A block holds `"ERROR 1"` and `"Error 2"`. Which flag matches both
   with one pattern, and what does it preserve for capture?
5. `findall` returns `["1", "2"]` from `"error 1 ok error 2"`. What
   bookkeeping did you *not* have to write, and which lesson retired
   that class?
6. A gate uses `search(r"error")` and counts a reboot note as an
   incident. Which Pitfall number, and what single call change fixes it?

---

## Practice

Volume follows the SUPPORTING pipeline. Work top to bottom. The domain
is service-log pattern extraction throughout. Full specs live in
`exercises.ipynb`; write each deliverable in its stated file (R16 —
no `solution.py`, no double-write), then run the **Driver:** cell.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | three questions + compiled patterns |
| E2 | Easy | [REAL-WORLD] | groups + findall/finditer harvest |
| E3 | Easy | [REAL-WORLD] | flags + anchored boundary validation |
| M1 | Medium | [REAL-WORLD] | multi-pattern classifier with conversions |
| M2 | Medium | [REAL-WORLD] | learner-composed extract→report pipeline |
| H1 | Hard | [DEBUG] | 4-plant hunt: greed, anchor, dot, flag (+ 7-row chain each) |
| Challenge | Micro Build | [REAL-WORLD] | pattern-extract CLI: Flow, house entry, byte-exact |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Diagnostic,
not a target.

Completion evidence (SUPPORTING — Level 3): patterns written
independently with the right question per call, captures converted at
the boundary, the H1 hunt resolved with four 7-row chains, the
Challenge running as a pattern-extraction pipeline with byte-exact
output.
