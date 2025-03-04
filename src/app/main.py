from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes import api_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api_router, prefix="")


@app.get("/")
def read_root():
    return {"Hello": "World"}
