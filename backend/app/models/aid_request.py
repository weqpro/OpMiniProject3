"""aid request model"""

import datetime
from typing import List

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base
from app.utils import AidRequestStatus


class AidRequest(Base):
    """
    Requests created by soldier
    """

    __tablename__ = "aid_request"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), index=True, nullable=True)
    image: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(
        String(40), default=AidRequestStatus.PENDING, nullable=False
    )
    deadline: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    soldier_id: Mapped[int] = mapped_column(ForeignKey("soldier.id"), nullable=False)
    volunteer_id: Mapped[int] = mapped_column(ForeignKey("volunteer.id"), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=True)

    @staticmethod
    def create_dummy() -> "AidRequest":
        return AidRequest(
            id=123,
            name="Name",
            description="Some description",
            image="shit",
            deadline=datetime.datetime.now(),
            location="somewhere",
            tags=["josci", "duje"],
            status="not done",
            soldier_id=1234,
            category=None,
        )
