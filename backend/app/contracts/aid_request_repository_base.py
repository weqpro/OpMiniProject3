from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING
from app.schemas import SearchOptionsSchema

if TYPE_CHECKING:
    from app.models.aid_request import AidRequest


class AidRequestRepositoryBase(ABC):
    @abstractmethod
    async def search(
        self, search_options: SearchOptionsSchema
    ) -> Sequence["AidRequest"]: ...
