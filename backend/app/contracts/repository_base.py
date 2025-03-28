"""
module of RepositoryBase implementation
"""

from typing import Sequence
from typing import Type, Any
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql.expression import ColumnExpressionArgument
from app.repository.repository_context import RepositoryContext


class RepositoryBase[T]:
    """
    Class of RepositoryBase implementation
    """

    def __init__(self, repository: RepositoryContext, model: Type[T]):
        self.__repository = repository
        self.__model = model

    async def create(self, value: T) -> T:
        """
        Adds new object to database
        """
        async with self.__repository.session as session:
            try:
                session.add(value)
                await session.commit()
                await session.refresh(value)
                return value
            except SQLAlchemyError as e:
                await session.rollback()
                raise e

    async def delete(self, value: T) -> None:
        """
        Deletes object by id
        """
        async with self.__repository.session as session:
            try:
                await session.delete(value)
                await session.commit()
                return
            except SQLAlchemyError as e:
                await session.rollback()
                raise e

    async def find(
        self, *order_by: ColumnElement | str, **filter_by: Any
    ) -> Sequence[T]:
        """
        Gets objects with the specified ordering, and filtering.
        """
        async with self.__repository.session as session:
            stmt = select(self.__model).order_by(*order_by).filter_by(**filter_by)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def find_by_condition(
        self,
        condition: ColumnExpressionArgument[bool],
        *order_by: ColumnElement | str,
        **filter_by: Any,
    ) -> Sequence[T]:
        """
        Gets objects with the specified ordering, and filtering.
        """
        async with self.__repository.session as session:
            stmt = (
                select(self.__model)
                .where(condition)
                .order_by(*order_by)
                .filter_by(**filter_by)
            )
            result = await session.execute(stmt)
            return result.scalars().all()
