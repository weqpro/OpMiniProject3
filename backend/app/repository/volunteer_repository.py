from collections.abc import Sequence, Callable
from typing import override
from contextlib import AbstractAsyncContextManager

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql.expression import ColumnExpressionArgument

from app.contracts import RepositoryBase, VolunteerRepositoryBase
from app.models import Volunteer
from app.repository import RepositoryContext, get_repository_context


class VolunteerRepository(RepositoryBase[Volunteer], VolunteerRepositoryBase):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )
        super().__init__(session_maker, Volunteer)

    @override
    async def find(self, *order_by: ColumnElement | str) -> Sequence[Volunteer]:
        async with self._session_maker() as session:
            stmt = (
                select(self._model)
                .options(
                    selectinload(Volunteer.requests),
                    selectinload(Volunteer.reviews),
                )
                .order_by(*order_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()

    @override
    async def find_by_condition(
        self,
        condition: ColumnExpressionArgument[bool],
        *order_by: ColumnElement | str,
    ) -> Sequence[Volunteer]:
        async with self._session_maker() as session:
            stmt = (
                select(self._model)
                .where(condition)
                .options(
                    selectinload(Volunteer.requests),
                    selectinload(Volunteer.reviews),
                )
                .order_by(*order_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()


async def get_volunteer_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> VolunteerRepository:
    return VolunteerRepository(context)
