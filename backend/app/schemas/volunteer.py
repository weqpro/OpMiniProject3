'''Volunteer schema module'''
from pydantic import BaseModel

class Volunteer(BaseModel):
    '''
    The schema used to validate and structure data
    related to volunteer
    '''
    id: int
    name: str
    surname: str
    email: str
    password: str
    phone_number: str
    rating: float
