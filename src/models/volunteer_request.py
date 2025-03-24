'''volunteer request model'''
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class VolunteerRequest(Base):
    '''
    Relationship between volunteers and requests
    '''
    __tablename__ = "volunteer_request"

    id = Column(Integer, primary_key=True, index=True)
    volunteer_id = Column(Integer, ForeignKey("volunteer.id"))
    aid_request_id = Column(Integer, ForeignKey("request.id"))

    volunteer = relationship("Volunteer", back_populates="requests")
    aid_request = relationship("AidRequest", back_populates="volunteers")
