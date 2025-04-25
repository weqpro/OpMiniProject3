from fastapi import APIRouter, Depends, Form, HTTPException, status, BackgroundTasks
from app.schemas import SoldierSchemaIn, VolunteerSchemaIn
from app.services import get_soldier_service, get_volunteer_service
from app.auth import (
    authenticate_soldier,
    create_access_token,
    authenticate_volunteer,
)
from app.services import VolunteerService, SoldierService
from app.models.volunteer import Volunteer
from app.auth import get_current_volunteer, get_current_soldier, get_current_user_from_token
from app.mailer import send_registration_email

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register/soldier", response_model=SoldierSchemaIn)
async def register_soldier(
    data: SoldierSchemaIn,
    background_tasks: BackgroundTasks,
    service: SoldierService = Depends(get_soldier_service),
):
    soldier = await service.create_soldier(data)
    background_tasks.add_task(
        send_registration_email,
        email=soldier.email,
        full_name=f"{soldier.name} {soldier.surname}"
    )
    return soldier

  
@router.post("/register/volunteer", response_model=VolunteerSchemaIn)
async def register_volunteer(
    data: VolunteerSchemaIn,
    background_tasks: BackgroundTasks,
    service: VolunteerService = Depends(get_volunteer_service),
):
    volunteer = await service.create(data)
    background_tasks.add_task(
        send_registration_email,
        email=volunteer.email,
        full_name=f"{volunteer.name} {volunteer.surname}"
    )
    return volunteer


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
