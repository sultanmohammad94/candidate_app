from pydantic import BaseModel, Field

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    UUID: str = Field(..., alias="user_id")

