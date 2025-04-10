from fastapi import Depends, FastAPI

from app.services.aid_request_service import AidRequestService, get_aid_request_service

app = FastAPI()


@app.get("/")
async def read_root(
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
):
    return await aid_request_service.dummy_search()


# @app.post("/aid-requests/", response_model=AidRequestOut)
# async def create_aid_request(
#     aid_request: AidRequestCreate,
#     db: Session = Provide[ApplicationContainer.db],
#     aid_request_service: AidRequestService = Provide[
#         ApplicationContainer.aid_request_service
#     ],
# ):
#     """
#     Create a new aid request by a soldier.
#     """
#     created_aid_request = await aid_request_service.create_aid_request(db, aid_request)
#     return created_aid_request
#
#
# @app.post("/reviews/", response_model=ReviewOut)
# async def create_review(
#     review: ReviewCreate,
#     db: Session = Provide[ApplicationContainer.db],
#     review_service: ReviewService = Provide[ApplicationContainer.review_service],
# ):
#     """
#     Create a new review for a volunteer by a soldier.
#     """
#     created_review = await review_service.create_review(db, review)
#
#     return created_review
