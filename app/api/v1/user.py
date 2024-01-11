from routes.user import router
from models.user import User


users = []

@router.post('/', tags=['User'])
async def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully"}