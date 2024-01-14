import unittest
from factories.user_factory import UserFactory

class TestUserFactory(unittest.TestCase):
    def test_create_user(self):
        user = UserFactory.create()
        self.assertIsNotNone(user)

    def test_bulk_create_users(self):
        users = UserFactory.create_batch(5)
        self.assertEqual(len(users), 5)
        
if __name__ == '__main__':
    unittest.main()
