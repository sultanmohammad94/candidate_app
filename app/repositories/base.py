from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Optional

T = TypeVar('T')

class IRepository(Generic[T], ABC):
    """This class represents the base repository in the application."""
    
    @abstractmethod
    def get(self, id: str) -> T:
        '''Returns an item from the repository'''
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Optional[List[T]]:
        '''Returns all items from the repository'''
        raise NotImplementedError

    @abstractmethod
    def create(self, item: T) -> T:
        '''Add a new item to the repository'''
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        '''Delete an item from the repository'''
        raise NotImplementedError

    @abstractmethod
    def update(self, id: str, item: T) -> T:
        '''Update an existing item in the repository'''
        raise NotImplementedError
