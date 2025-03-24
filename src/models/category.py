'''category model'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    '''
    Categories to which requests belong
    '''
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    requests = relationship("AidRequest", back_populates="category")
