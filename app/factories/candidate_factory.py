import factory
from models.candidate import CandidateBaseModel
from factories.profile_factory import ProfileFactory
from faker import Faker
from enums.career_level import CareerLevel
from enums.degree_type import DegreeType
from enums.gender import Gender
from enums.job_major import JobMajor
from enums.nationality import Nationality
from enums.skills import Skills


fake = Faker()

class CandidateFactory(factory.Factory):
    """This class represents a candidate factory that can be used to generate candidates."""
    
    class Meta:
        model = CandidateBaseModel
        
    # Use the profile factory to create candidates.
    # profile = factory.SubFactory(ProfileFactory)
    
    #TODO: Must be replaced with a factory later.
    #? I have tried the pydantic_factories but it does not work.
    
    first_name = factory.LazyFunction(lambda: fake.first_name())
    last_name = factory.LazyFunction(lambda: fake.last_name())
    email = factory.LazyFunction(lambda: fake.email())
    UUID = factory.LazyFunction(lambda: str(fake.uuid4()))
    
    career_level = fake.random_element(elements=[e.value for e in CareerLevel])
    job_major = fake.random_element(elements=[e.value for e in JobMajor])
    years_of_experience = factory.LazyFunction(lambda: fake.random_int(min=0, max=50))
    degree_type = fake.random_element(elements=[e.value for e in DegreeType])
    skills = [fake.random_element(elements=[e.value for e in Skills]) for _ in range(fake.random_int(min=1, max=5))]
    nationality = fake.random_element(elements=[e.value for e in Nationality])
    city = fake.city()
    salary = fake.random_int(min=50000, max=150000)
    gender = fake.random_element(elements=[e.value for e in Gender])
