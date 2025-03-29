"""volunteer request model"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base import Base


class VolunteerRequest(Base):
    """
    Relationship between volunteers and requests
    """

    __tablename__ = "volunteer_request"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    volunteer_id: Mapped[int] = mapped_column(ForeignKey("volunteer.id"))
    aid_request_id: Mapped[int] = mapped_column(ForeignKey("request.id"))

    volunteer = relationship("Volunteer", back_populates="requests")
    aid_request = relationship("AidRequest", back_populates="volunteers")
