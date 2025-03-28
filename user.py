'''user model'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    '''
    Represents a generic user
    '''
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(55))
    surname = Column(String(55))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    phone_number = Column(String(15), unique=True)