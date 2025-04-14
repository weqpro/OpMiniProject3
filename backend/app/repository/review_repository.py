from collections.abc import Sequence
from typing import override

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement

from app.contracts.repository_base import RepositoryBase
from app.models.review import Review
from app.repository.repository_context import RepositoryContext, get_repository_context


class ReviewRepository(RepositoryBase[Review]):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        self._session_maker = context.session_maker
        super().__init__(self._session_maker, Review)

    async def get_reviews_for_volunteer(self, volunteer_id: int) -> list[Review]:
        async with self._session_maker() as session:
            stmt = select(self._model).where(self._model.volunteer_id == volunteer_id)
            result = await session.execute(stmt)
            return result.scalars().all()


async def get_review_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> ReviewRepository:
    return ReviewRepository(context)
