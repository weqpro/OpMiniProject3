from fastapi import APIRouter, Depends, Query

from app.schemas import SearchOptionsSchema, AidRequestSchema
from app.services import AidRequestService, get_aid_request_service

router = APIRouter(prefix="/aid_requests", tags=["aid_requests"])


@router.get("/search")
async def search(
    tags: list[str] = Query([], description="List of tags to filter by"),
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    text: str = Query(..., description="Search text"),
):
    search_options: SearchOptionsSchema = SearchOptionsSchema(text=text, tags=tags)

    return await aid_request_service.search(search_options)


@router.post("/create")
async def create(
    aid_request: AidRequestSchema,
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
):
    return await aid_request_service.create_aid_request(aid_request)
