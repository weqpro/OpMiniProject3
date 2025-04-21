from sqlalchemy import func
from app.models import Volunteer, Review
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import VolunteerRepository, get_volunteer_repository
from app.schemas import VolunteerSchemaIn, VolunteerSchema
from fastapi import Depends
from contextlib import asynccontextmanager
from app.repository.repository_context import get_repository_context


class VolunteerService:
    def __init__(self, repo: VolunteerRepository, session_maker) -> None:
        self.__repo = repo
        self.__session_maker = session_maker

    async def create(self, data: VolunteerSchemaIn) -> Volunteer:
        entity = Volunteer(**data.model_dump())
        return await self.__repo.create(entity)

    async def get_by_id(self, volunteer_id: int) -> Volunteer | None:
        result = await self.__repo.find_by_condition(Volunteer.id == volunteer_id)
        volunteer = next(iter(result), None)

        if volunteer is None:
            return None

        avg_rating = await self._get_average_rating(volunteer_id)

        return VolunteerSchema(
            id=volunteer.id,
            name=volunteer.name,
            surname=volunteer.surname,
            email=volunteer.email,
            password=volunteer.password,
            phone_number=volunteer.phone_number,
            rating=avg_rating if avg_rating is not None else 0.0,
        )
        # result = await self.__repo.find_by_condition(Volunteer.id == volunteer_id)
        # return next(iter(result), None)
        
    async def _get_average_rating(self, volunteer_id: int) -> float | None:
        async with self.__session_maker() as session:
            result = await session.execute(
                func.avg(Review.rating).select().where(Review.volunteer_id == volunteer_id)
            )
            return result.scalar()

    async def delete(self, volunteer_id: int) -> None:
        result = await self.__repo.find_by_condition(Volunteer.id == volunteer_id)
        entity = next(iter(result), None)
        if entity:
            await self.__repo.delete(entity)

async def get_volunteer_service(
    repo: VolunteerRepository = Depends(get_volunteer_repository),
    context = Depends(get_repository_context),
) -> VolunteerService:
    return VolunteerService(repo, context.session_maker)
