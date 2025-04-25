from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Float
from app.models.base import Base

class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    latitude:  Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)