# Project Based Lessons

Material for learning the tools you need while building the Stage 4 portfolio projects.

Each project has its own folder. Each Concept Kit teaches one sprint's concepts, and a practice folder next to it lets you try them before you build.

---

## Dataset Readiness API

### A1: Upload, Validate, Report

Read: [dataset-readiness-api_A1_concept-kit.md](dataset-readiness-api/dataset-readiness-api_A1_concept-kit.md)

Practice: [A1-practice](dataset-readiness-api/A1-practice)

**What you learn**

- **Pydantic constraints:** `Field(min_length, max_length, gt, ge, lt, le, pattern, strict)`, `ConfigDict`, and the exact error type each one produces.
- **Validators:** when to use `@field_validator` or `@model_validator` instead of a constraint, and why `"   "` passes `min_length=1`.
- **Error reports:** how to flatten `ValidationError.errors()` into safe `row`, `field` and `message` items, and why raw `ctx` must never reach a response.
- **Custom exceptions:** several domain exceptions with several handlers, plus overriding `RequestValidationError` and `StarletteHTTPException`, so errors share one JSON shape.
- **Multipart uploads:** why files use `multipart/form-data`, how `UploadFile`, `File` and `Form` work, and the edge cases (empty file, binary file, `curl` content type, reading twice).
- **Parsing files:** a JSON array versus JSONL, the BOM, blank lines, and decode errors.
- **API contract:** `response_model` and `responses` so `/docs` shows 200, 400 and 415.
- **Testing and running:** boundary tests with `TestClient` (`files=` and `data=`), `python -m pytest`, `uvicorn`, `curl -F`, and a small environment config pattern.

**What you practice**

| Exercise | You build |
|---|---|
| E1 | A constrained Pydantic model with a whitespace validator, and a function that flattens Pydantic errors |
| E2 | A multipart FastAPI app with form metadata, several exception handlers and boundary tests |
| M1 | A lazy generator that yields only valid records |
| H1 | A debugging drill with three planted bugs |

**Decisions the kit leaves to you**

- How a service signals failure: a domain exception or `HTTPException`.
- 415 or 422 for an unsupported file type.
- What to do when the `file` part is missing.
- What a bad line in a JSONL file should become.

---

### A2: Quality Engine and Cleaned Export

Read: [dataset-readiness-api_A2_concept-kit.md](dataset-readiness-api/dataset-readiness-api_A2_concept-kit.md)

Practice: [A2-practice](dataset-readiness-api/A2-practice)

**What you learn**

- **NumPy fundamentals:** `ndarray`, `dtype`, vectorization vs loops, `min`/`max`/`mean`/`median`, boolean masks (`&`, `|`, `~`), empty-array traps (`ValueError`/`nan`), and casting scalars to native `int`/`float`.
- **Pandas DataFrames:** building from validated Pydantic records (`model_dump`), `.loc`/`.iloc`, `.copy()` and `.reset_index(drop=True)`, `.isna()` vs broken `== None`, vectorized `.str.strip()`/`.str.len()`, and `duplicated`/`drop_duplicates` (`keep="first"` vs `keep=False`).
- **Vectorization trade-offs:** why vectorized operations replace `iterrows()` and `apply(axis=1)`.
- **JSONL export & FastAPI downloads:** `to_json(orient="records", lines=True, force_ascii=False)`, `Response` vs `StreamingResponse`, `media_type="application/x-ndjson"`, `Content-Disposition`, and round-trip `TestClient` checks.
- **Environment config:** reading typed thresholds dynamically via `os.getenv` + Pydantic `BaseModel` settings testable with `monkeypatch.setenv`.

**What you practice**

| Exercise | You build |
|---|---|
| E1 | NumPy character-length stats (`LengthStats`) and inclusive-bound outlier counter |
| E2 | Pandas cleaner that trims text, computes missing-note ratio and exact duplicate count, and resets index |
| M1 | Env-configured FastAPI JSONL cleaning and file-download endpoint with `400` empty-result handling |
| H1 | A debugging drill with three planted Pandas/NumPy bugs (`== None`, `keep=False`, empty guard) |

**Decisions the kit leaves to you**

- Returning `(summary, valid_records)` from one shared validator vs splitting functions.
- Nested `LengthStats` sub-models vs flat length fields in `/datasets/quality`.
- Whether `/datasets/clean` drops length outliers or keeps them.
- The exact rule-based readiness verdict and `0`-row exception policy.
