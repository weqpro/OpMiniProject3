"""aid request model"""

import datetime
from sqlalchemy.dialects.postgresql import TSVECTOR, REGCONFIG
from sqlalchemy import (
    TEXT,
    Computed,
    String,
    ForeignKey,
    DateTime,
    cast,
    func,
    literal_column,
)
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base
from app.utils import AidRequestStatus


_SIMPLE_CFG = literal_column("'simple'").cast(REGCONFIG)


class AidRequest(Base):
    """
    Requests created by soldier
    """

    __tablename__ = "aid_request"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
    image: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(
        String(40), default=AidRequestStatus.PENDING, nullable=False
    )
    deadline: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    soldier_id: Mapped[int] = mapped_column(ForeignKey("soldier.id"), nullable=False)
    volunteer_id: Mapped[int] = mapped_column(ForeignKey("volunteer.id"), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=True)

    textsearch: Mapped[TSVECTOR] = mapped_column(
        TSVECTOR,
        Computed(
            func.setweight(func.to_tsvector(_SIMPLE_CFG, name), "A").op("||")(
                func.setweight(
                    func.to_tsvector(cast(_SIMPLE_CFG, REGCONFIG), description), "B"
                )
            ),
            persisted=True,
        ),
        nullable=False,
    )

    @staticmethod
    def create_dummy() -> "AidRequest":
        return AidRequest(
            id=123,
            name="Name",
            description="Some description",
            image="shit",
            deadline=datetime.datetime.now(),
            location="somewhere",
            status="not done",
            soldier_id=1234,
            category=None,
        )
