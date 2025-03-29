from abc import ABC, abstractmethod
from app.models.volunteer import Volunteer


class VolunteerRepositoryBase(ABC):
    @abstractmethod
    def get_volunteer_by_email(self, email: str) -> Volunteer | None:
        """Find volunteer by email"""
        pass

    @abstractmethod
    def get_volunteers_for_aid_request(self, aid_request_id: int) -> list[Volunteer]:
        """Get all volunteers for a specific help request"""
        pass

