from fastapi import APIRouter, Depends, Form, HTTPException, status
from app.schemas import SoldierSchemaIn, VolunteerSchemaIn
from app.services import SoldierService, VolunteerService, get_soldier_service, get_volunteer_service
from app.auth import get_password_hash, authenticate_soldier, create_access_token, verify_password
from app.repository.volunteer_repository import get_volunteer_repository
from app.models.volunteer import Volunteer

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
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = await create_access_token({"sub": soldier.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/token/volunteer")
async def login_volunteer(
    username: str = Form(...),
    password: str = Form(...),
    volunteer_repo = Depends(get_volunteer_repository),
):
    volunteer: Volunteer | None = await volunteer_repo.find_by_email(username)
    if not volunteer or not await verify_password(password, volunteer.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = await create_access_token({"sub": volunteer.email})
    return {"access_token": token, "token_type": "bearer"}