from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models import Soldier
from repository_base import RepositoryBase

class SoldierRepositoryBase(RepositoryBase[Soldier], ABC):
    def __init__(self, session: Session):
        super().__init__(session, Soldier)

    @abstractmethod
    def get_soldier_by_email(self, email: str) -> Soldier | None:
        '''Find soldier by email'''
        pass