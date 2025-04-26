from fastapi import APIRouter, Depends, HTTPException

from app.models.soldier import Soldier

from app.services import (
    SoldierService,
    AidRequestService,
    get_soldier_service,
    get_aid_request_service,
)
from app.schemas import SoldierSchema, AidRequestSchema, AidRequestSchemaIn, SoldierUpdateSchema, ChangePasswordSchema
from app.auth import get_current_soldier, get_password_hash, get_current_volunteer

router = APIRouter(prefix="/soldiers", tags=["soldiers"])

@router.get("/me", response_model=SoldierSchema)
async def get_me(
    service: SoldierService = Depends(get_soldier_service),
    user=Depends(get_current_soldier),
):
    return await service.get_by_id(user.id)


@router.post("/create")
async def create(
    soldier: SoldierSchema,
    soldier_service: SoldierService = Depends(get_soldier_service),
) -> SoldierSchema:
    soldier.password = await get_password_hash(soldier.password)
    result: Soldier = await soldier_service.create_soldier(soldier)
    return SoldierSchema.model_validate(result)

@router.delete("/me")
async def delete(
    service: SoldierService = Depends(get_soldier_service),
    user=Depends(get_current_soldier),
):
    await service.delete(user.id)
    return {"detail": "Soldier deleted"}

@router.get("/soldier-info/{soldier_id}")
async def get_soldier_info(
    soldier_id: int,
    user=Depends(get_current_volunteer),
    service: SoldierService = Depends(get_soldier_service)
):
    soldier = await service.get_by_id(soldier_id)
    if not soldier:
        raise HTTPException(status_code=404, detail="Військового не знайдено")

    return {
        "name": soldier.name,
        "surname": soldier.surname,
        "phone_number": soldier.phone_number,
        "email": soldier.email,
    }

@router.post("/create_request")
async def create_aid_request(
    aid_request: AidRequestSchemaIn,
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
    soldier: Soldier = Depends(get_current_soldier),
) -> AidRequestSchema:
    result = await aid_request_service.create(aid_request, soldier.id)
    return AidRequestSchema.model_validate(result)

@router.put("/me", response_model=SoldierSchema)
async def update_me(
    data: SoldierUpdateSchema,
    service: SoldierService = Depends(get_soldier_service),
    user=Depends(get_current_soldier),
):
    return await service.update_me(user.id, data)

@router.post("/change-password")
async def change_password(
    data: ChangePasswordSchema,
    service: SoldierService = Depends(get_soldier_service),
    user=Depends(get_current_soldier),
):
    await service.change_password(user.email, data.current_password, data.new_password)
    return {"detail": "Password changed"}
