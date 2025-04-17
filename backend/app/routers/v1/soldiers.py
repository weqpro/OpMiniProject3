from fastapi import APIRouter, Depends, HTTPException

from app.models.soldier import Soldier

from app.services import (
    SoldierService,
    AidRequestService,
    get_soldier_service,
    get_aid_request_service,
)
from app.schemas import SoldierSchema, AidRequestSchema, AidRequestSchemaIn
from app.auth import get_current_soldier, get_password_hash

router = APIRouter(prefix="/soldiers", tags=["soldiers"])


@router.post("/create_request")
async def create_aid_request(
    aid_request: AidRequestSchemaIn,
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    soldier_service: SoldierService = Depends(get_soldier_service),
    soldier: Soldier = Depends(get_current_soldier),
) -> AidRequestSchema:
    result = await aid_request_service.create_aid_request(aid_request, soldier.id)
    return AidRequestSchema.model_validate(result)


@router.delete("/delete_request/{request_id}")
async def delete(
    request_id: int,
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    soldier: Soldier = Depends(get_current_soldier),
):
    soldier.requests


@router.put("/update_request/{request_id}", response_model=AidRequestSchema)
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
