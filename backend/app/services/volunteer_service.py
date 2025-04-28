from fastapi import Depends, HTTPException
from sqlalchemy import func
from app.models import Volunteer, Review, Volunteer
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import VolunteerRepository, get_volunteer_repository
from app.schemas import VolunteerSchemaIn, VolunteerUpdateSchema, VolunteerSchema
from contextlib import asynccontextmanager
from app.repository.repository_context import get_repository_context
from .encoder.encoder import get_password_hash, verify_password

class VolunteerService:
    def __init__(self, repo: VolunteerRepository, session_maker) -> None:
        self.__repo = repo
        self.__session_maker = session_maker

    async def create(self, data: VolunteerSchemaIn) -> Volunteer:
        data_dict = data.model_dump()
        data_dict["password"] = await get_password_hash(data_dict["password"])
        entity = Volunteer(**data_dict)
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

    async def update_me(self, volunteer_id: int, data: VolunteerUpdateSchema) -> VolunteerSchema:
        volunteer_list = await self.__repo.find_by_condition(Volunteer.id == volunteer_id)
        volunteer = next(iter(volunteer_list), None)
        if not volunteer:
            raise HTTPException(status_code=404, detail="Volunteer not found")

        if not await verify_password(data.password, volunteer.password):
            raise HTTPException(status_code=403, detail="Incorrect password")

        update_data = data.model_dump(exclude_unset=True)
        update_data.pop("password", None)

        for key, value in update_data.items():
            if hasattr(volunteer, key):
                setattr(volunteer, key, value)

        await self.__repo.update(
            condition=(Volunteer.id == volunteer.id),
            **update_data
        )

        return VolunteerSchema.model_validate(volunteer)

    async def change_password(self, email: str, old_pass: str, new_pass: str):
        result = await self.__repo.find_by_condition(Volunteer.email == email)
        user = next(iter(result), None)
        if not user or not await verify_password(old_pass, user.password):
            raise HTTPException(status_code=403, detail="Incorrect password")

        user.password = await get_password_hash(new_pass)
        await self.__repo.update(
            condition=(Volunteer.id == user.id),
            password=user.password
        )

    async def find_by_email(self, email: str) -> Volunteer | None:
        volunteers = await self.__repo.find_by_condition(Volunteer.email == email)
        return volunteers[0] if volunteers else None


async def get_volunteer_service(
    repo: VolunteerRepository = Depends(get_volunteer_repository),
    context = Depends(get_repository_context),
) -> VolunteerService:
    return VolunteerService(repo, context.session_maker)
