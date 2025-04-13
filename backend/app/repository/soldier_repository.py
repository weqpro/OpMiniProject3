from collections.abc import Callable, Sequence
from typing import override
from typing import Any
from contextlib import AbstractAsyncContextManager

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql.expression import ColumnExpressionArgument

from app.contracts.repository_base import RepositoryBase
from app.contracts.soldier_repository_base import SoldierRepositoryBase
from app.models.soldier import Soldier
from app.repository.repository_context import RepositoryContext, get_repository_context


class SoldierRepository(RepositoryBase[Soldier], SoldierRepositoryBase):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )

        super().__init__(session_maker, Soldier)

    @override
    async def find(self, *order_by: ColumnElement | str) -> Sequence[Soldier]:
        async with self._session_maker() as session:
            stmt = (
                select(self._model)
                .options(
                    selectinload(Soldier.requests),
                    selectinload(Soldier.reviews),
                )
                .order_by(*order_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()

    @override
    async def find_by_condition(
        self,
        condition: Any,
        *order_by: ColumnElement | str,
    ) -> Sequence[Soldier]:
        async with self._session_maker() as session:
            stmt = (
                select(self._model)
                .where(condition)
                .options(
                    selectinload(Soldier.requests),
                    selectinload(Soldier.reviews),
                )
                .order_by(*order_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()


async def get_soldier_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> SoldierRepository:
    return SoldierRepository(context)
