"""E1 - write your solution here (blank on purpose).

Deliverables:
- SampleRecord
- flatten_errors
"""

from pydantic import BaseModel, Field, field_validator, ValidationError


class SampleRecord(BaseModel):
    code: str = Field(pattern=r"^DS-\d{2}$")
    prompt: str = Field(min_length=1, max_length=200, strict=True)
    score: int = Field(ge=1, le=5, strict=True)
    notes: str | None = None

    @field_validator("prompt")
    def reject_blank_whitespace(cls, prompt: str) -> str:
        cleaned = prompt.strip()
        if not cleaned:
            raise ValueError("must not be blank or whitespace-only")
        return cleaned

def flatten_errors(exc: ValidationError) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    
    for err in exc.errors():
        loc_parts = [str(part) for part in err["loc"]]
        field = ".".join(loc_parts) if loc_parts else ""
        message = err["msg"]
        
        items.append({"field": field, "message": message})
        
    return items
