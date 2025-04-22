from fastapi import HTTPException, Depends
from app.models import Review, AidRequest, Volunteer
from app.utils import AidRequestStatus
from app.schemas import ReviewCreate, ReviewOut
from app.repository import ReviewRepository, get_review_repository, AidRequestRepository
from app.repository import get_review_repository, get_aid_request_repository
from app.repository.repository_context import get_repository_context
from sqlalchemy import func

class ReviewService:
    def __init__(self, repo: ReviewRepository, session_maker, requestRepo: AidRequestRepository) -> None:
        self.__repo = repo
        self.__session_maker = session_maker
        self.__request_repo = requestRepo

    async def create(self, data: ReviewCreate, soldier_id: int) -> ReviewOut:
        requests = await self.__request_repo.find_by_condition(
            (AidRequest.id == data.request_id) &
            (AidRequest.soldier_id == soldier_id) &
            (AidRequest.status == AidRequestStatus.COMPLETED.value)
        )
        request = next(iter(requests), None)
        if not request:
            raise HTTPException(status_code=400, detail="Cannot review: no completed request for this soldier")

        existing = await self.__repo.find_by_condition(Review.request_id == data.request_id)
        if existing:
            raise HTTPException(status_code=400, detail="Review already exists for this request")

        review = Review(
            review_text=data.review_text,
            rating=data.rating,
            tags=data.tags,
            volunteer_id=request.volunteer_id,
            soldier_id=soldier_id,
            request_id=request.id
        )
        await self.__repo.create(review)

        avg_rating = await self._get_average_rating(review.volunteer_id)
        await self._update_volunteer_rating(review.volunteer_id, avg_rating)

        return review

    async def _get_average_rating(self, volunteer_id: int) -> float:
        async with self.__session_maker() as session:
            result = await session.execute(
                func.avg(Review.rating).select().where(Review.volunteer_id == volunteer_id)
            )
            return result.scalar() or 0.0

    async def _update_volunteer_rating(self, volunteer_id: int, rating: float):
        async with self.__session_maker() as session:
            result = await session.execute(
                Volunteer.__table__.update()
                .where(Volunteer.id == volunteer_id)
                .values(rating=rating)
            )
            await session.commit()

async def get_review_service(
    review_repo: ReviewRepository = Depends(get_review_repository),
    request_repo: AidRequestRepository = Depends(get_aid_request_repository),
    context = Depends(get_repository_context),
) -> ReviewService:
    return ReviewService(review_repo, context.session_maker, request_repo)


