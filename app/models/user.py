from models.profile import ProfileBaseModel

class UserBaseModel(ProfileBaseModel):
    """This class represents a the base model for users in the application."""
    pass
    

class UserCreateModel(UserBaseModel):
    """This class represents the model used to create a new user"""
    pass

class UserUpdateModel(UserBaseModel):
    """This class represents the model used to update a new user"""
    pass