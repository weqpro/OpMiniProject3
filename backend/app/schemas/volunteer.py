"""Volunteer schema module"""

from pydantic import BaseModel


class VolunteerSchemaIn(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    phone_number: str


class VolunteerSchema(VolunteerSchemaIn):
    id: int
    rating: float

    class Config:
        from_attributes = True
