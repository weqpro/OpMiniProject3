from fastapi import Depends
from app.models import Volunteer
from app.repository import VolunteerRepository, get_volunteer_repository
from app.schemas import VolunteerSchemaIn
from .encoder.encoder import get_password_hash


class VolunteerService:
    def __init__(self, repo: VolunteerRepository) -> None:
        self.__repository = repo

    async def create(self, data: VolunteerSchemaIn) -> Volunteer:
        data_dict = data.model_dump()
        data_dict["password"] = await get_password_hash(data_dict["password"])
        entity = Volunteer(**data_dict)
        return await self.__repository.create(entity)

    async def get_by_id(self, volunteer_id: int) -> Volunteer | None:
        result = await self.__repository.find_by_condition(Volunteer.id == volunteer_id)
        return next(iter(result), None)

    async def delete(self, volunteer_id: int) -> None:
        result = await self.__repository.find_by_condition(Volunteer.id == volunteer_id)
        entity = next(iter(result), None)
        if entity:
            await self.__repository.delete(entity)

async def get_volunteer_service(
    repo: VolunteerRepository = Depends(get_volunteer_repository),
) -> VolunteerService:
    return VolunteerService(repo)
