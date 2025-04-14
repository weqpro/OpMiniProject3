from collections.abc import Sequence
from typing import override

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
        self._session_maker = context.session_maker
        super().__init__(self._session_maker, AidRequest)


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
