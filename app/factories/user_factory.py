import factory
from faker import Faker
from models.user import UserBaseModel

fake = Faker()

class UserFactory(factory.Factory):
    """This class represents a user factory that can be used to generate users."""
    
    class Meta:
        model = UserBaseModel
        
    # Use the profile factory to create users.
    # profile = factory.SubFactory(ProfileFactory)
    
    #TODO: Must be replaced with a factory later.
    #? I have tried the pydantic_factories but it does not work.
    
    first_name = factory.LazyFunction(lambda: fake.first_name())
    last_name = factory.LazyFunction(lambda: fake.last_name())
    email = factory.LazyFunction(lambda: fake.email())
    UUID = factory.LazyFunction(lambda: str(fake.uuid4()))