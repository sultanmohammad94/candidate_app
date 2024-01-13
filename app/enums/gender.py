from enum import Enum

class Gender(str, Enum):
    """This class represents the Gender of the users."""
    
    MALE = "Male"
    FEMALE = "Female"
    NOT_SPECIFIED = "Not specified"