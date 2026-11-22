"""PROVIDED models and exceptions for Sprint A2 practice. Do not edit."""
from pydantic import BaseModel, Field, field_validator


class EmptyDataError(Exception):
    """Raised when no valid records remain for analysis or export."""


class LengthStats(BaseModel):
    min: int
    max: int
    mean: float
    median: float


class ReviewRecord(BaseModel):
    title: str = Field(min_length=1, strict=True)
    body: str = Field(min_length=1, strict=True)
    note: str | None = None

    @field_validator("title", "body")
    @classmethod
    def reject_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be blank")
        return value
