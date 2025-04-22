"""review model"""

from typing import List

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, ForeignKey, Boolean, String, Text, SmallInteger
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import CheckConstraint

from app.models.base import Base


class Review(Base):
    """
    Reviews of volunteers from soldiers
    """

    __tablename__ = "review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    review_text: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    reported: Mapped[bool] = mapped_column(Boolean, default=False)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
    soldier_id: Mapped[int] = mapped_column(ForeignKey("soldier.id"))
    volunteer_id: Mapped[int] = mapped_column(ForeignKey("volunteer.id"))
    request_id: Mapped[int] = mapped_column(ForeignKey("aid_request.id"), unique=True)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5', name='rating_range_check'),
    )
    # soldier: Mapped["Soldier"] = relationship("Soldier", back_populates="reviews")
    # volunteer: Mapped["Volunteer"] = relationship("Volunteer", back_populates="reviews")
