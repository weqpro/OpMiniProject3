from fastapi import Depends

from app.schemas.search_options import SearchOptions
from app.schemas.aid_request import AidRequestSchema
from app.models.aid_request import AidRequest
from app.repository.aid_request_repository import (
    AidRequestRepository,
    get_aid_request_repository,
)


class AidRequestService:
    def __init__(
        self,
        aid_request_repository: AidRequestRepository,
    ) -> None:
        self.__repository: AidRequestRepository = aid_request_repository

    async def search(self, search_options: SearchOptions | None = None) -> None:
        if search_options is None:
            search_options = SearchOptions(text="", tags=[])

        await self.__repository.find_by_condition(
            AidRequest.name.contains(search_options.text)
        )

    async def dummy_search(self) -> list[AidRequest]:
        return [AidRequest.create_dummy(), AidRequest.create_dummy()]

    async def create_aid_request(self, aid_request: AidRequestSchema) -> AidRequest:
        return await self.__repository.create(AidRequest(**aid_request.model_dump()))

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
