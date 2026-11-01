# Lesson 27 — Datetime (Tier: SUPPORTING)

Stage 3, eleventh topic — the last lesson-shaped one. You have sliced
date strings since Weekly Project 2 (`date[:7]`, `"09:00"`, hand-checked
shapes). This lesson replaces string luck with date values: parsed
once, compared and differenced as objects, formatted once at the edge.

SUPPORTING tier — Level 3 bar: parse, validate, compute, and format
dates independently on real data. One focused sitting, then the skill
transfers into the Stage project (tenures, due dates, run timestamps)
and every schedule-shaped pipeline after it.

Business domain for this lesson is fresh: the subscription tenure
reporter. No patterns, no guards, no telemetry. New business, same
engineering discipline.

---

## Objective

By the end of this lesson you can:

- Parse with `strptime` and format with `strftime`/`isoformat`,
  keeping the round-trip identity (`format(parse(x)) == x`) as the
  canonical check.
- Compute with `date`/`datetime`/`timedelta` (tenures, durations,
  boundary days) instead of hand arithmetic on strings.
- Reject non-canonical dates (don't normalize them) with exact error
  messages at the boundary.
- Name naive-vs-aware comparison as the trap (UTC anchoring stated,
  deep tz machinery deferred).
- Name `zoneinfo` deep use and `dateutil` as deliberate omissions —
  recognized, not drilled.

---

## Why This Matters

The billing run computes subscription tenures from signup strings.
Version 1 slices: `months = (end[:4] - start[:4]) * 12 + ...` — hand
arithmetic on four substrings. Last quarter a signup read `"2026-13-99"`.
It sliced fine, subtracted fine, and billed a customer for negative
eleven months. The quarter before, `"1/5/2026"` (day-first, single
digits) sorted after `"12/25/2025"` and the aging report inverted.

Why are the previous tools insufficient? String order works only on
canonical shapes, and nothing enforces canonical — every new format is
a new special case. Hand subtraction re-implements calendars badly
(leap years, month lengths, boundaries).

What capability do we need? Dates as *values*: parsed once into
objects that compare, subtract, and format correctly by construction —
with rot rejected at the gate, never normalized into silence.

What feature provides it? The `datetime` trio: `strptime` parses,
`date`/`timedelta` compute, `strftime`/`isoformat` present. The WP2
reject-don't-normalize rule becomes a type guarantee instead of a
hand-rolled special case.

Practical consequence — what breaks without it? The month-slice
class: ordering and aging correct on canonical samples, wrong on every
drifted format — green drivers, wrong bills. The H1 drill plants
exactly it.

Urgency, stated plainly: the stage project bills, ages, and timestamps
everything. Every date it touches as a string is a `"2026-13-99"`
waiting to happen. This lesson is the last gate before that project —
after it, only the Asyncio collapse stands between you and the
capstone discussion.

Deliberate omissions: `zoneinfo` deep use (UTC anchoring stated, zone
lore deferred); `dateutil` (third-party, never required); calendar
edge lore beyond leap-day (named, not drilled).

---

## Mental Model

A canonical date string is a **serial number**; a `date` object is the
**item it identifies**.

```text
"2026-02-30"  ──strptime──▶  ValueError (no such item — rejected, never fixed)
"2026-02-28"  ──strptime──▶  date(2026, 2, 28) ──isoformat──▶ "2026-02-28" (round trip)
                                                      ── strftime("%d %b") ──▶ "28 Feb" (display)
date(2026,3,1) − date(2026,2,1)  =  timedelta(days=28)  (calendars handled inside)
```

Three rules run everything:

1. Parse validates: impossible dates raise instead of existing.
2. The round trip is the canon check: `isoformat(parse(x)) == x`
   proves canonical; anything else is rot.
3. Compute on objects, format at the edge: arithmetic never touches
   strings, display never touches objects.

---

## Core Concept

### 1. `strptime` parses and validates in one act

Problem: signup strings arrive in the wild — `"2026-01-05"`,
`"1/5/2026"`, `"2026-13-99"`. Slicing accepts all three and computes
on all three.

Why pre-checks are insufficient: a regex can pin shape (`\d{4}-\d{2}`),
but shape is not validity — `"2026-13-99"` is well-shaped nonsense.

Capability needed: parse-and-validate as one atomic verdict.

Feature: `datetime.strptime(text, "%Y-%m-%d").date()` — returns the
date or raises `ValueError`. Impossible dates die here, where the
text enters:

```python
from datetime import datetime

datetime.strptime("2026-01-05", "%Y-%m-%d").date()   # date(2026, 1, 5)
datetime.strptime("2026-13-99", "%Y-%m-%d")          # ValueError — no such date
```

Consequence of missing this: validation as a second hand-rolled pass
that drifts from the parse it guards.

### 2. The round trip is the canon check (WP2 retrieval, now typed)

Problem: `"1/5/2026"` parses under `"%m/%d/%Y"` — but is it canonical?
The report needs one shape out, whatever shape came in.

Why re-formatting is insufficient alone: formatting without comparing
normalizes silently — drift in, canon out, nobody told.

Capability needed: distinguish canonical input from parseable rot.

Feature: the identity `d.isoformat() == text` after parsing with the
canonical format. Equal means canonical; unequal means
reject-don't-normalize:

```python
def parse_canonical(text):
    try:
        d = datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("invalid date: bad value")
    if d.isoformat() != text:
        raise ValueError("invalid date: not canonical")
    return d
```

Consequence of missing this: the month-slice class returns —
`"2026-1-5"` accepted, reports fragmented by shape.

### 3. Compute on objects (`timedelta` does calendars)

Problem: tenure in days between two strings. Hand math needs month
lengths, leap rules, borrow logic — a calendar re-implemented badly.

Why integer day-counts are insufficient: day numbers without month
context still need the table. Objects carry the context.

Capability needed: subtract dates, get durations, add durations.

Feature: `date` subtraction yields `timedelta`; `.days` reads it;
`date + timedelta` advances:

```python
from datetime import date

(date(2026, 3, 1) - date(2026, 2, 1)).days   # 28 — February handled inside
date(2026, 1, 5) + timedelta(days=30)          # date(2026, 2, 4)
```

Consequence of missing this: tenure math correct on 30-day months,
wrong on February — the latent class in a calendar costume.

### 4. Format at the edge (`isoformat` stores, `strftime` shows)

Problem: one shape must store (`"2026-01-05"`), another must display
(`"05 Jan 2026"`). Mixing them corrupts both.

Why one-format-everywhere is insufficient: storage needs sortability
(ISO), humans need readability — one shape cannot serve both.

Capability needed: canonical storage format plus deliberate display
formats, converted at the boundary in each direction.

Feature: `isoformat()` for storage/canonical output; `strftime`
for display (`"%d %b %Y"`, `"%Y-%m-%d"`):

```python
d = date(2026, 1, 5)
d.isoformat()                 # "2026-01-05" — stores, sorts, compares
d.strftime("%d %b %Y")        # "05 Jan 2026" — shows
```

Consequence: storage stays canonical by construction; display never
leaks back into logic.

### 5. Format-string swaps (`%m` vs `%d` — the quiet transposition)

Problem: `"%Y-%d-%m"` parses `"2026-05-01"` as May 1st... no — as
*January 5th*. The transposition is silent on every day ≤ 12 and
explodes only on day 13+.

Why code review misses it: the format string *looks* right at a
glance, and twelve-thirteenths of test data can't distinguish it.

Capability needed: a convention that makes the swap visible.

Feature: canonical-first discipline — `%Y-%m-%d` is the only
parse/store shape in graded code; display formats live in exactly
one named place. Plus the round-trip test, which catches swaps on
any day-13+ sample.

Consequence of missing this (Pitfall 3, H1 plants it): tenures off
by months on every date past the 12th, green January fixtures.

### 6. Naive vs aware: the comparison trap (stated, not drilled)

Problem: `datetime.now()` minus a stored UTC timestamp — the
subtraction raises `TypeError: can't subtract offset-naive and
offset-aware datetimes`, or worse, silently compares wall clocks
across zones.

Why ignoring zones is insufficient: the error is intermittent
(only where zones differ) and the silent variant is wrong by whole
hours — billing-grade wrong.

Capability needed: a stated anchoring rule for this codebase.

Feature (posture, not machinery): all graded datetimes are naive
UTC by convention — arithmetic stays in plain `date`/`timedelta`
space, never mixing aware stamps. Mixed comparisons are a review
finding. Deep `zoneinfo` work is deferred by design.

Consequence: no `TypeError` in graded code, no silent zone drift —
and the convention is written down, not assumed.

---

## Practical Examples

Example A — the gate (E3 is this, specified exactly):

```python
from datetime import datetime, date

CANON = "%Y-%m-%d"

def parse_date(text: str) -> date:
    """Canonical YYYY-MM-DD or ValueError (exact messages in spec)."""
    try:
        d = datetime.strptime(text, CANON).date()
    except ValueError:
        raise ValueError("invalid date: bad value")
    if d.isoformat() != text:
        raise ValueError("invalid date: not canonical")
    return d
```

Example B — tenure math (M1 is this):

```python
from datetime import date

def tenure_days(start: date, end: date) -> int:
    """Days between two dates; negative when end precedes start."""
    return (end - start).days

tenure_days(date(2026, 1, 5), date(2026, 3, 1))   # 55
```

Example C — display at the edge:

```python
date(2026, 1, 5).strftime("%d %b %Y")   # "05 Jan 2026"
date(2026, 1, 5).isoformat()            # "2026-01-05"
```

---

## Engineering Notes

- **Parse once, at entry.** Strings become dates at the boundary;
  everything downstream takes `date`. A function accepting a date
  string deep in the pipeline is a smell.
- **Reject, don't normalize.** Non-canonical input raises with the
  exact message — the WP2 rule, now typed. Normalizing drift into
  silence is how `-11 month` bills happen.
- **Canonical storage, display at print.** `isoformat()` in files
  and reports-as-data; `strftime` only where humans read.
- **One parse format in graded code.** `%Y-%m-%d` unless the spec
  names another. Format-string variety is a bug farm.
- **Day-13+ samples in every test.** Any suite that only exercises
  days ≤ 12 cannot catch `%m`/`%d` swaps — review rejects it.
- **Annotate dates as dates:**

```python
from datetime import date, timedelta

def tenure_days(start: date, end: date) -> int: ...
def shift(day: date, delta: timedelta) -> date: ...
```

- **When NOT datetime:** a year-month bucket for grouping wants the
  ISO prefix (`iso[:7]` — still legitimate on *canonical* output);
  a fixed display label wants a constant. Datetimes are for *values
  that compute*.
- **Naive-UTC convention, written once.** All graded datetimes naive
  UTC; mixed comparisons are review findings.

---

## Common Pitfalls

1. **Month-slice ordering** — `s[:7]` groups by shape, not by date;
   drifted formats fragment groups. Parse first, then bucket.
2. **Leap-day blindness** — hand arithmetic forgets Feb 29; object
   subtraction never does. Tests include a leap span.
3. **Format-string swap** (`%Y-%d-%m`) — silent ≤ 12th, explosive
   after. Canonical-first + day-13+ samples.
4. **Normalizing rot** — accepting `"2026-1-5"` by reformatting.
   Reject with the exact message.
5. **Naive-vs-aware comparison** — `TypeError` or silent zone drift.
   Naive-UTC convention, stated once.
6. **String arithmetic on dates** — subtracting ISO strings
   lexicographically works until formats drift. Objects subtract.

---

## Connection to Previous Knowledge

- **Boundary validation (L8):** same rule, new values — exact
  messages, reject where text enters.
- **Reject-don't-normalize (WP2):** the rule graduates from
  hand-rolled check to type guarantee.
- **Typing (L14/L23):** `date`/`timedelta` join the honest-annotation
  habit; strings stop impersonating dates at signatures.
- **Project structure (L20–L26 house):** Challenge keeps `main(argv)`
  (full `sys.argv`) + guard, Path-first I/O, no module-level
  executable code.
- **Spec-literalness (standing watch):** every Driver must match its
  Expected block byte-exact.

---

## Quick Recall

Answer from memory before coding:

1. `"2026-13-99"` under `strptime` with `"%Y-%m-%d"` — parsed or
   `ValueError`? What does that verdict buy that a shape regex can't?
2. `parse("2026-1-5")` succeeds but `isoformat() != text`. Canonical
   or rot — and what must the gate do?
3. Tenure between `date(2024, 2, 1)` and `date(2024, 3, 1)` — how many
   days, and which leap fact does hand math need that subtraction
   doesn't?
4. `strftime("%Y-%d-%m")` on May 1st prints what a reader takes for
   which date? Why do January fixtures never catch it?
5. A naive `datetime.now()` minus a stored UTC-aware stamp — what are the
   two failure modes, and what one-line convention prevents both?
6. An aging report groups by `s[:7]` and fragments on `"2026-1-5"`.
   Which Pitfall number, and what single pipeline change fixes it?

---

## Practice

Volume follows the SUPPORTING pipeline. Work top to bottom. The domain
is subscription tenure throughout: signups are date strings, tenures
are day counts, reports bucket by month. Full specs live in
`exercises.ipynb`; write each deliverable in its stated file (R16 —
no `solution.py`, no double-write), then run the **Driver:** cell.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | parse/format round-trips, exact messages |
| E2 | Easy | [REAL-WORLD] | date arithmetic (tenures, shifts, boundaries) |
| E3 | Easy | [REAL-WORLD] | canonical gate (reject-don't-normalize) |
| M1 | Medium | [REAL-WORLD] | tenure classifier with buckets |
| M2 | Medium | [REAL-WORLD] | learner-composed aging pipeline |
| H1 | Hard | [DEBUG] | 4-plant hunt: slice-order, leap, swap, normalize (+ 7-row chain each) |
| Challenge | Micro Build | [REAL-WORLD] | tenure-report CLI: Flow, house entry, byte-exact |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Diagnostic,
not a target.

Completion evidence (SUPPORTING — Level 3): dates parsed, validated,
computed, and formatted independently; the H1 hunt resolved with four
7-row chains; the Challenge running as a tenure pipeline with
byte-exact output.
