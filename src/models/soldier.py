'''soldier model'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Soldier(Base):
    '''
    Represents a military member who can submit aid requests
    '''
    __tablename__ = "soldier"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(55))
    surname = Column(String(55))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    phone_number = Column(String(15), unique=True)
    unit = Column(String(100))
    subunit = Column(String(100))
    battalion = Column(String(255))

    requests = relationship("AidRequest", back_populates="soldier")
    reviews = relationship("Review", back_populates="soldier")
