"""volunteer model"""

from typing import List

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import Base

from app.models.review import Review
from app.models.aid_request import AidRequest


class Volunteer(Base):
    """
    Represents a volunteer who provides assistance
    """

    __tablename__ = "volunteer"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(55), nullable=False)
    surname: Mapped[str] = mapped_column(String(55), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)

    requests: Mapped[List[AidRequest]] = relationship()
    reviews: Mapped[List[Review]] = relationship(Review, cascade="all, delete-orphan")
