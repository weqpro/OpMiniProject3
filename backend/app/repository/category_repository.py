from collections.abc import Callable, Sequence
from typing import override, Any
from contextlib import AbstractAsyncContextManager

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement

from app.contracts.repository_base import RepositoryBase
from app.contracts.category_repository_base import CategoryRepositoryBase
from app.models.category import Category
from app.repository.repository_context import RepositoryContext, get_repository_context


class CategoryRepository(RepositoryBase[Category], CategoryRepositoryBase):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )
        super().__init__(session_maker, Category)


async def get_category_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> CategoryRepository:
    return CategoryRepository(context)
