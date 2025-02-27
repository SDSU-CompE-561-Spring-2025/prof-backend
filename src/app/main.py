from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes.user import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router, prefix="/auth", tags=["User"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
