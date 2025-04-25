from sqlalchemy.dialects.postgresql import insert

from .seed_data import CATEGORIES, CITIES
from app.models import Category, City
from app.repository import RepositoryContext, get_repository_context


async def seed_categories() -> None:
    context: RepositoryContext = get_repository_context()
    async with context.session_maker() as session:
        # turn each namedtuple into a dict
        rows = [{"id": cat.id, "name": cat.name} for cat in CATEGORIES]

        stmt = (
            insert(Category).values(rows).on_conflict_do_nothing(index_elements=["id"])
        )

        await session.execute(stmt)
        await session.commit()


async def seed_cities() -> None:
    context: RepositoryContext = get_repository_context()
    async with context.session_maker() as session:
        # turn each CitySeed into a dict matching your model columns
        rows = [
            {
                "id": city.id,
                "name": city.name,
                "latitude": city.latitude,
                "longitude": city.longitude,
            }
            for city in CITIES
        ]

        # insert, but do nothing if a row with the same id already exists
        stmt = insert(City).values(rows).on_conflict_do_nothing(index_elements=["id"])

        await session.execute(stmt)
        await session.commit()
