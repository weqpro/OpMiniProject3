from pydantic import BaseModel, EmailStr
from typing import Optional


class SoldierSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    phone_number: str
    unit: str
    subsubunit: str
    battalion: str


class SoldierSchema(SoldierSchemaIn):
    id: int

    class Config:
        from_attributes = True

class SoldierUpdateSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    phone_number: Optional[str] = None
    unit: Optional[str] = None
    subsubunit: Optional[str] = None
    battalion: Optional[str] = None
    password: str

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class ChangePasswordSchema(BaseModel):
    current_password: str
    new_password: str
