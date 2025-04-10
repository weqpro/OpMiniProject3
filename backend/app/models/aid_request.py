"""aid request model"""

import datetime
from typing import List
from enum import Enum as PyEnum

from sqlalchemy import String, ForeignKey, DateTime, ARRAY
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import Base
from app.models.category import Category


class AidRequestStatus(PyEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progres"
    COMPLETED = "completed"


class AidRequest(Base):
    """
    Requests created by soldier
    """

    __tablename__ = "aid_request"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
    image: Mapped[str] = mapped_column(String(255))
    end_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), index=True, nullable=False
    )
    location: Mapped[str] = mapped_column(String(100))
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), index=True, nullable=True)
    status: Mapped[str] = mapped_column(String(40), nullable=False)

    soldier_id: Mapped[int] = mapped_column(ForeignKey("soldier.id"), nullable=False)
    volunteer_id: Mapped[int] = mapped_column(ForeignKey("volunteer.id"), nullable=True)

    category: Mapped[Category] = relationship()
    status: Mapped[str] = mapped_column(
        default=AidRequestStatus.PENDING, nullable=False
    )
    deadline: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), index=True, nullable=True)
    status: Mapped[str] = mapped_column(String(40), nullable=False)

    @staticmethod
    def create_dummy() -> "AidRequest":
        return AidRequest(
            id=123,
            name="Name",
            description="Some description",
            image="shit",
            end_date=datetime.datetime.now(),
            location="somewhere",
            tags=["josci", "duje"],
            status="not done",
            soldier_id=1234,
            category=None,
        )
