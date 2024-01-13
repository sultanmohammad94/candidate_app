import factory
from faker import Faker
from models.profile import ProfileBaseModel

fake = Faker()

class ProfileFactory(factory.Factory):
    """This class represents a profile factory that can be used to generate profiles."""
    
    class Meta:
        model = ProfileBaseModel

    first_name = factory.LazyFunction(lambda: fake.first_name())
    last_name = factory.LazyFunction(lambda: fake.last_name())
    email = factory.LazyFunction(lambda: fake.email())
    UUID = factory.LazyFunction(lambda: fake.uuid4())
    