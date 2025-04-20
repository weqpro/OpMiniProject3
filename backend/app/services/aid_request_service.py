from collections.abc import Sequence

from fastapi import Depends
from sqlalchemy.sql.expression import ColumnExpressionArgument
from sqlalchemy import func, or_, select


from app.models import Category
from app.schemas import SearchOptionsSchema
from app.schemas import AidRequestSchema, AidRequestSchemaIn
from app.models import AidRequest
from app.repository import (
    AidRequestRepository,
    get_aid_request_repository,
)
from app.utils import AidRequestStatus


class AidRequestService:
    def __init__(
        self,
        aid_request_repository: AidRequestRepository,
        session_maker,
    ) -> None:
        self.__repository: AidRequestRepository = aid_request_repository
        
        self.__session_maker = session_maker

    async def search(self, search_options: SearchOptionsSchema | None = None) -> list[AidRequest]:
        if search_options is None:
            search_options = SearchOptionsSchema(text="", tags=[])

        term = search_options.text or ""
        tags = search_options.tags

        search_column = func.coalesce(AidRequest.name, '').self_group()

        async with self.__session_maker() as session:
            stmt = (
                select(AidRequest)
                .where(
                    or_(
                        search_column.bool_op('%')(term),
                        AidRequest.tags.overlap(tags),
                    )
                )
                .order_by(func.similarity(search_column, term).desc())
            )

            result = await session.execute(stmt)
            return list(result.scalars().all())

    # async def search(
    #     self, search_options: SearchOptionsSchema | None = None
    # ) -> list[AidRequest]:
    #     if search_options is None:
    #         search_options = SearchOptionsSchema(text="", tags=[])

    #     aid_requests: Sequence[AidRequest] = await self.__repository.find_by_condition(
    #         AidRequest.name.contains(search_options.text),
    #         AidRequest.tags.overlap(search_options.tags),
    #     )
    #     return list(aid_requests)

    # async def dummy_search(self) -> list[AidRequest]:
    #     return [AidRequest.create_dummy(), AidRequest.create_dummy()]

    async def create_aid_request(
        self, aid_request: AidRequestSchemaIn, soldier_id: int
    ) -> AidRequest:
        aid_request_data = aid_request.model_dump()
        new_aid_request: AidRequest = AidRequest(
            soldier_id=soldier_id,
            status=AidRequestStatus.PENDING,
            **aid_request_data,
        )

        return await self.__repository.create(new_aid_request)

    async def get_all(self) -> Sequence[AidRequest]:
        return await self.__repository.find()

    async def get_by_id(self, request_id: int) -> AidRequest | None:
        result = await self.__repository.find_by_condition(AidRequest.id == request_id)
        return next(iter(result), None)

    async def get_by_soldier(self, soldier_id: int) -> Sequence[AidRequest]:
        return await self.__repository.find_by_condition(
            AidRequest.soldier_id == soldier_id
        )

    async def get_unassigned(self) -> Sequence[AidRequest]:
        return await self.__repository.find_by_condition(
            AidRequest.volunteer_id.is_(None)
        )

    async def create(
        self, aid_request: AidRequestSchemaIn, soldier_id: int
    ) -> AidRequest:
        aid_request_data = aid_request.model_dump()
        new_aid_request: AidRequest = AidRequest(
            soldier_id=soldier_id,
            status=AidRequestStatus.PENDING,
            **aid_request_data,
        )
        return await self.__repository.create(new_aid_request)

    async def update(
        self, request_id: int, data: AidRequestSchemaIn
    ) -> AidRequest | None:
        return await self.__repository.update(
            AidRequest.id == request_id, **data.model_dump()
        )

    async def delete(self, request_id: int) -> None:
        result = await self.__repository.find_by_condition(AidRequest.id == request_id)
        entity = next(iter(result), None)
        if entity:
            await self.__repository.delete(entity)


async def get_aid_request_service(
    aid_request_repository: AidRequestRepository = Depends(get_aid_request_repository),
) -> AidRequestService:
    return AidRequestService(aid_request_repository)
