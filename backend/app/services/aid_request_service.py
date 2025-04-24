from collections.abc import Sequence
from fastapi import Depends, HTTPException


from app.schemas import SearchOptionsSchema
from app.schemas import (
    AidRequestSchemaIn,
    AidRequestSchemaInWithoutVolId,
    AidRequestSchemaUpdate,
)
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
    ) -> None:
        self.__repository: AidRequestRepository = aid_request_repository

    async def search(
        self, search_options: SearchOptionsSchema | None = None
    ) -> list[AidRequest]:
        if search_options is None:
            search_options = SearchOptionsSchema(text="", tags=[])

        aid_requests = await self.__repository.search(search_options=search_options)
        return [await self._add_image_url(r) for r in aid_requests]

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

    async def get_all(self) -> list[AidRequest]:
        requests = await self.__repository.find()
        return [await self._add_image_url(r) for r in requests]

    async def get_by_id(self, request_id: int) -> AidRequest | None:
        result = await self.__repository.find_by_condition(AidRequest.id == request_id)
        entity = next(iter(result), None)
        return await self._add_image_url(entity) if entity else None

    async def get_by_soldier(self, soldier_id: int) -> Sequence[AidRequest]:
        result = await self.__repository.find_by_condition(
            AidRequest.soldier_id == soldier_id
        )
        return [await self._add_image_url(r) for r in result]

    async def get_unassigned(self) -> list[AidRequest]:
        requests = await self.__repository.find_by_condition(
            AidRequest.volunteer_id.is_(None)
        )
        return [await self._add_image_url(r) for r in requests]

    async def create(
        self, aid_request: AidRequestSchemaInWithoutVolId, soldier_id: int
    ) -> AidRequest:
        aid_request_data = aid_request.model_dump()
        new_aid_request: AidRequest = AidRequest(
            soldier_id=soldier_id,
            status=AidRequestStatus.PENDING.value,
            **aid_request_data,
        )
        return await self.__repository.create(new_aid_request)

    async def update(self, request_id: int, data: AidRequestSchemaUpdate) -> AidRequest:
        result = await self.__repository.update(
            AidRequest.id == request_id, **data.model_dump()
        )
        entity: AidRequest | None = next(iter(result), None)

        if entity is None:
            raise HTTPException(status_code=404, detail="Request not found")

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)

        if "status" in update_data:
            entity.status = update_data["status"]

        await self.__repository.update(
            condition=(AidRequest.id == entity.id), **update_data
        )
        return await self._add_image_url(entity)

    async def get_by_volunteer(self, volunteer_id: int) -> Sequence[AidRequest]:
        result = await self.__repository.find_by_condition(
            AidRequest.volunteer_id == volunteer_id
        )
        return [await self._add_image_url(r) for r in result]

    async def delete(self, request_id: int) -> None:
        result = await self.__repository.find_by_condition(
            (AidRequest.id == request_id)
            & (AidRequest.status == AidRequestStatus.PENDING.value)
        )
        entity = next(iter(result), None)
        if not entity:
            raise HTTPException(status_code=404, detail="Pending request not found")

        await self.__repository.delete(entity)

    async def publish(self, request_id: int) -> AidRequest | None:
        result = await self.__repository.find_by_condition(AidRequest.id == request_id)
        entity: AidRequest | None = next(iter(result), None)
        if not entity:
            return None

        entity.status = AidRequestStatus.IN_PROGRESS.value
        await self.__repository.update(
            condition=(AidRequest.id == entity.id), status=entity.status
        )
        return await self._add_image_url(entity)

    async def _add_image_url(self, entity: AidRequest) -> AidRequest:
        if entity.image:
            entity.image = f"/api/v1/aid_requests/uploads/{entity.image}"
        return entity

    async def complete(self, request_id: int, volunteer_id: int) -> AidRequest | None:
        result = await self.__repository.find_by_condition(
            (AidRequest.id == request_id)
            & (AidRequest.volunteer_id == volunteer_id)
            & (AidRequest.status == AidRequestStatus.IN_PROGRESS.value)
        )
        request = next(iter(result), None)

        if not request:
            return None

        request.status = AidRequestStatus.COMPLETED.value
        await self.__repository.update(
            condition=(AidRequest.id == request.id), status=request.status
        )
        return request


async def get_aid_request_service(
    aid_request_repository: AidRequestRepository = Depends(get_aid_request_repository),
) -> AidRequestService:
    return AidRequestService(aid_request_repository)
