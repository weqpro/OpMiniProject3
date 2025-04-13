from collections.abc import Sequence
from fastapi import Depends

from app.models import Category
from app.schemas import SearchOptionsSchema
from app.schemas import AidRequestSchema
from app.models import AidRequest
from app.repository import (
    AidRequestRepository,
    get_aid_request_repository,
)


class AidRequestService:
    def __init__(
        self,
        aid_request_repository: AidRequestRepository,
    ) -> None:
        self.__repository: AidRequestRepository = aid_request_repository

    async def search(
        self, search_options: SearchOptionsSchema | None = None
    ) -> list[AidRequest]:
        if search_options is None:
            search_options = SearchOptionsSchema(text="", tags=[])

        aid_requests: Sequence[AidRequest] = await self.__repository.find_by_condition(
            AidRequest.name.contains(search_options.text),
            AidRequest.tags.overlap(search_options.tags),
        )
        return list(aid_requests)

    async def dummy_search(self) -> list[AidRequest]:
        return [AidRequest.create_dummy(), AidRequest.create_dummy()]

    async def create_aid_request(
        self,
        aid_request: AidRequestSchema,
    ) -> AidRequest:
        aid_request_data = aid_request.model_dump()
        category_data = aid_request_data.pop("category", None)

        new_aid_request: AidRequest = AidRequest(**aid_request_data)

        if category_data is not None:
            new_category = Category(**category_data)
            new_aid_request.category = new_category

        return await self.__repository.create(new_aid_request)

    # async def update_aid_request_status(
    #     self, db, aid_request_id: int, status: str
    # ) -> AidRequest:
    #     return await self.__repository.update_aid_request_status(
    #         db=db, aid_request_id=aid_request_id, status=status
    #     )
    #
    # async def set_volunteer_deadline(
    #     self, db, aid_request_id: int, deadline: datetime.datetime
    # ) -> AidRequestOut:
    #     return await self.__repository.set_volunteer_deadline(
    #         db=db, aid_request_id=aid_request_id, deadline=deadline
    #     )
    #
    # async def delete_aid_request(
    #     self, db, aid_request_id: int, soldier_id: int
    # ) -> bool:
    #     return await self.__repository.delete_aid_request(
    #         db=db, aid_request_id=aid_request_id, soldier_id=soldier_id
    #     )
    #
    # async def reject_aid_request(
    #     self, db, aid_request_id: int, volunteer_id: int
    # ) -> bool:
    #     return await self.__repository.reject_aid_request(
    #         db=db, aid_request_id=aid_request_id, volunteer_id=volunteer_id
    #     )


async def get_aid_request_service(
    aid_request_repository: AidRequestRepository = Depends(get_aid_request_repository),
) -> AidRequestService:
    return AidRequestService(aid_request_repository)
