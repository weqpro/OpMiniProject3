from collections.abc import Callable, Sequence
from typing import override
from contextlib import AbstractAsyncContextManager

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql.expression import ColumnExpressionArgument

from app.contracts.repository_base import RepositoryBase
from app.contracts.aid_request_repository_base import AidRequestRepositoryBase
from app.models.aid_request import AidRequest
from app.repository.repository_context import RepositoryContext, get_repository_context


class AidRequestRepository(RepositoryBase[AidRequest], AidRequestRepositoryBase):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )

        super().__init__(session_maker, AidRequest)

    @override
    async def find(self, *order_by: ColumnElement | str) -> Sequence[AidRequest]:
        """Gets objects with the specified ordering, and filtering."""
        async with self._session_maker() as session:
            stmt = (
                select(self._model)
                .options(selectinload(AidRequest.category))
                .order_by(*order_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()

    @override
    async def find_by_condition(
        self,
        condition: ColumnExpressionArgument[bool],
        *order_by: ColumnElement | str,
    ) -> Sequence[AidRequest]:
        """Gets objects with the specified ordering, and filtering."""
        async with self._session_maker() as session:
            stmt = (
                select(self._model)
                .options(selectinload(AidRequest.category))
                .where(condition)
                .order_by(*order_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()

    # @override
    # def get_aid_request_by_soldier(self, soldier_id: int) -> list[AidRequest]:
    #     """Get all aid requests for a specific soldier"""
    #     pass
    #
    # @override
    # def get_aid_request_by_category(self, category_id: int) -> list[AidRequest]:
    #     """Get all aid requests for a specific category"""
    #     pass


async def get_aid_request_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> AidRequestRepository:
    return AidRequestRepository(context)
