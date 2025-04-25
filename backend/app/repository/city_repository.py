from fastapi import Depends
from app.contracts.repository_base import RepositoryBase
from app.models.city import City
from app.repository.repository_context import RepositoryContext, get_repository_context
from sqlalchemy import func

class CityRepository(RepositoryBase[City]):
    def __init__(self, context: RepositoryContext) -> None:
        super().__init__(context.session_maker, City)

    async def get_by_name(self, name: str) -> City | None:
        res = await self.find_by_condition(
            func.lower(City.name) == name.lower()
        )
        return next(iter(res), None)

async def get_city_repository(
    context: RepositoryContext = Depends(get_repository_context),
) -> CityRepository:
    return CityRepository(context)