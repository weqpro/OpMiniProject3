from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.aid_request import AidRequest
    from app.schemas import SearchOptionsSchema


class AidRequestRepositoryBase(ABC):
    @abstractmethod
    async def search(
        self, search_options: SearchOptionsSchema
    ) -> Sequence[AidRequest]: ...
