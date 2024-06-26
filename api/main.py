from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.routers import users, recurrent_expenses
from .database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Loading tables...')
    create_db_and_tables()
    yield
    print('Shuting down...')


app = FastAPI(lifespan=lifespan)
app.include_router(users.router)
app.include_router(recurrent_expenses.router)
