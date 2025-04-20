from collections.abc import Sequence
from fastapi import Depends, HTTPException

from .encoder.encoder import get_password_hash, verify_password
from app.schemas import SoldierSchemaIn, SoldierUpdateSchema, SoldierSchema
from app.models import Soldier
from app.repository import (
    SoldierRepository,
    get_soldier_repository,
)


class SoldierService:
    def __init__(
        self,
        soldier_repository: SoldierRepository,
    ) -> None:
        self.__repository: SoldierRepository = soldier_repository

    async def create_soldier(self, data: SoldierSchemaIn) -> Soldier:
        data_dict = data.model_dump()
        data_dict["password"] = await get_password_hash(data_dict["password"])
        soldier = Soldier(**data_dict)
        return await self.__repository.create(soldier)

    async def get_all(self) -> Sequence[Soldier]:
        return await self.__repository.find()

    async def get_with_email(self, email: str) -> Soldier | None:
        result: Sequence[Soldier] = await self.__repository.find_by_condition(
            Soldier.email == email
        )
        return next(iter(result), None)

    async def update_me(self, soldier_id: int, data: SoldierUpdateSchema) -> SoldierSchema:
        soldier_list = await self.__repository.find_by_condition(Soldier.id == soldier_id)
        soldier = next(iter(soldier_list), None)
        if not soldier:
            raise HTTPException(status_code=404, detail="Soldier not found")

        if not await verify_password(data.password, soldier.password):
            raise HTTPException(status_code=403, detail="Incorrect password")

        update_data = data.model_dump(exclude_unset=True)
        update_data.pop("password", None)

        for key, value in update_data.items():
            if hasattr(soldier, key):
                setattr(soldier, key, value)

        await self.__repository.update(
            condition=(Soldier.id == soldier.id),
            **update_data
        )

        return SoldierSchema.model_validate(soldier)


async def get_soldier_service(
    soldier_repository: SoldierRepository = Depends(get_soldier_repository),
) -> SoldierService:
    return SoldierService(soldier_repository)
