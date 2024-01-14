from fastapi import APIRouter
from api.health_controller import HealthController
from services.health_services import HealthCheckService


health_router = APIRouter()
health_controller = HealthController(HealthCheckService())

@health_router.get("/health/", tags=["Health"], status_code=200)
async def check_health():
    '''Handling the Health Check Request.'''
    return health_controller.check()