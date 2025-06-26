from fastapi import APIRouter
from app.api.endpoints.mcqs import router 



api_router = APIRouter()
api_router.include_router(router, tags=["generate MCQS"])