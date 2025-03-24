from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models import AidRequest
from repository_base import RepositoryBase

class AidRequestRepositoryBase(RepositoryBase[AidRequest], ABC):
    def __init__(self, session: Session):
        super().__init__(session, AidRequest)

    @abstractmethod
    def get_aid_request_by_soldier(self, soldier_id: int) -> list[AidRequest]:
        '''Get all aid requests for a specific soldier'''
        pass

    @abstractmethod
    def get_aid_request_by_category(self, category_id: int) -> list[AidRequest]:
        '''Get all aid requests for a specific category'''
        pass