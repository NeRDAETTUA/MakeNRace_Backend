from fastapi.routing import APIRouter

from mnr.web.api import docs, dummy, echo, monitoring,team

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(team.router, prefix="/team", tags=["team"])
