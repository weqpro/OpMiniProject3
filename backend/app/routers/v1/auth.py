from fastapi import APIRouter, Depends, Form, HTTPException, status
from app.schemas import SoldierSchemaIn, VolunteerSchemaIn
from app.services import get_soldier_service, get_volunteer_service
from app.auth import (
    authenticate_soldier,
    create_access_token,
    authenticate_volunteer,
)
from app.services import VolunteerService, SoldierService
from app.models.volunteer import Volunteer
from app.auth import (
    get_current_user_from_token,
)


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register/soldier")
async def register_soldier(
    data: SoldierSchemaIn,
    service: SoldierService = Depends(get_soldier_service),
):
    return await service.create_soldier(data)


@router.post("/register/volunteer")
async def register_volunteer(
    data: VolunteerSchemaIn,
    service: VolunteerService = Depends(get_volunteer_service),
):
    return await service.create(data)


@router.post("/token/soldier")
async def login_soldier(
    username: str = Form(...),
    password: str = Form(...),
    soldier_service: SoldierService = Depends(get_soldier_service),
):
    soldier = await authenticate_soldier(username, password, soldier_service)
    if not soldier:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    token = await create_access_token({"sub": soldier.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token/volunteer")
async def login_volunteer(
    username: str = Form(...),
    password: str = Form(...),
    volunteer_service: VolunteerService = Depends(get_volunteer_service),
):
    volunteer = await authenticate_volunteer(username, password, volunteer_service)
    if not volunteer:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    token = await create_access_token({"sub": volunteer.email})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
async def get_current_user(user=Depends(get_current_user_from_token)):
    role = "volunteer" if isinstance(user, Volunteer) else "soldier"
    return {"id": user.id, "role": role}
