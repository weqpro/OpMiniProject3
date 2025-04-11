import asyncio
from collections.abc import AsyncGenerator
import os
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)
from sqlalchemy import text
import sqlalchemy.exc

from app.utils import Singleton

from app.models.soldier import Soldier
from app.models.volunteer import Volunteer
from app.models.aid_request import AidRequest
from app.models.base import Base


class MissingEnviromentVariableError(Exception):
    """if env variable was not found"""

    pass


class RepositoryContext(metaclass=Singleton):
    def __init__(self) -> None:
        password: str = self.__get_passwd()
        connection: str | None = os.getenv("DATABASE_URL")

        if connection is None:
            raise MissingEnviromentVariableError("Could not get DATABASE_URL")

        self.__engine: AsyncEngine = create_async_engine(
            connection.format(passwd=password),
            echo=False,
            pool_size=20,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800,
        )

        self.__session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.__engine, expire_on_commit=False
        )

        asyncio.create_task(self.init_db())

    async def init_db(self):
        print("Connecting to db...", flush=True)
        try:
            async with self.__engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        except sqlalchemy.exc.OperationalError as e:
            print(f"Failed (retry after 2s)\ne:{e}")
            await asyncio.sleep(2)
            await self.init_db()
        print("Conected to database", flush=True)

    def __del__(self) -> None:
        asyncio.run(self.__engine.dispose())

    def __get_passwd(self) -> str:
        """get s a password from secrets"""
        path = os.getenv("DATABASE_PASSWORD_FILE")
        if path is None:
            raise MissingEnviromentVariableError("Could not get DATABASE_PASSWORD_FILE")
        with open(path) as f:
            return f.read().rstrip("\n")

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
