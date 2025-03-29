'''volunteer model'''
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Volunteer(Base):
    '''
    Represents a volunteer who provides assistance
    '''
    __tablename__ = "volunteer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(55))
    surname = Column(String(55))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    phone_number = Column(String(15), unique=True)
    rating = Column(DECIMAL(2,1), default=0.0)

    requests = relationship("VolunteerRequest", back_populates="volunteer")
    reviews = relationship("Review", back_populates="volunteer")
