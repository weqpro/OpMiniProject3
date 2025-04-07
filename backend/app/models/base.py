# from sqlalchemy.ext.asyncio import AsyncAttrs
# from sqlalchemy.orm import DeclarativeBase


# class Base(AsyncAttrs, DeclarativeBase): ...

from sqlalchemy.ext.asyncio import AsyncAttrs, declarative_base

Base = declarative_base()
