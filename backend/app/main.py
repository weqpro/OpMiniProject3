from fastapi import FastAPI

from app.repository.repository_context import RepositoryContext
from app.routers.v1 import v1_router
from app.auth.routes import router as auth_router


app = FastAPI()
_ = RepositoryContext()

app.include_router(v1_router)
app.include_router(auth_router)
