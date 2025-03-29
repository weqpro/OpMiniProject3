from abc import ABC, abstractmethod
from app.models.soldier import Soldier


class SoldierRepositoryBase(ABC):
    @abstractmethod
    def get_soldier_by_email(self, email: str) -> Soldier | None:
        """Find soldier by email"""
        pass

