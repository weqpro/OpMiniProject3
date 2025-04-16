from collections.abc import Sequence
from fastapi import APIRouter, Depends, Query

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


@router.get("/")
async def get_all(
    soldier_service: SoldierService = Depends(get_soldier_service),
) -> list[SoldierSchema]:
    return list(
        map(lambda s: SoldierSchema.model_validate(s), await soldier_service.get_all())
    )


@router.post("/create")
async def create(
    soldier: SoldierSchema,
    soldier_service: SoldierService = Depends(get_soldier_service),
) -> SoldierSchema:
    soldier.password = await get_password_hash(soldier.password)
    result: Soldier = await soldier_service.create_soldier(soldier)
    return SoldierSchema.model_validate(result)


@router.post("/create_request")
async def create_aid_request(
    aid_request: AidRequestSchemaIn,
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    soldier: Soldier = Depends(get_current_soldier),
) -> AidRequestSchema:
    result = await aid_request_service.create_aid_request(aid_request, soldier.id)
    return AidRequestSchema.model_validate(result)