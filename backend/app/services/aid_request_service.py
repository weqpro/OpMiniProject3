from typing import List

from backend.app.models.aid_request import AidRequest
from backend.app.repository.repository_manager import RepositoryManager
from backend.app.repository.aid_request_repository import AidRequestRepository
from backend.app.schemas.search_options import SearchOptions
from backend.app.schemas.aid_request import AidRequestCreate, AidRequestOut
from backend.app.models.aid_request import AidRequestStatus
import datetime


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
    
    async def create_aid_request(self, db, aid_request: AidRequestCreate) -> AidRequestOut:
        return await self.__repository.create_aid_request(db=db, aid_request=aid_request)

    async def update_aid_request_status(self, db, aid_request_id: int, status: AidRequestStatus) -> AidRequestOut:
        return await self.__repository.update_aid_request_status(db=db, aid_request_id=aid_request_id, status=status)

    async def set_volunteer_deadline(self, db, aid_request_id: int, deadline: datetime.datetime) -> AidRequestOut:
        return await self.__repository.set_volunteer_deadline(db=db, aid_request_id=aid_request_id, deadline=deadline)

    async def delete_aid_request(self, db, aid_request_id: int, soldier_id: int) -> bool:
        return await self.__repository.delete_aid_request(db=db, aid_request_id=aid_request_id, soldier_id=soldier_id)

    async def reject_aid_request(self, db, aid_request_id: int, volunteer_id: int) -> bool:
        return await self.__repository.reject_aid_request(db=db, aid_request_id=aid_request_id, volunteer_id=volunteer_id)
