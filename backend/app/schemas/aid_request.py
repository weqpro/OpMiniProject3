"""AidRequest schema module"""

import datetime

from pydantic import BaseModel

from app.schemas.category import Category


class AidRequestSchema(BaseModel):
    """
    The schema used to validate and structure data
    related to aid requests
    """

    id: int
    name: str
    description: str
    image: str
    end_date: datetime.datetime
    location: str
    tags: list[str]
    status: str
    soldier_id: int
    category: Category
    deadline: datetime.datetime

    class Config:
        orm_mode = True
