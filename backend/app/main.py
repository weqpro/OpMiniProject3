from fastapi import FastAPI
from app.repository.repository_context import RepositoryContext

app = FastAPI()


@app.get("/")
async def read_root():
    _ = RepositoryContext()
    return {"Hello": "World"}
