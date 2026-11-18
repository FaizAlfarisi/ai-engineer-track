"""E2 - write your solution here (blank on purpose).

Deliverables:
- LineCountReport
- count_text_lines
- app
"""

from pydantic import BaseModel
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from models import BadUpload, EmptyUploadError, UnsupportedMediaError

class LineCountReport(BaseModel):
    source: str
    lines: int

def count_text_lines(raw: bytes, filename: str) -> int:
    if not filename.lower().endswith(".txt"):
        raise UnsupportedMediaError("unsupported media type")
    
    if not raw or not raw.strip():
        raise EmptyUploadError("empty file")
    
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise BadUpload("not text") from exc
    
    return len(text.splitlines())

app = FastAPI()

@app.exception_handler(EmptyUploadError)
async def empty_upload_handler(
    request: Request, exc: EmptyUploadError
) -> JSONResponse:
    return JSONResponse(
        status_code=400, 
        content={"detail": str(exc)}
    )
    
@app.exception_handler(BadUpload)
async def bad_upload_handler(
    request: Request, exc: BadUpload
) -> JSONResponse:
    return JSONResponse(
        status_code=400, 
        content={"detail": str(exc)}
    )
    
@app.exception_handler(UnsupportedMediaError)
async def unsupported_media_handler(
    request: Request, exc: UnsupportedMediaError
) -> JSONResponse:
    return JSONResponse(
        status_code=415, 
        content={"detail": str(exc)}
    )

@app.exception_handler(RequestValidationError)
async def request_validation_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    first = exc.errors()[0] if exc.errors() else {}
    loc = ".".join(str(p) for p in first.get("loc", ()))
    return JSONResponse(
        status_code=422, 
        content={"detail": f"{loc}: {first.get('msg', "Invalid request")}"}
    )

@app.post("/count-lines")
async def line_counter(
    file: UploadFile = File(...),
    source: str = Form("upload")
) -> LineCountReport:
    raw = await file.read()
    lines = count_text_lines(raw, file.filename or "")
    
    return LineCountReport(source=source, lines=lines)