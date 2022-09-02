from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def ping():
    return {"message": "healthy"}

@router.get("/auth")
def auth():
    return {"status": "Authenticated"}