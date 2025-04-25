from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
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
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )

        super().__init__(session_maker, Review)


async def get_review_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> ReviewRepository:
    return ReviewRepository(context)
