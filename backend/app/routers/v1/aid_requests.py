from fastapi import APIRouter, Depends, Query, HTTPException, Form, UploadFile, File, Depends
from app.schemas.aid_request import (
    AidRequestSchema,
    AidRequestSchemaIn,
    AidRequestSchemaInWithoutVolId,
    AidRequestSchemaUpdate,
    AidRequestCreateMultipart
)
from app.utils import AidRequestStatus
from app.schemas.search_options import SearchOptionsSchema
from app.services.aid_request_service import AidRequestService, get_aid_request_service
from app.auth import get_current_soldier, get_current_volunteer, get_current_user_from_token
from fastapi.encoders import jsonable_encoder
import os, shutil, json


router = APIRouter(prefix="/aid_requests", tags=["aid_requests"])

@router.get("/search")
async def search(
    tags: list[str] = Query([], description="List of tags to filter by"),
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    text: str = Query(..., description="Search text"),
):
    search_options = SearchOptionsSchema(text=text, tags=tags)
    return await aid_request_service.search(search_options)


@router.delete("/{request_id}")
async def delete(
    request_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    await service.delete(request_id)
    return {"ok": True}

@router.get("/by-volunteer/{volunteer_id}", response_model=list[AidRequestSchema])
async def get_by_volunteer(
    volunteer_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_by_volunteer(volunteer_id)

@router.post("/{request_id}/publish", response_model=AidRequestSchema)
async def publish(
    request_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user: dict = Depends(get_current_soldier),
):
    updated = await service.publish(request_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Request not found")
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
    user=Depends(get_current_user_from_token),
):
    return await service.get_unassigned()

@router.post("/", response_model=AidRequestSchema)
async def create(
    json_data: str = Form(...),
    image: UploadFile | None = File(None),
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    data_dict = json.loads(json_data)
    schema = AidRequestCreateMultipart(**data_dict)

    image_name = ""
    if image:
        os.makedirs("uploads/aid_requests", exist_ok=True)
        image_name = image.filename
        image_path = f"uploads/aid_requests/{image.filename}"
        with open(image_path, "wb") as f:
            shutil.copyfileobj(image.file, f)

    final_data = AidRequestSchemaInWithoutVolId(
        **schema.dict(),
        image=image_name
    )

    return await service.create(final_data, soldier_id=user.id)

@router.post("/{request_id}/assign", response_model=AidRequestSchema)
async def assign_request_to_volunteer(
    request_id: int,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_volunteer),
):
    data = AidRequestSchemaUpdate(
        volunteer_id=user.id,
        status=AidRequestStatus.IN_PROGRESS.value
    )
    updated = await service.update(request_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Request not found")
    return updated


@router.get("/", response_model=list[AidRequestSchema])
async def get_all(
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_all()

@router.put("/{request_id}", response_model=AidRequestSchema)
async def update_request(
    request_id: int,
    data: AidRequestSchemaUpdate,
    service: AidRequestService = Depends(get_aid_request_service),
    user=Depends(get_current_soldier),
):
    updated = await service.update(request_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Request not found")
    return updated

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

