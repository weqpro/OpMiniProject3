'''Soldier schema module'''
from pydantic import BaseModel


class Soldier(BaseModel):
    '''
    The schema used to validate and structure data
    related to soldier
    '''
    id: int
    name: str
    surname: str
    email: str
    password: str
    phone_number: str
    unit: str
    subunit: str
    battalion: str
