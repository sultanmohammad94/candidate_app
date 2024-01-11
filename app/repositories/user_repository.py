from repositories.base import IRepository
from pymongo.collection import Collection
from models.user import User
from typing import List, Optional

class UserMongoDBRepository(IRepository[User]):
    def __init__(self, collection: Collection):
        self.collection = collection

    def get(self, id: str) -> User:
        return self.collection.find_one({"uuid": id})

    def get_all(self) -> Optional[List[User]]:
        return list(self.collection.find())

    def create(self, user: User) -> User:
        self.collection.insert_one(user.dict())
        return user

    def delete(self, id: str) -> None:
        self.collection.delete_one({"uuid": id})

    def update(self, id: str, user: User) -> User:
        self.collection.update_one({"uuid": id}, {"$set": user.dict()})
        return user
