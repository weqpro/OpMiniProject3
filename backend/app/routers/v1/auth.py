# app/routers/v1/auth.py
from fastapi import APIRouter, Depends
from app.schemas import SoldierSchema, VolunteerSchema
from app.services import (
    SoldierService,
    VolunteerService,
    get_soldier_service,
    get_volunteer_service,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register/soldier")
async def register_soldier(
    data: SoldierSchema,
    service: SoldierService = Depends(get_soldier_service),
):
    return await service.create(data)


@router.post("/register/volunteer")
async def register_volunteer(
    data: VolunteerSchema,
    service: VolunteerService = Depends(get_volunteer_service),
):
    return await service.create(data)
