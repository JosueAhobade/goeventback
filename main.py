from fastapi import FastAPI
from database import Base, engine
from users import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
