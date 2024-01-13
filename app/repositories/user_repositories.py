from abc import ABC, abstractmethod
from typing import List, Optional
from models.user import UserBaseModel

class IUserRepository(ABC):
    """This Interface represents the base interface for the user repositories."""
    
    @abstractmethod
    def create_user(self, user: UserBaseModel) -> UserBaseModel:
        '''Add a user to the repository.'''
        pass

    @abstractmethod
    def get_user(self, user_uuid: str) -> Optional[UserBaseModel]:
        '''Get a user from the repository using its UUID'''
        pass

    @abstractmethod
    def update_user(self, user_uuid: str, user: UserBaseModel) -> Optional[UserBaseModel]:
        '''Update a user from the repository'''
        pass

    @abstractmethod
    def delete_user(self, user_uuid: str) -> bool:
        '''Delete a user from the repository'''
        pass


class UserInMemoryRepository(IUserRepository):
    """This class represents a user in memory repository."""
    def __init__(self):
        self.users = {}

    def create_user(self, user: UserBaseModel) -> UserBaseModel:
        '''Add a user to the repository'''
        if user.UUID in self.users:
            raise ValueError('User already exists')
        
        self.users[user.UUID] = user
        return user

    def get_user(self, user_uuid: str) -> Optional[UserBaseModel]:
        '''Get a user from the repository using uuid''' 
        return self.users.get(user_uuid)
    
    def update_user(self, user_uuid: str, user: UserBaseModel) -> Optional[UserBaseModel]:
        if user_uuid in self.users:
            self.users[user_uuid] = user
            return user
        return None

    def delete_user(self, user_uuid: str) -> bool:
        if user_uuid in self.users:
            del self.users[user_uuid]
            return True
        return False
