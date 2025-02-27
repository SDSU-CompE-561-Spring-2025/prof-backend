from app.core.config import get_settings

settings = get_settings()


# User CRUD operations
def create_user():
    print("User created successfully")
    return {
        "id": 1,
        "username": "SrJ1SQPRXLbRN_9vAFAedQrTV4NwmH0BGtCVr5A1QmARS1AxRX",
        "email": "user@example.com",
        "created_at": "2025-02-27T03:55:53.783Z",
    }
