from fastapi import APIRouter, Depends
from app.auth import get_current_soldier
from app.schemas import ReviewCreate, ReviewOut
from app.services import ReviewService, get_review_service


router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=ReviewOut)
async def create_review(
    data: ReviewCreate,
    service: ReviewService = Depends(get_review_service),
    user=Depends(get_current_soldier),
):
    return await service.create(data, soldier_id=user.id)
