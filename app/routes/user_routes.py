from fastapi import APIRouter
from api.user_controllers import InMemoryRepositoryUserController
from models.user import UserCreateModel, UserBaseModel
from factories.user_controller_factory import ControllerFactory
from repositories.user_repositories import UserInMemoryRepository

user_router = APIRouter()
#?You can easily change the router by changing the controller name
user_repo = UserInMemoryRepository()
#? Add controllers as much as needed
controllers = ControllerFactory.create_controllers(user_repo)
user_controller = ControllerFactory.get_controller_by_name(controllers, "in_memory")

@user_router.post("/user/", response_model=UserBaseModel)
async def create_user(user_data: UserCreateModel):
    return user_controller.create_user(user_data)

@user_router.get("/user/{user_uuid}", response_model=UserBaseModel)
async def read_user(user_uuid: str):
    return user_controller.read_user(user_uuid)
