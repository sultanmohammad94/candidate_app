from api.health_controller import HealthController
from services.health_services import HealthCheckService
from fastapi.exceptions import HTTPException
from unittest.mock import Mock
import pytest
from utils.logger import ApplicationLogger

@pytest.fixture
def health_check_service_mock():
    return Mock(spec=HealthCheckService)

def test_health_controller_check_running(health_check_service_mock):
    health_check_service_mock.check.return_value:str = "Server is running"
    health_controller = HealthController(health_check_service_mock)
    response: dict = health_controller.check()
    
    assert response == {'message': 'Server is running'}

def test_health_controller_check_not_running(health_check_service_mock):
    health_check_service_mock.check.side_effect = Exception("Server is not running")
    health_controller = HealthController(health_check_service_mock)
    
    with pytest.raises(HTTPException) as exc_info:
        health_controller.check()
        
    assert exc_info.value.detail == "Server is not running"
    assert exc_info.value.status_code == 500
