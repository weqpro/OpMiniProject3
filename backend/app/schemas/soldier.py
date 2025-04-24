from pydantic import BaseModel, EmailStr, constr, Field
from typing import Optional


class SoldierSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    phone_number: constr(pattern=r"^\+380\d{9}$")
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
    phone_number: Optional[constr(pattern=r"^\+380\d{9}$")] = None
    unit: Optional[str] = None
    subsubunit: Optional[str] = None
    battalion: Optional[str] = None
    password: str = Field(..., min_length=8)

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class ChangePasswordSchema(BaseModel):
    current_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8)
