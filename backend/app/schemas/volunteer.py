'''Volunteer schema module'''
from typing import Optional
from pydantic import BaseModel, EmailStr

class VolunteerSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    phone_number: str

class VolunteerUpdateSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    phone_number: Optional[str] = None
    password: str

    class Config:
        from_attributes = True

class VolunteerSchemaOut(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    phone_number: str

    class Config:
        from_attributes = True

class VolunteerSchema(VolunteerSchemaIn):
    id: int
    rating: float

    class Config:
        from_attributes = True

class ChangePasswordSchema(BaseModel):
    current_password: str
    new_password: str
