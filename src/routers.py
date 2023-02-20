from fastapi import APIRouter

from src.lstat.router import router_stat

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}


api_router.include_router(router_stat, prefix="/lstat", tags=["Статистика"])  #
