from models.user import UserBaseModel, ProfileBaseModel
from repositories.user_repositories import IUserRepository
from models.user import UserBaseModel
from typing import Optional

class UserCreateService:
    """This class is used to create add a new user to the repository."""
    
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: UserBaseModel) -> UserBaseModel:
        '''Create user if it is not already in the repository.'''
        is_exist = self.user_repository.get_user(user_uuid= user_data.UUID)
        if is_exist:
            raise ValueError('User already exists')
        
        user = UserBaseModel(**user_data.model_dump())
        created_user = self.user_repository.create_user(user)
        return created_user

class UserReadService:
    """This service is responsible for reading users from the user repository."""
    
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def get_user(self, user_uuid: str) -> Optional[UserBaseModel]:
        user = self.user_repository.get_user(user_uuid)
        return user
