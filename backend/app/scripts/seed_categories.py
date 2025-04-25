from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category

categories = [
    'Автозапчастини','Енергозабезпечення','Генератори', 'Гігієна та санітарія',
    'Інструменти / будматеріали','Медикаменти','Навігація','Одяг',
    'Побутові послуги','Польовий побут','Продукти харчування',
    'Ремонт','Розвідка та спостереження','Спорядження',
    'Техніка','Транспорт',"Зв'язок"
]

async def seed_categories(session: AsyncSession) -> None:
    existing = set(await session.scalars(select(Category.name)))
    for name in categories:
        if name not in existing:
            session.add(Category(name=name))
    await session.commit()