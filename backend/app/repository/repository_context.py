import asyncio
import os
from typing import AsyncContextManager
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)


class MissingEnviromentVariableError(Exception):
    """if env variable was not found"""

    pass


class RepositoryContext:
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

        print("Created")

    def __del__(self) -> None:
        asyncio.run(self.__engine.dispose())

    def __get_passwd(self) -> str:
        """get s a password from secrets"""
        path = os.getenv("DATABASE_PASSWORD_FILE")
        if path is None:
            raise MissingEnviromentVariableError("Could not get DATABASE_PASSWORD_FILE")
        with open(path) as f:
            return f.read().rstrip("\n")

    @property
    def session(self) -> AsyncContextManager[AsyncSession]:
        """returns yields a session from session pool"""
        return self.__session_maker()
