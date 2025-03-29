'''review model'''

from typing import List

from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import Integer, ForeignKey, Boolean, ARRAY, String, Text

from app.models.base import Base


class Review(Base):
    '''
    Reviews of volunteers from soldiers
    '''
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    review_text: Mapped[str] = mapped_column(Text, nullable=False)
    reported: Mapped[bool] = mapped_column(Boolean, default=False)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
    soldier_id: Mapped[int] = mapped_column(ForeignKey("soldier.id"))
    volunteer_id: Mapped[int] = mapped_column(ForeignKey("volunteer.id"))

    soldier: Mapped["Soldier"] = relationship("Soldier", back_populates="reviews")
    volunteer: Mapped["Volunteer"] = relationship("Volunteer", back_populates="reviews")
