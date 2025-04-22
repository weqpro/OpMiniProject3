import os
from datetime import timedelta, datetime, timezone
from typing import Literal
import jwt
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError,PyJWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.models.soldier import Soldier
from app.schemas.auth import TokenData
from app.services import SoldierService

from app.services.soldier_service import get_soldier_service
from app.services.volunteer_service import VolunteerService, get_volunteer_service
from app.utils import MissingEnviromentVariableError

from app.models.volunteer import Volunteer
from app.repository.volunteer_repository import get_volunteer_repository, VolunteerRepository

from app.repository.soldier_repository import get_soldier_repository

def __get_passwd() -> str:
    """get s a password from secrets"""
    path = "sercret"
    if path is None:
        raise MissingEnviromentVariableError("Could not get DATABASE_PASSWORD_FILE")
    with open(path) as f:
        return f.read().rstrip("\n")

JWT_SECRET: str = "secret"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 20


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def is_password_valid(password: str) -> bool:
    return len(password) >= 8

async def authenticate_soldier(
    username: str,
    password: str,
    soldier_service: SoldierService,
) -> Soldier | Literal[False]:
    """In our case the username is email"""
    if not is_password_valid(password):
        return False

    soldier: Soldier | None = await soldier_service.get_with_email(username)
    if not soldier:
        return False
    if not await verify_password(password, soldier.password):
        return False
    return soldier


async def authenticate_volunteer(
    username: str,
    password: str,
    volunteer_service: VolunteerService,
) -> Volunteer | Literal[False]:
    if not is_password_valid(password):
        return False

    volunteer: Volunteer | None = await volunteer_service.find_by_email(username)
    if not volunteer:
        return False
    if not await verify_password(password, volunteer.password):
        return False
    return volunteer

async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_soldier(
    token: str = Depends(oauth2_scheme),
    soldier_service: SoldierService = Depends(get_soldier_service),
) -> Soldier:
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not verify credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username = payload.get("sub")
        token_data: TokenData = TokenData(username=username)

        if token_data.username is None:
            raise auth_exception
    except InvalidTokenError:
        raise auth_exception

    soldier: Soldier | None = await soldier_service.get_with_email(token_data.username)
    if soldier is None:
        raise auth_exception
    return soldier

async def get_current_volunteer(
    token: str = Depends(oauth2_scheme),
    volunteer_repo: VolunteerRepository = Depends(get_volunteer_repository),
) -> Volunteer:
    print(f"TOKEN: {token}")
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not verify credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username = payload.get("sub")
        token_data: TokenData = TokenData(username=username)

        if token_data.username is None:
            raise auth_exception
    except InvalidTokenError:
        raise auth_exception

    volunteer: Volunteer | None = await volunteer_repo.find_by_email(token_data.username)
    if volunteer is None:
        raise auth_exception
    return volunteer

async def get_current_user_from_token(
    token: str = Depends(oauth2_scheme),
    volunteer_repo = Depends(get_volunteer_repository),
    soldier_repo = Depends(get_soldier_repository),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception

    volunteer = await volunteer_repo.find_by_email(email)
    if volunteer:
        return volunteer

    soldier = await soldier_repo.find_by_email(email)
    if soldier:
        return soldier

    raise credentials_exception