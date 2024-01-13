from enum import Enum

class DegreeType(str, Enum):
    """This class represents the education degree types."""
    
    BACHELOR = "Bachelor"
    MASTER = "Master"
    PHD = "PhD"
    HIGH_SCHOOL = "High School"