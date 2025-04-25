import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.repository.repository_context import RepositoryContext
from app.routers.v1 import v1_router
from app.auth.routes import router as auth_router
from app.scripts import seed_categories, seed_cities

repo_ctx = RepositoryContext()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# from app.seed import seed_categories

# _ = RepositoryContext()


@asynccontextmanager
async def lifespan(_: FastAPI):
    await seed_categories()  # seed categories on startup
    yield


# app = FastAPI(lifespan=lifespan)


app.include_router(v1_router)
app.include_router(auth_router)


@app.on_event("startup")
async def on_startup():
    # --- Temporarily commented out drop/recreate logic ---
    # async with repo_ctx.session_maker() as s:
    #     await s.execute(text(
    #         "ALTER TABLE aid_request DROP CONSTRAINT IF EXISTS aid_request_category_id_fkey"
    #     ))
    #     await s.execute(text("DROP TABLE IF EXISTS category"))
    #     await s.commit()
    #
    # await repo_ctx.ensure_db()
    #
    # async with repo_ctx.session_maker() as s:
    #     await seed_categories(s)
    #
    # async with repo_ctx.session_maker() as s:
    #     await s.execute(text(
    #         "ALTER TABLE aid_request ADD CONSTRAINT aid_request_category_id_fkey "
    #         "FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE SET NULL"
    #     ))
    #     await s.commit()

    await repo_ctx.ensure_db()

    async with repo_ctx.session_maker() as session:
        await seed_categories(session)
        await seed_cities(session)
