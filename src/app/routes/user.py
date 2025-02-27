from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
def register_user():
    return {"message": "User registered successfully"}


@router.post("/token")
async def login_for_access_token():
    return {"message": "User logged in successfully"}


def example_func():
    return "Hello from example_func"
