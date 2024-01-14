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

#* The name of the controller to be used for handling the requests
used_controller = "in_memory"
user_controller = ControllerFactory.get_controller_by_name(controllers, used_controller)


@user_router.post("/user/", response_model=UserBaseModel, tags=["User"], status_code=201)
async def create_user(user_data: UserCreateModel):
    '''Handling the user creation request using the constructed controller.'''
    return user_controller.create_user(user_data)

@user_router.get("/user/{user_uuid}", response_model=UserBaseModel, tags=["User"], status_code=200)
async def read_user(user_uuid: str):
    '''Handling the user reading request using the constructed controller.'''
    return user_controller.read_user(user_uuid)
