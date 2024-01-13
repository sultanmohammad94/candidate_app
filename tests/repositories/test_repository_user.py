import unittest
from repositories.user_repositories import UserInMemoryRepository
from factories.user_factory import UserFactory
from models.user import UserBaseModel
from utils.logger import ApplicationLogger


class TestUserInMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserInMemoryRepository()
        self.user_data = UserFactory.create()
        
        
    def test_create_user(self):
        user = UserBaseModel(**self.user_data.model_dump())
        user.first_name = 'John'
        created_user = self.user_repository.create_user(user)
        self.assertEqual(created_user.first_name, "John")

    def test_get_user(self):
        # Creating some test users
        users = UserFactory.create_batch(5)
        
        # Adding test users to the repository
        for user in users:
            test_user = user
            self.user_repository.create_user(test_user)
        
        # Add our test user to the repository
        self.user_repository.create_user(self.user_data)

        # Trying to fetch the test user
        user = self.user_repository.get_user(self.user_data.UUID)
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, self.user_data.first_name)

    def test_update_user(self):
        
        # Adding the test user to the repository
        self.user_repository.create_user(self.user_data)
        
        # Getting the id of the test user
        user_UUID = self.user_data.UUID
        # set new data for the test user
        updated_user_data = {
            "first_name": "Updated",
            "last_name": "Doe",
            "email": "updated.doe@example.com",
            "UUID": user_UUID
        }
        # creating a new user with the updated data
        updated_user = UserBaseModel(**updated_user_data)
        
        # Trying to update the user
        result = self.user_repository.update_user(user_UUID, updated_user)
        self.assertIsNotNone(result)

    def test_delete_non_existing_user(self):
        # Try to delete non-existing user
        user_UUID = self.user_data.UUID
        result = self.user_repository.delete_user(user_UUID)
        self.assertFalse(result)
        
    def test_delete_existing_user(self):
        # Adding the user to the repository
        self.user_repository.create_user(self.user_data)
        user_UUID = self.user_data.UUID
        result = self.user_repository.delete_user(user_UUID)
        self.assertTrue(result)
        
    def test_unique_user(self):
        self.user_repository.create_user(self.user_data)
        with self.assertRaises(Exception):
            self.user_repository.create_user(self.user_data)

        
if __name__ == '__main__':
    unittest.main()
