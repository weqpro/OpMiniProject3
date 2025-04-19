"""AidRequest schema module"""

import datetime

from pydantic import BaseModel


class AidRequestSchema(BaseModel):
    """
    The schema used to validate and structure data
    related to aid requests
    """

    name: str
    description: str
    tags: list[str]
    image: str
    location: str
    status: str
    deadline: datetime.datetime

    soldier_id: int
    volunteer_id: int | None
    category_id: int | None

    class Config:
        orm_mode = True


class AidRequestSchemaIn(BaseModel):
    """
    The schema used to validate and structure data
    related to aid requests
    """

    name: str
    description: str
    tags: list[str]
    image: str
    location: str
    deadline: datetime.datetime

    volunteer_id: int | None
    category_id: int | None

    class Config:
        orm_mode = True
