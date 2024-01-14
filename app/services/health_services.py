class HealthCheckService:
    """This service is responsible for reading users from the user repository."""
    
    def check(self)->str:
        try:
            return "Server is running"
        except Exception as e:
            
            return "Server is not running"
            