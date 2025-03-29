from .repository_context import RepositoryContext
from .aid_request_repository import AidRequestRepository
from app.models.aid_request import AidRequest


class RepositoryManager:
    def __init__(self) -> None:
        self.__context = RepositoryContext()
        self.__aid_request_repository = AidRequestRepository(self.__context, AidRequest)

    @property
    def aid_request(self) -> AidRequestRepository:
        return self.__aid_request_repository
