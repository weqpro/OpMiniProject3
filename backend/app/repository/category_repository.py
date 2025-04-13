from collections.abc import Callable
from typing import override
from contextlib import AbstractAsyncContextManager

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.contracts import RepositoryBase
from app.models import Category
from app.repository import RepositoryContext, get_repository_context


class CategoryRepository(RepositoryBase[Category]):
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
