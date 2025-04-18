from fastapi import APIRouter, Depends, Query, HTTPException

from app.schemas import AidRequestSchema, SearchOptionsSchema
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


@router.get("/get/{request_id}", response_model=AidRequestSchema)
async def get_by_id(
    request_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
):
    result = await service.get_by_id(request_id)
    if not result:
        raise HTTPException(404, detail="Request not found")
    return result
