"""category model"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class Category(Base):
    """
    Categories to which requests belong
    """

    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255))
    request_id: Mapped[int] = mapped_column(ForeignKey("aid_request.id"))
