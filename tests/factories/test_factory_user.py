import unittest
from factories.user_factory import UserFactory
from utils.logger import ApplicationLogger

class TestUserFactory(unittest.TestCase):
    def test_create_user(self):
        user = UserFactory.create()
        ApplicationLogger().log_debug(f'USER: {user}')
        self.assertIsNotNone(user)

    def test_bulk_create_users(self):
        users = UserFactory.create_batch(5)
        self.assertEqual(len(users), 5)
        
if __name__ == '__main__':
    unittest.main()
