from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_volunteer, get_current_soldier
from app.services import VolunteerService, get_volunteer_service
from app.schemas import VolunteerSchema, VolunteerSchemaIn, VolunteerUpdateSchema, VolunteerSchemaOut, ChangePasswordSchema

router = APIRouter(prefix="/volunteers", tags=["volunteers"])

@router.get("/{volunteer_id}")
async def get_one(
    volunteer_id: int,
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_soldier),
):
    # return await service.get_by_id(volunteer_id)
    volunteer = await service.get_by_id(volunteer_id)
    if volunteer is None:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer


@router.get("/me", response_model=VolunteerSchemaOut)
async def get_me(
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_by_id(user.id)

@router.delete("/me")
async def delete(
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_volunteer),
):
    await service.delete(user.id)
    return {"detail": "Volunteer deleted"}


@router.put("/me", response_model=VolunteerSchemaOut)
async def update_me(
    data: VolunteerUpdateSchema,
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_volunteer),
):
    return await service.update_me(user.id, data)

@router.post("/change-password")
async def change_password(
    data: ChangePasswordSchema,
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_volunteer),
):
    await service.change_password(user.email, data.current_password, data.new_password)
    return {"detail": "Password changed"}
