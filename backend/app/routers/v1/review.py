from fastapi import APIRouter, Depends
from app.auth import get_current_soldier
from app.schemas import ReviewCreate, ReviewOut
from app.services import ReviewService, get_review_service
from app.auth import get_current_volunteer

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=ReviewOut)
async def create_review(
    data: ReviewCreate,
    service: ReviewService = Depends(get_review_service),
    user=Depends(get_current_soldier),
):
    return await service.create(data, soldier_id=user.id)

@router.get("/by-volunteer/{volunteer_id}", response_model=list[ReviewOut])
async def get_reviews_by_volunteer(
    volunteer_id: int,
    service: ReviewService = Depends(get_review_service),
    user=Depends(get_current_volunteer),
):
    return await service.get_by_volunteer(volunteer_id)
