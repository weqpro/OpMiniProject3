from collections.abc import Sequence
from typing import override

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
        self._session_maker = context.session_maker
        super().__init__(self._session_maker, Category)

async def get_category_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> CategoryRepository:
    return CategoryRepository(context)
