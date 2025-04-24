from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.repository.repository_context import RepositoryContext
from app.routers.v1 import v1_router
from app.auth.routes import router as auth_router
from app.seed import seed_categories

_ = RepositoryContext()


@asynccontextmanager
async def lifespan(_: FastAPI):
    await seed_categories()  # seed categories on startup
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(v1_router)
app.include_router(auth_router)
