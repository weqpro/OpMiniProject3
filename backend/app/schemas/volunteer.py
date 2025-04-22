'''Volunteer schema module'''
from typing import Optional
from pydantic import BaseModel, EmailStr, constr


class VolunteerSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: constr(pattern=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
    phone_number: constr(pattern=r'^\+380\d{9}$')

class VolunteerUpdateSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    phone_number: Optional[constr(pattern=r'^\+380\d{9}$')] = None
    password: constr(pattern=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

    class Config:
        from_attributes = True

class VolunteerSchemaOut(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    phone_number: constr(pattern=r'^\+380\d{9}$')

    class Config:
        from_attributes = True

class VolunteerSchema(VolunteerSchemaIn):
    id: int
    rating: float

    class Config:
        from_attributes = True

class ChangePasswordSchema(BaseModel):
    current_password: constr(pattern=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
    new_password: constr(pattern=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
