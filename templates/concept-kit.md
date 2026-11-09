# Concept Kit — [Topic] ([Sprint ID])

> Stage 4 compact lesson. Seven sections, 2–4 exercises. Strip unrelated
> fluff, but **never strip a mechanism required by the Sprint Brief or
> exercises**. Whenever a slice or topic combines multiple distinct
> mechanisms, teach **each** mechanism with its own Why-Chain, "when to
> use vs when NOT to use" decision rule, parameter/constraint/config
> semantics, and runnable worked example (`CURRICULUM.md` Adaptive
> Mechanism Depth & Coverage Contract).

## 1. Objective + success check

**Intent:** [What the learner will be able to do and build in this slice, in one bold line.]

Success check: [A concrete thing they can demo, implement, and explain at the end.]

## 2. Mental model (one visual)

[One Mermaid or ASCII visual. Labels ≤ 6 words. Split over ~12 nodes.
Never decorative.]

## 3. Why-Chain + Decision Rules (repeat per distinct mechanism in the slice)

For **each** distinct mechanism, API, or configuration hook required by
the Sprint Brief or exercises:

1. Problem: ...
2. Why the previous approach is insufficient: ...
3. New capability needed: ...
4. Feature that provides it: ...
5. How it works (including key parameters / constraints / configuration hooks and failure behavior): ...
6. Consequence — what breaks without it: ...
7. **Decision Rule (When to use vs When NOT to use / Alternatives):**
   - Use `[Feature A]` when ...
   - Do **not** use `[Feature A]` (use `[Alternative B]` instead) when ...
   - **Parameter / Constraint / Config Semantics Table:**
     | Parameter / Constraint / Hook | Required? | Purpose & Behavior | Failure / Error Produced |
     |-------------------------------|-----------|--------------------|--------------------------|
     | ...                           | ...       | ...                | ...                      |

## 4. Worked examples (one runnable example per distinct mechanism)

[Provide one small, complete, runnable example for **each** distinct
mechanism the slice requires. Show how the mechanism is configured,
invoked, and verified without writing the learner's sprint solution.]

```python
# Worked example 1 — [Mechanism A]
```

```python
# Worked example 2 — [Mechanism B (repeat for each mechanism in the slice)]
```

## 5. Pitfalls (3+, numbered — specs reference by number)

1. **Symptom** → cause → fix.
2. **Symptom** → cause → fix.
3. **Symptom** → cause → fix.

## 6. Practice (E1, E2, M1, H1-[DEBUG]) + retrieval

Every exercise: `## Intent`, rule, output format, constraints. Blank
solutions where the deliverable lives. Hints conceptual only.

- **E1** `[REAL-WORLD]` — ...
- **E2** `[REAL-WORLD]` — ...
- **M1** `[REAL-WORLD]` — current + previous concept.
- **H1** `[DEBUG]` — N planted bugs; expected result stated; 7-row chain
  filled as fixed.

Retrieval (5 questions, no notes):

1. ...
2. ...
3. ...
4. ...
5. ...

## 7. Sprint Slice & Exercise Coverage Matrix (mandatory build gate)

| Requirement (Exercise or Sprint Brief Deliverable) | Construct / API / Mechanism Needed | Taught in Kit Section (or `PROVIDED`) |
|----------------------------------------------------|------------------------------------|---------------------------------------|
| `E1` / `E2` / `M1` / `H1`                          | ...                                | Section 3.x + Worked Example x        |
| Sprint Brief Deliverable 1                         | ...                                | Section 3.x + Worked Example x        |
| Sprint Brief Deliverable 2                         | ...                                | Section 3.x + Worked Example x        |
