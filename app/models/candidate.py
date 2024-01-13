from models.profile import ProfileBaseModel
from pydantic import Field
from typing import List, Optional


class CandidateBaseModel(ProfileBaseModel):
    """This class represents a candidate model in the application."""
    
    career_level: str = Field(..., description="Career level")
    job_major: str = Field(..., description="Job major")
    years_of_experience: int = Field(..., description="Years of experience")
    degree_type: str = Field(..., description="Degree type")
    skills: List[str] = Field(..., description="Skills")
    nationality: str = Field(..., description="Nationality")
    city: str = Field(..., description="City")
    salary: int = Field(..., description="Salary")
    gender: str = Field(..., description="Gender")
    
class CandidateCreateModel(CandidateBaseModel):
    """This class updating a candidate create model which is responsible for creating candidates."""
    pass

class CandidateUpdateModel(CandidateBaseModel):
    """This class represents a candidate update model which is responsible for updating candidates."""
    pass