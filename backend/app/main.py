import datetime

from fastapi import Depends, FastAPI

from app.repository.repository_context import RepositoryContext
from app.schemas.aid_request import AidRequestSchema
from app.schemas.category import CategorySchema
from app.schemas.search_options import SearchOptions
from app.services.aid_request_service import AidRequestService, get_aid_request_service


app = FastAPI()
_ = RepositoryContext()


@app.get("/api/v1/search")
async def search(
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
):
    return await aid_request_service.search(SearchOptions(text="", tags=["one"]))


@app.post("/api/v1/create")
async def create(
    aid_request_service: AidRequestService = Depends(get_aid_request_service),
):
    aid_request: AidRequestSchema = AidRequestSchema(
        id=123,
        name="Name",
        description="Some description",
        image="shit",
        deadline=datetime.datetime.now(),
        location="somewhere",
        tags=["josci", "duje"],
        status="not done",
        soldier_id=1,
        category=CategorySchema(id=1, name="one", request_id=123),
    )

    return await aid_request_service.create_aid_request(aid_request)


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
