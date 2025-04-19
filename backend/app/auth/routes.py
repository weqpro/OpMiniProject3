from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import Token
from app.services import SoldierService, get_soldier_service
from .auth import authenticate_soldier, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    soldier_service: SoldierService = Depends(get_soldier_service),
):
    soldier = await authenticate_soldier(
        form_data.username, form_data.password, soldier_service
    )
    if not soldier:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": soldier.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
