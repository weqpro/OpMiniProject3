from collections.abc import Callable, Sequence
from typing import override
from contextlib import AbstractAsyncContextManager

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql.expression import ColumnExpressionArgument

from app.contracts.repository_base import RepositoryBase
from app.models.category import Category
from app.repository.repository_context import RepositoryContext, get_repository_context


class CategoryRepository(RepositoryBase[Category]):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )
        super().__init__(session_maker, Category)

    async def find(self, *order_by: ColumnElement | str) -> Sequence[Category]:
        async with self._session_maker() as session:
            stmt = select(self._model).order_by(*order_by)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def find_by_condition(
        self,
        condition: ColumnExpressionArgument[bool],
        *order_by: ColumnElement | str,
    ) -> Sequence[Category]:
        async with self._session_maker() as session:
            stmt = select(self._model).where(condition).order_by(*order_by)
            result = await session.execute(stmt)
            return result.scalars().all()


async def get_category_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> CategoryRepository:
    return CategoryRepository(context)
