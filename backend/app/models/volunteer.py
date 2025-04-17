"""volunteer model"""

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import ARRAY

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
    ratings: Mapped[list[float]] = mapped_column(
        ARRAY[Float], default=[], nullable=False
    )

    requests: Mapped[list[AidRequest]] = relationship()
    reviews: Mapped[list[Review]] = relationship(Review, cascade="all, delete-orphan")
