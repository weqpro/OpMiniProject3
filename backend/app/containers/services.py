from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Dependency
from app.services.aid_request_service import AidRequestService


class ServiceContainer(DeclarativeContainer):
    repository = Dependency()

    aid_request_service: Singleton[AidRequestService] = Singleton(repository=repository)
