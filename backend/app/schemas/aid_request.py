'''AidRequest schema module'''
from typing import List
import datetime
from sqlalchemy import LargeBinary
from pydantic import BaseModel
from enum import Enum

class AidRequestStatusEnum(str, Enum):
    PENDING = "Очікування"
    IN_PROGRESS = "В процесі"
    COMPLETED = "Виконано"

class AidRequestBase(BaseModel):
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
    volunteer_deadline: datetime.datetime
    
class AidRequestCreate(AidRequestBase):
    pass

class AidRequestOut(AidRequestBase):
    id: int
    status: AidRequestStatusEnum

    class Config:
        orm_mode = True
