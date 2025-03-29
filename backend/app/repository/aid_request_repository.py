from typing import override
from app.contracts.repository_base import RepositoryBase
from app.contracts.aid_request_repository_base import AidRequestRepositoryBase
from app.models.aid_request import AidRequest


class AidRequestRepository(RepositoryBase[AidRequest], AidRequestRepositoryBase):
    @override
    def get_aid_request_by_soldier(self, soldier_id: int) -> list[AidRequest]:
        """Get all aid requests for a specific soldier"""
        pass

    @override
    def get_aid_request_by_category(self, category_id: int) -> list[AidRequest]:
        """Get all aid requests for a specific category"""
        pass
