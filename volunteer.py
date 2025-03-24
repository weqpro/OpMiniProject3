from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models import Volunteer, Soldier, AidRequest
from repository_base import RepositoryBase

class VolunteerRepositoryBase(RepositoryBase[Volunteer], ABC):
    def __init__(self, session: Session):
        super().__init__(session, Volunteer)

    @abstractmethod
    def get_volunteer_by_email(self, email: str) -> Volunteer | None:
        '''Find volunteer by email'''
        pass

    @abstractmethod
    def get_volunteers_for_aid_request(self, aid_request_id: int) -> list[Volunteer]:
        '''Get all volunteers for a specific help request'''
        pass