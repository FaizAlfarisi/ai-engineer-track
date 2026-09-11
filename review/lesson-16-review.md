# Lesson 16 Review — Dataclass

**Date:** 2026-09-11
**Score:** 92/100
**Topics:** `@dataclass`, auto-generated `__init__`/`__repr__`/`__eq__`,
field annotations as the class spec, `field(default_factory=...)`, mutable
-default traps, `frozen=True` and `FrozenInstanceError`, `asdict()` +
JSON with an Enum-aware encoder, composing dataclasses, enum identity
(`is` vs `==` to a string), refactoring onto a frozen model.

---

## Strengths

- **Results: all 7 drivers byte-exact** (E1–E3, M1–M2, H1, Challenge),
  verified by running every notebook driver against the learner's real
  files in a temp copy. **`mypy main.py` and `mypy main_h1.py` both
  clean** — the "whole entry-point set" lesson from L15 held.
- **Quick Recall 6/6**, including the non-obvious ones: why `list` needs
  `default_factory` (the shared-object aliasing), and why frozen ⇒
  hashable (equality can never change, so the hash never needs to).
- **H1 — all four planted bugs caught and correctly attributed:**
  shared mutable default (import-time `ValueError`), the `amount: str`
  annotation lie, frozen-record mutation (`FrozenInstanceError`), and
  `kind == "income"` (never True ⇒ wrong net). The in-conversation
  explanation was accurate and complete — the writing-up happened under
  emergency duty, so the worked model below is the study artifact.
- **Refactor discipline (Challenge):** the L15 expense package rebuilt
  natively on the frozen model — `Kind(record["kind"])` on load,
  `signed_amount()` for the sign rule, same interfaces, byte-exact
  output. "Swap the model, keep the contract."
- **GenAI use was disclosed, not smuggled.** The learner hit genuinely
  new territory (dataclass *purpose*, enum solving pattern, the frozen
  constraint), reread the lesson multiple times, went to Google, and
  ultimately asked a generative model to **explain concepts** — not to
  write the solution. All four H1 fixes were the learner's own.

## Improvements

- **The H1 bug report in `solution.py` is blank.** The debugging skill
  was proven (all four caught, explained correctly, in real time), but
  the protocol write-up didn't happen under duty. The worked model below
  closes that gap; the learner's practice is to transcribe it by hand
  once (writing it out *is* the retrieval). Borderline commentary bucket.
- **Enum problem solving was genuinely hard** — the learner's own
  reflection names it. The `==`-to-string drift is the exact failure
  mode of "the value looks right but the type is different"; the
  identity contract (`is`) is the resolution. Carried as a watch item,
  not a miss: it held in practice (kind.py uses `is`), the *search* was
  the struggle.
- **Concept-level reliance on GenAI** for brand-new shapes. Disclosed,
  acceptable at SUPPORTING the first time, but the wean target is set:
  concept explanation should move toward the lesson + reviewer first,
  GenAI last. Drivers still rule as ground truth.

## H1 — worked model bug report (study artifact)

**Bug 1 — shared mutable default (import-time `ValueError`).**
*observed:* `transactions: list[Transaction] = []` →
`ValueError: mutable default <class 'list'> ... is not allowed: use
default_factory`. *expected:* `transactions: list[Transaction] =
field(default_factory=list)`. *root cause:* a dataclass evaluates
defaults **once at class creation** — every `Budget` would share the
*one* list; mutate in one, it leaks to all. `default_factory` calls
`list()` fresh per instance. Same aliasing as E2, made loud at import.

**Bug 2 — annotation lie (`amount: str`).** *observed:* the field says
`str`, the callers pass numbers, `signed_amount()` returns floats and
`net()` sums them. *expected:* `amount: float`. *root cause:* runtime
never checks the declared type — the lie only bites when something
trusts the annotated fields as the spec (`mypy` is that something).
Program ran "fine" and printed a sweet `79.50`; the lie sailed. On a
dataclass, the annotated fields **are** the code — L14 discipline,
sharpened.

**Bug 3 — frozen record mutated (runtime `FrozenInstanceError`).**
*observed:* `self.amount = extra` inside `mark_spent` →
`FrozenInstanceError: cannot assign to field 'amount'`. *expected:*
`mark_spent` **returns a new** `Transaction(self.date, self.category,
self.kind, extra)` and `main_h1.py` rebinds
`txn = txn.mark_spent(txn.amount)`. *root cause:* `frozen=True` removes
`__setattr__` — instances are immutable by construction. The constraint
forces the *replace-don't-edit* pattern, and that immutability is
exactly why frozen instances are safe as dict keys (the Quick Recall Q3
answer).

**Bug 4 — enum compared to a string (`kind == "income"`).**
*observed:* the comparison can never be `True` (`Kind` member vs `str`
are different types), so every record counted as expense →
`net: -120.50` against the expected `79.50`. *expected:*
`self.kind is Kind.INCOME`. *root cause:* the enum exists so code
compares **identity** (`is`), never naked strings. String equality
against the "value" is the natural drift the enum type is designed to
kill.

**Failure ladder (why the drill is solvable one fix at a time):**
import `ValueError` → runtime `FrozenInstanceError` → wrong number →
silent type lie (only `mypy` sees it). Each bug blocks exactly one layer
further down the road; fixing in order moves the failure forward.

## Suggestions

- **Transcribe the model report by hand** into your own words, once.
  You caught all four live — writing them down keys the pattern.
- **For a "fix," re-run the whole ladder, not just the last step:**
  import → run → numbers → `mypy`, both entry points. That loop is the
  debugging protocol.
- **Move GenAI down your toolchain for new-but-nameable concepts:**
  lesson reread → Google → reviewer → GenAI last. The fun you had
  ("so much fresh info") is the signal you should chase the *gap*, not
  the shortcut.
- **Enum watch item:** whenever a check "should work but doesn't" and
  the values look identical, ask *what types are on each side of the
  operator* — that question alone would have made Bug 4 a two-second
  find next time.

## Learning Note

The lesson's thesis landed visibly: a dataclass is "a class whose spec
IS its annotations." The learner watched the boilerplate of L15
disappear into three auto-generated dunders, then hit the two real
prices of that: **defaults are created once** (so shared-object bugs
become visible at import) and **frozen is a promise the runtime
enforces** (so replace-don't-edit becomes a design pattern, not a
suggestion). Best artifact: the Challenge refactor — same interfaces,
byte-exact output, a data model that signs itself. The duty-compressed
debug day still produced a correct 4/4 bug catch; the model report
closes the write-up gap. L13 reflection still owed; WP2 kickoff opens
next.