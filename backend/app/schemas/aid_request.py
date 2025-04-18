"""AidRequest schema module"""

import datetime

from pydantic import BaseModel

from app.schemas.category import CategorySchema


class AidRequestSchema(BaseModel):
    """
    The schema used to validate and structure data
    related to aid requests
    """
    id : int
    name: str
    description: str
    tags: list[str]
    image: str
    location: str
    status: str
    deadline: datetime.datetime

    soldier_id: int
    volunteer_id: int
    category_id: int

    class Config:
        orm_mode = True
