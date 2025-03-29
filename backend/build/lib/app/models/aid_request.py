"""aid request model"""

from sqlalchemy import Column, Integer, String, ForeignKey, Date, LargeBinary, ARRAY
from sqlalchemy.orm import relationship
from app.models.base import Base


class AidRequest(Base):
    """
    Requests created by soldier
    """

    __tablename__ = "aid_request"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(1000))
    image = Column(LargeBinary)
    end_date = Column(Date)
    location = Column(String(100))
    tags = Column(ARRAY(String))
    status = Column(String(40))
    soldier_id = Column(Integer, ForeignKey("soldier.id"))
    category_id = Column(Integer, ForeignKey("category.id"))

    soldier = relationship("Soldier", back_populates="requests")
    category = relationship("Category", back_populates="requests")
    volunteers = relationship("VolunteerRequest", back_populates="aid_request")
