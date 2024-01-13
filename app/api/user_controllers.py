from abc import ABC, abstractmethod
from fastapi import HTTPException
from services.user_services import UserCreateService, UserReadService
from repositories.user_repositories import IUserRepository, UserInMemoryRepository
from models.user import UserCreateModel, UserBaseModel

class UserControllerBase(ABC):
    """This class represents a user base controller it deals with user repository and services."""
    
    def __init__(self, user_repo: IUserRepository):
        self.user_create_service = UserCreateService(user_repo)
        self.user_read_service = UserReadService(user_repo)

    @abstractmethod
    def create_user(self, user_data: UserCreateModel) -> UserBaseModel:
        """Handle the creation of a new user."""
        pass

    @abstractmethod
    def read_user(self, user_uuid: str) -> UserBaseModel:
        """Handling the read of a user."""
        pass


class InMemoryRepositoryUserController(UserControllerBase):
    """This class is responsible for handling the user in memory repository and services"""
    def __init__(self):
        super().__init__(UserInMemoryRepository())

    def create_user(self, user_data: UserCreateModel) -> UserBaseModel:
        created_user = self.user_create_service.create_user(user_data)
        return created_user

    def read_user(self, user_uuid: str) -> UserBaseModel:
        user = self.user_read_service.get_user(user_uuid)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user