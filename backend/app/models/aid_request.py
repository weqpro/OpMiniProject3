"""aid request model"""

import datetime
from typing import List

from sqlalchemy import String, ForeignKey, LargeBinary, DateTime, ARRAY
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import Base


class AidRequest(Base):
    """
    Requests created by soldier
    """

    __tablename__ = "aid_request"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1000))
    image: Mapped[LargeBinary] = mapped_column(LargeBinary)
    end_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    location: Mapped[str] = mapped_column(String(100))
    tags: Mapped[List[str]] = mapped_column(ARRAY(String))
    status: Mapped[str] = mapped_column(String(40))
    soldier_id: Mapped[int] = mapped_column(ForeignKey("soldier.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    # soldier = relationship("Soldier", back_populates="requests")
    # category = relationship("Category", back_populates="requests")
    # volunteers = relationship("VolunteerRequest", back_populates="aid_request")

    @staticmethod
    def create_dummy() -> "AidRequest": ...
