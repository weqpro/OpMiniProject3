from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
from typing import override

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

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


async def get_aid_request_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> AidRequestRepository:
    return AidRequestRepository(context)
