from typing import List

from fastapi import FastAPI
from dependency_injector.wiring import inject, Provide
from sqlalchemy.orm import Session

from app.containers.application_container import ApplicationContainer
from app.models.aid_request import AidRequest
from app.schemas.responses.search_response import AidRequestSearchResponse
from app.schemas.aid_request import AidRequestCreate, AidRequestOut
from app.services.aid_request_service import AidRequestService
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewOut 
from app.services.review_service import ReviewService # дописати сервіс для відгуку

global app
app = FastAPI()


def create_app():
    application = ApplicationContainer()
    application.wire(modules=[__name__])


@app.get("/", response_model=AidRequestSearchResponse)
@inject
async def read_root(
    aid_request_service: AidRequestService = Provide[ApplicationContainer],
):
    return {"result": await aid_request_service.dummy_search()}

@app.post("/aid-requests/", response_model=AidRequestOut)
@inject
async def create_aid_request(
    aid_request: AidRequestCreate,
    db: Session = Provide[ApplicationContainer.db],
    aid_request_service: AidRequestService = Provide[ApplicationContainer.aid_request_service],
):
    """
    Create a new aid request by a soldier.
    """
    created_aid_request = await aid_request_service.create_aid_request(db, aid_request)
    return created_aid_request

@app.post("/reviews/", response_model=ReviewOut)
@inject
async def create_review(
    review: ReviewCreate,
    db: Session = Provide[ApplicationContainer.db],
    review_service: ReviewService = Provide[ApplicationContainer.review_service],
):
    """
    Create a new review for a volunteer by a soldier.
    """
    created_review = await review_service.create_review(db, review)

    return created_review


if __name__ == "__main__":
    create_app()
