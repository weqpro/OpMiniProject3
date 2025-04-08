from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Singleton
from .services import ServiceContainer
from app.repository.repository_manager import RepositoryManager


class ApplicationContainer(DeclarativeContainer):
    services = Container(ServiceContainer, repository=RepositoryManager())
    review_service = Singleton(ReviewService)
