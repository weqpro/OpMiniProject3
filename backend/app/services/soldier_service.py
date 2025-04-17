from collections.abc import Sequence
from fastapi import Depends

from app.schemas import SoldierSchema
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

    async def create(
        self,
        soldier: SoldierSchema,
    ) -> Soldier:
        return await self.__repository.create(Soldier(**soldier.model_dump()))

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
