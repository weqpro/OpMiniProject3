from fastapi import APIRouter, Depends, Query, HTTPException

from app.schemas.aid_request import AidRequestSchema, AidRequestSchemaIn
from app.schemas.search_options import SearchOptionsSchema
from app.services.aid_request_service import AidRequestService, get_aid_request_service
from app.auth import get_current_soldier, get_current_volunteer

router = APIRouter(prefix="/aid_requests", tags=["aid_requests"])


@router.get("/search")
async def search(
    tags: list[str] = Query([], description="List of tags to filter by"),
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    text: str = Query(..., description="Search text"),
):
    search_options: SearchOptionsSchema = SearchOptionsSchema(text=text, tags=tags)

    return await aid_request_service.search(search_options)


@router.delete("/{request_id}")
async def delete(
    request_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    await service.delete(request_id)
    return {"ok": True}


@router.get("/{request_id}", response_model=AidRequestSchema)
async def get_by_id(
    request_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_volunteer),
):
    result = await service.get_by_id(request_id)
    if not result:
        raise HTTPException(404, detail="Request not found")
    return result


@router.put("/{request_id}", response_model=AidRequestSchema)
async def update(
    request_id: int,
    arequest: AidRequestSchemaIn,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    updated = await service.update(request_id, arequest)
    if not updated:
        raise HTTPException(404, detail="Request not found")
    return updated


@router.get("/by-soldier/{soldier_id}", response_model=list[AidRequestSchema])
async def get_by_soldier(
    soldier_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    return await service.get_by_soldier(soldier_id)


@router.get("/unassigned", response_model=list[AidRequestSchema])
async def get_unassigned(
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_unassigned()


@router.post("/", response_model=AidRequestSchema)
async def create(
    arequest: AidRequestSchemaIn,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    return await service.create(arequest, soldier_id=user["id"])


@router.get("/", response_model=list[AidRequestSchema])
async def get_all(
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_all()

