from abc import ABC, abstractmethod
from services.health_services import HealthCheckService
from fastapi.exceptions import HTTPException
from utils.logger import ApplicationLogger


class HealthBaseController(ABC):
    def __init__(self, service: HealthCheckService):
        self._service = service
        
    """This class represents the base class of the Health Check Controller."""
    
    @abstractmethod
    def check(self)->dict:
        raise NotImplementedError
    

class HealthController(HealthBaseController):
    """This class implements the base Interface of the Health Check Controller."""
    def check(self)->dict:
        '''Return whether the server is running or not.'''
        try:
            message = self._service.check()
            return {'message': message}
        except Exception as e:
            ApplicationLogger().log_error(f"Exception raised while handling the HealthController.check: {str(e)}")
            raise HTTPException(detail="Server is not running", status_code=500)
