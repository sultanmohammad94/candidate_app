from api.user_controllers import InMemoryRepositoryUserController, UserControllerBase
from repositories.user_repositories import IUserRepository, UserInMemoryRepository
from typing import List, Tuple

class ControllerFactory:
    """This class is responsible for creating controllers for a given user repository."""
    
    @staticmethod
    def create_controllers(repository: IUserRepository) -> List[Tuple[str, UserControllerBase]]:
        controllers = []
        if isinstance(repository, UserInMemoryRepository):
            controllers.append(("in_memory", InMemoryRepositoryUserController()))
        else:
            raise ValueError("Unsupported repository type")
        return controllers

    @staticmethod
    def get_controller_by_name(controllers: List[Tuple[str, UserControllerBase]], name: str) -> UserControllerBase:
        for controller_name, controller in controllers:
            if controller_name == name:
                return controller
        raise ValueError("Controller not found")