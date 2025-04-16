from abc import ABC, abstractmethod
from typing import Sequence
from app.models.aid_request import AidRequest

class AidRequestRepositoryBase(ABC):

    @abstractmethod
    async def create(self, value: AidRequest) -> AidRequest:
        ...

    @abstractmethod
    async def update(self, condition, **values) -> None:
        ...

    @abstractmethod
    async def delete(self, value: AidRequest) -> None:
        ...

    @abstractmethod
    async def find(self, *order_by) -> Sequence[AidRequest]:
        ...

    @abstractmethod
    async def find_by_condition(self, condition, *order_by) -> Sequence[AidRequest]:
        ...
