from typing import List

from fastapi import FastAPI
from dependency_injector.wiring import inject, Provide

from app.containers.application_container import ApplicationContainer
from app.models.aid_request import AidRequest
from app.schemas.responses.search_response import AidRequestSearchResponse
from app.services.aid_request_service import AidRequestService

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


if __name__ == "__main__":
    create_app()
