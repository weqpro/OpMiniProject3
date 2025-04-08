from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Dependency
from app.services.aid_request_service import AidRequestService
from app.services.review_service import ReviewService # написати

class ServiceContainer(DeclarativeContainer):
    repository = Dependency()

    aid_request_service: Singleton[AidRequestService] = Singleton(repository=repository)
    review_service = Singleton(ReviewService)
    