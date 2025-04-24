"""soldier model"""

from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import Base

from app.models.aid_request import AidRequest
from app.models.review import Review


class Soldier(Base):
    """
    Represents a military member who can submit aid requests
    """

    __tablename__ = "soldier"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(55), nullable=False)
    surname: Mapped[str] = mapped_column(String(55), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=True)
    unit: Mapped[str] = mapped_column(String(100), nullable=False)
    subsubunit: Mapped[str] = mapped_column(String(100), nullable=False)
    verified_until: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    battalion: Mapped[str] = mapped_column(String(255))

    requests: Mapped[list[AidRequest]] = relationship(
        AidRequest, cascade="all, delete-orphan"
    )
    reviews: Mapped[list[Review]] = relationship(Review, cascade="all, delete-orphan")
