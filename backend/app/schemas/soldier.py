"""Soldier schema module"""

from pydantic import BaseModel


class SoldierSchema(BaseModel):
    """
    The schema used to validate and structure data
    related to soldier
    """
    id:int
    name: str
    surname: str
    email: str
    password: str
    phone_number: str
    unit: str
    subsubunit: str
    battalion: str

    model_config = {"from_attributes": True}
