# Sprint A1 Coverage Audit: Dataset Readiness API

**Type:** coverage audit of the Concept Kit before the build. This is not a scored code review, because no A1 code exists yet.

**Kit:** `lessons/project_based_lessons/dataset-readiness-api/dataset-readiness-api_A1_concept-kit.md`

**Rule applied:** `CURRICULUM.md` Coverage Contract. Each mechanism needs a Why-Chain, a when-to-use rule, a parameter and error table, and a runnable worked example. The kit and this file record the matrix.

## Result

The original kit failed the contract. The revised kit passes it.

| Check | Before | After |
|---|---|---|
| Template sections | 6 | 7, including the coverage matrix |
| Distinct mechanisms with their own Why-Chain, decision rule and table | 0 (one combined chain) | 8 (sections 3.1 to 3.8), plus a decisions table in 3.9 |
| Runnable worked examples | 1 | 8 |
| Pitfalls | 3 | 10 |
| Exercises | E1, E2, M1, H1 | Same four; E1 and E2 extended |
| Matrix | Missing | Section 7, one row per brief deliverable and per exercise |

## Gaps found and how they were closed

| Gap | Closed in |
|---|---|
| Pydantic constraints had no parameter table | Kit 3.1, Example 1 |
| No rule for constraint versus validator | Kit 3.2, Example 2 |
| Error flattening was a one-line pitfall | Kit 3.3, Example 3 |
| Only one exception handler shown | Kit 3.4, Example 4 |
| `File` and `Form` untaught, one `UploadFile` example | Kit 3.5, Example 5 |
| JSON array and JSONL parsing untaught | Kit 3.6, Example 6 |
| `/docs` showing 400 and 415 untaught | Kit 3.7, Example 7 |
| `TestClient` with `files=` and `data=`, run commands, env config thin | Kit 3.8, Example 8 |

## Facts verified by running code

| Fact | Result |
|---|---|
| `"   "` passes `min_length=1` | True |
| `str_strip_whitespace=True` rejects it | True |
| Constraint error types (`string_too_short`, `greater_than`, `less_than_equal`, `string_pattern_mismatch` and the rest) | Match the kit table |
| Lax mode accepts `"5"`, `5.0` and `True` for an `int`, rejects `5.5` | True |
| An `int` for a `str` field is rejected | True |
| Extra keys are ignored by default; `extra="forbid"` gives `extra_forbidden` | True |
| `@model_validator` errors have an empty `loc` | True |
| Raw `exc.errors()` fails `json.dumps` after a validator error | True |
| `curl -F` sends `application/octet-stream` for `.jsonl` | True |
| A binary upload raises `UnicodeDecodeError`, not `JSONDecodeError` | True |
| A `BaseModel` next to `UploadFile` makes the body `multipart/form-data` and returns 422 | True (corrected a wrong claim in my first draft) |
| Uploads need `python-multipart`; FastAPI's error text names it | True |

## Coverage matrix

The full matrix lives in kit section 7. Summary:

| Requirement | Kit section |
|---|---|
| Upload accepts JSON array or JSONL | 3.5, 3.6 |
| Record schema | 3.1, 3.2 |
| Validate every row, collect errors | 3.3 |
| Structured summary as a Pydantic schema | 3.3, 3.7 |
| 400 and 415, never 500 | 3.4, 3.6 |
| `/docs` reflects the contract | 3.7 |
| Boundary tests from a clean checkout | 3.8 |
| Config from env | 3.8 (PROVIDED pattern) |
| README, ARCHITECTURE, DECISIONS, `docs/demo.md` | Learner prose (R18), reviewed not taught |
| E1, E2, M1, H1 | 3.1 to 3.8, as mapped in kit section 7 |

## Verification evidence

- All 8 python blocks in kit section 4, extracted and run in order as one program: exit code 0.
- Practice suites against reference solutions kept outside the repo: 20 passed.
- Blank deliverables fail on import. `h1_buggy.py` fails its three bug tests.
- Script check: every section, example and pitfall number in the matrix exists, and every symbol each suite imports is named in its exercise spec.

## Notes for the build review

- Solutions in `A1-practice` are blank (R16).
- Learner decisions still open: 415 or 422, missing `file` handling, a bad JSONL line, and the failure signal from services.
- `docs/decision.md` item 1 (422 for unsupported files) rests on a premise the kit corrects: FastAPI never checks file type.
- Starlette prints a deprecation warning about `httpx2`; it is only a note.

