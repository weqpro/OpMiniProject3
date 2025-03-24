from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models import User
from repository_base import RepositoryBase

class UserRepositoryBase(RepositoryBase[User], ABC):
    def __init__(self, session: Session):
        super().__init__(session, User)

    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        """Find user by email"""
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User | None:
        """Find user by ID"""
        pass

    @abstractmethod
    def get_all_users(self) -> list[User]:
        """Get all users"""
        pass

    @abstractmethod
    def create_user(self, user: User) -> None:
        """Create a new user"""
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        """Update user data"""
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        """Delete user"""
        pass
