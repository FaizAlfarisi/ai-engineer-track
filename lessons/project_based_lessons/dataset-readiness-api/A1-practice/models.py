"""PROVIDED - shared by the A1 kit exercises. Do not edit."""
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    note: str | None = None


class BadUpload(Exception):
    """Raised when an uploaded file cannot be used at all."""


class EmptyUploadError(Exception):
    """Raised when an uploaded file is empty or whitespace-only."""


class UnsupportedMediaError(Exception):
    """Raised when an uploaded file has an unsupported extension or media type."""
