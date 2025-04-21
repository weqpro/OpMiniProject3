from pydantic import BaseModel, Field
from typing import List, Optional

class ReviewBase(BaseModel):
    """Base schema for a review."""
    review_text: str
    rating: int = Field(..., ge=1, le=5)
    tags: List[str]
    soldier_id: int
    volunteer_id: int

class ReviewCreate(ReviewBase):
    """
    Schema for creating a new review.

    Inherits all fields from ReviewBase.
    """
    pass

class ReviewOut(ReviewBase):
    """Schema for returning a review from the API."""
    id: int
    reported: bool

    class Config:
        orm_mode = True