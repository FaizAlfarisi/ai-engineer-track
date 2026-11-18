# Sprint A1 Review — Dataset Readiness API

**Date:** 2026-11-18
**Repo:** `https://github.com/FaizAlfarisi/dataset-readiness-api` (`9a651b3 finalized A1`)
**Score:** 91/100 (bucket-derived; Hint-1 bar cap 94)
**Topics:** Pydantic (`BaseModel`, `Field` constraints, `@field_validator`, `ValidationError.errors()`), FastAPI (`UploadFile`/`File`, multiple `@app.exception_handler`, `RequestValidationError` override, `/docs` & `/openapi.json`), HTTP/API boundary testing (`TestClient`).
**Tier:** CORE (Stage 4 Portfolio Sprint A1).

---

## Verification Evidence

- **Clean-checkout run (staging copy of final tree):** `python -m pytest -v` → **32 passed** in `0.72s` (`test_datasets_api.py` + `conftest.py`).
- **A1-practice Concept Kit drills:** `python -m pytest` (`test_e1.py`, `test_e2.py`, `test_m1.py`, `test_h1.py`) → **20 passed** in `0.35s`; 3 seven-row chains completed in `debug_report.md`.
- **Live server & demo:** `python -m uvicorn app.main:app` booted cleanly; `curl -F "file=@sample.jsonl"` returned `200` with `{"total":1,"valid":1,"invalid":0,"errors":[]}`; `GET /docs` returned `200`.
- **Suite health (vacuous-test check):** **5/5** deliberate mutations caught (`UnicodeDecodeError` catch drop, missing `.json` `invalid += 1`, allowing empty `[]`, disabling whitespace validator, breaking `loc` flattening).
- **Spec-literalness:** Pass — `POST /datasets/validate` contract, `{total, valid, invalid, errors[{row, field, message}]}`, `400`/`415`, and updated `docs/demo.md` match live behavior.

---

## Strengths

1. **Clean layering:** `app/services/data_processor.py` has zero FastAPI imports; `app/main.py` owns upload metadata gating, byte read-once, and domain-exception mapping via multiple `@app.exception_handler` hooks plus a `RequestValidationError` override.
2. **Thorough input & error edge cases:** Handles UTF-8 BOM, binary bytes, non-list JSON, empty `[]`, whitespace-only files, malformed JSONL lines, non-object items, `{}`/`null`/`0` JSONL rows (with `__row__` error records), and `curl`'s `application/octet-stream`.
3. **Disciplined engineering decisions & portfolio prose:** `DECISIONS.md` records concrete alternatives and consequences (including FastAPI auto-`422` docs vs `400` runtime override), and `ARCHITECTURE.md` captures components, Mermaid request flow, error model, and invariants.

---

## Bucket Score

Total = **91/100**.

| Bucket (max) | Score | Note |
|---|---|---|
| Correctness (25) | 24 | Clean-copy 32/32 green; uvicorn + curl + `/docs` verified; `docs/demo.md` 415 mismatch fixed pre-commit. −1: leftover `GET /` hello-world route in `app/main.py` outside A1 slice scope. |
| Logic (20) | 18 | Sound upload gating, BOM decoding, and error flattening. −1: unreachable `or "unknown"` fallback in `validate_upload_metadata`; −1: two initial JSONL loop defects (`continue` after `JSONDecodeError`, falsy `if not parsed:` dropping `errors` on `{}`/`null`/`0`) surfaced across diagnostic review rounds. |
| Readability (15) | 14 | Clear structure, clean error contracts, helpful doc comments. −1: `ARCHITECTURE.md` § 5 invariants omit the protecting test names and `.env.example` stays unwired. |
| Naming (10) | 9 | Zero builtin shadowing; distinct exception handler names (`handle_*`) in repo code. −1: slight schema suffix inconsistency (`DatasetSummarySchema`/`ErrorResponseSchema` vs `DatasetRecord`/`RowErrorItem`). |
| Maintainability (10) | 8 | Pure-service separation and `extract_row_errors` extraction. −2: duplicated `DatasetRecord.model_validate` + `ValidationError` + counter block across `.json` and `.jsonl` branches in `data_processor.py` (deferred to A2 refactor). |
| Pythonic style (10) | 9 | Good type hints and `from exc` chaining. −1: missing `@classmethod` on `@field_validator`, unused `Form` import in `main.py`, duplicate inline `import json` and inconsistent leading `/` on route strings in `test_datasets_api.py`. |
| Testing (5) | 4 | 32 parametrized tests passing 5/5 vacuous mutation checks. −1: no test asserting `GET /docs` / `/openapi.json` contract. |
| Performance (5) | 5 | Reads uploaded bytes once; no premature optimization. |

---

## Audit & Assistance Summary

- **Hint dependency level (`0–4`):** `1` — `A1-practice` drills (`E1`–`H1`) solved at Level `0`; initial A1 build involved conceptual/spec-boundary Q&A (self-rated `2` due to friction, conceptual-only Level `1` under rubric); review rounds 1–2 used Level `1` diagnostic prompts (`Expected / Observed / Question`) only.
- **Independent-fix ratio:** `100%` of code & bug fixes implemented independently (`0` reviewer-applied code fixes; `ARCHITECTURE.md` § 3 Mermaid diagram/restructure and `README.md` tree formatting assisted from learner's first draft per `RULES.md` R18).
- **Coverage check:** Verified clean in `lessons/project_based_lessons/dataset-readiness-api/dataset-readiness-api_A1_concept-kit.md` (§ 7 matrix) and `review/dataset-readiness-api_A1-coverage-audit.md`.

---

## Reflection & Carry-Forward to Sprint A2

- **Root causes surfaced:** Thought `except json.JSONDecodeError` inside a `for` loop skipped remaining lines without `continue`; applied `H1`'s `if not parsed:` count-only pattern to A1 without noticing it broke the *"every invalid row records an error entry"* invariant.
- **Transfer confirmed:** Unprompted reuse of generators (`M1`), custom domain exceptions + `try/except/from exc` chaining, parametrized `pytest` fixtures, and JSON/UTF-8 error gating.
- **Retro habits carried into A2:** Test small functions incrementally with quick sanity probes before writing large test suites; use `@pytest.mark.parametrize` for compact edge-case matrices; defer minor A1 helper deduplication (`_validate_and_record_row`, `@classmethod`, dropping `GET /`) cleanly into A2.
- **Time studied:** ~2 weeks wall / 5–6h focused (within one sprint cycle).
