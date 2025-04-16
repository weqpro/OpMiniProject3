from fastapi import APIRouter, Depends
from app.auth import get_current_volunteer
from app.services import VolunteerService, get_volunteer_service
from app.schemas import VolunteerSchema, VolunteerSchemaIn

router = APIRouter(prefix="/volunteers", tags=["volunteers"])


@router.get("/{volunteer_id}")
async def get_one(
    volunteer_id: int,
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_by_id(volunteer_id)

@router.delete("/{volunteer_id}")
async def delete(
    volunteer_id: int,
    service: VolunteerService = Depends(get_volunteer_service),
    user=Depends(get_current_volunteer),
):
    return await service.delete(volunteer_id)
