from collections.abc import Sequence
from fastapi import Depends, HTTPException
from haversine import haversine
from app.models import Category
from app.schemas import SearchOptionsSchema
from app.schemas import AidRequestSchema, AidRequestSchemaIn, AidRequestSchemaInWithoutVolId, AidRequestSchemaUpdate
from app.models import AidRequest
from app.repository import (
    AidRequestRepository,
    get_aid_request_repository,
    CityRepository,
    get_city_repository
)
from app.utils import AidRequestStatus
from app.repository.city_repository import get_city_repository, CityRepository

class AidRequestService:
    def __init__(
        self,
        aid_request_repository: AidRequestRepository = Depends(get_aid_request_repository),
        city_repository: CityRepository = Depends(get_city_repository),
    ) -> None:
        self.__repository = aid_request_repository
        self.__cityrepo = city_repository

    async def search(self, search_options: SearchOptionsSchema | None = None) -> list[AidRequest]:
        if search_options is None:
            search_options = SearchOptionsSchema(text="", tags=[])
        aid_requests = await self.__repository.find_by_condition(
            AidRequest.name.contains(search_options.text),
            AidRequest.tags.overlap(search_options.tags),
        )
        return [self._add_image_url(r) for r in aid_requests]

    async def dummy_search(self) -> list[AidRequest]:
        return [AidRequest.create_dummy(), AidRequest.create_dummy()]

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
        return [self._add_image_url(r) for r in requests]

    async def get_by_id(self, request_id: int) -> AidRequest | None:
        result = await self.__repository.find_by_condition(AidRequest.id == request_id)
        entity = next(iter(result), None)
        return self._add_image_url(entity) if entity else None

    async def get_by_soldier(self, soldier_id: int) -> Sequence[AidRequest]:
        result = await self.__repository.find_by_condition(AidRequest.soldier_id == soldier_id)
        return [self._add_image_url(r) for r in result]

    async def get_unassigned(self) -> list[AidRequest]:
        requests = await self.__repository.find_by_condition(AidRequest.volunteer_id.is_(None))
        return [self._add_image_url(r) for r in requests]

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

    async def update(self, request_id: int, soldier_id: int, data: dict, image: str | None = None) -> AidRequest:
        result = await self.__repository.find_by_condition(
            (AidRequest.id == request_id) & (AidRequest.soldier_id == soldier_id)
        )
        entity: AidRequest | None = next(iter(result), None)

        if not entity:
            raise HTTPException(status_code=404, detail="Request not found")

        if not data and not image:
            raise HTTPException(status_code=422, detail="Nothing to update")

        if image:
            data["image"] = image

        for key, value in data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)

        await self.__repository.update(condition=(AidRequest.id == entity.id), **data)
        return self._add_image_url(entity)

    async def update_volunteer_assignment(self, request_id: int, data: AidRequestStatus) -> AidRequest | None:
        result = await self.__repository.find_by_condition(AidRequest.id == request_id)
        entity: AidRequest | None = next(iter(result), None)

        if not entity:
            return None

        entity.volunteer_id = data.volunteer_id
        entity.status = data.status

        await self.__repository.update(
            condition=(AidRequest.id == request_id),
            volunteer_id=data.volunteer_id,
            status=data.status
        )

        return self._add_image_url(entity)

    async def get_by_volunteer(self, volunteer_id: int) -> Sequence[AidRequest]:
        result = await self.__repository.find_by_condition(AidRequest.volunteer_id == volunteer_id)
        return [self._add_image_url(r) for r in result]

    async def delete(self, request_id: int) -> None:
        result = await self.__repository.find_by_condition(
            (AidRequest.id == request_id) & (AidRequest.status == AidRequestStatus.PENDING.value)
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
        await self.__repository.update(condition=(AidRequest.id == entity.id), status=entity.status)
        return self._add_image_url(entity)

    def _add_image_url(self, entity: AidRequest) -> AidRequest:
        if entity.image:
            entity.image = f"/api/v1/aid_requests/uploads/{entity.image}"
        return entity

    async def complete(self, request_id: int, volunteer_id: int) -> AidRequest | None:
        result = await self.__repository.find_by_condition(
            (AidRequest.id == request_id) &
            (AidRequest.volunteer_id == volunteer_id) &
            (AidRequest.status == AidRequestStatus.IN_PROGRESS.value)
        )
        request = next(iter(result), None)

        if not request:
            return None

        request.status = AidRequestStatus.COMPLETED.value
        await self.__repository.update(condition=(AidRequest.id == request.id), status=request.status)
        return request

    async def get_requests_nearest_to_city(
            self,
            volunteer_city_name: str,
    ) -> list[AidRequest]:
        city_from = await self.__cityrepo.get_by_name(volunteer_city_name)
        if not city_from:
            raise HTTPException(status_code=400, detail="City not found")

        active_reqs = await self.__repository.find_by_condition(AidRequest.volunteer_id.is_(None))
        distances: list[tuple[AidRequest, float]] = []
        for req in active_reqs:
            city_to = await self.__cityrepo.get_by_name(req.location)
            if city_to:
                d = haversine(
                    (city_from.latitude, city_from.longitude),
                    (city_to.latitude, city_to.longitude)
                )
                distances.append((req, d))

        distances.sort(key=lambda x: x[1])
        return [self._add_image_url(req) for req, _ in distances]

async def get_aid_request_service(
    aid_request_repository: AidRequestRepository = Depends(get_aid_request_repository),
    city_repository:    CityRepository       = Depends(get_city_repository),
) -> AidRequestService:
    return AidRequestService(aid_request_repository, city_repository)

