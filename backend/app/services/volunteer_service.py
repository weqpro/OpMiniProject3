from fastapi import Depends, HTTPException
from app.models import Volunteer
from app.repository import VolunteerRepository, get_volunteer_repository
from app.schemas import VolunteerSchemaIn, VolunteerUpdateSchema, VolunteerSchema
from .encoder.encoder import get_password_hash, verify_password


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

    async def update_me(self, volunteer_id: int, data: VolunteerUpdateSchema) -> VolunteerSchema:
        volunteer_list = await self.__repository.find_by_condition(Volunteer.id == volunteer_id)
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

        await self.__repository.update(
            condition=(Volunteer.id == volunteer.id),
            **update_data
        )

        return VolunteerSchema.model_validate(volunteer)


async def get_volunteer_service(
    repo: VolunteerRepository = Depends(get_volunteer_repository),
) -> VolunteerService:
    return VolunteerService(repo)
