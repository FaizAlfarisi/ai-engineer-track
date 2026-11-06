# Project Based Lessons

Material for learning the tools you need while building the Stage 4 portfolio projects.

Each project has its own folder. Each Concept Kit teaches one sprint's concepts, and a practice folder next to it lets you try them before you build.

---

## Dataset Readiness API

### A1: Upload, Validate, Report

Read: [dataset-readiness-api_A1_concept-kit.md](dataset-readiness-api/dataset-readiness-api_A1_concept-kit.md)

Practice: [A1-practice](dataset-readiness-api/A1-practice)

**What you learn**

- How an uploaded file travels through a web request: client, route, service, validation, response.
- Which layer should decide a status code, and why services should stay free of HTTP.
- How FastAPI handles routes, `UploadFile`, response models, exception handlers and the generated `/docs` page.
- What FastAPI checks for you (the shape of the request) and what it never checks (the file type).
- How Pydantic v2 validates a record and reports every problem, through `ValidationError.errors()` with `type`, `loc` and `msg`.
- Why strict typing matters: an `int` is not accepted as a `str`, and an empty string breaks `min_length`.
- Why a binary upload crashes a handler that only catches `JSONDecodeError`.
- How to write boundary tests with `TestClient`, and how tests import your app.

**What you practice**

| Exercise | You build |
|---|---|
| E1 | A function that turns Pydantic errors into a flat list of `field` and `message` |
| E2 | A small FastAPI app with honest error codes and boundary tests |
| M1 | A lazy generator that yields only valid records |
| H1 | A debugging drill with three planted bugs |

**Decisions the kit leaves to you**

- How a service signals failure: a domain exception or `HTTPException`.
- 415 or 422 for an unsupported file type.
- What to do when the `file` part is missing.
- What a bad line in a JSONL file should become.
