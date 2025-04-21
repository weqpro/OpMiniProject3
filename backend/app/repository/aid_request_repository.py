from collections.abc import Callable, Sequence
from contextlib import AbstractAsyncContextManager
from typing import override

from fastapi import Depends
from sqlalchemy.dialects.postgresql.types import TSVECTOR, TSQUERY
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import ColumnElement, func, select

from app.contracts.repository_base import RepositoryBase
from app.contracts.aid_request_repository_base import AidRequestRepositoryBase
from app.models.aid_request import AidRequest
from app.repository.repository_context import RepositoryContext, get_repository_context
from app.schemas import SearchOptionsSchema


class AidRequestRepository(RepositoryBase[AidRequest], AidRequestRepositoryBase):
    @override
    def __init__(self, context: RepositoryContext) -> None:
        session_maker: Callable[..., AbstractAsyncContextManager[AsyncSession]] = (
            context.session_maker
        )

        super().__init__(session_maker, AidRequest)

    @override
    async def search(self, search_options: SearchOptionsSchema) -> Sequence[AidRequest]:
        async with self._session_maker() as session:
            tsquery: ColumnElement[TSQUERY] = func.plainto_tsquery(
                "simple", search_options.text
            )

            rank: ColumnElement[float] = func.func.ts_rank_cd(
                AidRequest.textsearch, tsquery, 32
            ).label("rank")  # mode 32 for normalization (rank/rank+1)

            stmt = (
                select(AidRequest)
                .where(AidRequest.textsearch.match(tsquery))  # equivalent to @@
                .order_by(rank.desc())
            )

            result = await session.execute(stmt)
            return result.scalars().all()


async def get_aid_request_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> AidRequestRepository:
    return AidRequestRepository(context)
