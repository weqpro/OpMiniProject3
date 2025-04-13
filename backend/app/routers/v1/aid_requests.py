import datetime

from fastapi import APIRouter, Depends, Query

from app.schemas import SearchOptionsSchema, AidRequestSchema, CategorySchema
from app.services import AidRequestService, get_aid_request_service

router = APIRouter(prefix="/api/v1/aid_requests", tags=["aid_requests"])


@router.get("/search")
async def search(
    text: str = Query(..., description="Search text"),
    tags: list[str] = Query([], description="List of tags to filter by"),
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
):
    search_options: SearchOptionsSchema = SearchOptionsSchema(text=text, tags=tags)

    return await aid_request_service.search(search_options)


@router.post("/create")
async def create(
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
):
    aid_request: AidRequestSchema = AidRequestSchema(
        id=123,
        name="Name",
        description="Some description",
        image="shit",
        deadline=datetime.datetime.now(),
        location="somewhere",
        tags=["josci", "duje"],
        status="not done",
        soldier_id=1,
        category=CategorySchema(id=1, name="one", request_id=123),
    )

    return await aid_request_service.create_aid_request(aid_request)
