from collections.abc import Sequence
from fastapi import APIRouter, Depends, Query

from app.models.soldier import Soldier
from app.services import SoldierService, get_soldier_service
from app.schemas import SoldierSchema

router = APIRouter(prefix="/api/v1/soldiers", tags=["soldiers"])


@router.post("/create")
async def create(
    soldier: SoldierSchema,
    soldier_service: SoldierService = Depends(get_soldier_service),
) -> SoldierSchema:
    result: Soldier = await soldier_service.create_soldier(soldier)
    return SoldierSchema.model_validate(result)


@router.get("/")
async def get_all(
    soldier_service: SoldierService = Depends(get_soldier_service),
) -> list[SoldierSchema]:
    return list(
        map(lambda s: SoldierSchema.model_validate(s), await soldier_service.get_all())
    )
