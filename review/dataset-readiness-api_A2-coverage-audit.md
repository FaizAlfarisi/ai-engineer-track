# Sprint A2 Coverage Audit: Dataset Readiness API

**Type:** Pre-build Coverage Contract audit of the Sprint A2 Concept Kit. Not a scored code review (no A2 code written yet).

**Kit:** `lessons/project_based_lessons/dataset-readiness-api/dataset-readiness-api_A2_concept-kit.md`

**Rule applied:** `CURRICULUM.md` Coverage Contract (`A1` paired layout reference). Every mechanism required by Sprint A2 (`projects/stage-4-setup/A2.md`) and `A2-practice/` (`E1`, `E2`, `M1`, `H1-[DEBUG]`) must have its own 6-step Why-Chain, decision rule, parameter/behavior table, standalone runnable worked example, and pitfall links.

## Summary

| Check | Result |
|---|---|
| Template sections | 7 (Section 3 pairs concepts with standalone worked examples; Section 4 provides the map; Section 7 is the coverage matrix) |
| Distinct paired mechanisms | 11 (`3.1` to `3.11`), plus decision trade-offs in `3.12` |
| Runnable standalone worked examples | 11 (`Worked Example 3.1` to `3.11`, Product Reviews domain) — all 11 executed independently with exit code `0` |
| Pitfalls | 10 (`Symptom -> Cause -> Fix`), linked from Section 3 & Section 6 |
| Practice exercises | `E1`, `E2`, `M1` (blank deliverables per R16), `H1-[DEBUG]` (3 planted bugs), `models.py` (`PROVIDED`) |
| Practice suites vs external reference (`scratch/ref_a2/`) | `17 passed in 1.13s` |
| Vacuous-test checks | Blank `e1_stats.py`, `e2_clean.py`, `m1_export_app.py` fail collection with `ImportError`; `h1_buggy.py` fails all 3 bug tests (`3 failed, 1 passed`) |
| Matrix & symbol integrity | `0` broken references across `3.1`–`3.12`, examples `3.1`–`3.11`, pitfalls `1`–`10`, and all imported test symbols |

## Runtime Facts Verified by Executing Code

Environment: Python `3.12.4`, `pandas 2.2.3`, `numpy 1.26.4`, `FastAPI 0.162.0`, `Pydantic 2.13.4`, `httpx 0.28.1`.

| Fact | Result |
|---|---|
| `np.min(np.array([], dtype=np.int64))` raises `ValueError` | True |
| `np.mean(np.array([], dtype=np.int64))` returns `nan` + warning | True |
| `JSONResponse(content={"mean": float("nan")})` raises `ValueError` (not JSON compliant) | True |
| `json.dumps({"n": np.int64(5)})` raises `TypeError` | True |
| `pd.DataFrame([])["body"]` raises `KeyError` | True |
| `(df["note"] == None)` returns `[False, False]` even when `note` is `None` | True |
| `df["note"].isna()` returns `[True, False]` | True |
| `df["note"].str.strip()` preserves `None` without crashing | True |
| `df["note"].str.len()` upcasts to `float64` with `nan` when `None` is present | True |
| `duplicated(..., keep="first").sum()` is `1` vs `keep=False` is `2` on one duplicated pair | True |
| `(s < 5) or (s > 100)` raises `ValueError: The truth value of a Series is ambiguous` | True |
| `to_json(orient="records", lines=True, force_ascii=False)` preserves UTF-8 (`"café"`) and emits `null` | True |
| `Response(..., media_type="application/x-ndjson", Content-Disposition=...)` round-trips cleanly in `TestClient` | True |
