from pydantic import BaseModel, Field


class ProfileBaseModel(BaseModel):
    """This class represents a profile model which can be used as a base model for users with profiles."""
    
    first_name: str = Field(min_length=1, description="First name of the user")
    last_name: str = Field(min_length=1, description="Last name of the user")
    email: str = Field(min_length=1, description="Email of the user")
    UUID: str = Field(min_length=1, description="UUID of the user")