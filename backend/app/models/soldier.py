'''soldier model'''

from typing import List

from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import Base

class Soldier(Base):
    '''
    Represents a military member who can submit aid requests
    '''
    __tablename__ = "soldier"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(55))
    surname: Mapped[str] = mapped_column(String(55))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(15), unique=True)
    unit: Mapped[str] = mapped_column(String(100))
    subunit: Mapped[str] = mapped_column(String(100))
    battalion: Mapped[str] = mapped_column(String(255))

    requests: Mapped[List["AidRequest"]] = relationship(
        "AidRequest", back_populates="soldier", cascade="all, delete-orphan")
    reviews: Mapped[List["Review"]] = relationship(
        "Review", back_populates="soldier", cascade="all, delete-orphan")
