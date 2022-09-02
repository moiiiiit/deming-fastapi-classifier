from fastapi import APIRouter
from src.endpoints.general import general 
from src.endpoints.resNet50 import resNet50

router = APIRouter()
router.include_router(general.router)
router.include_router(resNet50.router)