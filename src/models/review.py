'''review model'''
from sqlalchemy import Column, Integer, ForeignKey, Boolean, ARRAY, String, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Review(Base):
    '''
    Reviews of volunteers from soldiers
    '''
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    review_text =  Column(Text)
    reported = Column(Boolean, default=False)
    tags = Column(ARRAY(String))
    soldier_id = Column(Integer, ForeignKey("soldier.id"))
    volunteer_id = Column(Integer, ForeignKey("volunteer.id"))

    soldier = relationship("Soldier", back_populates="reviews")
    volunteer = relationship("Volunteer", back_populates="reviews")
