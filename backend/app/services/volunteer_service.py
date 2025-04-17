from fastapi import Depends
from app.models import Volunteer
from app.repository import VolunteerRepository, get_volunteer_repository
from app.schemas import VolunteerSchemaIn


class VolunteerService:
    def __init__(self, repo: VolunteerRepository) -> None:
        self.__repo = repo

    async def create(self, data: VolunteerSchemaIn) -> Volunteer:
        entity = Volunteer(**data.model_dump())
        return await self.__repo.create(entity)

    async def get_by_id(self, volunteer_id: int) -> Volunteer | None:
        result = await self.__repo.find_by_condition(Volunteer.id == volunteer_id)
        return next(iter(result), None)

    async def delete(self, volunteer_id: int) -> None:
        result = await self.__repo.find_by_condition(Volunteer.id == volunteer_id)
        entity = next(iter(result), None)
        if entity:
            await self.__repo.delete(entity)
            
    async def get_with_email(self, email: str) -> Volunteer | None:
        result = await self.__repo.find_by_condition(Volunteer.email == email)
        return next(iter(result), None)


async def get_volunteer_service(
    repo: VolunteerRepository = Depends(get_volunteer_repository),
) -> VolunteerService:
    return VolunteerService(repo)
