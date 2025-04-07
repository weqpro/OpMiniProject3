# from sqlalchemy.ext.asyncio import AsyncAttrs
# from sqlalchemy.orm import DeclarativeBase


# class Base(AsyncAttrs, DeclarativeBase): ...

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class Base(AsyncAttrs, declarative_base()):
    pass

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def create_user(db_session, name: str, email: str):
    new_user = User(name=name, email=email)
    db_session.add(new_user)
    await db_session.commit()
    return new_user

async def get_user(db_session, user_id: int):
    result = await db_session.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return result.fetchone()

async def main():
    await init_db()

    async with AsyncSessionLocal() as session:
        user = await create_user(session, "Ivan", "ivan@example.com")
        print(f"New user: {user.name}, {user.email}")

        retrieved_user = await get_user(session, user.id)
        print(f"Retrieved user: {retrieved_user.name}, {retrieved_user.email}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
