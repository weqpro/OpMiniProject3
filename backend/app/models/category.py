'''category model'''

from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.models.base import Base


class Category(Base):
    '''
    Categories to which requests belong
    '''
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255))

    requests: Mapped[list["AidRequest"]] = relationship(
        "AidRequest", back_populates="category", cascade="all, delete-orphan")
