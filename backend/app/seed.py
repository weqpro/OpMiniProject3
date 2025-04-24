from sqlalchemy.dialects.postgresql import insert

from app.seed_data import CATEGORIES
from app.models import Category
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
