from collections.abc import Sequence
from fastapi import Depends

from .encoder.encoder import get_password_hash
from app.schemas import SoldierSchemaIn
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

async def get_soldier_service(
    soldier_repository: SoldierRepository = Depends(get_soldier_repository),
) -> SoldierService:
    return SoldierService(soldier_repository)
