from pydantic import BaseModel, EmailStr


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
