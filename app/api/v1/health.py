from routes.health import router
from services.health import HealthService


@router.get("/", status_code=200, tags=['Health'])
async def server_health():
    '''This endpoint is used to check whether the server is on or off.'''
    try:
        result = HealthService().check_server_health()
        return {"message": result}
    except:
        return {"message": "Server is not running"}
    
@router.get("/list_dbs", status_code=200, tags=['Health'])
async def list_dbs():
    '''This endpoint is used to check whether the server is on or off.'''
    try:
        result = HealthService().list_dbs()
        return {"message": result}
    except Exception as e:
        
        return {"message": str(e)}