'''AidRequest schema module'''
from typing import List
import datetime
from sqlalchemy import LargeBinary
from pydantic import BaseModel


class AidRequest(BaseModel):
    '''
    The schema used to validate and structure data
    related to aid requests
    '''
    id: int
    name: str
    description: str
    image: LargeBinary
    end_date: datetime.datetime
    location: str
    tags: List[str]
    status: str
    soldier_id: int
    category_id: int
