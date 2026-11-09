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
