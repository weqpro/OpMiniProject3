"""AidRequest schema module"""

import datetime

from pydantic import BaseModel

from app.schemas.category import CategorySchema


class AidRequestSchema(BaseModel):
    """
    The schema used to validate and structure data
    related to aid requests
    """

    id: int
    name: str
    description: str
    image: str
    location: str
    tags: list[str]
    status: str
    soldier_id: int
    category: CategorySchema
    deadline: datetime.datetime

    class Config:
        orm_mode = True
