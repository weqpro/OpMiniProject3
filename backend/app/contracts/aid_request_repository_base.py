from abc import ABC, abstractmethod
from app.models.aid_request import AidRequest


class AidRequestRepositoryBase(ABC):
    @abstractmethod
    def get_aid_request_by_soldier(self, soldier_id: int) -> list[AidRequest]:
        """Get all aid requests for a specific soldier"""
        pass

    @abstractmethod
    def get_aid_request_by_category(self, category_id: int) -> list[AidRequest]:
        """Get all aid requests for a specific category"""
        pass

