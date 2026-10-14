# DSA Week 4 — Config Audit (Stack)

Pattern: **stack** (first contact). Interview target: recognize
LIFO-shaped problems, implement without hints, state time/space
complexity, explain trade-offs out loud.

## Problem statement (pinned — do not reinterpret)

The nightly deploy config nests three section-marker types: `()`,
`[]`, `{}`. A mismatched file pages the on-call.

Implement in `solution.py`:

```python
def audit(s: str) -> int | None:
```

- Return the **index of the first offending bracket**.
- Return **`None`** if the string is balanced (empty string counts
  as balanced).
- "First offending" means, scanning left to right: an unmatched
  closer, or a mismatch against the nearest unclosed opener. A lone
  opener with no partner offends at **its own index** — but only once
  the whole scan proves nothing closes it: report the *first* such
  opener (lowest index among unclosed).
- Non-bracket characters are ordinary content: ignore them.

Examples (exact):

- `audit("")` → `None`
- `audit("([{}])")` → `None`
- `audit("([)]")` → `2` (the `)` mismatches the nearest unclosed `[`)
- `audit("(((")` → `0` (first unclosed opener)
- `audit("())")` → `2` (extra closer)
- `audit("a(b[c]d)e")` → `None` (content ignored)

## Session flow (track pattern)

1. Brute force first — correct beats clever. Say it out loud.
2. Optimize (single pass).
3. Complexity comparison, out loud (time + space; why space can't
   beat O(n) worst-case; when the stack stays shallow in practice).
4. Senior-engineer review pass.
5. Verbal explanation, mandatory: the invariant sentence
   ("the stack top always holds ..."), mismatch cases, complexity.

## Your record (fill as you go — this README is yours)

### Brute-force approach
Repeatedly delete only adjacent matching pairs — () then [] then {} — rescan until nothing deletes. Empty remainder = balanced. Example: ([{}]) → ([]) → () → empty. On ([)] nothing adjacent matches, so it sticks — that stuck remainder is the failure signal. Cost O(n²): each full scan costs O(n), up to O(n) scans.

### Optimized approach
The idea of this approach is looping through the enumerated str to stack the opener bracket, if found out a closer bracket, then validate it with the each pair of bracket. The implementation using list pop method to extract the last item of the stack. Invalid pair means the closer bracket is the offending bracket. Non empty stack means the first item of stack is the offending bracket.

### Complexity (with the crossing argument)
The time complexity for this approach is O(N) since we are looping through the lengh of string and the rest operation is a constant action, no more time consumed. The space complexity is O(N) as well the list of opener cost the worst of the lenght of string, worst case is all-openers (must hold all n), shallow in practice (real nesting 2–3 deep).

### Verbal-explanation notes
The stack approach is to collect the opener bracket to a list, the closer bracket found will be validated with the pair of each bracket. Validation requires the last stacked opener bracket, its uses the list pop method, then validate this results in either cancelation or return the offending idx.

### Edge cases covered

- [✓] empty string → `None`
- [✓] lone opener(s) → first opener index
- [✓] extra closer → its index
- [✓] interleaved types (`([)]`) → mismatch index
- [✓] non-bracket content ignored
- [✓] deep nesting

## Log rows (mentor fills at close-out)

- `PROGRESS.md` → DSA Log Week 4.
- `DAILY_LOG.md` → session entry.
