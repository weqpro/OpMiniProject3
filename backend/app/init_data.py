from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category

PREDEFINED_CATEGORIES = [
    "Автозапчастини",
    "Енергозабезпечення",
    "Гігієна та санітарія",
    "Інструменти / будматеріали",
    "Медикаменти",
    "Навігація",
    "Одяг",
    "Побутові послуги",
    "Польовий побут",
    "Продукти харчування",
    "Ремонт",
    "Розвідка та спостереження",
    "Спорядження",
    "Техніка",
    "Транспорт",
    "Зв'язок"
]


async def init_categories(session: AsyncSession) -> None:
    for name in PREDEFINED_CATEGORIES:
        stmt = select(Category).where(Category.name == name)
        result = await session.execute(stmt)
        existing = result.scalars().first()
        if not existing:
            session.add(Category(name=name))
    await session.commit()