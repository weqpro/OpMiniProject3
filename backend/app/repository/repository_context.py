import asyncio
import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)
from sqlalchemy import text
import sqlalchemy.exc

from app.utils import Singleton, MissingEnviromentVariableError
from app.models.base import Base
from app.models.soldier import Soldier
from app.models.volunteer import Volunteer
from app.models.aid_request import AidRequest


class RepositoryContext(metaclass=Singleton):
    def __init__(self) -> None:
        password = "1234"
        connection = "postgresql+asyncpg://postgres:1234@localhost:5432/fortistest"

        if connection is None:
            raise MissingEnviromentVariableError("Missing DB connection string")

        self.__engine: AsyncEngine = create_async_engine(
            connection,
            echo=False,
            pool_size=20,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800,
        )

        self.__session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.__engine, expire_on_commit=False
        )

    async def init_db(self):
        print("Connecting to db...", flush=True)
        try:
            async with self.__engine.begin() as conn:
                await conn.execute(text("DROP TABLE IF EXISTS aid_request CASCADE"))
                await conn.execute(text("DROP TABLE IF EXISTS category CASCADE"))
                await conn.run_sync(Base.metadata.drop_all)
                await conn.run_sync(Base.metadata.create_all)
        except sqlalchemy.exc.OperationalError as e:
            print(f"Failed (retry after 2s)\ne:{e}")
            await asyncio.sleep(2)
            await self.init_db()
        print("Connected to database", flush=True)

    def __del__(self):
        if hasattr(self, "_RepositoryContext__engine"):
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    asyncio.create_task(self.__engine.dispose())
                else:
                    loop.run_until_complete(self.__engine.dispose())
            except Exception:
                pass

    @asynccontextmanager
    async def session_maker(self) -> AsyncGenerator[AsyncSession, None]:
        session: AsyncSession = self.__session_maker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


def get_repository_context() -> RepositoryContext:
    return RepositoryContext()
