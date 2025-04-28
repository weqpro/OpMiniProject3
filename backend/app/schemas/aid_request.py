"""AidRequest schema module"""

import datetime
from typing import Optional
from app.utils import AidRequestStatus
from pydantic import BaseModel


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
    image: str
    location: str
    deadline: datetime.datetime

    volunteer_id: int | None
    category_id: int | None

class AidRequestSchemaInWithoutVolId(BaseModel):
    name: str
    description: str
    image: str
    location: str
    deadline: datetime.datetime
    category_id: int

    class Config:
        orm_mode = True

class AidRequestCreateMultipart(BaseModel):
    name: str
    description: str
    location: str
    deadline: datetime.datetime
    category_id: int

class AidRequestSchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    deadline: Optional[datetime.datetime] = None
    volunteer_id: Optional[int] = None
    category_id: Optional[int] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class AidRequestAssignStatus(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    image: Optional[str] = None
    location: Optional[str] = None
    deadline: Optional[datetime.datetime] = None
    volunteer_id: Optional[int] = None
    category_id: Optional[int] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
