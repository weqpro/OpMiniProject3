from typing import List

from app.models.aid_request import AidRequest
from app.repository.repository_manager import RepositoryManager
from app.repository.aid_request_repository import AidRequestRepository
from app.schemas.search_options import SearchOptions


class AidRequestService:
    def __init__(self, repository: RepositoryManager) -> None:
        self.__repository: AidRequestRepository = repository.aid_request

    async def search(self, search_options: SearchOptions | None = None) -> None:
        if search_options is None:
            search_options = SearchOptions(None)

    async def dummy_search(
        self, search_options: SearchOptions | None = None
    ) -> List[AidRequest]:
        return [AidRequest.create_dummy(), AidRequest.create_dummy()]
