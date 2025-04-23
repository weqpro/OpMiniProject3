from typing import Optional
from pydantic import BaseModel, EmailStr, constr, Field


class VolunteerSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    phone_number: constr(pattern=r'^\+380\d{9}$')

class VolunteerUpdateSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    phone_number: Optional[constr(pattern=r'^\+380\d{9}$')] = None
    password: str = Field(..., min_length=8)

    class Config:
        from_attributes = True

class VolunteerSchemaOut(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    phone_number: constr(pattern=r'^\+380\d{9}$')
    rating: float = 0.0

    class Config:
        from_attributes = True

class VolunteerSchema(VolunteerSchemaIn):
    id: int
    rating: float

    class Config:
        from_attributes = True

class ChangePasswordSchema(BaseModel):
    current_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8)
